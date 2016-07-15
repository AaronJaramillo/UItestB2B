class Nav:

	def filterLinks_byTag(self, text, driver):
		elements = driver.find_elements_by_tag_name('a')
		for i in elements:
			if i.text == text:
				return i.click()
	def goHome(self, driver):
		homeButtton = driver.find_element_by_xpath('/html/body/form/div[2]/div/header/div[2]/div[1]/div/div[1]/h1/a/img').click()

	def orderPad_nav(self, driver):
		self.orderItemBox = driver.find_element_by_xpath('//*[@id="ctl00_E2wOrderPad1_DataGrid1_ctl02_txtitem"]')
		self.QTYbox = driver.find_element_by_css_selector("input#ctl00_E2wOrderPad1_DataGrid1_ctl02_txtQty.form-control")
		self.add_button = driver.find_element_by_xpath("/html/body/form/div[2]/div/section/div/div/div/div/aside/div/div/div/div/div[3]/div/input[2]")
	
	def userBar_nav(self, driver):
		self.log_in = driver.find_element_by_xpath('//*[@id="ctl00_E2wHeader1_LoginView1_lbl1_Login"]')
		self.username = driver.find_element_by_id('ctl00_E2wHeader1_txtUserId')
		self.password = driver.find_element_by_id('ctl00_E2wHeader1_txtPassword')
		self.login_button = driver.find_element_by_id('ctl00_E2wHeader1_btn1_login')
	
	def mainUserNav(self, driver):
		self.logOut(driver)
		self.cartButton(driver) 
		self.myLists = driver.find_element_by_id("ctl00_E2wHeader1_lbl1_MyList")
		self.myAccount = driver.find_element_by_id("ctl00_E2wHeader1_lbl1_Account")

	def listNavs(self, driver):
		self.listName_box = driver.find_element_by_id("ctl00_CustomerMainContent_txtlistname")
		self.listDescription_box = driver.find_element_by_id("ctl00_CustomerMainContent_txtDesc")
		self.addList = driver.find_element_by_id("ctl00_CustomerMainContent_btn_AddList")
		self.deleteList = driver.find_element_by_id("ctl00_CustomerMainContent_btn_deleteList")
		try:
			self.addListToCart = driver.find_element_by_id("ctl00_CustomerMainContent_btn_addtocart")
		except:
			print("failed to load button")

	def confirm(self, driver):
		return driver.find_element_by_id("ctl00_CustomerMainContent_btn_yes")
	
	def listRadio(self, driver):
		return driver.find_element_by_id("radio1")
		
	def getMetaList(self, driver):
		try:
			return driver.find_element_by_css_selector("table#ctl00_CustomerMainContent_DgItems.Grid>tbody>tr.GridRow>td")
		except:
			pass

	def addListNav(self, driver):
		self.addlistName = driver.find_element_by_id("ctl00_CustomerMainContent_txtListName")
		self.addlistDescription = driver.find_element_by_id("ctl00_CustomerMainContent_txtDesc")
		self.addnewList = driver.find_element_by_id("ctl00_CustomerMainContent_btn_add")


	def logOut(self, driver):
		self.sign_outLink = driver.find_element_by_xpath("/html/body/form/div[2]/div/header/div[1]/div/div/div[2]/div/div/p/a[2]/span")

	def cartButton(self, driver):
		self.myCart = driver.find_element_by_css_selector('a#ctl00_E2wHeader1_lnk1ViewCart i.top-icon.fa.fa-shopping-cart')
	
	def cartCount(self, driver):
		self.cartCounter = driver.find_element_by_id('ctl00_E2wHeader1_e2wCart_lbl1CartItemCount')
	
	def cartNavs(self, driver):
		self.emptyCart_button = driver.find_element_by_id('ctl00_CustomerMainContent_btn_EmptyCart')
		self.checkout_button = driver.find_element_by_id('ctl00_CustomerMainContent_btn_ProceedToCheckout')
	
	def click_navBar(self, label, driver):
		self.filterLinks_byTag(label, driver)
	
	def click_productMenu(self, label, driver):
		self.filterLinks_byTag(label, driver)
	
	def click_categoryMenu(self, label, driver):
		self.filterLinks_byTag(label, driver)	
	
	def click_categorySubMenu(self, label, driver):
		self.filterLinks_byTag(label, driver)
	
	def xCellUpload_button(self, driver):
		return driver.find_element_by_id("ctl00_CustomerMainContent_btn_uploadfromexcel")
	
	def excelNavs(self, driver):
		self.ATC = driver.find_element_by_id('ctl00_CustomerMainContent_btn_upload')
		self.sheetName = driver.find_element_by_id('ctl00_CustomerMainContent_txt_sheetname')
		self.upload = driver.find_element_by_id('ctl00_CustomerMainContent_fileUpload')
	
	def addItemtoList(self, driver):
		return driver.find_element_by_id('ctl00_CustomerMainContent_btn_additems')

	def getAddToList(self, driver):
		return driver.find_element_by_id('ctl00_CustomerMainContent_e2wItemLayout1_lnkbtn1_addtolist')
	
	def getQTYBox(self, boxNum, driver):
		box = "/html/body/form/div[2]/div/section/div/div/div/div/div/div[6]/div/div[2]/div/div/div[" + str(boxNum) +"]/div/div/div[2]/div[2]/div/ul/li[3]/div/div/input"
		return driver.find_element_by_xpath(box)
		
	def getProduct_ATC(self, driver):
		return driver.find_element_by_id('ctl00_CustomerMainContent_e2wItemLayout1_lnkbtn1_addtocart')

	def getOrderNavs(self, driver):
		self.PONum = driver.find_element_by_id('ctl00_CustomerMainContent_TBCustPO')
		self.continueButton = driver.find_element_by_id('ctl00_CustomerMainContent_btn_Continue')

	def confirmPay(self, driver):
		driver.find_element_by_id("ctl00_CustomerMainContent_btn_PayAndConfirm").click()