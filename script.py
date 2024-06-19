import os,requests
print("hi!!!!!!!!!!")
print(len(os.getenv("WH")))
r=requests.post(os.getenv("WH"), json={"content":":)))))"})
