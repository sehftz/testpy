import os
import requests
import datetime
print("hi!!!!!!!!!!")
r=requests.post(os.getenv("WH"), files={"a.txt":"m"*3000})
