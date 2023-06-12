import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""
# write code to print the value of key2
data = json.loads(sampleJson)

print(data['key2'])
