import mysql.connector as SQL
import requests
import json
import itertools
import string
print(list(string.ascii_lowercase))
alphabets = list(string.ascii_lowercase)
lst = [alphabets, alphabets, alphabets]
for code in itertools.product(*lst):
    
    params = {
        'code': code 
    }
    r = requests.get(
        'https://timetable.iit.artsci.utoronto.ca/api/20199/courses', params=params)
    r_dict = r.json()

    r_dict_keys = list(r_dict.keys())
    # parse course info
    course_keys = ['courseId', 'code', 'org', 'orgName', 'courseTitle', 'courseDescription', 'prerequisite', 'corequisite',
                'exclusion', 'recommendedPreparation', 'section', 'session', 'breadthCategories']
    mydb = SQL.connect(host='localhost', user='huakun',
                    password='', database='public')
    cursor = mydb.cursor()

    # clear the table before inserting, comment it out as needed
    # query = ("truncate courseInfo;")
    # cursor.execute(query)

    # each key is a full course name of a course
    count = 0
    for key in r_dict_keys:
        course_data_dict = {}
        full_course_code = key
        course = r_dict[key]
        for course_key in course_keys:
            course_data_dict[course_key] = course[course_key]
        course_data_dict["courseId"] = int(course_data_dict["courseId"])
        course_data_dict['full_course_code'] = full_course_code
        num_keys = len(course_data_dict)
        sql_values_s_holder = '(' + num_keys * '%s,'
        sql_values_s_holder = sql_values_s_holder[0:-1] + ')'
        db_table_titles = str(tuple(course_data_dict.keys()))
        db_table_titles = db_table_titles.replace("'", "")
        row_data = list(course_data_dict.values())
        query = ("INSERT IGNORE INTO course_info "
                + db_table_titles +
                "VALUES " + sql_values_s_holder)
        cursor.execute(query, row_data)
        count += 1
    mydb.commit()
    cursor.close()
    mydb.close()
