# BlaBlaCar tests
Автотесты для функционала [добавления cобственной поездки](https://www.blablacar.ru/offer-seats/1) сервиса BlaBlaCar.
- Используемые средства автоматизации: Python 3.7, Selenium Webdriver, unittest, DDT
- Система непрерывной интеграции: Jenkins CI
- Браузер: Mozilla Firefox

##### Информация о поездке
[![Build Status](http://localhost:8080/buildStatus/icon?job=blablacar_information)](http://localhost:8080/job/blablacar_information) 
* [Автотесты](https://github.com/alisaaniskina/blablacar_test/blob/master/test_information_trip.py), проверяющие обработку пользовательских пунктов отправки и прибытия, даты и времени поездок.
* [Отчеты о найденных ошибках](https://github.com/alisaaniskina/blablacar_test/blob/master/bug-reports/trip_information.txt)

##### Детали поездки
[![Build Status](http://localhost:8080/buildStatus/icon?job=blablacar_details&build=13)](http://localhost:8080/job/blablacar_details/13/) 
* [Автотесты](https://github.com/alisaaniskina/blablacar_test/blob/master/test_trip_details.py) для проверки обработки введённых цен, количества пассажиров и соответствия требуемым условиям.
