# В ЭТОМ ФАЙЛЕ ТОЛЬКО ФУНКЦИЯ СРАВНЕНИЯ ДЛЯ ИСКЛЮЧЕНИЯ ПОЛНОСТЬЮ ПЕРЕСЕКАЮЩИХСЯ ЗОН
# СОВМЕСТИТЬ АЛГОРИТМЫ В ФУНКЦИЮ

# VERTICAL WALL ZONE (for v_areas)

# wall area
x1_z1 = 4
x2_z1 = 5
y1_z1 = 1
y2_z1 = 3

# checked area
x1_z2 = 1
x2_z2 = 5
y1_z2 = 1
y2_z2 = 3

if ((x1_z2 <= x1_z1) and 
    (x2_z2 >= x2_z1) and
    (y1_z2) >= (y1_z1) and
    (y2_z2) <= (y2_z1)):
    print('exclude this area')
else:
    print('leave this area')

# HORIZONTAL WALL ZONE (for h_areas)

# wall area
x1_z1 = 2
x2_z1 = 3
y1_z1 = 2
y2_z1 = 3

# checked area
x1_z2 = 1
x2_z2 = 5
y1_z2 = 1
y2_z2 = 4

if ((x1_z2 >= x1_z1) and 
    (x2_z2 <= x2_z1) and
    (y1_z2) <= (y1_z1) and
    (y2_z2) >= (y2_z1)):
    print('exclude this area')
else:
    print('leave this area')