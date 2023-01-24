import time
from selenium.webdriver.common.by import By
from browser import Driver_Chrom
from bs4 import BeautifulSoup as bs


class Parser:
    def __init__(self, brand: list = None):
        self.brand = brand
        self.xpath_for_last_page = '//a[@class="number"]'
        self.url_for_find_all_links = 'https://spb.vseinstrumenti.ru/category/stroitelnyj-instrument-6474/'
        self.xpath_for_find_all_links = "//a[@href = 'https://spb.vseinstrumenti.ru/category/akkumulyatornyj-instrument-2392/']//ancestor::div[1]"
        self.xpath_for_name = ".//a[@data-qa='product-name']"
        self.xpath_for_price = ".//p[@data-qa='product-price-current']"
        self.xpath_for_cards = "//div[@data-qa='products-tile']"
        self.check_availability = ".// div[contains(@data-qa, 'not-available')]"

    def get_last_page(self, link: str = '') -> int:
        driver = Driver_Chrom().loadChrome(headless=True)
        driver.implicitly_wait(10)
        driver.get(link)
        try:
            last_page = min(int(driver.find_elements(By.XPATH, self.xpath_for_last_page)[-1].text) + 1, 200)
        except:
            last_page = 1
        driver.close()
        driver.quit()
        return last_page

    def get_all_links(self) -> list:
        driver = Driver_Chrom().loadChrome(headless=True)
        driver.implicitly_wait(10)
        driver.get(self.url_for_find_all_links)
        class_element = driver.find_elements(By.XPATH, self.xpath_for_find_all_links)[1].get_attribute('class')
        xpath_for_all = f'//div[contains(@class, "{class_element}")]//a'
        all_links_driver = driver.find_elements(By.XPATH, xpath_for_all)
        all_links = set(map(lambda x: x.get_attribute('href'), all_links_driver))
        driver.close()
        driver.quit()
        return all_links

    def parser_page(self, page: int = 1, link: str = '') -> list:
        url = link if page == 1 else f'{link}/page{page}'
        driver = Driver_Chrom().loadChrome(headless=True)
        driver.get(url)
        time.sleep(5)
        data_result = []
        all_cards_on_the_page = driver.find_elements(By.XPATH, self.xpath_for_cards)
        for card in all_cards_on_the_page:
            try:
                card.find_element(By.XPATH,  self.check_availability)
                break
            except:
                name = card.find_element(By.XPATH, self.xpath_for_name).get_attribute('title')
                price = card.find_element(By.XPATH, self.xpath_for_price).text.replace(' р.', '').replace(' ', '')
                data_result.append((name, price))
        driver.close()
        driver.quit()
        return data_result