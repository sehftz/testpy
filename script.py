from os import getenv
from requests import get, post
from re import findall
from socket import socket

def request(path):
    with socket() as sock:
        sock.connect((getenv("LK"),80))
        sock.send(f"GET {path} HTTP/1.0\r\nHost:{getenv('LK')}\r\nConnection:close\r\n\r\n".encode())
        buf = b""
        while data := sock.recv(4096):
            buf += data
        print(buf)
        return buf.decode()

def c_m():
    return findall(r"(?s)ID (\d+).*?> (.*?)<.*?> (.*?)<.*?> (.*?)<.*?s\((.*?), (.*?)\)", request(getenv("LK_C_M")))

print("hi!!!!!!!!!!")
c_abs_last = get(get(getenv("WH_C_ABS_LAST")).json()["attachments"][0]["url"]).text
c_abs_last = [chunk.split("\n") for chunk in c_abs_last.split("\n\n")]
c_abs_current = c_m()

diff = []

for last, current in zip(c_abs_last, c_abs_current):
    if tuple(last) != current:
        diff.append(current)

if len(diff) > 0:
    post(getenv("WH"), files={"file":("a.txt","\n\n".join("\n".join(e) for e in diff))})
