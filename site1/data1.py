import requests
import json
import base64
import sys

#endpoint = 'https://api.ximilar.com/your-endpoint'
endpoint = 'https://api.ximilar.com/recognition/v2/classify/'
headers = {
#    'Authorization': "Token __TOKEN__",
#   'Content-Type': 'application/json'
   'Authorization': "Token 0fdd6a2783765b4238beeabd677f1d9da04c902c",
   'Content-Type': 'application/json'
}
fpath=sys.argv[1]
# First way to load base64
with open(fpath, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# Second way to load base64 data with opencv
# import cv2
#image = cv2.imread(__IMAGE_PATH__) # this will return image in BGR
#retval, buffer = cv2.imencode('.jpg', image)
#encoded_string = base64.b64encode(buffer).decode('utf-8')

data = {
    'records': [{"_base64": encoded_string}],
    'task_id': "6eb714a7-d2c1-44b4-aaf5-c95a93b2ab49"
}

response = requests.post(endpoint, headers=headers, data=json.dumps(data))
#print(type(response.json()))
output = response.json()
returnval = (output["records"][0]["best_label"]["name"])

print((output["records"][0]["best_label"]["name"]))

#print(output["records"])
#print(json.dumps(response.json(), indent=2))
