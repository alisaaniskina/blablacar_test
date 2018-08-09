class MyTripPage:

    def __init__(self, driver):
        self.driver = driver
        self._trip_information_form = None
        self._header_navigation = None

    @property
    def trip_information_form(self):
        if self._trip_information_form is None:
            from trip_information_form import TripInformationForm
            self._trip_information_form = TripInformationForm(self.driver)
        return self._trip_information_form

    @property
    def header_navigation(self):
        if self._header_navigation is None:
            from header_navigation import HeaderNavigation
            self._header_navigation = HeaderNavigation(self.driver)
        return self._header_navigation

    def open(self, url):
        self.driver.get(url)
