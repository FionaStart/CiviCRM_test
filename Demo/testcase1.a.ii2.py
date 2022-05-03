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
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[4]/nav/ul/li[3]/ul/li[1]').click()
    driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div/div/div[2]/form/div[2]/div/div/div/div[2]/div[5]/button').click()   #Click Search
    driver.find_element(By.XPATH, '//*[@id="rowid155"]/td[3]/a').click()   # Select contact 1,1
    driver.find_element(By.XPATH, '//*[@id="ui-id-12"]').click()          #Click Relationships

#--------------------Add relationships to validate current/inactive relationship-----#
def add_relationship(startdate, enddate, enabled, select_contact_xpath):

    driver.find_element(By.CSS_SELECTOR, '#contact-summary-relationship-tab > div.action-link > a').click()#Click Add Relationship
    driver.implicitly_wait(10)
    web_load()
    driver.find_element(By.CSS_SELECTOR, '#s2id_relationship_type_id > a > span.select2-arrow').click()#Select Relationship Type
    driver.implicitly_wait(10)
    web_load()
    #ul = driver.find_element(By.CSS_SELECTOR, '#select2-results-26')
    ul = driver.find_element(By.XPATH, '/html/body/div[14]/ul')
    #ul.find_element(By.CSS_SELECTOR, '#select2-result-label-4').click()# Type = Benifits Specialist is
    ul.find_element(By.XPATH, '/html/body/div[14]/ul/li[1]').click()# Type = Benifits Specialist is
    ul = driver.find_element(By.CSS_SELECTOR, '#s2id_related_contact_id')
    ul.find_element(By.CSS_SELECTOR, '#s2id_autogen2').send_keys('1')#Select Contacts, type in '1'
    #web_load()
    #driver.implicitly_wait(20)
    ul = driver.find_element(By.XPATH, '/html/body/div[16]/ul')
    ul.find_element(By.XPATH, select_contact_xpath).click()  #Select different Contact to avoid insert duplicated data

    if startdate!=None:

       driver.find_element(By.XPATH, '/html/body/div[10]/div[2]/form/div[2]/table/tbody/tr[4]/td[2]/span[1]/input[2]').send_keys(startdate) #Input Startdate
    if enddate!=None:
       driver.find_element(By.XPATH, '/html/body/div[10]/div[2]/form/div[2]/table/tbody/tr[4]/td[2]/span[2]/input[2]').send_keys(enddate) #Input Enddate

    if enabled == 'NO':
       driver.find_element(By.XPATH, '/html/body/div[10]/div[2]/form/div[2]/table/tbody/tr[9]/td[2]/input[2]').click()  # Enabled NO


    driver.find_element(By.XPATH, '/html/body/div[10]/div[11]/div/button[1]').click() #Save Relataionship
    web_load()
    now_time = time.strftime("%Y_%m_%d %H_%M_%S")
    driver.get_screenshot_as_file('img_{}_TestCase1.a.ii2.png'.format(now_time))  # Screenshot and save named with current time
    js = "var q=document.documentElement.scrollTop=10000"  # scroll page down
    driver.execute_script(js)
    web_load()
    driver.get_screenshot_as_file('img_{}_TestCase1.a.ii2_down.png'.format(now_time))  # Screenshot and save inactive relathonship

def web_close(): #Close page
    driver.quit()

def web_load():  #Page wait
    time.sleep(loading_time)

if __name__=='__main__':
    web_init()
    auto_login(username, pwd, uid_xpath, pwd_xpath, button_xpath)
    val_contact_relation()

# test case1.a.ii: Start date = Null, Enddate > today, Enabled = NO
    add_relationship(None, '05/05/2022', 'NO', '/html/body/div[16]/ul/li[5]')
    web_close()




