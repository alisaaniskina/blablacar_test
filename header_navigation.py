from base_component import BaseComponent


class HeaderNavigation(BaseComponent):
    selectors = {
        'offer_trip': '//a[@class="Header-navigationButton c-button c-button--primary"]',
        'sign_in': '//a[@class="Header-navigationText"][1]',
        'sign_up': '//a[@class="Header-navigationText"][2]'
    }

    # переход на страницу регистрации
    def go_to_sign_in(self):
        self.driver.find_element_by_xpath(self.selectors['sign_in']).click()

    # переход на страницу входа в аккаунт
    def go_to_sign_up(self):
        self.driver.find_element_by_xpath(self.selectors['sign_up']).click()

    # переход на страницу создания собственной поездки
    def go_to_offer_trip(self):
        self.driver.find_element_by_xpath(self.selectors['offer_trip']).click()
