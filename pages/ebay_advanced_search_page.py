from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import Base_page

class Advanced_search_page(Base_page):
		ENTER_KEYWORDS_OR_ITEM_NUMBER = (By.ID,'_nkw')
		KEYWORD_OPTIONS = (By.XPATH,'//select[@name="_in_kw"]')
		EXCLUDE_WORDS_FROM_SEARCH = (By.ID,"_ex_kw")
		SEARCH_CATEGORIES = (By.ID,'e1-1')
		SEARCH_BUTTON = (By.CSS_SELECTOR,'div[class="adv-s mb space-top"]>button')


def enter_keywords_or_item_number(self, product):
	self.chrome.find_element(*self.ENTER_KEYWORDS_OR_ITEM_NUMBER).send_keys(product)

def select_keyword_options(self):
	keyword_dropdown = Select(self.chrome.find_element(*self.KEYWORD_OPTIONS))
	keyword_dropdown.select_by_visible_text("Exact words, exact order")

def select_search_category(self, category):
	category_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORIES))
	category_dropdown.select_by_visible_text(category)

def exclude_word_from_search(self, exclude_product):
	self.chrome.find_element(*self.EXCLUDE_WORDS_FROM_SEARCH).send_keys(exclude_product)

def click_search_button(self):
	self.wait_and_click_element_by_selector(*self.SEARCH_BUTTON)