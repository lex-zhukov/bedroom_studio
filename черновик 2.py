def wall_point(wall, point, p1, p2, p0, p):
    if ((wall[p] == point[p]) and
        max([wall[p1], wall[p2]]) > point[p0] > min([wall[p1], wall[p2]])):
        return True
    else:
        return False

wall = {'x': 0.0, 'y1': 0.0, 'y2': 3.0}
point = {'x': 0.0, 'y': 1.0}
aaa = wall_point(wall, point, 'y1', 'y2', 'y', 'x')
print(aaa)  
