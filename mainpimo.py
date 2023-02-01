import machine, time
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY
#import a_webserver

# overclock to 200Mhz
machine.freq(200000000)

# create galactic object and graphics surface for drawing
galactic = GalacticUnicorn()
graphics = PicoGraphics(DISPLAY)

brightness = 0.2

# returns the id of the button that is currently pressed or
# None if none are
def pressed():
    if galactic.is_pressed(GalacticUnicorn.SWITCH_A):
        return GalacticUnicorn.SWITCH_A
    if galactic.is_pressed(GalacticUnicorn.SWITCH_B):
        return GalacticUnicorn.SWITCH_B
    if galactic.is_pressed(GalacticUnicorn.SWITCH_C):
        return GalacticUnicorn.SWITCH_C
    if galactic.is_pressed(GalacticUnicorn.SWITCH_D):
        return GalacticUnicorn.SWITCH_D
    return None

graphics.set_font("bitmap6")
graphics.set_pen(graphics.create_pen(0, 0, 0))
graphics.clear()
graphics.set_pen(graphics.create_pen(255, 0, 255))
###
#graphics.text(".", 0, -5, -1, 1)
#graphics.text(".", 52, -5, -1, 1)
###
graphics.text("Hallo", 14, -1, -1, 1)
graphics.text("Stephan", 8, 5, -1, 1)
galactic.update(graphics)

# wait for a button to be pressed and load that effect
while True:
    if pressed() == GalacticUnicorn.SWITCH_A:
        import clock as effect
        break
    if pressed() == GalacticUnicorn.SWITCH_B:
        import eighties_super_computer as effect
        break
    if pressed() == GalacticUnicorn.SWITCH_C:
        import rainbow as effect
        break
    if pressed() == GalacticUnicorn.SWITCH_D:
        import techcree as effect
        break
    
# wait until all buttons are released
while pressed() != None:
    time.sleep(0.1)
    
effect.graphics = graphics
effect.init()

brightness = 0.2
sleep = False
was_sleep_pressed = False
   

# wait
while True:
    # if A, B, C, or D are pressed then reset
    if pressed() != None:
        machine.reset()
    
    sleep_pressed = galactic.is_pressed(GalacticUnicorn.SWITCH_SLEEP)
    if sleep_pressed and not was_sleep_pressed:
        sleep = not sleep
        
    was_sleep_pressed = sleep_pressed
    

    if sleep:
        # fade out if screen not off
        galactic.set_brightness(galactic.get_brightness() - 0.05)
        
        if galactic.get_brightness() > 0.0:
            effect.draw()

        # update the display
        galactic.update(graphics)
    else:
        effect.draw()
        
        # update the display
        galactic.update(graphics)
            
        # brightness up/down
        if galactic.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_UP):
            brightness += 0.05
        if galactic.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_DOWN):
            brightness -= 0.05
            
        galactic.set_brightness(brightness)
        
    # pause for a moment (important or the USB serial device will fail
    time.sleep(0.001)
