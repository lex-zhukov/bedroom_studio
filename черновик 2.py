# В ЭТОМ ФАЙЛЕ ФУНКЦИИ С ПРОШЛОЙ НЕДЕЛИ, СКОРЕЕ ВСЕГО НЕ ПОНАДОБЯТСЯ, СЛИШКОМ СЛОЖНЫЕ, ОБЕ

#!!!!!! Перемещать выбраную стену в конец списка стен после выполнения прораммы !!!!!!

overlaped_v_areas = []
deleted_areas = []

def cross_area(area, control_lst): # функция для вертикальной зоны, исключает зоны со сквозной outside-зоной.
    crds = area.prnt()
    x1 = crds['x1'] 
    x2 = crds['x2']
    y1 = crds['y1']
    y2 = crds['y2']
    ran = (abs(x1 - x2) * 1000) - 2
    mm = 0
    for mm in range(ran):
        mm += 0.001 
        test_point = {'x':(min([x1, x2]) + mm), 'y':(min([y1, y2]) + 0.001)}
        for zone in control_lst: # контрольным списком будет outside_areas после фокус теста
            first_value = zone.point_belongs(test_point['x'], test_point['y'])
            first_result += first_value
    mm = 0
    for mm in range(ran):
        mm += 0.001 
        test_point = {'x':(min([x1, x2]) + mm), 'y':(max([y1, y2]) - 0.001)}
        for zone in control_lst: # контрольным списком будет outside_areas после фокус теста
            second_value = zone.point_belongs(test_point['x'], test_point['y'])
            second_result += second_value
    if first_value * second_value == True:
        deleted_areas.append(area)
    elif first_value + second_value == False:
        print('area is OK')
    elif (first_value == False) and (second_value == True):
        new_area = ?????????????
        v_areas.append(new_area)
    elif (first_value == True) and (second_value == False):
        new_area = ?????????????
        v_areas.append(new_area)


# Накладывающиеся зоны, последняя проверка:

for point in focus_lst:
    for area in v_areas: # выделяем накладывающиеся зоны для выбраного фокуса
        value = area.point_belongs(point['x'], point['y'])
        if value == True:
            overlaped_v_areas.append(area)
    for area in overlaped_v_areas: # удаляем накладывающиеся зоны из основного списка зон
        v_areas.remove(area)
    v_areas.append(min(overlaped_v_areas)) # возвращаем нужную зону в основной список зон