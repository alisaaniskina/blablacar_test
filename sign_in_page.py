class SignInPage:

    def __init__(self, driver):
        self.driver = driver
        self._sign_in_form = None
        self._header_navigation = None

    @property
    def sign_in_form(self):
        from sign_in_form import SignInForm
        if self._sign_in_form is None:
            self._sign_in_form = SignInForm(self.driver)
        return self._sign_in_form

    @property
    def header_navigation(self):
        from header_navigation import HeaderNavigation
        if self._header_navigation is None:
            self._header_navigation = HeaderNavigation(self.driver)
        return self._header_navigation

    def open(self, url):
        self.driver.get(url)
