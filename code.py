def on_pin_pressed_p0():
    global isOn, gameStart, gamerunning
    if isOn == False:
        isOn = True
    else:
        isOn = False
        gameStart = False
        gamerunning = False
        basic.clear_screen()
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global gameStart
    gameStart = False
    basic.clear_screen()
    basic.show_number(p1Score)
    basic.pause(5000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def scrollDots():
    for index in range(randint(1, 4)):
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # . # . #
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . # . # .
            """)

def on_button_pressed_ab():
    global p1Score
    p1Score = 5
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global gameStart
    gameStart = False
    basic.clear_screen()
    basic.show_number(p2Score)
    basic.pause(5000)
    gameStart = True
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

time = 0
gamerunning = False
gameStart = False
isOn = False
p2Score = 0
p1Score = 0
p1Score = 0
p2Score = 0

def on_forever():
    global gameStart, gamerunning, p1Score, time, p2Score, isOn
    if isOn:
        gameStart = False
        basic.pause(randint(1000, 5000))
        scrollDots()
        gameStart = True
        gamerunning = True
        basic.show_leds("""
            . . # . .
            . . # . .
            . . # . .
            . . . . .
            . . # . .
            """)
        while gameStart:
            if input.pin_is_pressed(TouchPin.P1):
                gamerunning = False
                gameStart = False
                basic.show_string("A")
                basic.pause(500)
                basic.clear_screen()
                music.play(music.string_playable("G B A G C5 B A B ", 360),
                    music.PlaybackMode.UNTIL_DONE)
                p1Score += 1
                basic.show_string("" + str(time) + "s")
                time = 0
            if input.pin_is_pressed(TouchPin.P2):
                gamerunning = False
                gameStart = False
                basic.show_string("B")
                basic.pause(500)
                basic.clear_screen()
                music.play(music.string_playable("G B A G C5 B A B ", 360),
                    music.PlaybackMode.UNTIL_DONE)
                p2Score += 1
                basic.show_string("" + str(time) + "s")
                time = 0
        basic.pause(3000)
        basic.clear_screen()
        if p1Score == 5:
            music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
                music.PlaybackMode.IN_BACKGROUND)
            basic.show_string("P1 WINS!")
            isOn = False
        if p2Score == 5:
            music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
                music.PlaybackMode.IN_BACKGROUND)
            basic.show_string("P2 WINS")
            isOn = False
basic.forever(on_forever)

def on_every_interval():
    global time
    if gamerunning:
        time += 0.1
loops.every_interval(100, on_every_interval)
