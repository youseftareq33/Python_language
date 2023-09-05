import math,random,json
from datetime import datetime

print("power in math: ",math.pow(3,2))
print("---------------------------------")
print("current date and time in datetime: ",datetime.now())
print("---------------------------------")
print("random integer from (1,100) in random: ",random.randint(1,100))
print("---------------------------------")
json_text='{"id":1202057,"name":"Ahmad","age":25}'
json_adapter= json.loads(json_text)
print("get the name from json format in json: "+json_adapter["name"])
