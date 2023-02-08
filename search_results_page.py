from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import Base_page


class Search_results_page(Base_page):
		ELEMENT_TO_BE_ADDED_TO_CART = (By.XPATH,"//span[contains(text(),'Apple iPhone 14 Pro Unlocked eSim, Pre-Order..')]")
		COLOUR_DROPDOWN = (By.ID,"x-msku__select-box-1000")
		STORAGE_CAPACITY_DROPDOWN = (By.ID,"x-msku__select-box-1001")
		LOCK_STATUS_DROPDOWN = (By.ID,"x-msku__select-box-1002")
		SIM_CARD_SLOT = (By.ID,"x-msku__select-box-1003")
		property_dictionary = {}
		property = []

		def open_identified_product(self):
				self.chrome.find_element(*self.ELEMENT_TO_BE_ADDED_TO_CART).click()

		def add_element_to_dictionary(self, property, value):
				self.property_dictionary[property] = value
				return self.property_dictionary

		def choose_product_specifications(self, *args):