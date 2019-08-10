import requests
import json
params = {
    'code': 'CSC209'
}
r = requests.get('https://timetable.iit.artsci.utoronto.ca/api/20199/courses', params=params)
r_dict = r.json()
print(r_dict)
print(r.url)
# save json file locally
with open('tmp.json', 'w') as f:
    json.dump(r_dict, f)
