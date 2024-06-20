import os,requests
import datetime
print("hi!!!!!!!!!!")
print(len(os.getenv("WH")))
r=requests.post(os.getenv("WH"), json={"content":datetime.datetime.now().isoformat()})
