from graphics import *
from math import *
win=GraphWin("MyWin", 1600, 800)

# x, y - up left corner of the base of house


# Create grass
grass = Rectangle(Point(0, 700), Point(1600, 800))
grass.setFill("green")

def Draw_grass():
	grass.draw(win)


# Create sky
sky = Rectangle(Point(0, 0), Point(1600, 700))
sky.setFill("#8cfffb")

def Draw_sky():
	sky.draw(win)


# Create house
x = 550
y = 480
kx = 0.8
ky = 0.8
	
home = Rectangle(Point(x, y), Point(x + 500 * kx, y + 400 * ky))
home.setFill("#B97A57")
	
tube = Rectangle(Point(x + 50 * kx, y - 250 * ky), Point(x + 150 * kx, y))
tube.setFill("#7F7F7F")
		
roof = Polygon(Point(x, y), Point(x + 250 * kx, y - 300 * ky), Point(x + 500 * kx, y))
roof.setFill("#ED1C24")

door = Rectangle(Point(x + 25 * kx, y + 100 * ky), Point(x + 200 * kx, y + 400 * ky))
door.setFill("#482425")

left_hand = Circle(Point(x + 50 * kx, y + 250 * ky), 10 * kx)
left_hand.setFill("#FFF200")

right_hand = Circle(Point(x + 175 * kx, y + 250 * ky), 10 * kx)
right_hand.setFill("#FFF200")

window1 = Rectangle(Point(x + 270 * kx, y + 120 * ky), Point(x + 370 * kx, y + 320 * ky))
window1.setFill("#d5a1d2")

window2 = Rectangle(Point(x + 370 * kx, y + 120 * ky), Point(x + 470 * kx, y + 160 * ky))
window2.setFill("#00e800")

window3 = Rectangle(Point(x + 370 * kx, y + 160 * ky), Point(x + 470 * kx, y + 320 * ky))
window3.setFill("#f8dd86")

window_roof = Circle(Point(x + 250 * kx, y - 150 * ky), 50 * kx)
window_roof.setFill("#9ddceb")

def Draw_house():
	home.draw(win)
	tube.draw(win)
	roof.draw(win)
	door.draw(win)
	left_hand.draw(win)
	window_roof.draw(win)
	window1.draw(win)
	window2.draw(win)
	window3.draw(win)

# Create tree
x = 1300
y = 450
kx = 2
ky = 2
	
crown3 = Circle(Point(x, y), 75 * kx)
crown3.setFill("green")

crown2 = Circle(Point(x, y - 75 * kx), 50 * kx)
crown2.setFill("green")

crown1 = Circle(Point(x, y - 125 * kx), 25 * kx)
crown1.setFill("green")

stem = Polygon(Point(x, y - 60 * ky), 
	Point(x + 10 * kx, y + 150 * ky), 
	Point(x - 10 * kx, y + 150 * ky), 
	Point(x, y - 60 * ky))
stem.setFill("brown")

stick = Polygon(Point(x, y + 30 * ky), 
	Point(x - 50 * kx, y - 40 * ky), 
	Point(x, y + 60 * ky), 
	Point(x + 50 * kx, y - 40 * ky),
	Point(x, y + 30 * ky))
stick.setFill("brown")

def Draw_tree():
	crown1.draw(win)
	crown2.draw(win)
	crown3.draw(win)
	stick.draw(win)
	stem.draw(win)


# Create sun
x = 800
y = 100
R = 40

sun = Circle(Point(x, y), R)
sun.setFill("yellow")

sunshine1 = Polygon(Point(x, y - 1.5 * R), 
	Point(x + R/2, y - R/2), 
	Point(x + 1.5 * R, y),
	Point(x + R/2, y + R/2),
	Point(x, y + 1.5 * R),
	Point(x - R/2, y + R/2), 
	Point(x - 1.5 * R, y),
	Point(x - R/2, y - R/2),
	Point(x, y - 1.5 * R))
sunshine1.setFill("yellow")

sunshine2 = Polygon(Point(x - 1.2 * R, y - 1.2 * R), 
	Point(x, y - R/2), 
	Point(x + 1.2 * R, y - 1.2 * R),
	Point(x + R/2, y),
	Point(x + 1.2 * R, y + 1.2 * R),
	Point(x, y + R/2), 
	Point(x - 1.2 * R, y + 1.2 * R),
	Point(x - R/2, y),
	Point(x - 1.2 * R, y - 1.2 * R))
sunshine2.setFill("yellow")

def Draw_sun():
	sunshine1.draw(win)
	sunshine2.draw(win)
	sun.draw(win)


# Create cloud
x = 100
y = 100
kx = 0.7
ky = 0.7

cloud1 = Oval(Point(x, y), Point(x + 300 * kx, y + 150 * ky))
cloud1.setFill("white")
	
cloud2 = Oval(Point(x - 100 * kx, y + 100 * ky), Point(x + 200 * kx, y + 200 * ky))
cloud2.setFill("white")

cloud3 = Oval(Point(x + 100 * kx, y + 75 * ky), Point(x + 400 * kx, y + 230 * ky))
cloud3.setFill("white")

cloud4 = Oval(Point(x + 320 * kx, y + 130 * ky), Point(x + 490 * kx, y + 200 * ky))
cloud4.setFill("white")

def Draw_cloud():
	cloud1.draw(win)
	cloud2.draw(win)
	cloud3.draw(win)
	cloud4.draw(win)


# Create man
x = 450
y = 500
k = 1

hair = Rectangle(Point(x - 30 * k, y - 35 * k), Point(x + 30 * k, y))
hair.setFill("black")

head = Circle(Point(x, y), 30 * k)
head.setFill("brown")

eye1 = Circle(Point(x - 9 * k, y - 5 * k), 3 * k)
eye1.setFill("#000000")

eye2 = Circle(Point(x + 9 * k, y - 5 * k), 3 * k)
eye2.setFill("#000000")

nose = Polygon(Point(x, y), 
	Point(x + 4 * k, y + 9 * k), 
	Point(x - 4 * k, y + 9 * k),
	Point(x, y))
nose.setFill("brown")

mouth = Line(Point(x - 8 * k, y + 18 * k), Point(x + 8 * k, y + 18 * k))
mouth.setWidth(3)

shirt = Polygon(Point(x - 32 * k, y + 27 * k), 
	Point(x + 32 * k, y + 27 * k), 
	Point(x + 60 * k, y + 70 * k),
	Point(x + 50 * k, y + 80 * k),
	Point(x + 30 * k, y + 50 * k),
	Point(x + 25 * k, y + 100 * k), 
	Point(x - 25 * k, y + 100 * k),
	Point(x - 30 * k, y + 50 * k),
	Point(x - 50 * k, y + 80 * k),
	Point(x - 60 * k, y + 70 * k),
	Point(x - 32 * k, y + 27 * k))
shirt.setFill("white")

hand1 = Circle(Point(x - 55 * k, y + 75 * k), 7 * k)
hand1.setFill("brown")

hand2 = Circle(Point(x + 55 * k, y + 75 * k), 7 * k)
hand2.setFill("brown")

jeans = Polygon(Point(x - 25 * k, y + 100 * k), 
	Point(x + 25 * k, y + 100 * k), 
	Point(x + 25 * k, y + 200 * k),
	Point(x + k, y + 200 * k),
	Point(x + k, y + 120 * k),
	Point(x - k, y + 120 * k), 
	Point(x - k, y + 200 * k),
	Point(x - 25 * k, y + 200 * k),
	Point(x - 25 * k, y + 100 * k),
	Point(x + 25 * k, y + 100 * k))
jeans.setFill("blue")

boot1 = Polygon(Point(x - 25 * k, y + 200 * k), 
	Point(x - 25 * k, y + 215 * k), 
	Point(x - k, y + 215 * k),
	Point(x - k, y + 200 * k),
	Point(x - 25 * k, y + 200 * k))
boot1.setFill("black")

boot2 = Polygon(Point(x + 25 * k, y + 200 * k), 
	Point(x + 25 * k, y + 215 * k), 
	Point(x + k, y + 215 * k),
	Point(x + k, y + 200 * k),
	Point(x + 25 * k, y + 200 * k))
boot2.setFill("black")

bow = Polygon(Point(x, y + 40 * k), 
	Point(x + 15 * k, y + 30 * k), 
	Point(x + 15 * k, y + 50 * k),
	Point(x, y + 40 * k),
	Point(x - 15 * k, y + 30 * k),
	Point(x - 15 * k, y + 50 * k), 
	Point(x, y + 40 * k))
bow.setFill("red")

def Draw_man():
	hair.draw(win)
	hand1.draw(win)
	hand2.draw(win)
	shirt.draw(win)
	jeans.draw(win)
	boot1.draw(win)
	boot2.draw(win)
	head.draw(win)
	eye1.draw(win)
	eye2.draw(win)
	nose.draw(win)
	mouth.draw(win)
	bow.draw(win)

# Create rain

rain1 = Line(Point(50, 200), Point(0, 900))
rain1.setWidth(2)
rain1.setFill("blue")

rain2 = Line(Point(100, 200), Point(50, 900))
rain2.setWidth(2)
rain2.setFill("blue")

rain3 = Line(Point(150, 200), Point(100, 900))
rain3.setWidth(2)
rain3.setFill("blue")

rain4 = Line(Point(200, 200), Point(150, 900))
rain4.setWidth(2)
rain4.setFill("blue")

rain5 = Line(Point(250, 200), Point(200, 900))
rain5.setWidth(2)
rain5.setFill("blue")

rain6 = Line(Point(300, 200), Point(250, 900))
rain6.setWidth(2)
rain6.setFill("blue")

rain7 = Line(Point(350, 200), Point(300, 900))
rain7.setWidth(2)
rain7.setFill("blue")

rain8 = Line(Point(400, 200), Point(350, 900))
rain8.setWidth(2)
rain8.setFill("blue")

def Draw_rain():
	rain1.draw(win)
	rain2.draw(win)
	rain3.draw(win)
	rain4.draw(win)
	rain5.draw(win)
	rain6.draw(win)
	rain7.draw(win)
	rain8.draw(win)

def Movement():
	x = 100
	xc = 2
	g = 256
	b = 256
	gb = 256
	bb = 256
	rb = 256
	for i in range(1500):
		cloud4.move(xc, 0)
		cloud3.move(xc, 0)
		cloud2.move(xc, 0)
		cloud1.move(xc, 0)

		rain1.move(xc, 0)
		rain2.move(xc, 0)
		rain3.move(xc, 0)
		rain4.move(xc, 0)
		rain5.move(xc, 0)
		rain6.move(xc, 0)
		rain7.move(xc, 0)	
		rain8.move(xc, 0)					

		x = x + xc
		if x > 1600 or x < 0 :
			xc = - xc
	
		sunshine2.move(10 * cos(i * pi / 180), 10 * sin(i * pi / 180))
		sunshine1.move(10 * cos(i * pi / 180), 10 * sin(i * pi / 180))
		sun.move(10 * cos(i * pi / 180), 10 * sin(i * pi / 180))

		g = g - (i + 1) % 2
		if g > 20:
			color_grass = color_rgb(0, g, 0)
			grass.setFill(color_grass)

		b -= (i + 1) % 2
		if b > 20:
			color_jeans = color_rgb(0, 0, b)
			jeans.setFill(color_jeans)
		
		gb -= (i + 1) % 2
		rb -= (i + 1) % 2
		bb -= (i + 1) % 2
		if gb > 120:
			color_shirt = color_rgb(rb, gb, bb)
			shirt.setFill(color_shirt)



Draw_sky()
Draw_sun()
Draw_grass()
Draw_cloud()
Draw_tree()
Draw_house()
Draw_man()
Draw_rain()

Movement()

win.getMouse()
win.close()
