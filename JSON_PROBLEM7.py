import json

data = {
   "company":{
      "employee":{
         "name":"emma",
         "payble":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}

try:
    check = json.dumps(data)
    print(check)
except:
    raise ValueError("Bro-Bro Something went wrong. Try Again")
