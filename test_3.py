from YandexPage import SearchHelper

""" Use 'pytest test_3.py -s' to see full output"""
def test_yandex_search_city(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Липецк")
    item = yandex_main_page.first_search_item()
    print(item)