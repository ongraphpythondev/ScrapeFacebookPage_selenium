from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


URL = "https://www.facebook.com/groups/622976662220480"
chrome_options = Options()
# chrome_options.add_argument("--headless")

chrome_service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.maximize_window()

driver.get(URL)

username = "Enter Username of FB"
password = "Enter Password of FB"

sleep(3)

# WebDriverWait(driver, 40).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div"))
#     ).click()
# sleep(2)
driver.find_element(By.ID, ":r5:").send_keys(username)
sleep(3)
driver.find_element(By.ID, ":r7:").send_keys(password)

driver.find_element(
    By.CSS_SELECTOR, "#login_popup_cta_form > div > div:nth-child(5) > div > div"
).click()
sleep(3)


print("------------------------------------------------------Image Url-----------------------------------------------------")
GroupImage = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div/a/div/div/div/div/div/img').get_attribute("src")
print(GroupImage)


print("------------------------------------------------------About this group-----------------------------------------------------")

Title = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/div/span/div/div').text
History = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div[4]/div/div/div[2]/div/div[2]/span/span",
).text
sleep(2)

print(Title)
print(History)

print("------------------------------------------------------Members-----------------------------------------------------")
Members = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div/div/h2/span/span/span",
).text

sleep(2)

Admin = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span",
).text

sleep(2)
print(Members)
print(Admin)


print("------------------------------------------------------Activity-----------------------------------------------------")
TodayPost = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/span",
).text
LastPost = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/span",
).text

TotalMember = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]/span",
).text
NoMember = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/span",
).text
sleep(2)
CreatedAccount = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div[3]/div/div/div[2]/div/div/span",
).text
sleep(2)

print(TodayPost)
print(LastPost)
print(TotalMember)
print(NoMember)
print(CreatedAccount)


driver.quit()
