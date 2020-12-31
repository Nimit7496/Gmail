import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import autoit


driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\OneDrive\\Desktop\\Assig\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%"
           "2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&"
           "flowEntry=ServiceLogin")
driver.maximize_window()
# Email
driver.find_element_by_id("identifierId").send_keys("autoworld7496")
# Next button
driver.find_element_by_class_name("VfPpkd-RLmnJb").click()
# Pass
driver.find_element_by_name("password").send_keys("Auto@1234")
# Pass Next Button
driver.find_element_by_css_selector("#passwordNext > div > button > div.VfPpkd-RLmnJb").click()
time.sleep(3)
# Compose Button
driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div"
                             "/div").click()
time.sleep(3)
# TO
to = driver.find_element_by_tag_name("textarea")
driver.implicitly_wait(5)
to.clear()
to.send_keys("nimitsharma4@gmail.com")
to.send_keys(Keys.ENTER)
time.sleep(3)

# Subject
sub = driver.find_element_by_name("subjectbox")
driver.implicitly_wait(5)
sub.click()
sub.send_keys("TESTING")

# Content
time.sleep(3)
txt = driver.find_element_by_xpath("//div[@class = 'Am Al editable LW-avf tS-tW']")
driver.implicitly_wait(5)
txt.send_keys("This mail is automated generated through python selenium")

# Attachment
time.sleep(3)
ele = driver.find_element_by_xpath("//div[@class='a1 aaA aMZ']")
time.sleep(5)
ele.click()
time.sleep(5)

upload = ("C:\\Users\\Admin\\PycharmProjects\\Gmail\\venv\\Tests\\Fileupload.exe")
autoit.run(upload)

# Send

snd = driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")
driver.implicitly_wait(5)
snd.click()
print("Email Sent Successfully ")

driver.close()
