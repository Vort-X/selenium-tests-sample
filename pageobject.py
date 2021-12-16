from selenium.webdriver.common.by import By


class Page:
    def __init__(self, driver, url):
        driver.get(url)
        self.driver = driver

    def get_search_form_from_menu(self):
        self.driver.find_element(By.CSS_SELECTOR, 'svg.octicon.octicon-three-bars').click()
        return self.driver.find_element(By.CSS_SELECTOR, 'input.form-control.input-sm.header-search-input'
                                                         '.jump-to-field.js-jump-to-field.js-site-search-focus')

    def get_repos_search_results_text(self):
        repo_list = self.driver.find_element(By.CLASS_NAME, 'repo-list')
        res = repo_list.find_elements(By.TAG_NAME, 'li')
        return [r.text for r in res]

    def get_tabs_from_search_results(self):
        return self.driver.find_elements(By.CLASS_NAME, 'menu-item')

    def get_users_list(self):
        user_search_results = self.driver.find_element(By.ID, 'user_search_results')
        users_box = user_search_results.find_element(By.CSS_SELECTOR, 'div.Box.border-0')
        users_links = users_box.find_elements(By.CSS_SELECTOR, 'div.f4.text-normal')
        return [link.text for link in users_links]

    def get_marketplace_list(self):
        marketplace_search_results = self.driver.find_element(By.ID, 'marketplace_search_results')
        marketplace_links = marketplace_search_results.find_elements(By.CLASS_NAME, 'no-underline')
        return [link.text for link in marketplace_links]
