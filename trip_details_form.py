from base_component import BaseComponent


class TripDetailsForm(BaseComponent):

    selectors = {
        'list_routes': '//div[@class="price-stage-container"]',
        'seat_count': '//input[@id="new_publication_step2_seatCount"]',
        'guarantee_back_seat': '//input[@id="new_publication_step2_is_comfort"]',
        'comment_arrival': '//textarea[@id="new_publication_step2_comment"]',
        'comment_backward': '//textarea[@id="new_publication_step2_comment_return"]',
        'same_comment': '//input[@id="new_publication_step2_same_comment_for_return"]',
        'agree_terms': '//input[@id="new_publication_step2_cgu"]',
        'next_step_button': '//button[@id="track-step2-submit"]',
        'previous_step_button': '//a[@class="u-blue padding-right"]',
        'rules': '//a[@href="#commentRulesModal"]',
        'term_of_use': '//label[@id="new_publication_step2_cgu"]/a[1]',
        'privacy_policy': '//label[@id="new_publication_step2_cgu"]/a[2]',
        'price': '//input[@id="new_publication_step2_prices_%s"]',
        'errors': '//p[@class="alert alert-error no-icon u-clearfix js-formError _test-formError "]'
    }

    def get_price_by_route(self):
        prices = []
        routes = len(self.driver.find_elements_by_xpath(self.selectors['list_routes']))
        for count in range(routes):
            price = self.driver.find_element_by_xpath(self.selectors['price'] % count).get_attribute("value")
            prices.append(price)
        return prices

    # получение всех городов из списка всех маршрутов
    def get_points_routes(self):
        routes = self.driver.find_elements_by_xpath(self.selectors['list_routes']).text
        # здесь нужно придумать, как собрать данные с нескольких маршрутов,
        # чтобы удобно было проверять
        for route in routes:
            pass

    # заполнение полей "Цена с пассажира"
    def price_by_passengers(self, prices):
        # собираются все строки, содержащие маршруты
        routes = len(self.driver.find_elements_by_xpath(self.selectors['list_routes']))
        for count in range(routes):
            self.driver.find_element_by_xpath(self.selectors['price'] % count).send_keys(prices[count])

    # заполнение значения свободных мест
    def free_seats(self, seat_count):
        seat = self.driver.find_element_by_xpath(self.selectors['seat_count'])
        seat.clear()
        seat.send_keys(seat_count)
        # seat.submit()
        # confirm = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//button[@class="Button u-blue-bg"]')))
        # confirm.click()

    # выбор/снятие выбора "Максимум два пассажира на заднем сиденье"
    def guarantee_back_seat(self):
        self.driver.find_element_by_xpath(self.selectors['guarantee_back_seat']).click()

    # не работает
    # заполнение поля "Информация о поездке"
    def fill_departure_comment(self, comment):
        self.driver.find_element_by_xpath(self.selectors['comment_arrival']).send_keys(comment)

    # заполнение поля "Комментарий к обратной поездке"
    def fill_backward_comment(self, comment):
        self.driver.find_element_by_xpath(self.selectors['same_comment']).click()
        self.driver.find_element_by_xpath(self.selectors['comment_backward']).send_keys(comment)

    # снятие выбора/выбор "Условия пользовательского соглашения"
    def agree_policy(self, ):
        self.driver.find_element_by_xpath(self.selectors['agree_terms']).click()

    # подтверждение отправки формы, кнопка "Продолжить"
    def next_step(self):
        self.driver.find_element_by_xpath(self.selectors['next_step_button']).click()

    # перейти к предыдущему пункту, кнопка "Назад"
    def previous_step(self):
        self.driver.find_element_by_xpath(self.selectors['previous_step_button']).click()

    # переход по ссылке "Ознакомьтесь с правилами"
    def read_rules(self):
        self.driver.find_element_by_xpath(self.selectors['rules']).click()

    # переход по ссылке "Условия использования"
    def term_of_use(self):
        self.driver.find_element_by_xpath(self.selectors['term_of_use']).click()

    # переход по ссылке "Политика конфиденциальности"
    def privacy_policy(self):
        self.driver.find_element_by_xpath(self.selectors['privacy_policy']).click()

    # получение всех ошибок, выданных формой
    def get_all_errors(self):
        error_text = []
        errors = self.driver.find_elements_by_xpath(self.selectors['errors'])
        for error in errors:
            error_text.append(error.text)
        return error_text
