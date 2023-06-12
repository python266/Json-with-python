import json

sampleJson = {"id": 1, "name": "value2", "age": 29}

data = json.dumps(sampleJson,indent=2,sort_keys=True)
print(data)

with open("Json.txt", "w") as f:
    f.write(data)
    print(f)
f.close()