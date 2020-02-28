from Base import BasePage
from selenium.webdriver.common.by import By

class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_YANDEX_FAST_SEARCH_ITEM = (By.CSS_SELECTOR, ".suggest2-item__fact")
    LOCATOR_YANDEX_SEARCH_ITEM = (By.CSS_SELECTOR, ".suggest2-item__text")

class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def fast_search_item(self):
        item = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_FAST_SEARCH_ITEM, time=2).text
        return item

    def first_search_item(self):
        item = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_ITEM, time=2).text
        return item

