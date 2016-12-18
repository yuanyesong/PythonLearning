from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
from PIL import Image
# import random
import pytesseract

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2729.4 Safari/537.36"
)
phantomjs_executable_path = "D:/Program Files (x86)/phantomjs-2.1.1/"\
                            "phantomjs-2.1.1-windows/bin/phantomjs"
driver = webdriver.PhantomJS(
    executable_path=phantomjs_executable_path,
    port=0,
    desired_capabilities=dcap)
url = "http://59.52.128.92:8000"
login_url = url + "/Login/login"
homepage = url+"/Login/index"
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
login_data = {"userName": "baidujxtgb", "userPwd": "baidujxtgb"}
driver.get(url)
try:
    element = WebDriverWait(
        driver, 10, 0.5).until(lambda x: x.find_element_by_id("imgCode").is_displayed())
finally:
    print(driver.find_element_by_id("imgCode").get_attribute("title"))
    # print(driver.page_source)
    cookies = driver.get_cookies()
    print(cookies)
    s = requests.Session()
    for cookie in cookies:
        s.cookies.set(cookie['name'], cookie['value'])
    # for cookie in s.cookies.items:
    #     print(cookie['name'], cookie['value'])
    print('; '.join(['='.join(item) for item in s.cookies.items()]))
    # verifyCode_url = driver.find_element_by_id("imgCode").get_attribute("src")
    # print(verifyCode_url)
    # rad=random.random()
    # captcha_url=verifyCode_url+"&_id="+str(rad)
    # print(captcha_url)
    # driver.get(captcha_url)
    # print(driver.page_source)
    # with open("Code.jpg","wb") as f:
    #     f.write(captcha.content)
    # with open("Code.html", "w") as f:
    #     f.write(driver.page_source)
    driver.save_screenshot("screenshot.png")
    imgElement = driver.find_element_by_id("imgCode")
    left = imgElement.location["x"]
    top = imgElement.location["y"]
    right = imgElement.size["width"]
    bottom = imgElement.size["height"]
    screenshot = Image.open("screenshot.png")
    box = (left, top, left+right-3, top+bottom)
    print(box)
    captchaImg = screenshot.crop(box)
    captchaImg.save("captcha.png")
    verifycode = input("验证码: ")
    login_data["verifycode"] = verifycode
    requests.post(login_url, headers, login_data)
    driver.get(homepage)
    print(driver.page_source)
    try:
        element = WebDriverWait(
            driver, 10, 0.5).until(
                lambda x: x.find_element_by_id("ext-gen62").is_displayed())
    finally:
        print(driver.find_element_by_id("ext-gen62").text)
    driver.close()
