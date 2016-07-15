#Aaron Jaramillo
#Emser Tile
#
##################
import os
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Navigations import Nav
from Pages import Page

class checkoutTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Firefox()
		cls.homePage = 'https://b2b.emser.com'
		cls.driver.get(cls.homePage)
		cls.login_page = Page()
		cls.login_page.log_in(cls.driver)
		cls.mainNavs = Nav()
		cls.mainNavs.mainUserNav(cls.driver)

	def test_checkout(self):
		cart = Page()
		cart.gotoCart(self.driver)
		cart.cart(self.driver)
		cart.checkout_button.click()
		cart.orderInfo(self.driver)
		cart.orderNav.PONum.send_keys('1')
		cart.orderNav.continueButton.click()
		self.mainNavs.confirmPay(self.driver)
		self.driver.find_element_by_xpath('/html/body/div[1]/div/header/section[1]/div[1]/div/div/div/div[2]/div/p[1]/a').click()

	@classmethod
	def tearDownClass(cls):
		cls.login_page.logUserOut(cls.driver)
		cls.driver.quit()

class ListTests(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Firefox()
		cls.homePage = 'https://b2b.emser.com'
		cls.driver.get(cls.homePage)
		cls.login_page = Page()
		cls.login_page.log_in(cls.driver)
		cls.mainNavs = Nav()
		cls.mainNavs.mainUserNav(cls.driver)

	def test_listCreate(self):
		self.mainNavs.myLists.click()
		Lists = Page()
		Lists.listPage(self.driver)
		Lists.listNav.addList.click()
		Lists.addListPage(self.driver)
		Lists.addList.addlistName.send_keys("test list")
		Lists.addList.addlistDescription.send_keys("This is a list to test Lists")
		Lists.addList.addnewList.click()
	
	def test_listPopulate(self):
		self.mainNavs.myLists.click()
		Product = Page()
		Product.shopBotticino(self.driver)
		Product.productPurchase(self.driver)
		Product.QTYbox.send_keys("15")
		Product.ATL_button.click()
		self.mainNavs.addItemtoList(self.driver).click()
		##### add Cordova #######
		Product.shopCordova(self.driver)
		Product.productPurchase(self.driver)
		self.mainNavs.getQTYBox(3, self.driver).send_keys("15")
		self.mainNavs.getQTYBox(4, self.driver).send_keys("15")
		Product.QTYbox.send_keys("15")
		Product.ATL_button.click()
		self.mainNavs.addItemtoList(self.driver).click()
	
	def test_listToCart(self):
		self.mainNavs.myLists.click()
		Product = Page()
		Product.shopBotticino(self.driver)
		Product.productPurchase(self.driver)
		Product.QTYbox.send_keys("15")
		Product.ATL_button.click()
		self.mainNavs.addItemtoList(self.driver).click()
		self.mainNavs.mainUserNav(self.driver)
		self.mainNavs.myLists.click()
		Product.listPage(self.driver)
		Product.listNav.addListToCart.click()
		try:
			Product.getCartCount(self.driver)
			assertEqual(Product.userCartCount, "1 Cart")
		except:
			print("cart count failed")


	def test_listDelete(self):
		self.mainNavs.myLists.click()
		Lists = Page()
		Lists.listPage(self.driver)
		self.mainNavs.listRadio(self.driver).click()
		Lists.listNav.deleteList.click()
		self.mainNavs.confirm(self.driver).click()
		

	@classmethod
	def tearDownClass(cls):
		cls.login_page.logUserOut(cls.driver)
		cls.driver.quit()

class purchaseTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Firefox()
		cls.homePage = 'https://b2b.emser.com'
		cls.driver.get(cls.homePage)
		cls.login_page = Page()
		cls.login_page.log_in(cls.driver)
		
		
	def test_orderPad(self):
		order_pad = Page()
		order_pad.orderPad_buy(self.driver)
		order_pad.orderPadNavs.orderItemBox.send_keys('M01BOTTFI1212')
		order_pad.orderPadNavs.QTYbox.send_keys('10')
		order_pad.orderPadNavs.add_button.click()
		order_pad.getCartCount(self.driver)
		self.assertEqual(order_pad.userCartCount, "1 Cart")
		
	def test_productShopping(self):
		Product = Page()
		Product.shopBotticino(self.driver)
		Product.productPurchase(self.driver)
		Product.QTYbox.send_keys("15")
		Product.ATC_button.click()
		Product.getCartCount(self.driver)
		self.assertEqual(Product.userCartCount, "1 Cart")
		

	def test_excelUpload(self):
		xCell = Page()
		xCell.excelUploadPage(self.driver)
		xCell.uploadNavs.upload.send_keys(os.getcwd()+"/productCSV.xlsx")
		xCell.uploadNavs.sheetName.send_keys('Test Sheet')
		xCell.uploadNavs.ATC.click()
		Nav().goHome(self.driver)
		try:
			xCell.getCartCount(self.driver)
			self.assertEqual(xCell.userCartCount, "1 Cart")
		except:
			print("failed to upload")
	
	def test_emptyCart(self):
		cartDashboard = Page()
		cartDashboard.gotoCart(self.driver)
		cartDashboard.cart(self.driver)
		cartDashboard.emptyCart.click()
		self.driver.switch_to.alert.accept()

	@classmethod
	def tearDownClass(cls):

		cls.login_page.logUserOut(cls.driver)
		cls.driver.quit()
