import time
from selenium.webdriver.common.by import By
from browser import Driver_Chrom


class Parser:
    def __init__(self, brand: list = None):
        self.brand = brand
        xpath_for_names = '//div[@data-qa="products-tile"]/a[@data-qa="product-name"]'
        xpath_for_prices = '//div[@data-qa="products-tile"]//p[@data-qa="product-price-current"]'
        xpath_for_last_page = '//a[@class="number"]'
        url_for_find_all_links = 'https://spb.vseinstrumenti.ru/category/stroitelnyj-instrument-6474/'
        xpath_for_find_all_links = "//a[@href = 'https://spb.vseinstrumenti.ru/category/akkumulyatornyj-instrument-2392/']//ancestor::div[1]"

    def parser_page(self, page: int = 1, link: str = '') -> list:
        url = link if page == 1 else f'{link}/page{page}'
        driver = Driver_Chrom().loadChrome(headless=True)
        driver.get(url)
        time.sleep(1)
        names = driver.find_elements(By.XPATH, self.xpath_for_names)
        prices = driver.find_elements(By.XPATH, self.xpath_for_prices)
        all_names = list(map(lambda x: x.get_attribute('title'), names))
        all_prices = list(map(lambda x: x.text.strip(' р.').replace(' ', ''), prices))
        data_result = list(zip(all_names, all_prices))
        driver.close()
        driver.quit()
        return data_result

    def get_last_page(self, link: str = '') -> int:
        driver = Driver_Chrom().loadChrome(headless=True)
        driver.get(link)
        time.sleep(1)
        try:
            last_page = min(int(driver.find_elements(By.XPATH, self.xpath_for_last_page)[-1].text), 250)
        except:
            last_page = 1
        driver.close()
        driver.quit()
        return last_page

    def get_all_links(self) -> list:
        driver = Driver_Chrom().loadChrome(headless=True)
        driver.get(self.url_for_find_all_links)
        time.sleep(0.5)
        class_element = driver.find_elements(By.XPATH, self.xpath_for_find_all_links)[1].get_attribute('class')
        xpath_for_all = f'//div[contains(@class, "{class_element}")]//a'
        all_links_driver = driver.find_elements(By.XPATH, xpath_for_all)
        all_links = set(map(lambda x: x.get_attribute('href'), all_links_driver))
        return all_links
