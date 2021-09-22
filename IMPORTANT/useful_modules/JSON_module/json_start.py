import json
import random

json_str = """
{
"response": {
    "count": 41,
    "items": [{
        "first_name": "Andrei",
        "id": 303086218,
        "last_name": "Kanev",
        "can_access_closed": true
        }, {
        "first_name": "Tatyana",
        "id": 7446123,
        "last_name": "Bokhan",
        "can_access_closed": true
        }, {
        "first_name": "Lika",
        "id": 246578599,
        "last_name": "Lika",
        "can_access_closed": true
        }]
        }} """
print(type(json_str))

data = json.loads(json_str)

print(type(data))
for item in data['response']['items']:
    del item['can_access_closed']
    item['followers'] = random.randint(1, 200)
    print(item)

new_json = json.dumps(data, indent=2)
n_json = json.loads(new_json)

for item in n_json['response']['items']:
    print(item)


