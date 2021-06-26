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

def on_forever():
    RED.show_image(0)
    basic.pause(15000)
    RED_YELLOW.show_image(0)
    basic.pause(3000)
basic.forever(on_forever)