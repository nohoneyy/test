from YandexPage import SearchHelper

""" Use 'pytest test_1.py -s' to see full output"""
def test_yandex_search_weather(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Погода")
    item = yandex_main_page.first_search_item()
    degree = yandex_main_page.fast_search_item()
    print(item + " " + degree)

