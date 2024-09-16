basic.show_icon(IconNames.HEART)
basic.pause(2000)

def on_forever():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . # . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # . # .
        . . . . .
        """)
    basic.show_leds("""
        # # . # #
        . . . . .
        # . . . #
        . . . . .
        # # . # #
        """)
    basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . # . # .
        . . # . .
        . # . # .
        . . . . .
        """)
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
    basic.show_leds("""
        # . . . #
        . . . . .
        . . # . .
        . . . . .
        # . . . #
        """)
    basic.pause(500)
basic.forever(on_forever2)
