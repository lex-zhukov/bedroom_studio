class Area:
    
    def __init__(self, x1, x2, y1, y2):
        self.coordinate_x1 = x1
        self.coordinate_x2 = x2
        self.coordinate_y1 = y1
        self.coordinate_y2 = y2
    
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
    
#    def standing_wave(self, direction):
#        if dicrection == v:      
    
    def prnt(self):
        print(f"x1 = {self.coordinate_x1}, x2 = {self.coordinate_x2}, y1 = {self.coordinate_y1}, y2 = {self.coordinate_y2}")
    
    def look():
        print("look")


class Workarea(Area):
    
    def __init__(self, x1, x2, y1, y2):
        self.coordinate_x1 = x1
        self.coordinate_x2 = x2
        self.coordinate_y1 = y1
        self.coordinate_y2 = y2
        
    def set_area(self, lst):
        self.coordinate_x1 = lst[0]
        self.coordinate_x2 = lst[1]
        self.coordinate_y1 = lst[2]
        self.coordinate_y2 = lst[3]
        
class Sweet_spot(object):
    
    def __init__(self, x, y):
        self.coordinate_x = x
        self.coordinate_y = y

    def set_location(self, x, y):
        self.coordinate_x = x
        self.coordinate_y = y
    
    def prnt(self):
        print(f"x = {self.coordinate_x}, y = {self.coordinate_y}")

    def create_workarea(self, l, target, distance):
        if self.coordinate_x == target['x']:
            if self.coordinate_y < target['y']:
                a = self.coordinate_x - (0.749 * l)
                b = self.coordinate_x + (0.749 * l)
                c = self.coordinate_y + (0.999 * distance)
                d = self.coordinate_y - (0.249 * l)        
            elif self.coordinate_y > target['y']:
                a = self.coordinate_x - (0.749 * l)
                b = self.coordinate_x + (0.749 * l)
                c = self.coordinate_y - (0.999 * distance)
                d = self.coordinate_y + (0.249 * l)
        elif self.coordinate_y == target['y']:
            if self.coordinate_x < target['x']:
                d = self.coordinate_y - (0.749 * l)
                c = self.coordinate_y + (0.749 * l)
                b = self.coordinate_x + (0.999 * distance)
                a = self.coordinate_x - (0.249 * l)        
            elif self.coordinate_x > target['x']:
                d = self.coordinate_y - (0.749 * l)
                c = self.coordinate_y + (0.749 * l)
                b = self.coordinate_x - (0.999 * distance)
                a = self.coordinate_x + (0.249 * l)
        lst = [round(a, 3), round(b, 3), round(c, 3), round(d, 3)]
        return lst
        

# class Acoustic_system(Sweet_spot):
    
# class Acoustic_panel(Acoustic_system):





    
