# построение помещения по координатам
# инициализация стен и их направлений
# выделение прямоугольных зон
    # определить все горизонтальные стены
    # определить наложение друг на друга между всеми
    # если наложение есть, то создать зону, это будет x1 и x2
    # y1 и y2 взять из сравниваемых стен
    # повторить для вертикальных стен
# расчет стоячих волн по зонам
# выделение стены достаточной длины для размещения АС
# проверка площади для размещения точки прослушивания
# проверка отступа от всех стен

from class_file import Area

# l = 1 # длина (ширина) помещения
# sound_speed = 343.1 # скорость звука в студии (воздух, температура 20C, давление 1А)
# standing_wave = sound_speed / (l * 2) # формула стоячей волны
# print(standing_wave, "Hz")

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
        (a < b and c < d and ((b == d and a != c) or (a == c and b != d)))):
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

points = [{'x': 0.0, 'y': 0.0}, {'x': 0.0, 'y': 2.0}, {'x': 0.5, 'y': 2.0}, {'x': 0.5, 'y': 3.5}, {'x': 2.0, 'y': 3.5}, {'x': 2.0, 'y': 5.0}, {'x': 5.0, 'y': 5.0}, {'x': 5.0, 'y': 3.5}, {'x': 6.0, 'y': 3.5}, {'x': 6.0, 'y': 1.5}, {'x': 4.0, 'y': 1.5}, {'x': 4.0, 'y': 0.0}]
vertical_walls = []
horizontal_walls = []
v_areas = []
h_areas = []

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

print(vertical_walls)
print(horizontal_walls)

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

try:
    step = 0
    wall_length = 0
    while wall_length < (1.5 * l):
        wall_length = abs(vertical_walls[step]['y1'] - vertical_walls[step]['y2'])
        step += 1
        direction = 'v'
except IndexError:
    step = 0
    wall_length = 0
    while wall_length < (1.5 * l):
        wall_length = abs(horizontal_walls[step]['x1'] - horizontal_walls[step]['x2'])
        step += 1
        direction = 'h'
    
print(wall_length)
if direction == 'h':
    lst = horizontal_walls
elif direction == 'v':
    lst = vertical_walls
print(lst[step - 1])
print(direction)







   # определяем sweet spot (x, y)
    # проверяем размещение, проверяем удаленность от стен
    
