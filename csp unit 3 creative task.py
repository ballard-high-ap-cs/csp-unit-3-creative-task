from cmu_graphics import *
app.background='whitesmoke'
first = Label('Take off the tape!',200,50,size = 35)
first.visible=True
second = Label('oh.',200,50,size = 35)
second.visible=False
#have a fuction where we are dragging, will pull off the tape using the same function as the pig, after the tape has been completly pulled off, the banana will fall
#banana
Banana = Group(
    Rect(120,120,15,5,fill='sienna'),
    Polygon(120,125,135,125,140,150,115,150,fill=gradient('darkgoldenrod','goldenrod')),
    Polygon(115,150,140,150,150,160,170,205,130,220,110,180,fill=gradient('saddlebrown','darkgoldenrod','goldenrod')),
    Polygon(130,220,170,205,200,225,165,250,fill=gradient('darkgoldenrod','goldenrod')),
    Polygon(165,250,200,225,245,240,270,245,270,255,240,265,200,263,fill=gradient('darkgoldenrod','goldenrod')),
    Rect(270,245,5,10,fill='sienna')
    )
    
Splat = Group(
    Rect(130,390,150,10,fill='darkgoldenrod'),
    Oval(280,400,80,20,fill='darkgoldenrod'),
    Oval(130,400,80,20,fill='darkgoldenrod')
    )
Splat.visible=False

app.bananaHeight = [192.5, 215, 250, 300, 329,400]

def DrawDuctTape():
    cx = 90
    cy = 260
    for i in range(130):
        cx += 1
        cy-=1
        ductTape.add(
            Line(cx, cy, cx+30, cy+55, fill='silver')
            )
        ductTape.add(
            Line(cx+1, cy, cx+30, cy+55, fill='lightGray',dashes=True)
            )
            
ductTape = Group()
DrawDuctTape()
app.bananaCounter = 0

def onMouseDrag(mouseX,mouseY):
    farthestLeftBubble = None
    app.bananaCounter += 1
    
    if (len(ductTape.children) > 0):
        ductTape.remove(ductTape.children[0])
        ductTape.remove(ductTape.children[0])
        ductTape.remove(ductTape.children[0])
        ductTape.remove(ductTape.children[0])
        ductTape.remove(ductTape.children[0])

    elif (farthestLeftBubble != None):
        farthestLeftBubble.visible = False
        
    if (len(app.bananaHeight) > 0):
        if app.bananaCounter%8==0:
            bananaHeight = app.bananaHeight.pop(0)
            Banana.centerY = bananaHeight
            
    if Banana.centerY==400:
        Banana.visible=False
        Splat.visible=True
        first.visible=False
        second.visible=True
cmu_graphics.run()