from class_file import Area
from class_file import Workarea
from class_file import Sweet_spot

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

def add_check_points(lst, a1, a2, a, b): # добавляет дополнительные точки в длинные 
    for wall in lst:                     # стены для проверки рабочй зоны на препятствия
        if wall[a1] < wall[a2]:
            i = 0.75
            while i < abs(wall[a2] - wall[a1]):
                check_points.append({b:wall[b], a:(wall[a1] + i)})
                i += 0.75 
        elif wall[a1] > wall[a2]:
            i = 0.75
            while i < abs(wall[a1] - wall[a2]):
                check_points.append({b:wall[b], a:(wall[a2] + i)})
                i += 0.75

#points = [{'x': 0.0, 'y': 0.0}, {'x': 0.0, 'y': 3.0}, {'x': 0.5, 'y': 3.0}, {'x': 0.5, 'y': 4.5}, {'x': 1.5, 'y': 4.5}, {'x': 1.5, 'y': 1.0}, {'x': 2.0, 'y': 1.0}, {'x': 2.0, 'y': 6.0}, {'x': 5.0, 'y': 6.0}, {'x': 5.0, 'y': 4.5}, {'x': 6.0, 'y': 4.5}, {'x': 6.0, 'y': 2.5}, {'x': 4.0, 'y': 2.5}, {'x': 4.0, 'y': 0.0}]
# этот со стеной в зоне
points = [{'x': 0.0, 'y': 0.0}, {'x': 0.0, 'y': 3.0}, {'x': 0.5, 'y': 3.0}, {'x': 0.5, 'y': 4.5}, {'x': 2.0, 'y': 4.5}, {'x': 2.0, 'y': 6.0}, {'x': 5.0, 'y': 6.0}, {'x': 5.0, 'y': 4.5}, {'x': 6.0, 'y': 4.5}, {'x': 6.0, 'y': 2.5}, {'x': 4.0, 'y': 2.5}, {'x': 4.0, 'y': 0.0}]
#points = [{'x': 0.0, 'y': 0.0}, {'x': 0.0, 'y': 2.0}, {'x': 0.5, 'y': 2.0}, {'x': 0.5, 'y': 3.5}, {'x': 2.0, 'y': 3.5}, {'x': 2.0, 'y': 5.0}, {'x': 5.0, 'y': 5.0}, {'x': 5.0, 'y': 3.5}, {'x': 6.0, 'y': 3.5}, {'x': 6.0, 'y': 1.5}, {'x': 4.0, 'y': 1.5}, {'x': 4.0, 'y': 0.0}]
check_points = [{'x': 2.0, 'y': 1.0}]
vertical_walls = []
horizontal_walls = []
v_areas = []
h_areas = []
distance = 0

wall_number = 0
while wall_number < 4:
    wall_number = int(input("Введите число стен (4 или больше): "))

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

room_size = 0 # площадь помещения 

for area in v_areas:
    room_size += area.size()

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

# выбираем стену, достаточную для расположения АС
testing = False # проверка для выхода из цикла выбора стены
testing_val = False # техническое значение для цикла
n = 0
while testing == False:
    try:
        step = 0
        wall_length = 0
        while wall_length < (1.5 * l):
            wall_length = abs(vertical_walls[step]['y1'] - vertical_walls[step]['y2'])
            step += 1
            chosen_lst = vertical_walls
            direction = 'v' # исключить
    except IndexError:
        step = 0
        wall_length = 0
        while wall_length < (1.5 * l):
            wall_length = abs(horizontal_walls[step]['x1'] - horizontal_walls[step]['x2'])
            step += 1
            chosen_lst = horizontal_walls
            direction = 'h' # исключить
    
    print('..........')
    print('wall length:', wall_length)
    print('chosen wall:', chosen_lst[step - 1])
    print('direction:', direction)

    ss = Sweet_spot(0, 0) # объявление экземпляра класса точки прослушивания
    ss_location() # определяем и фиксируем положение точки прослушивания
    print('sweet spot:')
    ss.prnt()    

    # определяем зону прослушивания:
    wa = Workarea(0, 0, 0, 0) # объявление экземпляра класса зоны прослушивания
    chosen_wall = chosen_lst[step - 1] # выбранная стена
    target = target_search() # определяем точку в которую смотрит слушатель
    print('target', target)
    workarea_cds = ss.create_workarea(l, target, distance) # определяем зону прослушивания
    print('workarea:')
    wa.set_area(workarea_cds)
    wa.prnt()

    # и проверяем отсутствие в ней стен и углов:
        # делим все большие стены и добавляем точки
    for point in points:
        check_points.append(point) # копируем список точек в который добавим дополнительные
    add_check_points(vertical_walls, 'y1', 'y2', 'y', 'x')
    add_check_points(horizontal_walls, 'x1', 'x2', 'x', 'y')
    # print(check_points)
    nnn = 0
    for point in check_points:
        test = wa.point_belongs(point['x'], point['y'])  
        nnn += 1
        print(str(test) + str(nnn))
        if test == True:
            chosen_lst.pop(step - 1)
            testing_val = True
            break
        testing_val = False
                
    if testing_val == True:
        print(check_points)
        check_points = []
        del target
        del chosen_lst
        del wa
        del workarea_cds
        del test
        del ss
        continue
    else:
        testing = True # проверка для выхода из цикла выбора стены