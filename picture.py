from graphics import *
win=GraphWin("MyWin",1600,800)

# x, y - up left corner of the base of house

def House(x, y, kx, ky, if_tube, where_hand, if_window_roof, colorhome, colortube, colorroof, colordoor, colorhand, colorwindow1, colorwindow2, colorwindow3, colorwindowroof):

	home = Rectangle(Point(x, y), Point(x + 500*kx, y + 400*ky))
	home.setFill(colorhome)
	
	tube = Rectangle(Point(x + 50*kx, y - 250*ky), Point(x + 150*kx, y))
	tube.setFill(colortube)
		
	roof = Polygon(Point(x, y), Point(x + 250*kx, y - 300*ky), Point(x + 500*kx, y))
	roof.setFill(colorroof)

	door = Rectangle(Point(x + 25*kx, y + 100*ky), Point(x + 200*kx, y + 400*ky))
	door.setFill(colordoor)

	left_hand = Circle(Point(x + 50*kx, y + 250*ky), 10*kx)
	left_hand.setFill(colorhand)

	right_hand = Circle(Point(x + 175*kx, y + 250*ky), 10*kx)
	right_hand.setFill(colorhand)

	window1 = Rectangle(Point(x + 270*kx, y + 120*ky), Point(x + 370*kx, y + 320*ky))
	window1.setFill(colorwindow1)

	window2 = Rectangle(Point(x + 370*kx, y + 120*ky), Point(x + 470*kx, y + 160*ky))
	window2.setFill(colorwindow2)

	window3 = Rectangle(Point(x + 370*kx, y + 160*ky), Point(x + 470*kx, y + 320*ky))
	window3.setFill(colorwindow3)

	window_roof = Circle(Point(x + 250*kx, y - 150*ky), 50*kx)
	window_roof.setFill(colorwindowroof)

	home.draw(win)
	if if_tube == True:
		tube.draw(win)
	roof.draw(win)
	door.draw(win)
	if where_hand == 'left':
		left_hand.draw(win)
	elif where_hand == 'right':
		right_hand.draw(win)
	if if_window_roof == True:
		window_roof.draw(win)
	window1.draw(win)
	window2.draw(win)
	window3.draw(win)


def Tree(x, y, kx, ky, if_stick, colorcrown, colorstem):
	
	crown3 = Circle(Point(x, y), 75*kx)
	crown3.setFill(colorcrown)

	crown2 = Circle(Point(x, y - 75*kx), 50*kx)
	crown2.setFill(colorcrown)

	crown1 = Circle(Point(x, y - 125*kx), 25*kx)
	crown1.setFill(colorcrown)

	stem = Polygon(Point(x, y - 60*ky), 
		Point(x + 10*kx, y + 150*ky), 
		Point(x - 10*kx, y + 150*ky), 
		Point(x, y - 60*ky))
	stem.setFill(colorstem)

	stick = Polygon(Point(x, y + 30*ky), 
		Point(x - 50*kx, y - 40*ky), 
		Point(x, y + 60*ky), 
		Point(x + 50*kx, y - 40*ky),
		Point(x, y + 30*ky))
	stick.setFill(colorstem)

	crown1.draw(win)
	crown2.draw(win)
	crown3.draw(win)
	if if_stick == True:
		stick.draw(win)
	stem.draw(win)

def Sun(x, y, R, if_sunshine, color):

	sun = Circle(Point(x, y), R)
	sun.setFill(color)

	sunshine1 = Polygon(Point(x, y - 1.5*R), 
		Point(x + R/2, y - R/2), 
		Point(x + 1.5*R, y),
		Point(x + R/2, y + R/2),
		Point(x, y + 1.5*R),
		Point(x - R/2, y + R/2), 
		Point(x - 1.5*R, y),
		Point(x - R/2, y - R/2),
		Point(x, y - 1.5*R))
	sunshine1.setFill(color)

	sunshine2 = Polygon(Point(x - 1.2*R, y - 1.2*R), 
		Point(x, y - R/2), 
		Point(x + 1.2*R, y - 1.2*R),
		Point(x + R/2, y),
		Point(x + 1.2*R, y + 1.2*R),
		Point(x, y + R/2), 
		Point(x - 1.2*R, y + 1.2*R),
		Point(x - R/2, y),
		Point(x - 1.2*R, y - 1.2*R))
	sunshine2.setFill(color)

	if if_sunshine == True:
		sunshine1.draw(win)
		sunshine2.draw(win)
	sun.draw(win)

def Cloud(x, y, kx, ky, color):

	cloud1 = Oval(Point(x, y), Point(x + 300*kx, y + 150*ky))
	cloud1.setFill(color)
	
	cloud2 = Oval(Point(x - 100*kx, y + 100*ky), Point(x + 200*kx, y + 200*ky))
	cloud2.setFill(color)

	cloud3 = Oval(Point(x + 100*kx, y + 75*ky), Point(x + 400*kx, y + 230*ky))
	cloud3.setFill(color)

	cloud4 = Oval(Point(x + 320*kx, y + 130*ky), Point(x + 490*kx, y + 200*ky))
	cloud4.setFill(color)

	cloud1.draw(win)
	cloud2.draw(win)
	cloud3.draw(win)
	cloud4.draw(win)

def Man(x, y, k, if_bow, colorskin, colorhair, colorshirt, colorjeans, colorboot, colorbow):

	hair = Rectangle(Point(x - 30*k, y - 35*k), Point(x + 30*k, y))
	hair.setFill(colorhair)

	head = Circle(Point(x, y), 30*k)
	head.setFill(colorskin)

	eye1 = Circle(Point(x - 9*k, y - 5*k), 3*k)
	eye1.setFill("#000000")

	eye2 = Circle(Point(x + 9*k, y - 5*k), 3*k)
	eye2.setFill("#000000")

	nose = Polygon(Point(x, y), 
		Point(x + 4*k, y + 9*k), 
		Point(x - 4*k, y + 9*k),
		Point(x, y))
	nose.setFill(colorskin)

	mouth = Line(Point(x - 8*k, y + 18*k), Point(x + 8*k, y + 18*k))
	mouth.setWidth(3)

	shirt = Polygon(Point(x - 32*k, y + 27*k), 
		Point(x + 32*k, y + 27*k), 
		Point(x + 60*k, y + 70*k),
		Point(x + 50*k, y + 80*k),
		Point(x + 30*k, y + 50*k),
		Point(x + 25*k, y + 100*k), 
		Point(x - 25*k, y + 100*k),
		Point(x - 30*k, y + 50*k),
		Point(x - 50*k, y + 80*k),
		Point(x - 60*k, y + 70*k),
		Point(x - 32*k, y + 27*k))
	shirt.setFill(colorshirt)

	hand1 = Circle(Point(x - 55*k, y + 75*k), 7*k)
	hand1.setFill(colorskin)

	hand2 = Circle(Point(x + 55*k, y + 75*k), 7*k)
	hand2.setFill(colorskin)

	jeans = Polygon(Point(x - 25*k, y + 100*k), 
		Point(x + 25*k, y + 100*k), 
		Point(x + 25*k, y + 200*k),
		Point(x + k, y + 200*k),
		Point(x + k, y + 120*k),
		Point(x - k, y + 120*k), 
		Point(x - k, y + 200*k),
		Point(x - 25*k, y + 200*k),
		Point(x - 25*k, y + 100*k),
		Point(x + 25*k, y + 100*k))
	jeans.setFill(colorjeans)

	boot1 = Polygon(Point(x - 25*k, y + 200*k), 
		Point(x - 25*k, y + 215*k), 
		Point(x - k, y + 215*k),
		Point(x - k, y + 200*k),
		Point(x - 25*k, y + 200*k))
	boot1.setFill(colorboot)

	boot2 = Polygon(Point(x + 25*k, y + 200*k), 
		Point(x + 25*k, y + 215*k), 
		Point(x + k, y + 215*k),
		Point(x + k, y + 200*k),
		Point(x + 25*k, y + 200*k))
	boot2.setFill(colorboot)

	bow = Polygon(Point(x, y + 40*k), 
		Point(x + 15*k, y + 30*k), 
		Point(x + 15*k, y + 50*k),
		Point(x, y + 40*k),
		Point(x - 15*k, y + 30*k),
		Point(x - 15*k, y + 50*k), 
		Point(x, y + 40*k))
	bow.setFill(colorbow)

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
	if if_bow == True:
		bow.draw(win)




#START drawing

House(550, 360, 1, 1, True, 'left', True, "#B97A57", "#7F7F7F", "#ED1C24", "#482425", "#FFF200", "#d5a1d2", "#00e800", "#f8dd86", "#9ddceb")
House(25, 450, 1, 0.5, True, 'left', True, "#B97A57", "#7F7F7F", "#00e800", "#482425", "#FFF200", "#d1d6a0", "#9ad9e8", "#8694f7", "#9ddceb")
House(1200, 350, 0.5, 0.6, True, 'left', True, "#B97A57", "#f8dd86", "#f886e8", "#482425", "#FFF200", "#d7f887", "#d5a1d2", "#9ad9ea", "#9ddceb")
House(610, 50, 0.15, 0.15, True, 'left', True, "#B97A57", "#f8dd86", "#f886e8", "#482425", "#FFF200", "#9ddceb", "#9ddceb", "#9ddceb", "#9ddceb")

win.getMouse()
win.close()