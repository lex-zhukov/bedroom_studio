class Area:
    
    def __init__(self, x1, x2, y1, y2):
        self.coordinate_x1 = x1
        self.coordinate_x2 = x2
        self.coordinate_y1 = y1
        self.coordinate_y2 = y2
    
    def set_coordinate(self, c, v):
        if c == 'x1':
            self.coordinate_x1 = v
        elif c == 'x2':
            self.coordinate_x2 = v
        elif c == 'y1':
            self.coordinate_y1 = v
        elif c == 'y2':
            self.coordinate_y2 = v
        
    def get_coordinate(self, c):
        if c == 'x1':
            return self.coordinate_x1
        elif c == 'x2':
            return self.coordinate_x2
        elif c == 'y1':
            return self.coordinate_y1
        elif c == 'y2':
            return self.coordinate_y2
    
    def exclude(self): # добавляет 4 точки вокруг зоны "прицелом" для проверки
        length = abs(self.coordinate_y1 - self.coordinate_y2)
        width = abs(self.coordinate_x1 - self.coordinate_x2)
        focus = self.focus()
        overpoint = {'y':((focus['y']) + (length / 2) + 0.01), 'x':focus['x']}
        underpoint = {'y':((focus['y']) - (length / 2) - 0.01), 'x':focus['x']}
        rightpoint = {'x':((focus['x']) + (width / 2) + 0.01), 'y':focus['y']}
        leftpoint = {'x':((focus['x']) - (width / 2) - 0.01), 'y':focus['y']}
        lst = [overpoint, underpoint, rightpoint, leftpoint]
        return lst
    
    def focus(self):
        x = abs(self.coordinate_x1 - self.coordinate_x2)/2 + min([self.coordinate_x1, self.coordinate_x2])
        y = abs(self.coordinate_y1 - self.coordinate_y2)/2 + min([self.coordinate_y1, self.coordinate_y2])
        xy = {'x':x, 'y':y}
        return xy
    
    def size(self):
        length = abs(self.coordinate_y1 - self.coordinate_y2)
        width = abs(self.coordinate_x1 - self.coordinate_x2)
        size = length * width
        return size
    
    def point_belongs(self, x, y):
        if ((self.coordinate_x1 > x > self.coordinate_x2 or
             self.coordinate_x2 > x > self.coordinate_x1) and
            (self.coordinate_y1 > y > self.coordinate_y2 or
             self.coordinate_y2 > y > self.coordinate_y1)):
            return True
        else:
            return False
        
    def get_lines(self, dir):
        y_up = max([self.coordinate_y1, self.coordinate_y2]) - 0.001
        y_down = min([self.coordinate_y1, self.coordinate_y2]) + 0.001
        x_left = min([self.coordinate_x1, self.coordinate_x2]) + 0.001
        x_right = max([self.coordinate_x1, self.coordinate_x2]) - 0.001
        if dir == 'v': # зона из вертикальных стен
            upline = {'y':y_up, 'x1':x_left, 'x2':x_right}
            downline = {'y':y_down, 'x1':x_left, 'x2':x_right}
            linelist = [upline, downline]
        elif dir == 'h': # зона из горизонтальных стен
            leftline = {'x':x_left, 'y1':y_up, 'y2':y_down}
            rightline = {'x':x_right, 'y1':y_up, 'y2':y_down}
            linelist = [leftline, rightline]
        return linelist
    
    def get_dots(self):
        miny = min([self.coordinate_y1, self.coordinate_y2])
        maxy = max([self.coordinate_y1, self.coordinate_y2])
        minx = min([self.coordinate_x1, self.coordinate_x2])
        maxx = max([self.coordinate_x1, self.coordinate_x2])
        halfx = (abs(self.coordinate_x1 - self.coordinate_x2)/2) + minx
        halfy = (abs(self.coordinate_y1 - self.coordinate_y2)/2) + miny
        updot = {'x':halfx, 'y':maxy}
        downdot = {'x':halfx, 'y':miny}
        leftdot = {'x':minx, 'y':halfy}
        rightdot = {'x':maxx, 'y':halfy}
        dotlist = [updot, downdot, leftdot, rightdot]
        return dotlist
    
    def prnt(self):
        print(f"x1 = {self.coordinate_x1}, x2 = {self.coordinate_x2}, y1 = {self.coordinate_y1}, y2 = {self.coordinate_y2}")

class Workarea(Area):
    
    def __init__(self, x1, x2, y1, y2, direction):
        self.coordinate_x1 = x1
        self.coordinate_x2 = x2
        self.coordinate_y1 = y1
        self.coordinate_y2 = y2
        self.direction = direction
    
    def get_direction(self):
        direction = self.direction
        return direction
    
    def prnt(self):
        print(f"x1 = {self.coordinate_x1}, x2 = {self.coordinate_x2}, y1 = {self.coordinate_y1}, y2 = {self.coordinate_y2}, dir = {self.direction}")





    
