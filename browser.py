import undetected_chromedriver


class Driver_Chrom():
    def loadChrome(self, headless=False):
        chrome_options = undetected_chromedriver.ChromeOptions()
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument('--verbose')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-software-rasterizer')
        browser = undetected_chromedriver.Chrome(headless=headless, options=chrome_options)
        return browser