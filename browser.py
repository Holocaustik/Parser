import undetected_chromedriver


class Driver_Chrom():

    def loadChrome(self, headless=False):
        options = undetected_chromedriver.ChromeOptions()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--v=99")
        options.add_argument("--no-sandbox")
        browser = undetected_chromedriver.Chrome(headless=headless, options=options)
        return browser