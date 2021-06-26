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
basic.forever(function on_forever() {
    RED.showImage(0)
    basic.pause(15000)
    RED_YELLOW.showImage(0)
    basic.pause(3000)
})
