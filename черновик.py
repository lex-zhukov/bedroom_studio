from class_file import Area
import time

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
            area.prnt()
        elif lst == horizontal_walls:
            area = Area(coordinate_list[1], coordinate_list[2], lst[v1]['y'], lst[v2]['y'])
            h_areas.append(area)
            area.prnt()
    else:
        print(a, b, c, d, 'not overlaped')

#        area.prnt()  


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

def ex_through(lst, checked_area, wall_area):
    # вычисляет зоны с насквозь проходящей стеной, выделяет их в отдельный список
    # можно заменить функцию на универсальную и не использовать (сложная)
    global v_areas
    global h_areas
    x1_z1 = min([wall_area.get_coordinate('x1'), wall_area.get_coordinate('x2')]) 
    x2_z1 = max([wall_area.get_coordinate('x1'), wall_area.get_coordinate('x2')]) 
    y1_z1 = min([wall_area.get_coordinate('y1'), wall_area.get_coordinate('y2')]) 
    y2_z1 = max([wall_area.get_coordinate('y1'), wall_area.get_coordinate('y2')]) 
    x1_z2 = min([checked_area.get_coordinate('x1'), checked_area.get_coordinate('x2')]) 
    x2_z2 = max([checked_area.get_coordinate('x1'), checked_area.get_coordinate('x2')]) 
    y1_z2 = min([checked_area.get_coordinate('y1'), checked_area.get_coordinate('y2')]) 
    y2_z2 = max([checked_area.get_coordinate('y1'), checked_area.get_coordinate('y2')]) 
    if lst == v_areas:
        if ((x1_z2 <= x1_z1) and 
            (x2_z2 >= x2_z1) and
            (y1_z2 >= y1_z1) and
            (y2_z2 <= y2_z1)):
            excluded_v_areas.append(checked_area)
        else:
            return
    elif lst == h_areas:
        if ((x1_z1 <= x1_z2) and 
            (x2_z1 >= x2_z2) and
            (y1_z1 >= y1_z2) and
            (y2_z1 <= y2_z2)):
            excluded_h_areas.append(checked_area)
        else:
            return  

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
        text = 'зона не outside'
        print('.......................')
        zone.prnt()
        print(text)
        print('.......................')
        return

    zone.prnt()
    print(over_result)
    print(under_result)
    print(right_result)
    print(left_result)
    wallcheck_areas[0].prnt()
    for point in check_points:
        ask = wallcheck_areas[0].point_belongs(point['x'], point['y'])
        if ask == True:
            print('стена есть: ')
            zone.prnt()
            print('.......................')
            wallcheck_areas.clear()
            break
    else:
        lst.append(zone)

def empty_check(area, dir, wall): # функция проверяет зоны на находжение в них стен
    lines = area.get_lines(dir)   # и распределяет их по спискам для фильтрации
    result = []
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
        result.append(res)
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

points = [{'x': 0.0, 'y': 0.0}, {'x': 0.0, 'y': 3.0}, {'x': 0.5, 'y': 3.0}, {'x': 0.5, 'y': 4.5}, {'x': 1.5, 'y': 4.5}, {'x': 1.5, 'y': 1.0}, {'x': 2.0, 'y': 1.0}, {'x': 2.0, 'y': 6.0}, {'x': 5.0, 'y': 6.0}, {'x': 5.0, 'y': 4.5}, {'x': 6.0, 'y': 4.5}, {'x': 6.0, 'y': 2.5}, {'x': 4.0, 'y': 2.5}, {'x': 4.0, 'y': 0.0}]
# этот со стеной в зоне (14)

#points = [{'x': 0.0, 'y': 0.0}, {'x': 0.0, 'y': 3.0}, {'x': 0.5, 'y': 3.0}, {'x': 0.5, 'y': 4.5}, {'x': 2.0, 'y': 4.5}, {'x': 2.0, 'y': 6.0}, {'x': 5.0, 'y': 6.0}, {'x': 5.0, 'y': 4.5}, {'x': 6.0, 'y': 4.5}, {'x': 6.0, 'y': 2.5}, {'x': 4.0, 'y': 2.5}, {'x': 4.0, 'y': 0.0}]

check_points = []
vertical_walls = []
horizontal_walls = []
v_areas = []
h_areas = []
distance = 0

wall_number = 0
while wall_number < 4:
    wall_number = int(len(points))
    print('стен всего: ', wall_number)

# получаем точки углов (предполагается интерфейс, где их можно отметить на координатном поле):

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

# print(vertical_walls)
# print(horizontal_walls)

# выделяем зоны для расчета стоячих волн:

print("Зоны стоячих волн:")
wall_selection(vertical_walls, 'y1', 'y2')
print("...")
wall_selection(horizontal_walls, 'x1', 'x2')

# room_size = 0 # площадь помещения 

#for area in v_areas:
#    room_size += area.size()

# print(room_size, "m2")

print('v_areas:')
for area in v_areas:
    area.prnt()
print('h_areas:')
for area in h_areas:
    area.prnt()

focus_lst = [] # список фокусных точек
for area in v_areas:
    focus_point = area.focus()
    focus_lst.append(focus_point)
print(focus_lst)
print('points:   ')
print(len(focus_lst))

# РАБОТАТЬ ОТСЮДА

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
# excluded_v_areas = []
# excluded_h_areas = []

all_areas = v_areas + h_areas
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

for area in v_areas: # проверяем зоны на наличие стен
    for wall in vertical_walls:
        empty_check(area, 'v', wall)

for area in h_areas: # проверяем зоны на наличие стен
    for wall in horizontal_walls:
        empty_check(area, 'h', wall)

# убираем дубликаты из списков для фильтрации, переопределяем списки:

upcut_areas = list(set(upcut_areas))
downcut_areas = list(set(downcut_areas))
leftcut_areas = list(set(leftcut_areas))
rightcut_areas = list(set(rightcut_areas))
outside_areas = list(set(outside_areas))

print(upcut_areas)
print(downcut_areas)
print(leftcut_areas)
print(rightcut_areas)
print(outside_areas)



# for zone in outside_v_areas:
#     for area in v_areas:
#         ex_through(v_areas, area, zone)
    
# print('excluded zones:')
# for area in outside_areas:
#     area.prnt()



























# def focus_line_points(focus_point, direction):
#     line_points = []
#     add = 0.25
#     for i in range(10):
#         if direction == 'up':
#             y = focus_point['y'] + add
#             x = focus_point['x']
#         elif direction == 'down':
#             y = focus_point['y'] - add
#             x = focus_point['x']
#             if y < 0:
#                 break
#         elif direction == 'right':
#             x = focus_point['x'] + add
#             y = focus_point['y']
#         elif direction == 'left':
#             x = focus_point['x'] - add
#             y = focus_point['y']
#             if x < 0:
#                 break
#         line_points.append({'x':x, 'y':y})
#         add += 0.25
#     return line_points


# check_areas = [] # создаем проверочный список зон
# for area in v_areas: # добавляем зоны в проверочный список зон
#     check_areas.append(area)
# check_areas.remove(v_areas[7]) # убираем проверяемую зону из проверочного списка
# checklist = focus_line_points(focus_lst[7], 'up')    
    
# first_result = False
# count = 0
# for pos in checklist:
#     for area in check_areas:
#         result = area.point_belongs(pos['x'], pos['y'])
#         count += 1
#         print(result, count, pos)
#         area.prnt()
#         if result == True:
#             first_result = True
#             break

# print(first_result)
    
        
        
        
        
        
        
        
        
        
        
        