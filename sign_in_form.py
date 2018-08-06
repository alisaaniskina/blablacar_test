import time
from base_component import BaseComponent
from selenium.webdriver.support.ui import Select, WebDriverWait


class SignInForm(BaseComponent):
    selectors = {
        'gender_man': '//input[@id="registration_gender_0"]',
        'gender_woman': '//input[@id="registration_gender_1"]',
        'name': '//input[@id="registration_firstname"]',
        'surname': '//input[@id="registration_lastname"]',
        'email': '//input[@id="registration_email"]',
        'password': '//input[@id="registration_password_first"]',
        'agree_password': '//input[@id="registration_password_second"]',
        'year_of_birth': '//select[@id="registration_birthYear"]',
        'get_mail': '//input[@id="registration_newsletterFlag"]',
        'submit_button': '//button[@class="btn-validation btn-large full-width apply-btn-loader"]',
        'term_of_use': '//p[@class="smallprint"/a[1]',
        'privacy_policy': '//p[@class="smallprint"]/a[2]',
        'sign_up_facebook': '//a[@class="btn-social btn-facebook js-oauth-connect"]',
        'sign_up_vk': '//a[@class="btn-social btn-vkontakte js-oauth-connect"]',
        'sign_up': '//a[@class="btn-validation btn-large margin-left login-link"]',
        'errors': '//p[@class="alert alert-error no-icon u-clearfix js-formError _test-formError "]'
    }

    # установка выбора "Мужчина" или "Женщина"
    def set_gender(self, gender=None):
        if gender == 'man':
            self.driver.find_element_by_xpath(self.selectors['gender_man']).click()
        if gender == 'woman':
            self.driver.find_element_by_xpath(self.selectors['gender_woman']).click()

    # заполнение значений Имя, Фамилия, Электронная почта, Год рождения
    def set_user_info(self, name=None, surname=None, email=None, year=None):
        if name is not None:
            self.driver.find_element_by_xpath(self.selectors['name']).send_keys(name)
        if surname is not None:
            self.driver.find_element_by_xpath(self.selectors['surname']).send_keys(surname)
        if email is not None:
            self.driver.find_element_by_xpath(self.selectors['email']).send_keys(email)
        if year is not None:
            year_of_birth = Select(self.driver.find_element_by_xpath(self.selectors['year_of_birth']))
            year_of_birth.select_by_visible_text(year)

    # заполнение полей "Пароль" и "Подтверждение пароля"
    def set_password(self, password=None):
        if password["password"] is not None:
            self.driver.find_element_by_xpath(self.selectors['password']).send_keys(password["password"])
            time.sleep(1)
        if password["confirm"] is not None:
            self.driver.find_element_by_xpath(self.selectors['agree_password']).send_keys(password["confirm"])
            time.sleep(1)

    # снятие/установка выбора "Хочу получать новости"
    def set_get_mail(self):
        self.driver.find_element_by_xpath(self.selectors['get_mail']).click()

    # подтверждение отправки формы, кнопка "Зарегистрироваться через эл. почту"
    def submit_registration(self):
        self.driver.find_element_by_xpath(self.selectors['submit_button']).click()

    # переход по ссылке "Условия использования"
    def term_of_use(self):
        self.driver.find_element_by_xpath(self.selectors['term_of_use']).click()

    # переход по ссылке "Политика конфиденциальности"
    def privacy_policy(self):
        self.driver.find_element_by_xpath(self.selectors['privacy_policy']).click()

    # добавить сбор ошибок
    def get_errors(self):
        error_text = []
        errors = self.driver.find_elements_by_xpath(self.selectors['errors'])
        for error in errors:
            error_text.append(error.text)
        return error_text
