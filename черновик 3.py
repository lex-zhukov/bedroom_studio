# В ЭТОМ ФАЙЛЕ БУДЕТ ФУНКЦИЯ ОПРЕДЕЛЕНИЯ ЗОН С ЗАХОДОМ СТЕНЫ И ИХ ПРЕОБРАЗОВАНИЕМ
from class_file import Area
area = Area(0, 0, 0, 0)
area.set_coordinate('x1', 666)
area.prnt()
# если зоне принадлежит точка обратная false зоны outside, то зона recraft
# выделить все обратные точки зон стен