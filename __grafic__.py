#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
###### ГРАФИЧЕСКАЯ ЧАСТЬ # ГРАФИЧЕСКАЯ ЧАСТЬ # ГРАФИЧЕСКАЯ ЧАСТЬ # ГРАФИЧЕСКАЯ ЧАСТЬ #######
###### ГРАФИЧЕСКАЯ ЧАСТЬ # ГРАФИЧЕСКАЯ ЧАСТЬ # ГРАФИЧЕСКАЯ ЧАСТЬ # ГРАФИЧЕСКАЯ ЧАСТЬ #######
###### ГРАФИЧЕСКАЯ ЧАСТЬ # ГРАФИЧЕСКАЯ ЧАСТЬ # ГРАФИЧЕСКАЯ ЧАСТЬ # ГРАФИЧЕСКАЯ ЧАСТЬ #######
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

from svg_turtle import SvgTurtle

def grafic(points, variants):
    

    def draw_room(t, variant):
        def draw_element(t, variant, color, position, radius, text):
            t.fillcolor(color)
            t.pencolor('white')
            t.begin_fill()
            t.penup()
            t.penup()
            t.goto(((variant[position]['x'] - move_x) * 50), (((variant[position]['y'] - move_y) * 50) - (radius)))
            t.write(text, align = 'center', font = ("Verdana", 9, "normal"))
            t.pendown()
            if radius == 10:
                t.fd(10)
                t.lt(90)
                t.fd(20)
                t.lt(90)
                t.fd(20)
                t.lt(90)
                t.fd(20)
                t.lt(90)
                t.fd(10)
            else:
                t.circle(radius)
            t.end_fill()
        all_x = []
        all_y = []
        for point in points:
            all_x.append(point['x'])
            all_y.append(point['y'])    
        move_x = max(all_x) / 2
        move_y = max(all_y) / 2
        t.fillcolor('skyblue')
        t.pensize(0)
        t.begin_fill()
        t.penup()
        t.goto(((0 - move_x) * 50), ((0 - move_y) * 50))
        t.pendown()
        for point in points:
            t.goto(((point['x'] - move_x) * 50), ((point['y'] - move_y) * 50))
        t.goto(((0 - move_x) * 50), ((0 - move_y) * 50))
        t.end_fill()
        # здесь рисуем точки АС
            # первая
        draw_element(t, variant, 'blue', 0, 5, '')
            # вторая
        draw_element(t, variant, 'blue', 1, 5, '')
        # ss
        draw_element(t, variant, 'green', 3, 5, '')
        for pos in variant[5:]:
            draw_element(t, variant, 'black', variant.index(pos), 10, (str(variant.index(pos) - 4))) 
        t.hideturtle()

    def write_file(draw_func, filename, width, height):
        t = SvgTurtle(width, height)
        draw_func(t, variants[0])
        t.save_as(filename)

    def main():
        write_file(draw_room, 'pic_location.svg', 500, 500)
        print('done')

    main()