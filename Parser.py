import time
from selenium.webdriver.common.by import By
from browser import Driver_Chrom


class Parser:
    def __init__(self, brand: list = None):
        self.brand = brand

    def parser_page(self, page: int = 1) -> list:
        driver = Driver_Chrom().loadChrome(headless=True)
        url = f'https://spb.vseinstrumenti.ru/brand/{self.brand}/page{page}/?asc=desc&orderby=price' if page > 1 else f'https://spb.vseinstrumenti.ru/brand/{self.brand}/?asc=desc&orderby=price'
        driver.get(url)
        time.sleep(3)
        names = driver.find_elements(By.XPATH, '//div[@data-qa="products-tile"]/a[@data-qa="product-name"]')
        prices = driver.find_elements(By.XPATH, '//div[@data-qa="products-tile"]//p[@data-qa="product-price-current"]')
        all_names = list(map(lambda x: x.get_attribute('title'), names))
        all_prices = list(map(lambda x: x.text.strip(' р.').replace(' ', ''), prices))
        data_result = list(zip(all_names, all_prices))
        driver.close()
        driver.quit()
        return data_result

    def get_last_page(self) -> int:
        url = f'https://spb.vseinstrumenti.ru/brand/{self.brand}/?asc=desc&orderby=price'
        driver = Driver_Chrom().loadChrome(headless=True)
        driver.get(url)
        time.sleep(2)
        last_page = min(int(driver.find_elements(By.XPATH, '//a[@class="number"]')[-1].text), 100)
        driver.close()
        driver.quit()
        return last_page
