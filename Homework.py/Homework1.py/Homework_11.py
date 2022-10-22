""" 1. Создать класс TrafficLight (светофор):

● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● врамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт. """

""" from time import sleep
from datetime import datetime as dt

class TrafficLight:

    _states = {'red': 7, 'yellow': 2, 'green': 10}
_color = ''
def running(self):
        for color, sw_time in self._states.items():
             self._color = color
             start_state_time = dt.now()

        print(f"TrafficLight switched to state '{self._color}' "
                 f"on {sw_time} seconds")
        sleep(sw_time)

        print(f"TrafficLight leave state '{self._color}' after"
                f"{(dt.now() - start_state_time).seconds} seconds")
if __name__ == '__main__':
    tl = TrafficLight()
    tl.running() """



""" 2. Реализовать класс Road (дорога).
● определить атрибуты: length (длина), width (ширина);
● значения атрибутов должны передаваться при создании экземпляра класса;
● атрибуты сделать защищёнными;
● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна;
● проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т. """

""" class Road:
    _surface_spec_gravity: float = 0.02
def __init__(self, length: [int, float], width: [int, float]):
      """
  """   :param length: Длина дорожного полотна в метрах
    :param width: Ширина дорожного полотна в метрах """

""" self._length = float(length)
self._width = float(width)

def get_surface_gravity(self, thickness: float) ->[float, None]: """


""" Рассчет массы дорожного полотна заданной толщина
:param thickness: Толщина дорожного покрытия в сантиметрах
:return: Масса дорожного полотна в тоннах если все ОК, иначе None """

""" try:
        return (self._length * self._width
            * thickness * self._surface_spec_gravity)
except TypeError:
        return None


if __name__ == '__main__':
   try:
        road = Road(5000, 10)
        print(
            'Масса дорожного покрытия составит:',
             road.get_surface_gravity(20),
            'тонн'
         )
   except TypeError:
         print('класс Road требует 2 позиционных аргумента') """