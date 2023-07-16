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
        
class Sweet_spot(object):
    
    def __init__(self, x, y):
        self.coordinate_x = x
        self.coordinate_y = y

    def set_location(self, x, y):
        self.coordinate_x = x
        self.coordinate_y = y
    
    def prnt(self):
        print(f"x = {self.coordinate_x}, y = {self.coordinate_y}") 
        

# class Acoustic_system(Sweet_spot):
    
# class Acoustic_panel(Acoustic_system):





    
