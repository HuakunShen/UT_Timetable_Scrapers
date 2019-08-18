import mysql.connector as SQL
import pymysql
import requests
import string

COURSE_TABLE_NAME = 'course_info'
INSTRUCTOR_TABLE_NAME = 'instructors'
MEETINGS_TABLE_NAME = 'meetings'
SCHEDULE_TABLE_NAME = 'schedules'
INSTRUCTOR_KEYS = ['instructorId', 'firstName', 'lastName']
MEETING_KEYS = ['meetingId', 'teachingMethod', 'sectionNumber', 'subtitle', 'cancel', 'waitlist', 'online',
                'enrollmentCapacity', 'actualEnrolment', 'actualWaitlist', 'enrollmentIndicator']
SCHEDULE_KEYS = ['meetingDay', 'meetingStartTime', 'meetingEndTime', 'meetingScheduleId', 'assignedRoom1',
                 'assignedRoom2']


# search all courses
def parse_meetings(meetings):
    # meetings_keys = list(meetings.keys())
    for meeting_key in list(meetings.keys()):
        parse_meeting(meetings[meeting_key])


def parse_instructor(instructors):
    '''
    parse instructors and save into DB
    :param instructors:
    :return:
    '''
    if instructors:
        # print(instructors)
        for instructor_key in instructors.keys():
            instructor = instructors[instructor_key]
            instructor_dict = {}
            for instructor_attr in INSTRUCTOR_KEYS:
                instructor_dict[instructor_attr] = instructor[instructor_attr]
            save_to_DB(instructor_dict, INSTRUCTOR_TABLE_NAME)


def parse_schedule(schedules, meetingId):
    # print('meeting: ', meetingId)
    if schedules:
        for schedule_key in schedules.keys():
            schedule = schedules[schedule_key]
            schedule_dict = {'meetingId': meetingId}
            for schedule_attr in SCHEDULE_KEYS:
                schedule_dict[schedule_attr] = schedule[schedule_attr]
            save_to_DB(schedule_dict, SCHEDULE_TABLE_NAME)


def parse_meeting(meeting):
    # print("search meeting", meeting['meetingId'])
    parse_instructor(meeting['instructors'])
    parse_schedule(meeting['schedule'], meeting['meetingId'])
    meeting_dict = {}
    for meeting_key in MEETING_KEYS:
        try:
            meeting_dict[meeting_key] = meeting[meeting_key]
        except Exception as e:
            pass
    save_to_DB(meeting_dict, MEETINGS_TABLE_NAME)


def save_to_DB(value_dict, table_name):
    sql_values_s_holder = '(' + ','.join(['%s'] * len(value_dict)) + ')'
    db_table_titles = str(tuple(value_dict.keys())).replace("'", "")
    row_data = list(value_dict.values())
    query = ("INSERT IGNORE INTO " + table_name
             + db_table_titles +
             "VALUES " + sql_values_s_holder)
    cursor.execute(query, row_data)


if __name__ == '__main__':
    alphabets = list(string.ascii_lowercase)
    file_all_courses = open('all_courses.txt', 'w+')
    course_keys = ['courseId', 'code', 'org', 'orgName', 'courseTitle', 'courseDescription', 'prerequisite',
                   'corequisite',
                   'exclusion', 'recommendedPreparation', 'section', 'session', 'breadthCategories']
    # mydb = SQL.connect(host='mysqldb.cqcfrqhijmrx.us-east-2.rds.amazonaws.com', user='admin',
    #                    password='admin', port='3306', database='public')
    mydb = pymysql.connect('mysqldb.cqcfrqhijmrx.us-east-2.rds.amazonaws.com', user='admin', db='public',
                           passwd='admin', connect_timeout=5)
    cursor = mydb.cursor()
    # clear the table before inserting, comment it out as needed
    query = ("truncate course_info;")
    cursor.execute(query)
    mydb.commit()

    print("Spider Starts")

    for code in alphabets:
        params = {
            'code': code
        }
        r = requests.get(
            'https://timetable.iit.artsci.utoronto.ca/api/20199/courses', params=params)
        r_dict = r.json()
        print("Search Code: ", code)
        if type(r_dict) != dict:
            print(code + " doesn't exists")
            continue
        # else:
        #     file_all_courses.write(code + "\n")
        r_dict_keys = list(r_dict.keys())
        # parse course info

        # each key is a full course name of a course
        for key in r_dict_keys:
            # print("search course: ", key)
            course_data_dict = {}
            full_course_code = key
            file_all_courses.write(key + "\n")
            course = r_dict[key]
            for course_key in course_keys:
                course_data_dict[course_key] = course[course_key]
            course_data_dict["courseId"] = int(course_data_dict["courseId"])
            course_data_dict['full_course_code'] = full_course_code
            save_to_DB(course_data_dict, COURSE_TABLE_NAME)
            parse_meetings(course['meetings'])
            mydb.commit()

    cursor.close()
    mydb.close()

    file_all_courses.close()
