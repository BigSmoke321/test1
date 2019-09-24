from graphics import *
win=GraphWin("MyWin",1600,800)

# x, y - up left corner of the base of house

def House(x, y, kx, ky, colorhome, colortube, colorroof, colordoor, colorhand, colorwindow1, colorwindow2, colorwindow3):

	home = Rectangle(Point(x, y), Point(x + 500*kx, y + 400*ky))
	home.setFill(colorhome)

	tube=Rectangle(Point(x + 50*kx, y - 250*ky), Point(x + 150*kx, y))
	tube.setFill(colortube)

	roof=Polygon(Point(x, y), Point(x + 250*kx, y - 300*ky), Point(x + 500*kx, y))
	roof.setFill(colorroof)

	door=Rectangle(Point(x + 25*kx, y + 100*ky), Point(x + 200*kx, y + 400*ky))
	door.setFill(colordoor)

	hand=Circle(Point(x + 175*kx, y + 250*ky), 10*kx)
	hand.setFill(colorhand)

	window1 = Rectangle(Point(x + 270*kx, y + 120*ky), Point(x + 370*kx, y + 320*ky))
	window1.setFill(colorwindow1)

	window2 = Rectangle(Point(x + 370*kx, y + 120*ky), Point(x + 470*kx, y + 160*ky))
	window2.setFill(colorwindow2)

	window3 = Rectangle(Point(x + 370*kx, y + 160*ky), Point(x + 470*kx, y + 320*ky))
	window3.setFill(colorwindow3)

	home.draw(win)
	tube.draw(win)
	roof.draw(win)
	door.draw(win)
	hand.draw(win)
	window1.draw(win)
	window2.draw(win)
	window3.draw(win)


#START drawing

House(550, 360, 1, 1, "#B97A57", "#7F7F7F", "#ED1C24", "#482425", "#FFF200", "#d5a1d2", "#00e800", "#f8dd86")
House(25, 450, 1, 0.5, "#B97A57", "#7F7F7F", "#00e800", "#482425", "#FFF200", "#d1d6a0", "#9ad9e8", "#8694f7")
House(1200, 350, 0.5, 0.6, "#B97A57", "#f8dd86", "#f886e8", "#482425", "#FFF200", "#d7f887", "#d5a1d2", "#9ad9ea")
House(610, 50, 0.15, 0.15, "#B97A57", "#f8dd86", "#f886e8", "#482425", "#FFF200", "#9ddceb", "#9ddceb", "#9ddceb")

win.getMouse()
win.close()