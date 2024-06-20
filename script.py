import os,requests
import datetime
print("hi!!!!!!!!!!")
r=requests.post(os.getenv("WH"), json={"content":datetime.datetime.now().isoformat()})
