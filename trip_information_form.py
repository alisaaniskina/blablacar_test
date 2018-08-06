from base_component import BaseComponent
from selenium.webdriver.support.ui import Select, WebDriverWait


class TripInformationForm(BaseComponent):
    selectors = {
        'departure_place': '//input[@id="new_publication_step1_departurePlace_name"]',
        'arrival_place': '//input[@id="new_publication_step1_arrivalPlace_name"]',
        'middle_point': '//input[@id="new_publication_step1_stopovers_%s_name"]',
        'add_middle_point': '//a[@class="stage-add u-blue u-alignMiddle"]',

        'date_departure': '//input[@id="new_publication_step1_departureDate_date"]',
        'hour_departure': '//select[@id="new_publication_step1_departureDate_time_hour"]',
        'minute_departure': '//select[@id="new_publication_step1_departureDate_time_minute"]',
        'date_backward': '//input[@id="new_publication_step1_returnDate_date"]',
        'hour_backward': '//select[@id="new_publication_step1_returnDate_time_hour"]',
        'minute_backward': '//select[@id="new_publication_step1_returnDate_time_minute"]',
        'both_ways': '//input[@id="new_publication_step1_roundTrip"]',

        'next_step_button': '//button[@class="Button Button--primary Button--big u-right apply-btn-loader js-realSubmit"]',
        'errors': '//p[@class="alert alert-error no-icon u-clearfix js-formError _test-formError "]',
        'errors_place': '//p[@class="alert alert-error no-icon u-clearfix js-formError _test-formError js-placeError--backendValidation"]'
    }

    # заполнение поля "Откуда вы выезжаете"
    def fill_places(self, departure_place=None, arrival_place=None):
        if departure_place is not None:
            self.driver.find_element_by_xpath(self.selectors['departure_place']).send_keys(departure_place)
        if arrival_place is not None:
            self.driver.find_element_by_xpath(self.selectors['arrival_place']).send_keys(arrival_place)

    # заполнение значений промежуточных пунктов
    def fill_middle_point(self, points):
        for index in range(len(points)):
            self.driver.find_element_by_xpath(self.selectors['middle_point'] % index).send_keys(points[index])
            if index+1 < len(points):
                self.driver.find_element_by_xpath(self.selectors['add_middle_point']).click()

    # выбор/снятие выбора режима "Поездка в две стороны"
    def both_ways_trip(self):
        self.driver.find_element_by_xpath(self.selectors['both_ways']).click()

    # заполнение полей "Дата отправления"
    def date_departure(self, date=None):
        if "day" in date.keys():
            # попробовать добавить clear
            self.driver.find_element_by_xpath(self.selectors['date_departure']).send_keys(date["day"])
        if "hour" in date.keys():
            select_hour = Select(self.driver.find_element_by_xpath(self.selectors['hour_departure']))
            select_hour.select_by_visible_text(date["hour"])
        if "minute" in date.keys():
            select_minute = Select(self.driver.find_element_by_xpath(self.selectors['minute_departure']))
            select_minute.select_by_visible_text(date["minute"])

    # заполнение полей "Дата обратной поездки"
    def date_backward(self, date=None):
        if "day" in date.keys():
            self.driver.find_element_by_xpath(self.selectors['date_backward']).send_keys(date["day"])
        if "hour" in date.keys():
            select_hour = Select(self.driver.find_element_by_xpath(self.selectors['hour_backward']))
            select_hour.select_by_visible_text(date["hour"])
        if "minute" in date.keys():
            select_minute = Select(self.driver.find_element_by_xpath(self.selectors['minute_backward']))
            select_minute.select_by_visible_text(date["minute"])

    # подтверждение отправки формы
    def next_step(self):
        self.driver.find_element_by_xpath(self.selectors['next_step_button']).click()

    # получение всех ошибок, выданных формой
    def get_all_errors(self):
        error_text = []
        errors = self.driver.find_elements_by_xpath(self.selectors['errors'])
        errors.extend(self.driver.find_elements_by_xpath(self.selectors['errors_place']))
        for error in errors:
            error_text.append(error.text)
        return error_text
