import time
import requests


class NocaptchaAi:
    def __init__(self,apikey):
        self.apikey = apikey
    
    def log(self,data):
        open('logs.log','a+').write(f'{data}\n')
    
    def req(self,url=None,headers=None,data=None):
        while True:
            try:
                if data is None:
                    res = requests.get(url,headers=headers)
                    return res.text
                
                res = requests.post(url,headers=headers,json=data)
                return res.text
            
            except (requests.exceptions.ConnectionError,requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout):
                print("[x] connection error / timeout ",flush=True,end='\r')
                time.sleep(3)
                print("                                  ",flush=True,end="\r")
                continue
        
    def hcaptcha_token(self,site_key,site_url,user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"):
        url_in = "https://token.nocaptchaai.com/token"
        headers = {"Content-Type": "application/json", "apikey": self.apikey}
        data = {
            "url": site_url,
            "sitekey": site_key,
            "useragent": user_agent
        }
        res = self.req(url_in,headers,data)
        self.log(res.text)
        url_res = res.json()['url']
        while True:
            res = self.req(url_res,headers)
            self.log(res.text)
            if res.json()['status'] == "processed":
                return True,res.json()['token']
            
            if res.json()['status'] == 'processing':
                time.sleep(3)
                continue
            
            if res.json()['status'] == 'failed':
                return False,res.text