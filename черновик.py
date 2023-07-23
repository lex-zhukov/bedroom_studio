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


def add_check_points(lst, a1, a2, a, b): # добавляет дополнительные точки в длинные 
    for wall in lst:                     # стены для проверки рабочй зоны на препятствия
        if wall[a1] < wall[a2]:
            i = 0.1
            while i < abs(wall[a2] - wall[a1]):
                check_points.append({b:wall[b], a:(wall[a1] + i)})
                i += 0.1 
        elif wall[a1] > wall[a2]:
            i = 0.1
            while i < abs(wall[a1] - wall[a2]):
                check_points.append({b:wall[b], a:(wall[a2] + i)})
                i += 0.1

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

outside_areas = []

# ставим 4 точки вокруг зоны
# если 3 из них point_belongs = True, а одна False, то это потенциальная outside
# если со стороны False нет стены, то это outside



#for area in v_areas:
excluding = v_areas[0].exclude()
for area in v_areas:
    over_result = area.point_belongs(excluding[0]['x'], excluding[0]['y'])
    if over_result == True:
        break
for area in v_areas:
    under_result = area.point_belongs(excluding[1]['x'], excluding[1]['y'])
    if under_result == True:
        break
for area in v_areas:
    right_result = area.point_belongs(excluding[2]['x'], excluding[2]['y'])
    if right_result == True:
        break
for area in v_areas:
    left_result = area.point_belongs(excluding[3]['x'], excluding[3]['y'])
    if right_result == True:
        break
summ = int(over_result) + int(under_result) + int(left_result) + int(right_result)
if summ == 3:
    side = min([over_result, under_result, left_result, right_result])
    
    
    


        

print(over_result)
print(under_result)
print(right_result)
print(left_result)































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
    
        
        
        
        
        
        
        
        
        
        
        