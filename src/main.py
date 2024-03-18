from window import Window

def main():
    print("Hello World!")
    win = Window(800, 600)
    win.wait_for_close()
    print("Exited")

main()