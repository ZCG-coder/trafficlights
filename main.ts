let RED = images.createImage(`
. # # # .
. # # # .
. . . . .
. . . . .
. . . . .
`)
let RED_YELLOW = images.createImage(`
. # # # .
. # # # .
. # # # .
. . . . .
. . . . .
`)
let YELLOW = images.createImage(`
. . . . .
. # # # .
. # # # .
. . . . .
. . . . .
`)
let GREEN = images.createImage(`
. . . . .
. . . . .
. # # # .
. # # # .
. . . . .
`)
basic.forever(function on_forever() {
    RED.showImage(0)
    basic.pause(15000)
    RED_YELLOW.showImage(0)
    basic.pause(3000)
    GREEN.showImage(0)
    basic.pause(15000)
    YELLOW.showImage(0)
    basic.pause(3000)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.clearScreen()
    basic.showString("Program exit.")
    control.reset()
})
