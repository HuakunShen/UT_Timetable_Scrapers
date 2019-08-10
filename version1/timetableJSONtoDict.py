import requests
import json

params = {
    'code': 'CSC209'
}
r = requests.get('https://timetable.iit.artsci.utoronto.ca/api/20199/courses', params=params)
r_dict = r.json()
print(type(r_dict))

# print out all course names and codes from the response
for key in r_dict:
    print(key)

r_dict_keys = list(r_dict.keys())
# parse course info
full_course_code = r_dict_keys[0]
course = r_dict[full_course_code]

# courseId = course['courseId']
# code = course['code']
# org = course['org']
# orgName = course['orgName']
# courseTitle = course['courseTitle']
# courseDescription = course['courseDescription']
# prerequisite = course['prerequisite']
# corequisite = course['corequisite']
# exclusion = course['exclusion']
# recommendedPreparation = course['recommendedPreparation']
# section = course['section']
# session = course['session']
# breadthCategories = course['breadthCategories']

course_data_dict = {}
course_keys = ['courseId', 'code', 'org', 'orgName', 'courseTitle', 'courseDescription', 'prerequisite', 'corequisite',
               'exclusion', 'recommendedPreparation', 'section', 'session', 'breadthCategories']
for key in course_keys:
    course_data_dict[key] = course[key]
print(course_data_dict)
# parse lecture/tut sections
