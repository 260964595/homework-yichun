from selenium import webdriver
import unittest
import time
import login
import random
class WordPressLogin(unittest.TestCase):
	login_url='http://localhost/wordpress/wp-login.php'
	def setUp(self):
		self.dr=webdriver.Chrome()
	def test_login(self):
		#self.dr.get(self.login_url)
		login.login(self)
		'''self.dr.get(self.login_url)
		time.sleep(2)

		self.dr.find_element_by_name('log').send_keys('admin')
		self.dr.find_element_by_name('pwd').send_keys('admin')
		self.dr.find_element_by_name('wp-submit').click()
		print self.dr.current_url
		self.assertTrue('wp-admin' in self.dr.current_url)
		'''
	def test_createArticle(self):
		'''self.dr.get(self.login_url)
		time.sleep(2)

		self.dr.find_element_by_name('log').send_keys('admin')
		self.dr.find_element_by_name('pwd').send_keys('admin')
		self.dr.find_element_by_name('wp-submit').click()
		'''
		login.login(self)
		time.sleep(2)
		create_url='http://localhost/WordPress/wp-admin/post-new.php'
		title_or_content='new post'+str(time.time())
		self.dr.get(create_url)
		time.sleep(2)
		self.dr.find_element_by_name('post_title').send_keys(title_or_content)
		js="document.getElementById('content_ifr').contentWindow.document.body.innerHTML='"+title_or_content+"'"
		print js
		self.dr.execute_script(js)
		self.dr.find_element_by_name('publish').click()
		self.dr.get('http://localhost/WordPress/wp-admin/edit.php')
		self.assertTrue(title_or_content in self.dr.find_element_by_class_name('wp-list-table').text)
	def test_editArticle(self):
		login.login(self)
		time.sleep(2)

		elements=self.dr.find_elements_by_xpath("//input[@type='checkbox']")
		the_max=len(elements)
		index=random.randint(1,the_max-1)
		edit_url='http://localhost/WordPress/wp-admin/post.php?post='+str(index)+'&action=edit'
		title_or_content='edit post'+str(time.time())
		self.dr.get(edit_url)
		time.sleep(2)
		self.dr.find_element_by_name('post_title').send_keys(title_or_content)
		js="document.getElementById('content_ifr').contentWindow.document.body.innerHTML='"+title_or_content+"'"
		print js
		self.dr.execute_script(js)
		self.dr.find_element_by_name('save').click()
		self.dr.get('http://localhost/WordPress/wp-admin/edit.php')
		self.assertTrue(title_or_content in self.dr.find_element_by_class_name('wp-list-table').text)
    def test_delArticle(self):


	def tearDown(self):
		time.sleep(2)
		self.dr.quit()
if __name__=='__main__':
	unittest.main()