from names import *
from base_component import BaseComponent


class RouteInformation(BaseComponent):
    selectors = {
        'main_route': '//div[@class="publication-summary-container wrapper"]/p/strong',
        'date_arrival': '//dl[@class="dl-horizontal"]/dd[1]',
        'date_backward': '//dl[@class="dl-horizontal"]/dd[2]',
        'distance': '//dl[@class="dl-horizontal"]/dd[4]',
        'time_in_way': '//dl[@class="dl-horizontal"]/dd[5]',
        'release_co2': '//dl[@class="dl-horizontal"]/dd[6]'
    }

    @staticmethod
    def get_date_dict(date_in):
        date_in = date_in.text.split()
        time = date_in[4].split(':')
        date = {"day": date_in[1], "month": name_month[date_in[2]], "hour": time[0], "minute": time[1]}
        return date

    @staticmethod
    def get_date(date):
        date_out = {"day": date["day"].split('/')[0], "month": date["day"].split('/')[1],
                    "hour": date["hour"], "minute": date["minute"]}
        return date_out

    # получение значений начальной и конечной точки маршрута
    def get_route_points(self):
        route = self.driver.find_element_by_xpath(self.selectors['main_route'])
        route = route.text.split(' → ')
        return route

    # получение даты отправления
    def get_departure_date(self):
        date_arrival = self.driver.find_element_by_xpath(self.selectors['date_arrival'])
        date = RouteInformation.get_date_dict(date_arrival)
        return date

    # получение даты обратной поездки
    def get_backward_date(self):
        date_backward = self.driver.find_element_by_xpath(self.selectors['date_backward'])
        date = RouteInformation.get_date_dict(date_backward)
        return date

    # получение значения расстояния
    def get_distance(self):
        distance = self.driver.find_element_by_xpath(self.selectors['distance'])
        distance.text.split(' ')
        return distance[0]

    # получение значения времени в пути
    def get_time_in_way(self):
        time_in_way = self.driver.find_element_by_xpath(self.selectors['time_in_way'])
        time_in_way.text.split(' ')
        hour = time_in_way[0]
        minute = time_in_way[2]
        return hour, minute

    # получение значения выбросов СО2
    def get_release_co2(self):
        release_co2 = self.driver.find_element_by_xpath(self.selectors['release_co2'])
        return release_co2.text
