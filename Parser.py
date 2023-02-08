import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from browser import Driver_Chrom


class Parser:
    def __init__(self, brand: list = None):
        self.brand = brand
        self.xpath_for_last_page = '//a[@class="number"]'
        self.url_for_find_all_links = 'https://spb.vseinstrumenti.ru/category/stroitelnyj-instrument-6474/'
        self.xpath_for_find_all_links = "//a[@href = 'https://spb.vseinstrumenti.ru/category/akkumulyatornyj-instrument-2392/']//ancestor::div[1]"
        self.xpath_for_name = ".//a[@data-qa='product-name']"
        self.xpath_for_price = ".//p[@data-qa='product-price-current']"
        self.xpath_for_cards = "//div[contains(@data-qa, 'products-tile') and not(contains(@data-qa, 'light'))]"
        self.check_availability = ".// div[contains(@data-qa, 'not-available')]"
        self.button_next = "//div[@class='button-wrapper'][2]"
        self.xpath_code = ".//p[@data-qa='product-code-text']"

    def get_last_page(self, link: str = '') -> int:
        driver = Driver_Chrom().loadChrome(headless=True)
        driver.implicitly_wait(10)
        driver.get(link)
        try:
            last_page = min(int(driver.find_elements(By.XPATH, self.xpath_for_last_page)[-1].text), 200)
        except:
            last_page = 1
        finally:
            driver.close()
            driver.quit()
        return last_page

    def get_all_links(self) -> list:
        driver = Driver_Chrom().loadChrome(headless=True)
        driver.implicitly_wait(10)
        driver.get(self.url_for_find_all_links)
        try:
            class_element = driver.find_elements(By.XPATH, self.xpath_for_find_all_links)[1].get_attribute('class')
            xpath_for_all = f'//div[contains(@class, "{class_element}")]//a'
            all_links_driver = driver.find_elements(By.XPATH, xpath_for_all)
            all_links = set(map(lambda x: x.get_attribute('href'), all_links_driver))
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()

        return all_links

    def parser_page(self, last_page: int = 1, link: str = '') -> list:
        print(f"{link.replace('https://spb.vseinstrumenti.ru/category/', '')} всего {last_page} страниц")
        data_result = []
        check_finish = True
        counter = 0
        for i in range(1, last_page):
            if check_finish:
                driver = Driver_Chrom().loadChrome(headless=True)
                driver.get(f'{link}/page{i}/')
                print(i)
                time.sleep(1.6)
                all_cards_on_the_page = driver.find_elements(By.XPATH, self.xpath_for_cards)
                for card in all_cards_on_the_page:
                    try:
                        card.find_element(By.XPATH,  self.check_availability)
                        check_finish = False
                    except:
                        code = card.find_element(By.XPATH, self.xpath_code).text.replace('код: ', '')
                        name = card.find_element(By.XPATH, self.xpath_for_name).get_attribute('title')
                        product_link = card.find_element(By.XPATH, self.xpath_for_name).get_attribute('href')
                        price = card.find_element(By.XPATH, self.xpath_for_price).text.replace(' р.', '').replace(' ', '')
                        data_result.append((code, name, price, product_link))
                counter += 1
            else:
                break
            driver.close()
            driver.quit()
        print(f'спарсили всего {counter} из {last_page}')

        return data_result