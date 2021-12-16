import pytest
import time
from selenium.webdriver.common.keys import Keys


def test_search_repository(driver):
    search_string = "dotnet"
    result_string = "microsoft/dotnet"
    passed = False

    search_form = pytest.page.get_search_form_from_menu()
    search_form.send_keys(search_string)
    search_form.send_keys(Keys.RETURN)
    search_res = pytest.page.get_users_search_results_text()

    for rx in search_res:
        if rx.find(result_string) != -1:
            passed = True
            break
    assert passed


def test_search_user(driver):
    search_string = "Vort-X"
    user_tab_string = "Users"
    passed = False

    search_form = pytest.page.get_search_form_from_menu()
    search_form.send_keys(search_string)
    search_form.send_keys(Keys.RETURN)
    tabs = pytest.page.get_tabs_from_search_results()

    users_tab = 0
    for tab in tabs:
        if tab.text.find(user_tab_string) != -1:
            passed = True
            users_tab = tab
            break
    assert passed

    users_tab.click()
    users_list = pytest.page.get_users_list()
    assert len(users_list) == 1
    assert users_list[0] == search_string


def test_search_marketplace(driver):
    search_string = "microsoft"
    marketplace_tab_string = "Marketplace"
    result_string = "Microsoft Teams"
    passed = False

    search_form = pytest.page.get_search_form_from_menu()
    search_form.send_keys(search_string)
    search_form.send_keys(Keys.RETURN)
    tabs = pytest.page.get_tabs_from_search_results()

    marketplace_tab = 0
    for tab in tabs:
        if tab.text.find(marketplace_tab_string) != -1:
            passed = True
            marketplace_tab = tab
            break
    assert passed

    marketplace_tab.click()
    marketplace_list = pytest.page.get_marketplace_list()

    passed = False
    for marketplace in marketplace_list:
        if marketplace.find(result_string) != -1:
            passed = True
            break
    assert passed
