from window import Window
from line import Line
from point import Point

def main():
    width = 800
    height = 600
    win = Window(width, height)

    top_left_point = Point(0, 0)
    top_right_point = Point(width, 0)
    bottom_left_point = Point(0, height)
    bottom_right_point = Point(width, height)
    win.draw_line(Line(top_left_point, top_right_point), "black")
    win.draw_line(Line(top_left_point, bottom_left_point), "black")
    win.draw_line(Line(top_right_point, bottom_right_point), "black")
    win.draw_line(Line(bottom_left_point, bottom_right_point), "black")
    win.draw_line(Line(top_left_point, bottom_right_point), "red")
    win.draw_line(Line(top_right_point, bottom_left_point), "red")
    
    win.is_running = True
    print("Running!")
    win.wait_for_close()
    print("Closing...")

main()