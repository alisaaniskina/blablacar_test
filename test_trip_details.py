from ddt import ddt, file_data
import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from names import *
from home_page import HomePage
from my_trip_page import MyTripPage
from trip_details_page import TripDetailsPage


@ddt
class TripDetailsTest(TestCase):
    """
    Подготовка к тестам
        1. Зайти на сайт BlaBlaCar
        2. Перейти по ссылке "Предложить поездку"
        3. Ввести в поле "Откуда выезжаете" корректное значение (например, Новосибирск, Гагаринская)
        4. Ввести в поле "Куда вы едете" корректное значение (например, Барнаул, АлТГУ)
        5. Ввести в поле "Промежуточный пункт" корректное значение (Например, Томск)
        6. Заполнить поле "Дата отправления" корректными значениями (например, 05/09/2018 18:20)
        7. Заполнить поле "Дата обратной поездки" корректными значениями (например, 08/09/2018 13:00)
        8. Нажать кнопку "Продолжить"
    """

    place_departure = 'Новосибирск, Гагаринская'
    place_arrival = 'Барнаул, АлТГУ'
    middle_point = ['Томск']
    date_departure = {"day": "05/09/2018", "hour": "20", "minute": "10"}
    date_backward = {"day": "15/09/2018", "hour": "18", "minute": "20"}

    def setUp(self):
        # profile = webdriver.FirefoxProfile("C:/Users/Алиса/AppData/Roaming/Mozilla/Firefox/Profiles/67v3righ.user")
        options = Options()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)
        self.driver.maximize_window()
        page = HomePage(self.driver)
        page.open("https://www.blablacar.ru/")
        page.header_navigation.go_to_offer_trip()
        page = MyTripPage(self.driver)
        page.trip_information_form.fill_places(self.place_departure, self.place_arrival)
        page.trip_information_form.fill_middle_point(self.middle_point)
        page.trip_information_form.date_departure(self.date_departure)
        page.trip_information_form.date_backward(self.date_backward)
        page.trip_information_form.next_step()

    @file_data('tests/my_trip/trip_details/maximal_price.json')
    def test_maximal_price_by_passenger(self, price):
        expected_prices = ['550', '950']
        page = TripDetailsPage(self.driver)
        page.trip_details_form.price_by_passengers(price)
        actual_prices = page.trip_details_form.get_price_by_route()
        self.assertSequenceEqual(expected_prices, actual_prices)

    @file_data('tests/my_trip/trip_details/minimal_price.json')
    def test_minimal_price_by_passenger(self, price):
        expected_prices = ['160', '300']
        page = TripDetailsPage(self.driver)
        page.trip_details_form.price_by_passengers(price)
        actual_prices = page.trip_details_form.get_price_by_route()
        self.assertSequenceEqual(expected_prices, actual_prices)

    def test_not_confirm_drivers_license(self):
        expected_errors = [INCORRECT_INPUT, ERROR_CONFIRM_DRIVERS_LICENSE]
        page = TripDetailsPage(self.driver)
        page.trip_details_form.next_step()
        actual_errors = page.trip_details_form.get_all_errors()
        self.assertSequenceEqual(expected_errors, actual_errors)

    def test_count_seats_more_allowable(self):
        expected_errors = [INCORRECT_INPUT, ERROR_COUNT_SEATS_MORE_ALLOWABLE]
        page = TripDetailsPage(self.driver)
        page.trip_details_form.free_seats(9)
        page.trip_details_form.next_step()
        actual_errors = page.trip_details_form.get_all_errors()
        self.assertSequenceEqual(expected_errors, actual_errors)

    # -
    @file_data('tests/my_trip/trip_details/less_count_seats.json')
    def test_count_seats_less_allowable(self, count_seats):
        expected_errors = [INCORRECT_INPUT, ERROR_COUNT_SEATS_LESS_ALLOWABLE]
        page = TripDetailsPage(self.driver)
        page.trip_details_form.free_seats(count_seats)
        page.trip_details_form.next_step()
        actual_errors = page.trip_details_form.get_all_errors()
        self.assertSequenceEqual(expected_errors, actual_errors)

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
