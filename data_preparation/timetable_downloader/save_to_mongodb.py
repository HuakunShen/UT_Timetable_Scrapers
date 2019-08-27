import pymongo
import datetime
import string
import requests

client = pymongo.MongoClient(
    "mongodb+srv://admin:admin@database-6pxs9.mongodb.net/test?retryWrites=true&w=majority")
# client = pymongo.MongoClient('localhost', 27017)
db = client.ut_timetable


def save_one_to_mongodb(obj, collection):
    try:
        collection.insert_one(obj)
        return True
    except pymongo.errors.DuplicateKeyError as _:
        print("duplicate key: ", obj['_id'])
        return False


def parse_meetings(meetings):
    for meeting_key in meetings.keys():
        parse_meeting(meeting_key, meetings[meeting_key])


def parse_instructor(instructors):
    # print('Parsing Instructors')
    if instructors:
        for instructor_key in instructors.keys():
            instructor = instructors[instructor_key]
            instructor['_id'] = instructor_key
            instructor['update_date'] = datetime.datetime.utcnow()
            save_one_to_mongodb(instructor, db.instructors)


def parse_meeting(meeting_name, meeting):
    # print('Parsing Meetings')
    meeting_data = meeting.copy()
    meeting_data['name'] = meeting_name
    meeting_data['_id'] = meeting['meetingId']
    meeting_data['update_date'] = datetime.datetime.utcnow()
    save_one_to_mongodb(meeting_data, db.meetings)
    parse_instructor(meeting['instructors'])


if __name__ == "__main__":
    db.courses.drop()
    db.instructors.drop()
    db.meetings.drop()
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
            full_course_code = key
            print("Search Course: ", full_course_code)
            file_all_courses.write(key + "\n")
            course = r_dict[key]
            course_data = course.copy()
            course_data['_id'] = full_course_code
            course_data['full_course_code'] = full_course_code
            course_data['update_date'] = datetime.datetime.utcnow()

            if save_one_to_mongodb(course_data, db.courses):
                parse_meetings(course['meetings'])

    file_all_courses.close()
