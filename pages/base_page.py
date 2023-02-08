from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser


class Base_page(Browser):
		COOKIES_BUTTON = (By.ID,"gdpr-banner-accept")
		def accept_cookies(self):
				try:
						self.chrome.find_element(*self.COOKIES_BUTTON).click()
				except:
						pass

		def wait_and_click_element_by_selector(self, by, selector):
				WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((by, selector)))
				self.chrome.find_element(by,selector).click()