from engine import l, ss, h_areas, target

sw = ss.get_location()

if sw['x'] == target['x']:
    # вертикальое
    if sw['y'] < target['y']:
        direction = 'north'
    elif sw['y'] > target['y']:
        direction = 'south'
elif sw['y'] == target['y']:
    # горизонтальное
    if sw['x'] < target['x']:
        direction = 'east'
    elif sw['x'] > target['x']:
        direction = 'west'

def get_panels(direction):
    if direction == 'west' or 'east':
        co = 'x'
        co_0 = 'y'
        co_1 = 'y1'
        co_2 = 'y2'
    elif direction == 'north' or 'south':
        co = 'y'
        co_0 = 'x'
        co_1 = 'x1'
        co_2 = 'x2'

    # PANELS 1 and 2

    panx_12 = target[co]
    pany_1 = target[co_0] - (l / 2)
    pan_1 = {co:panx_12, co_0:pany_1}

    pany_2 = target[co_0] + (l / 2)
    pan_2 = {co:panx_12, co_0:pany_2}

    if direction == 'west' or 'south':
        panx_34 = sw[co] - (((abs(sw[co] - target[co]) - (l / 4)) / 4) * 3)
    elif direction == 'east' or 'north':
        panx_34 = sw[co] + (((abs(sw[co] - target[co]) - (l / 4)) / 4) * 3)

    panx_56 = sw[co]
    checkpoint_34 = {co:panx_34, co_0:sw[co_0]}

    # PANELS 3 and 4

    area_34 = []
    for area in h_areas: # v_areas
        found_area = area.point_belongs(checkpoint_34[co], checkpoint_34[co_0])
        if found_area == True:
            area_34.append(area)

    pany_3 = area_34[0].get_coordinate(co_1)
    pany_4 = area_34[0].get_coordinate(co_2)
    pan_3 = {co:panx_34, co_0:pany_3}
    pan_4 = {co:panx_34, co_0:pany_4}

    # PANELS 5 and 6

    area_56 = []
    for area in h_areas:
        found_area = area.point_belongs(sw[co], sw[co_0])
        if found_area == True:
            area_56.append(area)

    pany_5 = area_56[0].get_coordinate(co_1)
    pany_6 = area_56[0].get_coordinate(co_2)
    pan_5 = {co:panx_56, co_0:pany_5}
    pan_6 = {co:panx_56, co_0:pany_6}
    
    panels = [pan_1, pan_2, pan_3, pan_4, pan_5, pan_6]
    return panels