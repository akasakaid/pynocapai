# Pynocapai

Unofficial Library for nocaptchaai

# Installation

```
pip install pynocapai
```

# Available Method

## hcaptcha_token

get solve token for hcaptcha

```
from pynocapai import NocaptchaAi

sitekey="a5f74b19-9e45-40e0-b45d-47ff91b7a6c2"
site_url="accounts.hcaptcha.com"
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"

ai = NocaptchaAi('<apikey>')
status,solve = ai.hcaptcha_token(sitekey=sitekey,site_url=site_url,user_agent=user_agent)

if status:
    print(solve)
else:
    print(solve)
```