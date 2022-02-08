from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)
humid = round( sense.humidity, 1 )
hellblau = (50,50,255)
sense.show_message ("It", text_colour = hellblau)
gelb = (255,255,51)
sense.show_message ("is", text_colour = gelb)
rot = (255,0,0)
sense.show_message (str(humid), text_colour = rot)
blau = (0,0,255)
sense.show_message ("%", text_colour = blau)

o = (255, 128, 0)
G = (255, 255, 153)
g = (0,255,76)
_=(0,20,204)
bild = [
    _, _, _, _, _, _, _, o,
    _, _, _, _, g, _, _, _,
    _, _, g, _, g, _, _, _,
    _, _, g, g, g, _, g, _,
    _, _, _, g, g, g, g, _,
    _, _, _, g, g, _, _, _,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
 ]
_=(0,0,255)
o=(255,153,51)
a=(255,0,0)
fisch = [
    _, _, _, _, _, _, _, _,
    _, _, o, o, _, _, _, o,
    _, o, o, o, o, _, o, o,
    o, o, a, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    _, o, o, o, o, _, o, o,
    _, _, o, o, _, _, _, o,
    _, _, _, _, _, _, _, _,
 ]

if humid < 50:
   sense.set_pixels(bild)
else:
   sense.set_pixels(fisch)
  
sleep(3)
 
 
_ = (0,0,0)
g=(255,255,51)
r=(255,0,0)

# Stars
bild2 = [
    _, _, _, g, _, _, _, _,
    _, _, _, _, _, _, _, _,
    _, _, _, r, _, _, _, _,
    g, _, r, r, r, _, _, _,
    _, _, r, r, r, g, _, _,
    _, _, _, r, _, _, _, _,
    _, _, g, _, _, _, _, _,
    _, g, _, g, _, _, g, _,
 ] 
sense.set_pixels(bild2)
sleep(3)
    
if humid > 50:
   sense.set_pixels(bild)
else:
   sense.set_pixels(fisch)
  
sleep(3)

sense.show_message ("Hello from the Earth!", text_colour = rot, scroll_speed = 0.05)
# Earth
_=(0,0,255)
K=(0,0,0)
g=(0,255,0)
Earth = [
    K, K, K, _, _, K, K, K,
    K, _, _, _, _, _, _, K,
    _, _, _, _, _, g, _, _,
    _, _, _, g, g, g, _, _,
    _, _, _, _, g, g, _, _,
    K, _, _, _, _, _, _, K,
    K, _, _, _, _, _, _, K,
    K, K, K, _, _, _, K, K,
 ]
sense.set_pixels(Earth)
sleep(3)

Earth = [
   K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K,
    K, K, K, K, K, K, K, K,
 ]
sense.set_pixels(Earth)

 
 