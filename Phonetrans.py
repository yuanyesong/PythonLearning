import requests

url = "http://59.52.128.92:8000"
login_url = url + "/Login/login"
captcha_url = url + "/Forward/to?id=VerifyCode/Code"
headers = {
    "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "59.52.128.92:8000",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2729.4 Safari/537.36"
}
login_data = {
    "userName": "baidujxtgb",
    "userPwd": "baidujxtgb"
}

captcha_header = {
    "Accept": "image/webp,image/*,*/*;q=0.8",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Host": "59.52.128.92:8000",
    "Referer": "http://59.52.128.92:8000/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2729.4 Safari/537.36"
}


captcha = requests.get(captcha_url, stream=True)
print(captcha.content)
with open("Code.jpg", "wb") as f:
    f.write(captcha.content)
print("请输入验证码")
verifycode = input("验证码: ")
login_data["verifycode"] = verifycode
requests.post(login_url, headers, login_data)
response = requests.get("http://59.52.128.92:8000/Login/index")
print(response.text)