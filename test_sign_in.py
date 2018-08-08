import unittest
from unittest import TestCase
from selenium import webdriver
from ddt import ddt, file_data

from names import *
from sign_in_page import SignInPage


@ddt
class SignInTest(TestCase):
    errors = []
    gender = 'man'
    name = 'Шерлок'
    surname = 'Холмс'
    email = 'test_mail@email.ru'
    year_of_birth = '1987'
    password = {"password": "Pa$sw0rd", "confirm": "Pa$sw0rd"}

    def setUp(self):
        profile = webdriver.FirefoxProfile("C:/Users/Алиса/AppData/Roaming/Mozilla/Firefox/Profiles/67v3righ.user")
        self.driver = webdriver.Firefox(profile)
        self.driver.maximize_window()
        page = SignInPage(self.driver)
        page.open("https://www.blablacar.ru/register")

    def fill_sign_in_form(self):
        page = SignInPage(self.driver)
        page.sign_in_form.set_gender(self.gender)
        page.sign_in_form.set_user_info(self.name, self.surname, self.email, self.year_of_birth)
        page.sign_in_form.set_password(self.password)
        page.sign_in_form.submit_registration()
        errors = page.sign_in_form.get_errors()
        self.assertSequenceEqual(self.errors, errors)

    def test_empty_gender(self):
        self.errors = [ERROR_EMPTY_GENDER]
        self.gender = ""
        self.fill_sign_in_form()

    @file_data('tests/sign_in/incorrect_name.json')
    def test_incorrect_name(self, name):
        self.errors = [INCORRECT_NAME]
        self.name = name
        self.fill_sign_in_form()

    def test_empty_name(self):
        self.errors = [ERROR_EMPTY_NAME]
        self.name = ""
        self.fill_sign_in_form()

    @file_data('tests/sign_in/incorrect_surname.json')
    def test_incorrect_surname(self, surname):
        self.errors = [INCORRECT_SURNAME]
        self.surname = surname
        self.fill_sign_in_form()

    @unittest.SkipTest
    @file_data('tests/sign_in/incorrect_email.json')
    def test_incorrect_email(self, email):
        self.errors = [INCORRECT_EMAIL]
        self.email = email
        self.fill_sign_in_form()

    def test_already_use_email(self):
        self.errors = [ERROR_ALREADY_USE_EMAIL]
        self.email = 'test@mail.ru'
        self.fill_sign_in_form()

    @file_data('tests/sign_in/incorrect_password.json')
    def test_short_password(self, password):
        self.errors = [ERROR_SHORT_PASSWORD]
        self.password = password[0]
        self.fill_sign_in_form()

    def test_empty_password(self):
        self.errors = [ERROR_EMPTY_PASSWORD]
        self.password = ""
        self.fill_sign_in_form()

    @file_data('tests/sign_in/incorrect_confirm_password.json')
    def test_incorrect_confirm_password(self, password):
        self.errors = [ERROR_CONFIRM_PASSWORD]
        self.password = password[0]
        self.fill_sign_in_form()

    def test_empty_confirm_password(self):
        self.errors = [ERROR_CONFIRM_PASSWORD, ERROR_EMPTY_CONFIRM_PASSWORD, ]
        self.password = ""
        self.fill_sign_in_form()

    def test_empty_year_of_birth(self):
        self.errors = [ERROR_EMPTY_YEAR_OF_BIRTH]
        self.year_of_birth = ""
        self.fill_sign_in_form()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
