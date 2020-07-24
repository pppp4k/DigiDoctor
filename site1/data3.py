from ximilar.client import RestClient

pktoken = "1c8e08e081f62b6109512704cafafe622c26e36d"
pktask = '269f89a9-6077-4677-b4d4-e6311d029491'

client = RestClient(token=pktoken)
result = client.custom_endpoint_processing([{"_file": "testacne.jpg"}])
print(result)