from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# ChromeDriver yolu
chrome_driver_path = "C:\\chromedriver-win64\\chromedriver.exe"

# WebDriver
service = Service(chrome_driver_path)
driver = Chrome(service=service)

driver.get("http://okkess.online/Iletisim.aspx")  # Formun bulunduğu URL


try:
    # Ad alanı
    ad = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$TxtAd")
    ad.send_keys("John")

    
    # E-posta alanı
    email = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$TxtMail")  
    email.send_keys("john.doe@example.com")
    
    # Konu alanı
    konu = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$TxtKonu")
    konu.send_keys("Öneri")

    # Mesaj alanı
    mesaj = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$TxtMesaj")
    mesaj.send_keys("Bu bir test mesajıdır.")

    # Submit butonu
    submit_button = driver.find_element(By.ID, "ContentPlaceHolder1_Button1")
    submit_button.click()
    
    # Beklenen URL'ye yönlendirilip yönlendirilmediği
    assert "http://okkess.online/Anasayfa.aspx" in driver.current_url or "Başarılı" in driver.page_source
    print("Form başarıyla gönderildi.")
except Exception as e:
    print("Form gönderimi başarısız veya hata var: ", str(e))

# Tarayıcıyı kapatın
driver.quit()
