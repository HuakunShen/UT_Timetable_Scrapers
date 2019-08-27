import pymongo
import datetime
import string
import requests
# from pymongo import MongoClient


# client = pymongo.MongoClient(
#     "mongodb+srv://admin:admin@database-6pxs9.mongodb.net/test?retryWrites=true&w=majority")
client = pymongo.MongoClient('localhost', 27017)
db = client.ut_timetable
courses = db.course_infos
meetings = db.meetings
schedules = db.schedules
instructors = db.instructors

# save_one_to_mongodb(course1, courses)
# save_one_to_mongodb(course2, courses)
# save_one_to_mongodb(course3, courses)
# save_one_to_mongodb(course4, courses)


def save_one_to_mongodb(obj, collection):
    try:
        collection.insert_one(obj)
    except pymongo.errors.DuplicateKeyError as _:
        print("duplicate key: ", obj['_id'])


if __name__ == "__main__":
    alphabets = list(string.ascii_lowercase)
    file_all_courses = open('all_courses.txt', 'w+')
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
            course_data_dict = {}
            full_course_code = key
            file_all_courses.write(key + "\n")
            course = r_dict[key]
            course_data_dict['_id'] = full_course_code
            course_data_dict['full_course_code'] = full_course_code
            for course_key in course:
                if course_key == 'meetings':
                    continue
                course_data_dict[course_key] = course[course_key]
            save_one_to_mongodb(course_data_dict, courses)
            # for course_key in course_keys:
            #     course_data_dict[course_key] = course[course_key]
            # course_data_dict["courseId"] = int(course_data_dict["courseId"])
            # course_data_dict['full_course_code'] = full_course_code
            # save_to_DB(course_data_dict, COURSE_TABLE_NAME)
            # parse_meetings(course['meetings'])

    file_all_courses.close()


# course_keys = ['courseId', 'code', 'org', 'orgName', 'courseTitle', 'courseDescription', 'prerequisite',
#                'corequisite',
#                'exclusion', 'recommendedPreparation', 'section', 'session', 'breadthCategories']

course_info = {
    '_id': None,
    'courseId': None,
    'code': None,
    'org': None,
    'orgName': None,
    'courseTitle': None,
    'courseDescription': None,
    'prerequisite': None,
    'corequisite': None,
    'exclusion': None,
    'recommendedPreparatio': None,
    'section': None,
    'session': None,
    'breadthCategories': None
}
