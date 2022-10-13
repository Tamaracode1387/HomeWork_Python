#  Задача №1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#  Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный,
#  желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
#  третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
#  порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
#

# import time

# class TrafficLight():

#     red_wait = 7
#     yellow_wait = 2
#     green_wait = 1

#     red = 'красный'
#     yellow = 'желтый'
#     green = 'зеленый'

#     def __init__(self, color):
#         self.__color = color
        

#     def light_time(self, color, wait_period):
#         self.wait_period = wait_period
#         print(f'{color} свет - {self.wait_period} сек')
#         time.sleep(self.wait_period)

#     def running(self, color = ''):

#         if not color:
#             some_color = self.__color
#         else:
#             some_color = color

#         if some_color == self.red:
#             self.light_time('красный', self.red_wait)
#             self.light_time('желтый', self.yellow_wait)
#             self.light_time('зеленый', self.green_wait)
#         elif some_color == self.yellow:
#             self.light_time('желтый', self.yellow_wait)
#             self.light_time('зеленый', self.green_wait)
#             self.light_time('красный', self.red_wait)
#         else:
#             self.light_time('зеленый', self.green_wait)
#             self.light_time('красный', self.red_wait)
#             self.light_time('желтый', self.yellow_wait)

#         print('Цикл завершен')

# tl1 = TrafficLight('красный')
# tl1.running()

# tl2 = TrafficLight('желтый')
# tl2.running()

# tl3 = TrafficLight('зеленый')
# tl3.running()

########################################################################################################################

# Задача №2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать
# защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
#
# Например: 20м * 5000м * 25кг * 5см = 12500 т

# class Road():

#     # Вес асфальта в тоннах для 1 кв.м. полотна толщиной в 1 см
#     # Определяю его как private из соображений, что это константа, не подлежащая изменению
#     weight = 1.0

#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#         print(f'Длина дороги - {self._length} м., ширина дороги - {self._width} м.')

#     def get_weight(self, thickness):
#         weight = self._length * self._width * thickness * self.weight
#         print(f'Масса асфальта для укладки полотна толщиной {thickness} см, равна {weight} т')

#         return weight

# r1 = Road(1000, 10)
# w1 = r1.get_weight(10)

# r2 = Road(2000, 5)
# w2 = r2.get_weight(10)

