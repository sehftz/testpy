import os
import requests
import datetime
print("hi!!!!!!!!!!")
r=requests.post(os.getenv("WH"), files={"file":("a.txt","m\n"*9000)})
