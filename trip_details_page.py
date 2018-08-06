class TripDetailsPage:

    def __init__(self, driver):
        self.driver = driver
        self._trip_details_form = None
        self._route_information = None
        self._header_navigation = None

    @property
    def trip_details_form(self):
        from trip_details_form import TripDetailsForm
        if self._trip_details_form is None:
            self._trip_details_form = TripDetailsForm(self.driver)
        return self._trip_details_form

    @property
    def route_information(self):
        from route_information import RouteInformation
        if self._route_information is None:
            self._route_information = RouteInformation(self.driver)
        return self._route_information

    @property
    def header_navigation(self):
        from header_navigation import HeaderNavigation
        if self._header_navigation is None:
            self._header_navigation = HeaderNavigation(self.driver)
        return self._header_navigation

    def open(self, url):
        self.driver.get(url)
