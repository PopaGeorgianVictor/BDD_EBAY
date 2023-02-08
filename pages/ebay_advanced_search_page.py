from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import Base_page

class Advanced_search_page(Base_page):
		ENTER_KEYWORDS_OR_ITEM_NUMBER = (By.ID,'_nkw')
		KEYWORD_OPTIONS = (By.XPATH,'//select[@name="_in_kw"]')
		EXCLUDE_WORDS_FROM_SEARCH = (By.ID,"_ex_kw")
		SEARCH_CATEGORIES = (By.ID,'e1-1')
		SEARCH_BUTTON = (By.CSS_SELECTOR,'div[class="adv-s mb space-top"]>button')
