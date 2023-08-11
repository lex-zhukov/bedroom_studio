# В ЭТОМ ФАЙЛЕ ФУНКЦИЯ ОПРЕДЕЛЯЮЩАЯ ЗОНУ СО СТЕНОЙ (upline, downline...)

# EMPTY CHECK FOR AREAS

# метод для зоны get_lines
    


# WALL - СТЕНА В СПИСКАХ СТЕН
# UPLINE, DOWNLINE... - МНИМЫЕ СТЕНЫ ДЛЯ ПРОВЕРКИ

def empty_check(area, dir, wall):
    lines = area.get_lines(dir)
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

# Так мы проверим каждую зону на все стены, переместим True/True в excluded по направлениям,
# а True/False переместим по направлениям в recrafted. Удалим затем все outside и excluded 
# из основных списков, добавим recrafted с новыми размерами и зоны готовы.

# empty_check

if result == 2:
    exclded
elif result == 1:
    exclded
    recrafted
elif reslt == 0:
    None