from YandexPage import SearchHelper

""" Use 'pytest test_2.py -s' to see full output"""
def test_yandex_search_loto(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Лото")
    item = yandex_main_page.first_search_item()
    print(item)