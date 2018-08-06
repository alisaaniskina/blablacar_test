class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self._header_navigation = None

    @property
    def header_navigation(self):
        from header_navigation import HeaderNavigation
        if self._header_navigation is None:
            self._header_navigation = HeaderNavigation(self.driver)
        return self._header_navigation

    def open(self, url):
        self.driver.get(url)
