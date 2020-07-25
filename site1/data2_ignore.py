import http.client, urllib.parse, json
from urllib.parse import urlparse
from ximilar.client import RecognitionClient, DetectionClient
import requests
import base64

pktoken = "1c8e08e081f62b6109512704cafafe622c26e36d"
pktask = '269f89a9-6077-4677-b4d4-e6311d029491'
app_client = RecognitionClient(token=pktoken)
#detect_client = DetectionClient(token="0fdd6a2783765b4238beeabd677f1d9da04c902c")
client = RecognitionClient(token=pktoken)
task, status = client.get_task(task_id=pktask)
#tasks, status = client.get_all_tasks()
print(task)
result = task.classify([{'_file', 'testacne.jpg'}])
print(result)
# the result is in json/dictionary format and you can access it in following way:
best_label = result['records'][0]['best_label']
print(best_label)
