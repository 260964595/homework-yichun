from selenium import webdriver
import time
def login(self):
	dr=self.dr
	dr.get(self.login_url)
	time.sleep(2)
	dr.find_element_by_name('log').send_keys('admin')
	dr.find_element_by_name('pwd').send_keys('admin')
	dr.find_element_by_name('wp-submit').click()
	print dr.current_url