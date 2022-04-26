import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:/chromedriver.exe")
driver = webdriver.Chrome(service=s)

# en yeni otomobilleri listeleyen sayfaya gidiyoruz
searchedListUrl = 'https://www.sahibinden.com/otomobil?sorting=date_desc#!'


def sendMessageToTelegram(message):
    chatUrl = "https://api.telegram.org/botXXXXXXXX:YYYYYYYYY/sendMessage?chat_id=ZZZZZZZZZZZ&text=" \
              + message
    driver.get(chatUrl)


def startBot():
    driver.maximize_window()
    time.sleep(2)
    driver.get(searchedListUrl)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[13]").click()  # reklamı geçtik


if __name__ == '__main__':
    old_url = ""
    startBot()

    while 1:
        driver.refresh()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "/html/body/div[5]/div[4]/form/div/div[3]/table/tbody/tr[1]/td[5]/a[1]").click()  # ilanının linkine tıkladık
        currentUrl = driver.current_url
        if old_url == currentUrl:
            pass
        else:
            old_url = currentUrl
            sendMessageToTelegram(currentUrl)
            driver.back()
        driver.back()
        time.sleep(60)  # kaç saniye bekleyeceğini ayarlıyoruz
