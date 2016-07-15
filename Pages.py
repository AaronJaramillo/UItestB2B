from Navigations import Nav
from selenium.webdriver.common.keys import Keys
import time
class Page:

	def log_in(self, driver):
		userNav = Nav()
		userNav.userBar_nav(driver)
		userNav.log_in.click()
		userNav.username.send_keys('AuditAaron')
		userNav.password.send_keys('Emser12345')
		userNav.login_button.click()

	def orderPad_buy(self, driver):
		self.orderPadNavs = Nav()
		self.orderPadNavs.orderPad_nav(driver)

	def listPage(self, driver):
		self.listNav = Nav()
		self.listNav.mainUserNav(driver)
		self.listNav.listNavs(driver)

	def addListPage(self, driver):
		self.addList = Nav()
		self.addList.mainUserNav(driver)
		self.addList.addListNav(driver)

	def getCartCount(self, driver):
		self.cartNavs = Nav()
		self.cartNavs.cartCount(driver)
		self.userCartCount = self.cartNavs.cartCounter.text

	def excelUploadPage(self, driver):
		self.uploadNavs = Nav()
		self.uploadNavs.xCellUpload_button(driver).click()
		self.uploadNavs.excelNavs(driver)

	def productPurchase(self, driver):
		self.ATC_button = Nav().getProduct_ATC(driver)
		self.QTYbox = Nav().getQTYBox(1, driver)
		self.ATL_button = Nav().getAddToList(driver)

	def shopBotticino(self, driver):
		return driver.get('https://b2b.emser.com/ERP2Web50/e2wShoppingCatalog.aspx?parentId=3100001696&parentLink=2100000341:3100001690:3100001695:3100001696')
	
	def shopCordova(self, driver):
		return driver.get('https://b2b.emser.com/ERP2Web50/e2wShoppingCatalog.aspx?parentId=3100002136&parentLink=2100000341:3100001672:3100001673:3100002136')
	
	def gotoCart(self, driver):
		cart = Nav()
		cart.cartButton(driver)
		cart.myCart.click()
	
	def cart(self, driver):
		cartNav = Nav()
		cartNav.cartNavs(driver)
		self.emptyCart = cartNav.emptyCart_button
		self.checkout_button = cartNav.checkout_button

	def orderInfo(self, driver):
		self.orderNav = Nav()
		self.orderNav.getOrderNavs(driver)

	def logUserOut(self, driver):
		userNav = Nav()
		userNav.logOut(driver)
		userNav.sign_outLink.click()
