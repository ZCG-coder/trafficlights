RED = images.create_image("""
. # # # .
. # # # .
. . . . .
. . . . .
. . . . .
""")

RED_YELLOW = images.create_image("""
. # # # .
. # # # .
. # # # .
. . . . .
. . . . .
""")
YELLOW = images.create_image("""
. . . . .
. # # # .
. # # # .
. . . . .
. . . . .
""")
GREEN = images.create_image("""
. . . . .
. . . . .
. # # # .
. # # # .
. . . . .
""")

def on_forever():
    RED.show_image(0)
    basic.pause(15000)
    RED_YELLOW.show_image(0)
    basic.pause(3000)
    GREEN.show_image(0)
    basic.pause(15000)
    YELLOW.show_image(0)
    basic.pause(3000)

basic.forever(on_forever)

def on_button_pressed_a():
    basic.clear_screen()
    basic.show_string("Program exit.")
    control.reset()
input.on_button_pressed(Button.A, on_button_pressed_a)
