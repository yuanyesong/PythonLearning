from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from PIL import Image
import random

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
url = "http://59.52.128.92:8000/Forward/to?id=VerifyCode"+"&_id="
for i in range(0, 100):
    rad = random.random()
    captcha_url = url + str(rad)
    print(captcha_url)
    driver.get(captcha_url)
    driver.get("http://59.52.128.92:8000/VerifyCode/Code")
    print(driver.page_source)
    try:
        element = WebDriverWait(driver, 10, 0.5).until(
            lambda x: x.find_element_by_tag_name("img").is_displayed())
    finally:
        range = (0, 0, 72, 22)
        driver.save_screenshot("./sample/screenshot/" + str(i) + ".png")
        screenshot = Image.open("./sample/screenshot/" + str(i) + ".png")
        captchaImg = screenshot.crop(range)
        captchaImg.save("./sample/captcha/" + str(i)+".png")

driver.close()