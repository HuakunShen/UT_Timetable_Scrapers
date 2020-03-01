import json
import pymysql as mysql
# import mysql.connector as mysql
import requests
import string
from multiprocessing import Pool
import time
import os


def parse_meetings(meetings):
    for meeting_key in list(meetings.keys()):
        parse_meeting(meetings[meeting_key])


def parse_instructor(instructors):
    '''
    parse instructors and save into DB
    :param instructors:
    :return:
    '''
    global instructor_rows
    if instructors:
        for instructor_key in instructors.keys():
            instructor = instructors[instructor_key]
            instructor_dict = {}
            for instructor_attr in DB_INFO['instructor']['keys']:
                instructor_dict[instructor_attr] = instructor[instructor_attr]
            instructor_rows.append(tuple(instructor_dict.values()))


def parse_schedule(schedules, meetingId):
    # print('meeting: ', meetingId)
    global schedule_rows
    if schedules:
        for schedule_key in schedules.keys():
            schedule = schedules[schedule_key]
            schedule['meetingId'] = meetingId
            schedule_dict = {}
            for schedule_attr in DB_INFO['schedule']['keys']:
                schedule_dict[schedule_attr] = schedule[schedule_attr]
            schedule_rows.append(tuple(schedule_dict.values()))


def parse_meeting(meeting):
    global meeting_rows
    # print("search meeting", meeting['meetingId'])
    parse_instructor(meeting['instructors'])
    parse_schedule(meeting['schedule'], meeting['meetingId'])
    meeting_dict = {}
    for meeting_key in DB_INFO['meeting']['keys']:
        try:
            meeting_dict[meeting_key] = meeting[meeting_key]
        except Exception as e:
            meeting_dict[meeting_key] = None
    meeting_dict['meetingId'] = int(meeting_dict['meetingId'])
    meeting_rows.append(tuple(meeting_dict.values()))


def save_to_DB(subject):
    connection = mysql.connect(
        host=pwd[host]['host'], user=pwd[host]['user'], password=pwd[host]['password'], database='ut_timetable')
    cursor = connection.cursor()
    sql_values_s_holder = '(' + ','.join(['%s']
                                         * len(DB_INFO[subject]['keys'])) + ')'

    if subject == 'course':
        rows = course_rows
    elif subject == 'meeting':
        rows = meeting_rows
    elif subject == 'instructor':
        rows = instructor_rows
    elif subject == 'schedule':
        rows = schedule_rows
    db_table_titles = str(
        tuple(DB_INFO[subject]['keys'])).replace("'", "")
    query = ("INSERT IGNORE INTO " + DB_INFO[subject]['table_name']
             + db_table_titles +
             " VALUES " + sql_values_s_holder)

    cursor.executemany(query, rows)
    cursor.close()
    connection.commit()
    connection.close()


def run(code):
    # for code in alphabets:
    params = {
        'code': code
    }
    r = requests.get(
        'https://timetable.iit.artsci.utoronto.ca/api/20199/courses', params=params)
    r_dict = r.json()
    print("Search Code: ", code)
    if type(r_dict) != dict:
        print(code + " doesn't exists")
        return
    # else:
    #     file_all_courses.write(code + "\n")
    r_dict_keys = list(r_dict.keys())
    # parse course info

    # each key is a full course name of a course
    for key in r_dict_keys:
        # print("search course: ", key)
        course_data_dict = {}
        full_course_code = key
        # file_all_courses.write(key + "\n")
        course = r_dict[key]
        for course_key in DB_INFO['course']['keys']:
            if course_key in course:
                course_data_dict[course_key] = course[course_key]
        course_data_dict["courseId"] = int(course_data_dict["courseId"])
        course_data_dict['full_course_code'] = full_course_code
        course_rows.append(tuple(course_data_dict.values()))
        # save_to_DB(course_data_dict, DB_INFO['course']['table_name'])
        parse_meetings(course['meetings'])
        # connection.commit()

    for subject in DB_INFO:
        save_to_DB(subject)


if __name__ == "__main__":
    DB_INFO = {
        "course": {
            "table_name": 'course_info',
            "keys": ['courseId', 'code', 'org', 'orgName', 'courseTitle', 'courseDescription', 'prerequisite',
                     'corequisite',
                     'exclusion', 'recommendedPreparation', 'section', 'session', 'breadthCategories', 'full_course_code']
        },
        "meeting": {
            "table_name": 'meetings',
            "keys": ['meetingId', 'teachingMethod', 'sectionNumber', 'subtitle', 'cancel', 'waitlist', 'online',
                     'enrollmentCapacity', 'actualEnrolment', 'actualWaitlist', 'enrollmentIndicator']
        },
        "schedule": {
            "table_name": 'schedules',
            "keys": ['meetingId', 'meetingDay', 'meetingStartTime', 'meetingEndTime', 'meetingScheduleId', 'assignedRoom1',
                     'assignedRoom2']
        },
        "instructor": {
            "table_name": 'instructors',
            "keys": ['instructorId', 'firstName', 'lastName']
        }
    }

    course_rows = []
    instructor_rows = []
    meeting_rows = []
    schedule_rows = []

    # load password
    with open(os.getcwd() + '/pwd.json') as json_file:
        pwd = json.load(json_file)

    # connect to db
    host = "localhost"
    host = "aws"
    connection = mysql.connect(
        host=pwd[host]['host'], user=pwd[host]['user'], password=pwd[host]['password'], database='ut_timetable')
    cursor = connection.cursor()
    for subject in DB_INFO:
        cursor.execute("truncate " + DB_INFO[subject]['table_name'] + ";")
        connection.commit()
    cursor.close()
    connection.close()
    start_time = time.time()
    alphabets = list(string.ascii_lowercase)
    # for letter in alphabets:
    #     run(letter)
    p = Pool()
    result = p.map(run, alphabets)
    # for subject in DB_INFO:
    #     save_to_DB(subject)

    print("time used for multiprocessing: ", time.time() -
          start_time)  # print out the total process time
    # Eventually, there were 3389 lines of data in table course_info;
    # 4526 rows in instructors table
    # 7406 rows in meetings table
    # 7978 rows in schedules table
    # time used was 28.9 seconds
