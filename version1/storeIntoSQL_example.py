import mysql.connector as SQL
import requests
import json
import string

COURSE_TABLE_NAME = 'course_info'


# search all courses
def parse_meetings(meetings):
    # meetings_keys = list(meetings.keys())
    for meeting_key in list(meetings.keys()):
        parse_meeting(meetings[key])


def parse_instructor(instructors):
    for instructor_key in instructors.keys():
        instructor = instructors[instructor_key]
        keys = ['instructorId', 'firstName', 'lastName']
        instructor_dict = {}

        instructorId = instructor['instructorId']
        firstName = instructor['firstName']
        lastName = instructor['lastName']


def parse_meeting(meeting):
    parse_instructor(meeting['instructors'])


def save_to_DB(value_dict, coursor, table_name):
    sql_values_s_holder = '(' + ','.join(['%s'] * len(course_data_dict)) + ')'
    db_table_titles = str(tuple(course_data_dict.keys())).replace("'", "")
    row_data = list(course_data_dict.values())
    query = ("INSERT IGNORE INTO " + COURSE_TABLE_NAME
             + db_table_titles +
             "VALUES " + sql_values_s_holder)
    cursor.execute(query, row_data)



if __name__ == '__main__':
    alphabets = list(string.ascii_lowercase)
    file_all_courses = open('all_courses.txt', 'w+')
    course_keys = ['courseId', 'code', 'org', 'orgName', 'courseTitle', 'courseDescription', 'prerequisite',
                   'corequisite',
                   'exclusion', 'recommendedPreparation', 'section', 'session', 'breadthCategories']
    mydb = SQL.connect(host='localhost', user='huakun',
                       password='', database='public')
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
        # print(r_dict)
        if type(r_dict) != dict:
            print(code + " doesn't exists")
            continue
        else:
            file_all_courses.write(code + "\n")
        r_dict_keys = list(r_dict.keys())
        # parse course info

        # each key is a full course name of a course
        for key in r_dict_keys:
            course_data_dict = {}
            full_course_code = key
            course = r_dict[key]
            for course_key in course_keys:
                course_data_dict[course_key] = course[course_key]
            course_data_dict["courseId"] = int(course_data_dict["courseId"])
            course_data_dict['full_course_code'] = full_course_code
            save_to_DB(course_data_dict, cursor, COURSE_TABLE_NAME)
            parse_meetings(course['meetings'])

            mydb.commit()

    cursor.close()
    mydb.close()

    file_all_courses.close()
