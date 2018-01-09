from selenium import webdriver




driver = webdriver.Chrome('C:\\Users\Administrator\Desktop\chromedriver.exe')
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')


driver.add_cookie({'name':'_jc_save_fromStation','value':'%u5317%u4EAC%2CBJP'})
driver.add_cookie({'name':'_jc_save_toStation','value':'%u5929%u6D25%2CTJP'})
driver.add_cookie({'name':'_jc_save_fromDate','value':'2018-01-09'})

driver.refresh()


driver.find_element_by_id('query_ticket').click()

hemlpag = driver.page_source
print(hemlpag)