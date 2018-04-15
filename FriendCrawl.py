from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FacebookCrawler:
    LOGIN_URL = 'https://www.facebook.com/login.php?login_attempt=1&lwv=111'

    def __init__(self, login, password):
        # Firefox_options = webdriver.FirefoxOptions()
        # prefs = {"profile.default_content_setting_values.notifications": 2}
        # Firefox_options.add_experimental_option("prefs", prefs)
        ffprofile = webdriver.FirefoxProfile()
        ffprofile.set_preference("permissions.default.desktop-notification", 1)
        self.driver = webdriver.Firefox(ffprofile)
        self.wait = WebDriverWait(self.driver, 10)

        self.login(login, password)

    def login(self, login, password):
        self.driver.get(self.LOGIN_URL)

        # wait for the login page to load
        self.wait.until(EC.visibility_of_element_located((By.ID, "email")))

        self.driver.find_element_by_id('email').send_keys(login)
        self.driver.find_element_by_id('pass').send_keys(password)
        self.driver.find_element_by_id('loginbutton').click()

        # wait for the main page to load
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#findFriendsNav")))
    
    def goToGroups(self, profileUrl):
        self.driver.get(profileUrl)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#findFriendsNav")))
        
        # self.driver.find_element_by_css_selector("a#_6-6").click()
        self.driver.find_element_by_xpath("//a[@data-tab-key='about']").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#findFriendsNav")))

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                self.driver.find_element_by_css_selector("h3#medley_header_groups").click()
                # print('passed')
                break
            except:
                pass
                # print('loading still')
        return self.driver.page_source
        
        # self.information[]

    def goToFriends(self, profileUrl):
        """
        returns: Friends list as html
        """
        self.driver.get(profileUrl)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#findFriendsNav")))
        
        # self.driver.find_element_by_css_selector("a#_6-6").click()
        self.driver.find_element_by_xpath("//a[@data-tab-key='friends']").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#findFriendsNav")))


        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                self.driver.find_element_by_css_selector("h3#medley_header_groups").click()
                # print('passed')
                break
            except:
                pass
                # print('loading still')
        return (self.driver.find_element_by_xpath("//div[@id='pagelet_timeline_medley_friends']").get_attribute('innerHTML'))





    def _get_friends_list(self):
        return self.driver.find_element_by_css_selector(".friendBrowserNameTitle > a")

    def get_friends(self):
        # navigate to "friends" page
        self.driver.find_element_by_css_selector("a#findFriendsNav").click()
        self.driver.find_element_by_css_selector("a#findFriendsNav").click()


        # continuous scroll until no more new friends loaded
        num_of_loaded_friends = len(self._get_friends_list())
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                self.wait.until(lambda driver: len(self._get_friends_list()) > num_of_loaded_friends)
                num_of_loaded_friends = len(self._get_friends_list())
            except TimeoutException:
                break  # no more friends loaded

        return [friend.text for friend in self._get_friends_list()]
    
    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    profile = "https://www.facebook.com/agapito.delcorralgrande/"
    crawler = FacebookCrawler(login='checkptransfer@hotmail.com', password='d95-ggF-HFs-c7u',)
    crawler.goToGroups(profile)
    crawler.goToFriends(profile)
    
    # for friend in crawler.get_friends():
    #     print(friend)