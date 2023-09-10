from __classes__ import Area
from __classes__ import Workarea

def engine(points, grand_l):
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

    def empty_check(area, direction, wall_list): # функция проверяет зоны на находжение в них стен
        lines = area.get_lines(direction)   # и распределяет их по спискам для фильтрации
        result = [False, False]
        for wall in wall_list:
            if direction == 'v':
                a = lines[0] # upline
                b = wall
            elif direction == 'h':
                b = lines[0] # leftline
                a = wall
            for i in range(2):
                if ((max([b['y1'], b['y2']]) > a['y'] > min([b['y1'], b['y2']])) and
                    (max([a['x1'], a['x2']]) > b['x'] > min([a['x1'], a['x2']]))):
                    res = True
                else:
                    res = False
                if direction == 'v':
                    a = lines[1] # downline
                elif direction == 'h':
                    b = lines[1] # rightline
                result[i] = bool(result[i] + res)
        if sum(result) == 0:
            return
        elif sum(result) == 2:
            outside_areas.append(area)
        elif sum(result) == 1:
            outside_areas.append(area)
            if direction == 'v':
                if result[0] == False:
                    downcut_areas.append(area)
                elif result[1] == False:
                    upcut_areas.append(area)
            if direction == 'h':
                if result[0] == False:
                    rightcut_areas.append(area)
                elif result[1] == False:
                    leftcut_areas.append(area)
        return result

    def wall_length(wall):
    #    global l
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
                # по вертикальным слева от стены
                e = wall['x'] - 0.001                                # x1
                f = wall['x'] - distance - (0.249 * l)               # x2
                potencial_wa_v.append(Workarea(a, b, c, d, 'left'))
                potencial_wa_v.append(Workarea(e, f, c, d, 'right'))
        except KeyError:
            # по горизонтали сверху от стены
            wall_center = abs(wall['x1'] - wall['x2'])/2 + min([wall['x1'], wall['x2']])
            distance = ((l**2 - (0.5*l)**2)**0.5) + (0.25 * l)
            a = wall_center - (0.749 * l)                        # x1
            b = wall_center + (0.749 * l)                        # x2
            c = wall['y'] + 0.001                                # y1
            d = wall['y'] + distance + (0.249 * l)               # y2
            # по горизонтали снизу от стены
            e = wall['y'] - 0.001                                # y1
            f = wall['y'] - distance - (0.249 * l)               # y2
            potencial_wa_h.append(Workarea(a, b, c, d, 'down'))
            potencial_wa_h.append(Workarea(a, b, e, f, 'up'))

    def area_pass(area, lst): # функция для проверки потенциальных зон в подходящие
        focus = area.focus()
        for zone in all_areas:
            val_1 = zone.point_belongs(focus['x'], focus['y'])
            if val_1 == True:
                break
        if val_1 == False:
            return
        else:
            for point in check_points:
                val_2 = area.point_belongs(point['x'], point['y'])
                if val_2 == True:
                    return
            if val_2 == False:
                lst.append(area)
                
    def pan_center(area):
        def area_search(lst, val):
            for zone in lst:
                val_1 = zone.point_belongs(midpoint_dot['x'], midpoint_dot['y'])
                if val_1 == True:
                    area_34 = zone
                val_2 = zone.point_belongs(sweet_spot['x'], sweet_spot['y'])
                if val_2 == True:
                    area_56 = zone
            areas = [area_34, area_56]
            result = areas[val]
            return result
        def c_3456(val):
            if val == 'x':
                a = 'x1'
                b = 'x2'
            elif val == 'y':
                a = 'y1'
                b = 'y2'
            min_34 = min([area_34.get_coordinate(a), area_34.get_coordinate(b)])
            max_34 = max([area_34.get_coordinate(a), area_34.get_coordinate(b)])
            min_56 = min([area_56.get_coordinate(a), area_56.get_coordinate(b)])
            max_56 = max([area_56.get_coordinate(a), area_56.get_coordinate(b)])
            lst = [min_34, max_34, min_56, max_56]
            return lst
        wa = area
        direction = area.get_direction()
        focus = area.focus()
        distance = ((l**2 - (0.5*l)**2)**0.5) + (0.25 * l)
        midpoint = (((distance - (l / 4)) / 4) * 3)
        maxy = max([area.get_coordinate('y1'), area.get_coordinate('y2')])
        miny = min([area.get_coordinate('y1'), area.get_coordinate('y2')])
        maxx = max([area.get_coordinate('x1'), area.get_coordinate('x2')])
        minx = min([area.get_coordinate('x1'), area.get_coordinate('x2')])
        print('good')
        print(direction)
        if (direction == 'up') or (direction == 'down'):
            # pan_dir = v
            if direction == 'up':
                inv = -1
                target = {'x':focus['x'], 'y':maxy}
                sweet_spot = {'x':focus['x'], 'y':(maxy - distance)}
                midpoint_dot = {'x':focus['x'], 'y':(maxy - distance + midpoint)}
            elif direction == 'down':
                inv = 1
                target = {'x':focus['x'], 'y':miny}
                sweet_spot = {'x':focus['x'], 'y':(miny + distance)}
                midpoint_dot = {'x':focus['x'], 'y':(miny + distance - midpoint)}
            area_34 = area_search(v_areas, 0)
            area_56 = area_search(v_areas, 1)
            positions = c_3456('x')
            pan_1 = {'x':(focus['x'] - (0.5 * l)), 'y':target['y']}
            pan_2 = {'x':(focus['x'] + (0.5 * l)), 'y':target['y']}
            pan_3 = {'x':positions[0], 'y':(sweet_spot['y'] - (inv * midpoint))}
            pan_4 = {'x':positions[1], 'y':(sweet_spot['y'] - (inv * midpoint))}
            pan_5 = {'x':positions[2], 'y':sweet_spot['y']}
            pan_6 = {'x':positions[3], 'y':sweet_spot['y']}
        
        elif (direction == 'right') or (direction == 'left'):
            # pan_dir = h
            if direction == 'left':
                print('better')
                inv = 1
                target = {'y':focus['y'], 'x':minx}
                sweet_spot = {'y':focus['y'], 'x':(minx + distance)}
                midpoint_dot = {'y':focus['y'], 'x':(minx + distance - midpoint)}

            elif direction == 'right':
                print('better')
                inv = -1
                target = {'y':focus['y'], 'x':maxx}
                sweet_spot = {'y':focus['y'], 'x':(maxx - distance)}
                midpoint_dot = {'y':focus['y'], 'x':(maxx - distance + midpoint)}

            
            area_34 = area_search(h_areas, 0)
            area_56 = area_search(h_areas, 1)
            positions = c_3456('y')
            print('positions!!!!!!! = ', positions)
            pan_1 = {'y':(focus['y'] - (0.5 * l)), 'x':target['x']}
            pan_2 = {'y':(focus['y'] + (0.5 * l)), 'x':target['x']}
            pan_3 = {'y':positions[0], 'x':(sweet_spot['x'] - (inv * midpoint))}
            pan_4 = {'y':positions[1], 'x':(sweet_spot['x'] - (inv * midpoint))}
            pan_5 = {'y':positions[2], 'x':sweet_spot['x']}
            pan_6 = {'y':positions[3], 'x':sweet_spot['x']}
        panels_4_check = [pan_3, pan_4, pan_5, pan_6]
        # дольше проверка, что панели не стоят на углах стен
        pans_areas = []
        for panel in panels_4_check:
            a = panel['x']
            b = panel['y']
            if (area.get_direction() == 'up') or (area.get_direction() == 'down'):
                pans_areas.append(Area((a - 0.003), (a + 0.003), (b - 0.3), (b + 0.3)))
            elif (area.get_direction() == 'left') or (area.get_direction() == 'right'):
                pans_areas.append(Area((a - 0.3), (a + 0.3), (b - 0.003), (b + 0.003)))
        print('###')
        for area in pans_areas:
            area.prnt()
        print('###$')
        for pa in pans_areas:
            for point in points:
                chk = pa.point_belongs(point['x'], point['y'])
                if chk == True:
                    return
        variant = [wa, sweet_spot, target, pan_1, pan_2, pan_3, pan_4, pan_5, pan_6]
        pre_variants.append(variant)

    def side_panels(variant):
        
        def verticals():
            for panel in panels:
                for area in h_areas:
                    zone_1 = area.point_belongs(panel['x1'], panel['y'])
                    if zone_1 == True:
                        area_1 = area
                        break
                for area in h_areas:
                    zone_2 = area.point_belongs(panel['x2'], panel['y'])
                    if zone_2 == True:
                        area_2 = area
                        break
                if ((zone_1 + zone_2) < 2) or (area_1 == area_2):
                    panels_got.append(panel)
        # если 2 и больше, то устанавливаем координаты их центров                    
            if len(panels_got) < 2:
                return
            pan_centers = []
            for panel in panels_got:
                center = (abs(panel['x1'] - panel['x2']) / 2) + min([panel['x1'], panel['x2']])
                for area in h_areas:
                    loc = area.point_belongs(center, panel['y'])
                    if loc == True:
                        if variant[0].get_direction() == 'up':
                            coordinate = min([area.get_coordinate('y1'), area.get_coordinate('y2')])
                        elif variant[0].get_direction() == 'down':
                            coordinate = max([area.get_coordinate('y1'), area.get_coordinate('y2')])
                        break
                pan_centers.append({'x':center, 'y':coordinate})
        # проверяем не цепляют ли панели углы комнаты
            pans_areas = []
            for center in pan_centers:
                a = center['x']
                b = center['y']
                pans_areas.append(Area((a - 0.3), (a + 0.3), (b - 0.003), (b + 0.003)))
            panels_end = []
            for area in pans_areas:
                for point in points:
                    val = area.point_belongs(point['x'], point['y'])
                    if val == True:
                        break
                else:
                    panels_end.append(area.focus())
        # если осталось больше 2, то выводим их
            if len(panels_end) < 2:
                return
            else:
                variants.append(variant + panels_end)
        
        def horizontals():
            for panel in panels:
                for area in v_areas:
                    zone_1 = area.point_belongs(panel['x'], panel['y1'])
                    if zone_1 == True:
                        area_1 = area
                        break
                for area in v_areas:
                    zone_2 = area.point_belongs(panel['x'], panel['y2'])
                    if zone_2 == True:
                        area_2 = area
                        break
                if ((zone_1 + zone_2) < 2) or (area_1 == area_2):
                    panels_got.append(panel)
        # если 2 и больше, то устанавливаем координаты их центров                    
            if len(panels_got) < 2:
                return
            pan_centers = []
            for panel in panels_got:
                center = (abs(panel['y1'] - panel['y2']) / 2) + min([panel['y1'], panel['y2']])
                for area in v_areas:
                    loc = area.point_belongs(center, panel['x'])
                    if loc == True:
                        if variant[0].get_direction() == 'right':
                            coordinate = min([area.get_coordinate('x1'), area.get_coordinate('x2')])
                        elif variant[0].get_direction() == 'left':
                            coordinate = max([area.get_coordinate('x1'), area.get_coordinate('x2')])
                        break
                pan_centers.append({'x':coordinate, 'y':center})                
        # проверяем не цепляют ли панели углы комнаты
            pans_areas = []
            for center in pan_centers:
                a = center['x']
                b = center['y']
                pans_areas.append(Area((a - 0.003), (a + 0.003), (b - 0.3), (b + 0.3)))
            panels_end = []
            for area in pans_areas:
                for point in points:
                    val = area.point_belongs(point['x'], point['y'])
                    if val == True:
                        break
                else:
                    panels_end.append(area.focus())
        # если осталось больше 2, то выводим их
            if len(panels_end) < 2:
                return
            else:
                variants.append(variant + panels_end)
                
        # выбираем количество сайд панелей (2, 3 или 4, от ширины wa)
        wa_width = l * 1.5
        if 1.8 > wa_width >= 1.5:
    #*****************************************************************************************
    # ВЕРТИКАЛЬНЫЙ ВАРИАНТ ДЛЯ 2 ПАНЕЛЕЙ
    #*****************************************************************************************
            # расставляем точки для сайд панелей
            if (variant[0].get_direction() == 'up') or (variant[0].get_direction() == 'down'):
                panel_1 = {'y':(variant[1]['y']), 'x1':(variant[1]['x']), 'x2':(variant[1]['x'] - 0.6)}
                panel_2 = {'y':(variant[1]['y']), 'x1':(variant[1]['x']), 'x2':(variant[1]['x'] + 0.6)}
                panels = [panel_1, panel_2]
                panels_got = []
            # проверяем по 2 точки каждой панели по зонам от направления
                verticals()
                
    #*****************************************************************************************                
    # ГОРИЗОНТАЛЬНЫЙ ВАРИАНТ ДЛЯ 2 ПАНЕЛЕЙ
    #*****************************************************************************************
            elif (variant[0].get_direction() == 'right') or (variant[0].get_direction() == 'left'):
                panel_1 = {'y':(variant[1]['y']), 'x1':(variant[1]['x']), 'x2':(variant[1]['x'] - 0.6)}
                panel_2 = {'y':(variant[1]['y']), 'x1':(variant[1]['x']), 'x2':(variant[1]['x'] + 0.6)}
                panels = [panel_1, panel_2]
                panels_got = []
            # проверяем по 2 точки каждой панели по зонам от направления
                horizontals()
            
        elif 2.4 > wa_width >= 1.8:
    #*****************************************************************************************
    # ВЕРТИКАЛЬНЫЙ ВАРИАНТ ДЛЯ 3 ПАНЕЛЕЙ
    #*****************************************************************************************
            # расставляем точки для сайд панелей
            if (variant[0].get_direction() == 'up') or (variant[0].get_direction() == 'down'):
                panel_1 = {'y':(variant[1]['y']), 'x1':(variant[1]['x'] + 0.3), 'x2':(variant[1]['x'] - 0.3)}
                panel_2 = {'y':(variant[1]['y']), 'x1':(panel_1['x2']), 'x2':(panel_1['x2'] - 0.6)}
                panel_3 = {'y':(variant[1]['y']), 'x1':(panel_1['x1']), 'x2':(panel_1['x1'] + 0.6)}
                panels = [panel_1, panel_2, panel_3]
                panels_got = []
            # проверяем по 2 точки каждой панели по зонам от направления
                verticals()    
            
    #*****************************************************************************************                
    # ГОРИЗОНТАЛЬНЫЙ ВАРИАНТ ДЛЯ 3 ПАНЕЛЕЙ
    #*****************************************************************************************
            elif (variant[0].get_direction() == 'left') or (variant[0].get_direction() == 'right'):
                panel_1 = {'x':(variant[1]['x']), 'y1':(variant[1]['y'] + 0.3), 'y2':(variant[1]['y'] - 0.3)}
                panel_2 = {'x':(variant[1]['x']), 'y1':(panel_1['y2']), 'y2':(panel_1['y2'] - 0.6)}
                panel_3 = {'x':(variant[1]['x']), 'y1':(panel_1['y1']), 'y2':(panel_1['y1'] + 0.6)}
                panels = [panel_1, panel_2, panel_3]
                panels_got = []
            # проверяем по 2 точки каждой панели по зонам от направления
                horizontals()    
            
                
        elif wa_width >= 2.4:
    #*****************************************************************************************
    # ВЕРТИКАЛЬНЫЙ ВАРИАНТ ДЛЯ 4 ПАНЕЛЕЙ
    #*****************************************************************************************
            # расставляем точки для сайд панелей
            if (variant[0].get_direction() == 'up') or (variant[0].get_direction() == 'down'):
                panel_1 = {'y':(variant[1]['y']), 'x1':(variant[1]['x']), 'x2':(variant[1]['x'] - 0.6)}
                panel_2 = {'y':(variant[1]['y']), 'x1':(variant[1]['x']), 'x2':(variant[1]['x'] + 0.6)}
                panel_3 = {'y':(variant[1]['y']), 'x1':(panel_1['x2']), 'x2':(panel_1['x2'] - 0.6)}
                panel_4 = {'y':(variant[1]['y']), 'x1':(panel_2['x2']), 'x2':(panel_2['x2'] + 0.6)}
                panels = [panel_1, panel_2, panel_3, panel_4]
                panels_got = []
            # проверяем по 2 точки каждой панели по зонам от направления
                verticals()
            
    #*****************************************************************************************                
    # ГОРИЗОНТАЛЬНЫЙ ВАРИАНТ ДЛЯ 4 ПАНЕЛЕЙ
    #*****************************************************************************************
            elif (variant[0].get_direction() == 'left') or (variant[0].get_direction() == 'right'):
                panel_1 = {'x':(variant[1]['x']), 'y1':(variant[1]['y']), 'y2':(variant[1]['y'] - 0.6)}
                panel_2 = {'x':(variant[1]['x']), 'y1':(variant[1]['y']), 'y2':(variant[1]['y'] + 0.6)}
                panel_3 = {'x':(variant[1]['x']), 'y1':(panel_1['y2']), 'y2':(panel_1['y2'] - 0.6)}
                panel_4 = {'x':(variant[1]['x']), 'y1':(panel_2['y2']), 'y2':(panel_2['y2'] + 0.6)}
                panels = [panel_1, panel_2, panel_3, panel_4]
                panels_got = []
            # проверяем по 2 точки каждой панели по зонам от направления
                horizontals() 

    def get_results(variant):
        def add_AS(direction, target): # для расчета координат АС
            if (direction == 'up') or (direction == 'down'):
                if direction == 'up':
                    y = target['y'] - (l / 4) 
                elif direction == 'down':
                    y = target['y'] + (l / 4)
                x1 = target['x'] - (l / 2)
                x2 = target['x'] + (l / 2)    
                las = {'x':x1, 'y':y}
                ras = {'x':x2, 'y':y}
            elif (direction == 'left') or (direction == 'right'):
                if direction == 'right':
                    x = target['x'] - (l / 4) 
                elif direction == 'left':
                    x = target['x'] + (l / 4)
                y1 = target['y'] - (l / 2)
                y2 = target['y'] + (l / 2)    
                las = {'x':x, 'y':y1}
                ras = {'x':x, 'y':y2}
            lst_AS = [las, ras]
            return lst_AS
            
        def membrane(dot, direction): # для расчета толщин панелей
            sound_speed = 343.1 # скорость звука в студии (воздух, температура 20C, давление 1А)
            depth_values = ({'f1':1, 'f2':23, 'd':50}, {'f1':23, 'f2':25, 'd':45}, 
                            {'f1':25, 'f2':27, 'd':40}, {'f1':27, 'f2':29, 'd':35}, 
                            {'f1':29, 'f2':32, 'd':30}, {'f1':32, 'f2':35, 'd':25}, 
                            {'f1':35, 'f2':39, 'd':20}, {'f1':39, 'f2':46, 'd':15}, 
                            {'f1':46, 'f2':60, 'd':10})

            # выше значения толщин поглотителя в зависимости от частоты стоячей волны
            if direction == 'vertical':
                lst = v_areas
                c1 = 'x1'
                c2 = 'x2'
            elif direction == 'horizontal':
                lst = h_areas
                c1 = 'y1'
                c2 = 'y2'
            for area in lst:
                get_area = area.point_belongs(dot['x'], dot['y'])
                if get_area == True:
                    got_area = area
            dist = abs(got_area.get_coordinate(c1) - got_area.get_coordinate(c2)) 
            standing_wave = sound_speed / (dist * 2) # формула стоячей волны, частота в Гц
            if standing_wave >= 60:
                result = 0
                return result
            for value in depth_values:
                if value['f2'] > standing_wave >= value['f1']:
                    depth = value['d']
                    return depth
        
        ss = variant[1]
        if (variant[0].get_direction() == 'up') or (variant[0].get_direction() == 'down'):
            middot = {'x':(ss['x']), 'y':(variant[5]['y'])}
            ss_result = membrane(ss, 'vertical')
            middot_result = membrane(middot, 'vertical')
            other_dots = []
            for dot in variant[9:]:
                new_dot = {'x':dot['x'], 'y':ss['y']}
                other_dots.append(new_dot)
            other_panels = []
            for dot in other_dots:
                new_panel = membrane(dot, 'horizontal')
                other_panels.append(new_panel)
        elif (variant[0].get_direction() == 'left') or (variant[0].get_direction() == 'right'):
            middot = {'x':(variant[5]['x']), 'y':(ss['y'])}
            ss_result = membrane(ss, 'horizontal')
            middot_result = membrane(middot, 'horizontal')
            other_dots = []
            for dot in variant[9:]:
                new_dot = {'x':ss['x'], 'y':dot['y']}
                other_dots.append(new_dot)
            other_panels = []
            for dot in other_dots:
                new_panel = membrane(dot, 'vertical')
                other_panels.append(new_panel)
        variant[3]['depth'] = 0
        variant[4]['depth'] = 0
        variant[5]['depth'] = ss_result
        variant[6]['depth'] = ss_result
        variant[7]['depth'] = middot_result
        variant[8]['depth'] = middot_result
        step = 9
        for value in other_panels:
            variant[step]['depth'] = value
            step += 1

        location_AS = add_AS((variant[0].get_direction()), variant[2])
        for point in location_AS:
            variant.insert(0, point)

    check_points = [] # список точек для проверок
    vertical_walls = [] # список вертикальных стен
    horizontal_walls = [] # список горизонтальных стен
    v_areas = [] # список зон по вертикальным стенам
    h_areas = [] # список зон по горизонтальным стенам
    focus_lst = [] # список фокусных точек

    distance = 0

    wall_number = len(points)

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
        # woofer_size = '8"' # размер НЧ динамика АС
        l = 2.0 # базовое расстояние между АС и sweet spot
    elif 15 <= room_size < 20:
        # woofer_size = '6-7 inch'
        l = 1.5    
    elif 9 <= room_size < 15:
        # woofer_size = '5 inch'
        l = 1.5     
    elif 3 <= room_size < 9:
        # woofer_size = '3-4 inch'
        l = 1.2
    else:
        print('too small room')
    
    # ВСТАВКА СО СТОРОННИМ ЗНАЧЕНИЕМ БАЗЫ
    if l > grand_l >= 1.0:
        l = grand_l   
    
    print(room_size, "m2")

    # отфильтруем стены и выберем те, длина которых позволяет расположить АС
    # раскидаем их по спискам вертикальных и горизонтальных

    vertical_walls_AS = []
    horizontal_walls_AS = []



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



    # делаем потенциальные зоны с помощью функции

    for wall in vertical_walls_AS:
        wa_filter(wall)

    for wall in horizontal_walls_AS:
        wa_filter(wall)

    # вывод (для отладки)
    for area in potencial_wa_v:
        area.prnt()
    print('...........1')
    for area in potencial_wa_h:
        area.prnt()

    # проверим, находятся ли фокусы зон в комнате, и нет ли в зонах преград

    passed_wa_v = []
    passed_wa_h = []

    for area in potencial_wa_v:
        area_pass(area, passed_wa_v)

    for area in potencial_wa_h:
        area_pass(area, passed_wa_h)

    # вывод (для отладки)
    print('...........2')
    for area in passed_wa_v:
        area.prnt()
    print('...........2')
    for area in passed_wa_h:
        area.prnt()

    ##########################################################################################
    # ДАЛЕЕ МЫ ОБЪЯВЛЯЕМ ФУНКЦИИ ДЛЯ РАССТАНОВКИ ПАНЕЛЕЙ, ПРОВЕРЯЕМ И СНОВА ВИКИДЫВАЕМ ЗОНЫ,
    # КОТОРЫЕ НАМ НЕ ПОДХОДЯТ. ПОСЛЕ ЭТОГО ПОЛУЧАЕМ ОКОНЧАТЕЛЬНЫЙ СПИСОК ВАРИАНТОВ (ИХ ЧИСЛО)
    ##########################################################################################

    pre_variants = [] # варианты без сайд панелей
    for area in passed_wa_v:
        pan_center(area)    
    for area in passed_wa_h:
        pan_center(area)    
    print('pre_variants: ', pre_variants)


    ##########################################################################################
    # ДАЛЕЕ ИДЕТ БОЛЬШАЯ ФУНКЦИЯ ДЛЯ СОЗДАНИЯ И ПРОВЕРКИ САЙД ПАНЕЛЕЙ В РАЗНЫХ WA
    ##########################################################################################

    variants = [] # список, который мы получаем после всех проверок
    for variant in pre_variants:
        side_panels(variant)

    ###########################################################################################
    # ДАЛЕЕ ФУНКЦИЯ, КОТОРАЯ ДОБАВЛЯЕТ ТОЧКИ АС, А ТАКЖЕ ПАРАМЕТРЫ ВСЕМ ПАНЕЛЯМ, КОТОРЫЕ БУДУТ
    # ВЫВОДИТЬСЯ НА ИНТЕРФЕЙС, ПАРАМЕТРЫ КАЖДОЙ ПАНЕЛИ БУДУТ ДОБАВЛЕНЫ В СЛОВАРЬ С КООРДИНАТАМИ
    ###########################################################################################

    for variant in variants:
        get_results(variant)

    print('')
    print('RESULTS:')
    print('')
    for variant in variants: # вывод для отладки
        for i in variant:
            print(i)
        print('')

    # расчет будет закончен, нужно будет обеспечить вывод данных
            
    return variants
