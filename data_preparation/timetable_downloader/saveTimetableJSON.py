import requests
import json
params = {
    'code': 'CSC'
}
r = requests.get('https://timetable.iit.artsci.utoronto.ca/api/20199/courses', params=params)
# r = requests.get('https://timetable.iit.artsci.utoronto.ca/api/20199/courses', params=params)
r_dict = r.json()
print(len(r_dict))
for key in r_dict.keys():
    print(key)
# print(r.url)
# save json file locally
with open('tmp.json', 'w') as f:
    json.dump(r_dict, f)
