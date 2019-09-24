from graphics import *
win=GraphWin("MyWin",1000,1000)

c=Circle(Point(500,500),40)
r=Rectangle(Point(250,500),Point(750,900))
r.setFill("#B97A57")

r1=Rectangle(Point(300,250),Point(400,500))
r1.setFill("#7F7F7F")

p=Polygon(Point(250,500),Point(500,200),Point(750,500))
p.setFill("#ED1C24")

r2=Rectangle(Point(275,600),Point(450,900))
r2.setFill("#482425")

c1=Circle(Point(425,750),10)
c1.setFill("#FFF200")

r3=Rectangle(Point(520,620),Point(720,820))
r3.setFill("#99D9EA")

l=Line(Point(620,620),Point(620,820))

l1=Line(Point(620,660),Point(720,660))


r.draw(win)
r1.draw(win)
p.draw(win)
r2.draw(win)
c1.draw(win)
r3.draw(win)
l.draw(win)
l1.draw(win)

win.getMouse()
win.close()