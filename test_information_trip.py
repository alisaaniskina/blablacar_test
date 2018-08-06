from ddt import ddt, file_data
import unittest
from unittest import TestCase
from selenium import webdriver

from names import *
from my_trip_page import MyTripPage
from trip_details_page import TripDetailsPage


@ddt
class TripInformationTest(TestCase):
    errors = []
    place_departure = 'Новосибирск, Гагаринская'
    place_arrival = 'Барнаул, АлТГУ'
    date_departure = {"day": "05/08/2018", "hour": "20", "minute": "10"}
    date_backward = {"day": "15/08/2018", "hour": "18", "minute": "20"}

    def setUp(self):
        profile = webdriver.FirefoxProfile("C:/Users/Алиса/AppData/Roaming/Mozilla/Firefox/Profiles/67v3righ.user")
        self.driver = webdriver.Firefox(profile)
        self.driver.maximize_window()
        page = MyTripPage(self.driver)
        page.open("https://www.blablacar.ru/offer-seats/1")

    def fill_information_form(self):
        page = MyTripPage(self.driver)
        page.trip_information_form.fill_places(self.place_departure, self.place_arrival)
        page.trip_information_form.date_departure(self.date_departure)
        page.trip_information_form.date_backward(self.date_backward)
        page.trip_information_form.next_step()
        errors = page.trip_information_form.get_all_errors()
        self.assertSequenceEqual(self.errors, errors)

    # -
    @file_data('tests/my_trip/information_trip/correct_date.json')
    def test_correct_dates(self, departure, backward):
        self.date_departure = departure
        self.date_backward = backward
        self.fill_information_form()
        page = TripDetailsPage(self.driver)
        departure_date_out = page.route_information.get_departure_date()
        backward_date_out = page.route_information.get_backward_date()
        departure_date_in = page.route_information.get_date(self.date_departure)
        backward_date_in = page.route_information.get_date(self.date_backward)
        tests = [[backward_date_in, backward_date_out], [departure_date_in, departure_date_out]]
        for test in tests:
            with self.subTest(test=test):
                self.assertDictEqual(test[0], test[1], msg='Error in %s date' % test)

    @file_data('tests/my_trip/information_trip/incorrect_date.json')
    def test_incorrect_date_departure(self, date):
        self.errors = [INCORRECT_INPUT, INCORRECT_DATE_DEPARTURE]
        self.date_departure = date[0]
        self.fill_information_form()

    @file_data('tests/my_trip/information_trip/incorrect_date.json')
    def test_incorrect_date_backward(self, date):
        self.errors = [INCORRECT_INPUT, INCORRECT_DATE_BACKWARD]
        self.date_backward = date[0]
        self.fill_information_form()

    @file_data('tests/my_trip/information_trip/non_actual_date_departure.json')
    def test_non_actual_date_departure(self, departure, backward):
        self.errors = [INCORRECT_INPUT, NON_ACTUAL_DATE_DEPARTURE]
        self.date_departure = departure
        self.date_backward = backward
        self.fill_information_form()

    @file_data('tests/my_trip/information_trip/non_actual_date_backward.json')
    def test_non_actual_date_backward(self, departure, backward):
        self.errors = [INCORRECT_INPUT, NON_ACTUAL_DATE_BACKWARD]
        self.date_departure = departure
        self.date_backward = backward
        self.fill_information_form()

    @file_data('tests/my_trip/information_trip/incorrect_both_date.json')
    def test_incorrect_both_date(self, departure, backward):
        self.errors = [INCORRECT_INPUT, INCORRECT_DATE_DEPARTURE, INCORRECT_DATE_BACKWARD]
        self.date_departure = departure
        self.date_backward = backward

    def test_correct_place(self, departure, arrival):
        print(departure, arrival)
        city_in = ['Новосибирск', 'Барнаул']
        self.place_departure = departure
        self.place_arrival = arrival
        self.fill_information_form()
        page = TripDetailsPage(self.driver)
        city_out = page.route_information.get_route_points()
        self.assertSequenceEqual(city_in, city_out)

    def test_incorrect_arrival_place(self):
        self.errors = [ERROR_CREATE_ROUTE, INCORRECT_INPUT, INCORRECT_POINT]
        self.place_arrival = 'Эъхрпшй'
        self.fill_information_form()

    def test_incorrect_departure_place(self):
        self.errors = [ERROR_CREATE_ROUTE, INCORRECT_INPUT, INCORRECT_POINT]
        self.place_departure = 'Йшпрхъэ'
        self.fill_information_form()

    # -
    def test_incorrect_both_place(self):
        self.errors = [ERROR_CREATE_ROUTE, INCORRECT_POINT, INCORRECT_POINT, INCORRECT_INPUT]
        self.place_departure = 'Эъхрпшй'
        self.place_arrival = 'Йшпрхъэ'
        self.fill_information_form()

    def test_empty_departure_place(self):
        self.errors = [INCORRECT_INPUT, ERROR_EMPTY_PLACE_DEPARTURE]
        self.place_departure = ""
        self.fill_information_form()

    def test_empty_backward_place(self):
        self.errors = [INCORRECT_INPUT, ERROR_EMPTY_PLACE_BACKWARD]
        self.place_arrival = ""
        self.fill_information_form()

    def test_empty_both_places(self):
        self.errors = [INCORRECT_INPUT, ERROR_EMPTY_PLACE_DEPARTURE, ERROR_EMPTY_PLACE_BACKWARD]
        self.place_departure = ""
        self.place_arrival = ""
        self.fill_information_form()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
