from class_file_new import Area
from class_file_new import Workarea
from class_file_new import Sweet_spot

def walls(a, b):
    c_1 = (points[a]['x'])
    c_2 = (points[b]['x'])
    c_3 = (points[a]['y'])
    c_4 = (points[b]['y'])
    if c_1 == c_2 and c_3 != c_4:
        vertical_walls.append({'x':c_1, 'y1':c_3, 'y2':c_4})
    elif c_1 != c_2 and c_3 == c_4:
        horizontal_walls.append({'x1':c_1, 'x2':c_2, 'y':c_3})

def wall_selection(lst, p1, p2):
    val = len(lst)
    count_a = 0
    count_b = 0
    while count_b < val:
        while count_a != (val - 1):
            count_a += 1
            crd_1 = lst[count_b][p1]
            crd_2 = lst[count_b][p2]
            crd_3 = lst[count_a][p1]
            crd_4 = lst[count_a][p2]
            wall_overlap_comparison(crd_1, crd_2, crd_3, crd_4, lst, count_a, count_b)
        count_b += 1
        count_a = count_b

def wall_overlap_comparison(a, b, c, d, lst, v1, v2):
    if (((a > c > b) or (b > c > a)) or 
        ((a > d > b) or (b > d > a)) or 
        ((a == c and b == d) or (a == d and b == c)) or 
        (a < b and d < c and ((b == c and a != d) or (a == d and b != c))) or
        (a < b and c < d and ((b == d and a != c) or (a == c and b != d))) or
        (((b > d > a) and (b > c > a)) or ((d > b > c) and (d > a > c))) or 
        (b < a and d < c and ((a == c and b != d) or (b == d and a != c))) or
        (b < a and c < d and ((a == d and b != c) or (b == c and a != d)))):
        coordinate_list = sorted([a, b, c, d])
        if lst == vertical_walls:
            area = Area(lst[v1]['x'], lst[v2]['x'], coordinate_list[1], coordinate_list[2])
            v_areas.append(area)
        elif lst == horizontal_walls:
            area = Area(coordinate_list[1], coordinate_list[2], lst[v1]['y'], lst[v2]['y'])
            h_areas.append(area)
        area.prnt()  
    else:
        print('not overlaped')
        # return 0
        # нет наложения.  

def ss_location_support(val, val_0, ss_first, ss_second):
    point_check = {val:ss_first, val_0:ss_second}
    for area in v_areas:
        check = area.point_belongs(point_check[val], point_check[val_0])
        if check == True:
            if val == 'x':
                ss.set_location(ss_first, ss_second)
            elif val == 'y':
                ss.set_location(ss_second, ss_first)

def ss_location():
    global distance
    if chosen_lst == horizontal_walls:
        val = 'x'
        val_0 = 'y'
        val_1 = 'x1'
        val_2 = 'x2'
    elif chosen_lst == vertical_walls:
        val = 'y'
        val_0 = 'x'
        val_1 = 'y1'
        val_2 = 'y2'    

    if chosen_lst[step - 1][val_1] < chosen_lst[step - 1][val_2]:
        ss_first = chosen_lst[step - 1][val_1] + (0.5 * wall_length)
    else:
        ss_first = chosen_lst[step - 1][val_1] - (0.5 * wall_length)
    distance = ((l**2 - (0.5*l)**2)**0.5) + (0.25 * l)

    ss_second = chosen_lst[step - 1][val_0] - distance
    ss_location_support(val, val_0, ss_first, ss_second)
    ss_second = chosen_lst[step - 1][val_0] + distance
    ss_location_support(val, val_0, ss_first, ss_second)

def target_search():
    try:
        target_add = [chosen_wall['x1'], chosen_wall['x2']]
        target_x = (abs(chosen_wall['x2'] - chosen_wall['x1'])/2) + min(target_add)
        target_y = chosen_wall['y']
        target = {'x':target_x, 'y':target_y}
    except KeyError:
        target_add = [chosen_wall['y1'], chosen_wall['y2']]
        target_y = (abs(chosen_wall['y2'] - chosen_wall['y1'])/2) + min(target_add)
        target_x = chosen_wall['x']
        target = {'x':target_x, 'y':target_y}
    return target

def add_check_points(lst, a1, a2, a, b): # добавляет дополнительные точки в
    for wall in lst:                     # стены для проверки рабочй зоны на препятствия
        if wall[a1] < wall[a2]:
            i = 0.01
            while i < abs(wall[a2] - wall[a1]):
                check_points.append({b:wall[b], a:(wall[a1] + i)})
                i += 0.01 
        elif wall[a1] > wall[a2]:
            i = 0.01
            while i < abs(wall[a1] - wall[a2]):
                check_points.append({b:wall[b], a:(wall[a2] + i)})
                i += 0.01

def ex_areas(lst, zone):
    wallcheck_areas = []
    excluding = zone.exclude()
    for area in all_areas:
        over_result = area.point_belongs(excluding[0]['x'], excluding[0]['y'])
        if over_result == True:
            break
    for area in all_areas:
        under_result = area.point_belongs(excluding[1]['x'], excluding[1]['y'])
        if under_result == True:
            break
    for area in all_areas:
        right_result = area.point_belongs(excluding[2]['x'], excluding[2]['y'])
        if right_result == True:
            break
    for area in all_areas:
        left_result = area.point_belongs(excluding[3]['x'], excluding[3]['y'])
        if left_result == True:
            break
    summ = int(over_result) + int(under_result) + int(left_result) + int(right_result)
    if summ == 3:
        x_es = [(zone.get_coordinate('x1')), zone.get_coordinate('x2')]
        y_es = [(zone.get_coordinate('y1')), zone.get_coordinate('y2')]
        if over_result == False:
            wx_min = min(x_es) + 0.01 
            wx_max = max(x_es) - 0.01
            wy_min = max(y_es) - 0.01
            wy_max = max(y_es) + 0.01
        elif under_result == False:
            wx_min = min(x_es) + 0.01 
            wx_max = max(x_es) - 0.01
            wy_min = min(y_es) - 0.01
            wy_max = min(y_es) + 0.01
        elif right_result == False:
            wx_min = max(x_es) + 0.01 
            wx_max = max(x_es) - 0.01
            wy_min = min(y_es) + 0.01
            wy_max = max(y_es) - 0.01
        elif left_result == False:
            wx_min = min(x_es) + 0.01 
            wx_max = min(x_es) - 0.01
            wy_min = min(y_es) + 0.01
            wy_max = max(y_es) - 0.01
        wallcheck_areas.append(Area(wx_min, wx_max, wy_min, wy_max))
    else:
        return

    for point in check_points:
        ask = wallcheck_areas[0].point_belongs(point['x'], point['y'])
        if ask == True:
            wallcheck_areas.clear()
            break
    else:
        lst.append(zone)

def empty_check(area, dir, wall_list): # функция проверяет зоны на находжение в них стен
    lines = area.get_lines(dir)   # и распределяет их по спискам для фильтрации
    result = [False, False]
    for wall in wall_list:
        if dir == 'v':
            a = lines[0] # upline
            b = wall
        elif dir == 'h':
            b = lines[0] # leftline
            a = wall
        for i in range(2):
            if ((max([b['y1'], b['y2']]) > a['y'] > min([b['y1'], b['y2']])) and
                (max([a['x1'], a['x2']]) > b['x'] > min([a['x1'], a['x2']]))):
                res = True
            else:
                res = False
            if dir == 'v':
                a = lines[1] # downline
            elif dir == 'h':
                b = lines[1] # rightline
            result[i] = bool(result[i] + res)
    if sum(result) == 0:
        return
    elif sum(result) == 2:
        outside_areas.append(area)
    elif sum(result) == 1:
        outside_areas.append(area)
        if dir == 'v':
            if result[0] == False:
                downcut_areas.append(area)
            elif result[1] == False:
                upcut_areas.append(area)
        if dir == 'h':
            if result[0] == False:
                rightcut_areas.append(area)
            elif result[1] == False:
                leftcut_areas.append(area)
    return result

# без стены points = [{'x': 0.0, 'y': 0.0}, {'x': 0.0, 'y': 3.0}, {'x': 0.5, 'y': 3.0}, {'x': 0.5, 'y': 4.5}, {'x': 2.0, 'y': 4.5}, {'x': 2.0, 'y': 6.0}, {'x': 5.0, 'y': 6.0}, {'x': 5.0, 'y': 4.5}, {'x': 6.0, 'y': 4.5}, {'x': 6.0, 'y': 2.5}, {'x': 4.0, 'y': 2.5}, {'x': 4.0, 'y': 0.0}]
# со стеной 
points = [{'x': 0.0, 'y': 0.0}, {'x': 0.0, 'y': 3.0}, {'x': 0.5, 'y': 3.0}, {'x': 0.5, 'y': 4.5}, {'x': 1.5, 'y': 4.5}, {'x': 1.5, 'y': 1.0}, {'x': 2.0, 'y': 1.0}, {'x': 2.0, 'y': 6.0}, {'x': 5.0, 'y': 6.0}, {'x': 5.0, 'y': 4.5}, {'x': 6.0, 'y': 4.5}, {'x': 6.0, 'y': 2.5}, {'x': 4.0, 'y': 2.5}, {'x': 4.0, 'y': 0.0}]
#points = [{'x': 0.0, 'y': 0.0}, {'x': 0.0, 'y': 3.0}, {'x': 3.0, 'y': 3.0}, {'x': 3.0, 'y': 2.0}, {'x':3.5, 'y': 2.0}, {'x': 3.5, 'y': 1.5}, {'x': 4.0, 'y': 1.5}, {'x': 4.0, 'y': 3.0}, {'x': 5.0, 'y': 3.0}, {'x': 5.0, 'y': 1.0}, {'x': 4.0, 'y': 1.0}, {'x':4.0, 'y': 0.5}, {'x': 5.0, 'y': 0.5}, {'x': 5.0, 'y': 0.0}]
check_points = []
vertical_walls = []
horizontal_walls = []
v_areas = []
h_areas = []
distance = 0

wall_number = 0
while wall_number < 4:
    wall_number = int(input("Введите число стен (4 или больше): "))

# for i in range(wall_number):
#    i += 1
#    point_x = float(input(f"Введите координату x точки {i}: "))
#    point_y = float(input(f"Введите координату y точки {i}: "))
#    points.append({'x':point_x, 'y':point_y})

# получаем списки с координатами стен по направлениям (вертикальные/горизонтальные):
    
z = 0
while z < wall_number:
    walls(z - 1, z)
    z += 1

# выделяем зоны для расчета стоячих волн:

print("Зоны стоячих волн:")
wall_selection(vertical_walls, 'y1', 'y2')
print("...")
wall_selection(horizontal_walls, 'x1', 'x2')

########################################################################################
# СЕКЦИЯ С ФИЛЬТРАЦИЕЙ ЗОН #
########################################################################################

focus_lst = [] # список фокусных точек
for area in v_areas:
    focus_point = area.focus()
    focus_lst.append(focus_point)

for point in points:
    check_points.append(point) # копируем список точек в который добавим дополнительные
add_check_points(vertical_walls, 'y1', 'y2', 'y', 'x')
add_check_points(horizontal_walls, 'x1', 'x2', 'x', 'y')

upcut_areas = []
downcut_areas = []
leftcut_areas = []
rightcut_areas = []
outside_areas = []
outside_v_areas = []
outside_h_areas = []

all_areas = v_areas + h_areas

# получаем проецкии фокуса для каждой зоны и распределяем их в списки,
# в дальнейшем они понадобятся для переопределения зон:
updots = []
downdots = []
leftdots = []
rightdots = []

for area in all_areas:
    dots = area.get_dots()
    updots.append(dots[0])
    downdots.append(dots[1])
    leftdots.append(dots[2])
    rightdots.append(dots[3])

for area in v_areas: # проверяем зоны на наличие стен
    empty_check(area, 'v', vertical_walls)
# убираем дубликаты из списков для фильтрации, переопределяем списки:
upcut_areas = list(set(upcut_areas))
downcut_areas = list(set(downcut_areas))
outside_areas = list(set(outside_areas))
# удаляем лишние зоны
for area in outside_areas:
    v_areas.remove(area)
outside_areas.clear()    

for area in h_areas: # проверяем зоны на наличие стен
    empty_check(area, 'h', horizontal_walls)
# убираем дубликаты из списков для фильтрации, переопределяем списки:
leftcut_areas = list(set(leftcut_areas))
rightcut_areas = list(set(rightcut_areas))
outside_areas = list(set(outside_areas))
# удаляем лишние зоны
for area in outside_areas:
    h_areas.remove(area)
outside_areas.clear()

# переделываем зоны с дефектами (заходящей стеной):

for area in upcut_areas: # для зон со стеной сверху
    dots_check = []
    for point in downdots:
        checkdot = area.point_belongs(point['x'], point['y'])
        if checkdot == True:
            dots_check.append(point)
    dots_check.sort(key=lambda x: x.get('y'))
    new_crd = dots_check[0]['y'] 
    a_y1 = area.get_coordinate('y1')
    a_y2 = area.get_coordinate('y2')
    if a_y1 > a_y2:
        area.set_coordinate('y1', new_crd)
    elif a_y1 < a_y2:  
        area.set_coordinate('y2', new_crd)

for area in upcut_areas:
    v_areas.append(area)
    dots_check.clear()

for area in downcut_areas: # для зон со стеной снизу
    dots_check = []
    for point in updots:
        checkdot = area.point_belongs(point['x'], point['y'])
        if checkdot == True:
            dots_check.append(point)
    dots_check.sort(key=lambda x: x.get('y'))
    new_crd = dots_check[-1]['y'] 
    a_y1 = area.get_coordinate('y1')
    a_y2 = area.get_coordinate('y2')
    if a_y1 < a_y2:
        area.set_coordinate('y1', new_crd)
    elif a_y1 > a_y2:  
        area.set_coordinate('y2', new_crd)

for area in downcut_areas:
    v_areas.append(area)
    dots_check.clear()

for area in leftcut_areas: # для зон со стеной слева
    dots_check = []
    for point in rightdots:
        checkdot = area.point_belongs(point['x'], point['y'])
        if checkdot == True:
            dots_check.append(point)
    dots_check.sort(key=lambda x: x.get('x'))
    new_crd = dots_check[-1]['x'] 
    a_x1 = area.get_coordinate('x1')
    a_x2 = area.get_coordinate('x2')
    if a_x1 < a_x2:
        area.set_coordinate('x1', new_crd)
    elif a_x1 > a_x2:  
        area.set_coordinate('x2', new_crd)

for area in leftcut_areas:
    h_areas.append(area)
    dots_check.clear()
        
for area in rightcut_areas: # для зон со стеной справа
    dots_check = []
    for point in leftdots:
        checkdot = area.point_belongs(point['x'], point['y'])
        if checkdot == True:
            dots_check.append(point)
    dots_check.sort(key=lambda x: x.get('x'))
    new_crd = dots_check[0]['x'] 
    a_x1 = area.get_coordinate('x1')
    a_x2 = area.get_coordinate('x2')
    if a_x1 > a_x2:
        area.set_coordinate('x1', new_crd)
    elif a_x1 < a_x2:  
        area.set_coordinate('x2', new_crd)

for area in rightcut_areas:
    h_areas.append(area)
    dots_check.clear()        

check_number = len(all_areas)//2 # количество проверок зон на outside

for i in range(check_number): # повторяем проверки на outside, чтобы исключить 
                              # стены внутри стен в нескольких уровнях
    for zone in v_areas: # выделяем зоны outside в списках зон
        ex_areas(outside_v_areas, zone)
    for zone in h_areas:
        ex_areas(outside_h_areas, zone)
    for zone in outside_v_areas: # удаляем зоны outside из списков зон
        v_areas.remove(zone)
    for zone in outside_h_areas:
        h_areas.remove(zone)
    outside_v_areas.clear() # очищаем списки зон outside для исключения ошибок
    outside_h_areas.clear() # при следующем удалении
    all_areas.clear()
    all_areas = v_areas + h_areas

print('----------------')
for area in v_areas:
    area.prnt()
print('----------------')
for area in h_areas:
    area.prnt()

########################################################################################

room_size_1 = 0 # площадь помещения по вертикальным зонам
room_size_2 = 0 # площадь помещения по горизонтальным зонам 

for area in v_areas:
    room_size_1 += area.size()
for area in h_areas:
    room_size_2 += area.size()

if room_size_1 == room_size_2:
    room_size = room_size_1
else: # если расчет зон произошел верно, то вывдоится площадь помещения.
      # если возникли ошибки, то помещение слишком сложное.
    print('слишком сложное помещение')

if room_size >= 20:
    woofer_size = '8"' # размер НЧ динамика АС
    l = 2.0 # базовое расстояние между АС и sweet spot
elif 15 <= room_size < 20:
    woofer_size = '6-7 inch'
    l = 1.5    
elif 9 <= room_size < 15:
    woofer_size = '5 inch'
    l = 1.5     
elif 3 <= room_size < 9:
    woofer_size = '3-4 inch'
    l = 1.2
else:
    print('too small room')

print(room_size, "m2")

# отфильтруем стены и выберем те, длина которых позволяет расположить АС
# раскидаем их по спискам вертикальных и горизонтальных

vertical_walls_AS = []
horizontal_walls_AS = []
ss = Sweet_spot(0, 0) # объявление экземпляра класса точки прослушивания
wa = Workarea(0, 0, 0, 0) # объявление экземпляра класса зоны прослушивания

def wall_length(wall):
    global l
    try:
        if wall['x'] >= 0:
            a = 'y1'
            b = 'y2'
            newlist = vertical_walls_AS
    except KeyError:
        a = 'x1'
        b = 'x2'
        newlist = horizontal_walls_AS
    wall_length = abs(wall[a] - wall[b])
    if wall_length >= 1.5 * l:
        newlist.append(wall)

for wall in vertical_walls:
    wall_length(wall)
    
for wall in horizontal_walls:
    wall_length(wall)

print(vertical_walls_AS)
print('..............')
print(horizontal_walls_AS)

# получили возможные стены, дальше определяем возможные зоны прослушивания
# нужна функция определения центра стены, определения зон по обе стороны стены
# дальше мы отфильтруем зоны

potencial_wa_v = [] # потенциальные зоны у вертикальных стен
potencial_wa_h = [] # потенциальные зоны у горизонтальных стен

def wa_filter(wall):
    try:
        if wall['x'] >= 0:
            # по вертикальным справа от стены
            wall_center = abs(wall['y1'] - wall['y2'])/2 + min([wall['y1'], wall['y2']])
            distance = ((l**2 - (0.5*l)**2)**0.5) + (0.25 * l)
            a = wall['x'] + 0.001                                # x1
            b = wall['x'] + distance + (0.249 * l)               # x2
            c = wall_center - (0.749 * l)                        # y1
            d = wall_center + (0.749 * l)                        # y2
            # по вертикальным справа от стены
            e = wall['x'] - 0.001                                # x1
            f = wall['x'] - distance - (0.249 * l)               # x2
            potencial_wa_v.append(Area(a, b, c, d))
            potencial_wa_v.append(Area(e, f, c, d))
    except KeyError:
        # по горизонтали сверху от стены
        wall_center = abs(wall['x1'] - wall['x2'])/2 + min([wall['x1'], wall['x2']])
        distance = ((l**2 - (0.5*l)**2)**0.5) + (0.25 * l)
        # РАБОТАТЬ ОТСЮДА, ПРОВЕРИТЬ ВСЕ ЧТО ДАЛЬШЕ
        a = wall['x'] + 0.001                                # x1
        b = wall['x'] + distance + (0.249 * l)               # x2
        c = wall_center - (0.749 * l)                        # y1
        d = wall_center + (0.749 * l)                        # y2        
    


























