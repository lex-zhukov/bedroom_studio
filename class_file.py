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
    
#    def standing_wave(self, direction):
#        if dicrection == v:      
    
    def prnt(self):
        print(f"x1 = {self.coordinate_x1}, x2 = {self.coordinate_x2}, y1 = {self.coordinate_y1}, y2 = {self.coordinate_y2}")
    
    def look():
        print("whatta fuck r u looking")
        
class Sweet_spot(object):
    
    def __init__(self, x, y):
        self.coordinate_x = x
        self.coordinate_y = y

# class Acoustic_system(Sweet_spot):
    
# class Acoustic_panel(Acoustic_system):





    
