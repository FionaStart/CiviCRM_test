from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = "civicrm_user"
pwd = "civicrm_user"
loading_time = 10
uid_xpath = '//*[@id="edit-name"]'
pwd_xpath = '//*[@id="edit-pass"]'
button_xpath = '//*[@id="edit-submit"]'
login_url = r"https://qa-test:1z2a6iTzNmKPvHga@online-qa-test.ccdemo.site/"

driver = webdriver.Chrome()

#-----------------------Web Initiate-----------------------------#
def web_init():
    driver.maximize_window()       #Maximize window
    driver.implicitly_wait(10)     #Wait 10s
    driver.get(login_url)          #Open website https://online-qa-test.ccdemo.site/ 

#--------------------Auto login----------------------------------#
def auto_login(username, pwd, uid_xpath, pwd_xpath, button_xpath):

    web_load()
    driver.find_element(By.XPATH, uid_xpath).clear()   #Clear content in
    driver.find_element(By.XPATH, uid_xpath).send_keys(username)
    driver.find_element(By.XPATH, pwd_xpath).clear()
    driver.find_element(By.XPATH, pwd_xpath).send_keys(pwd)
    web_load()
    driver.find_element(By.XPATH, button_xpath).click()

#-------------------Find contact Mr.1.1,Locate Relationships----------------------#
def val_contact_relation():
    driver.find_element(By.LINK_TEXT, 'Search').click()
    web_load()
    driver.find_element(By.XPATH, '/html/body/div[4]/nav/ul/li[3]/ul/li[1]').click()
    driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div/div/div[2]/form/div[2]/div/div/div/div[2]/div[5]/button').click()   #Click Search
    driver.find_element(By.XPATH, '//*[@id="rowid155"]/td[3]/a').click()   # Select contact 1,1
    driver.find_element(By.XPATH, '//*[@id="ui-id-12"]').click()          #Click Relationships

#--------------------Add relationships to validate employee relationship-----#
def add_relationship(linkedin_url, website_url):

    driver.find_element(By.CSS_SELECTOR, '#contact-summary-relationship-tab > div.action-link > a').click()#Click Add Relationship
    driver.implicitly_wait(10)
    web_load()
    driver.find_element(By.CSS_SELECTOR, '#s2id_relationship_type_id > a > span.select2-arrow').click()#Select Relationship Type
    driver.implicitly_wait(10)
    web_load()
    driver.find_element(By.XPATH, '/html/body/div[14]/div/input').send_keys('E')
    driver.find_element(By.XPATH, '/html/body/div[14]/ul/li[5]').click()# Type = Employee of
    ul = driver.find_element(By.CSS_SELECTOR, '#s2id_related_contact_id')
    ul.find_element(By.CSS_SELECTOR, '#s2id_autogen2').send_keys('1')#Select Contacts, type in '1'
    ul = driver.find_element(By.XPATH, '/html/body/div[16]/ul')
    ul.find_element(By.XPATH, '//*[@id="select2-drop"]/ul/li[3]').click()  #Select a Contact

    ul = driver.find_element(By.XPATH, '/html/body/div[10]/div[2]/form/div[2]/div[1]/div[2]/div[2]')
    ul.find_element(By.XPATH, '/html/body/div[10]/div[2]/form/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]/input').send_keys(linkedin_url)
    driver.find_element(By.XPATH, '/html/body/div[10]/div[2]/form/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[2]/input').send_keys(website_url)

    driver.find_element(By.XPATH, '/html/body/div[10]/div[11]/div/button[1]').click() #Save Relataionship

    web_load()   # Screenshot and save named with current time
    now_time = time.strftime("%Y_%m_%d %H_%M_%S")
    driver.get_screenshot_as_file('img_{}_TestCase2.b.png'.format(now_time))

def web_close(): #Close page
    driver.quit()

def web_load():  #Page wait
    time.sleep(loading_time)

if __name__=='__main__':
    web_init()
    auto_login(username, pwd, uid_xpath, pwd_xpath, button_xpath)
    val_contact_relation()
# test case2.a: LinkedIn = URL,Websites =NoneURL
    add_relationship('http://www.linkedin.com/in/fangzhou-li', 'website_url')
    web_close()


