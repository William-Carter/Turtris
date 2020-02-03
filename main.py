# Copyright (c) 2019 William Carter
import turtle, time, sys, random

window = turtle.Screen()
window.tracer(0, 0)
GRIDWIDTH = 10
wallList = [
    (-40, 170),
    (-30, 170),
    (-20, 170),
    (-10, 170),
    (0, 170),
    (10, 170),
    (20, 170),
    (30, 170),
    (40, 170),
    (40, 160),
    (40, 150),
    (40, 140),
    (40, 130),
    (40, 120),
    (40, 110),
    (40, 100),
    (40, 90),
    (40, 80),
    (40, 70),
    (40, 60),
    (40, 50),
    (40, 40),
    (40, 30),
    (40, 20),
    (40, 10),
    (40, 0),
    (40, -10),
    (40, -20),
    (30, -20),
    (20, -20),
    (10, -20),
    (0, -20),
    (-10, -20),
    (-20, -20),
    (-30, -20),
    (-40, -20),
    (-50, -20),
    (-50, -10),
    (-50, 0),
    (-50, 10),
    (-50, 20),
    (-50, 30),
    (-50, 40),
    (-50, 50),
    (-50, 60),
    (-50, 70),
    (-50, 80),
    (-50, 90),
    (-50, 100),
    (-50, 110),
    (-50, 120),
    (-50, 130),
    (-50, 140),
    (-50, 150),
    (-50, 160),
    (-50, 170),
]
wallListTop = 160
wallListBottom = -20

collisionList = []
setup = turtle.Turtle()
setup.hideturtle()
setup.up()
setup.shape("square")
setup.turtlesize(0.45)
setup.speed(0)

collides = turtle.Turtle()
collides.hideturtle()
collides.up()
collides.shape("square")
collides.turtlesize(0.45)
collides.speed(0)

line = turtle.Turtle()
line.color("gray")
line.up()
line.hideturtle()
linesOn = True


def drawLines(lis):
    line.clear()
    global linesOn
    xList = []
    yList = []
    for object in lis:
        tup = object
        x = tup[0]
        y = tup[1]
        xList.append(x)
        yList.append(y)
    maxX = max(xList)
    maxY = max(yList)
    minX = min(xList)
    minY = min(yList)
    topLeft = (minX, maxY)
    bottomRight = (maxX, minY)
    line.setpos(topLeft)
    line.seth(0)
    line.setx(line.xcor() + (GRIDWIDTH / 2))
    if linesOn == "True":
        for i in range((int(bottomRight[0]) - int(topLeft[0])) // GRIDWIDTH):
            line.down()
            backup = line.pos()
            line.setpos(line.xcor(), bottomRight[1])
            line.up()
            line.setpos(backup)
            line.setpos(line.xcor() + GRIDWIDTH, line.ycor())

        line.setpos(topLeft)
        line.seth(0)
        line.sety(line.ycor() - 5)
        line.down()
        for j in range((int(topLeft[1]) - int(bottomRight[1])) // 10):
            line.down()
            backup = line.pos()
            line.setpos(bottomRight[0], line.ycor())
            line.up()
            line.setpos(backup)
            line.setpos(line.xcor(), line.ycor() - GRIDWIDTH)


def drawBoundary():
    global setup
    global wallList
    setup.clearstamps()
    for i in range(len(wallList)):
        setup.setpos(wallList[i])
        setup.stamp()


def drawCollisionList():
    global collides
    global collisionList
    collides.clearstamps()
    for i in collisionList:
        collides.color(i[1])
        collides.setpos(i[0])
        collides.stamp()


drawBoundary()
drawLines(wallList)


class tonktrono:
    def __init__(self, blockType, pos):
        self.block = blockType
        self.pos = pos
        self.color = blockType[1]

    def rotateBlock(self):
        newRotation = []
        currentString = ""
        for i in range(len(self.block[0][0])):
            for j in range(len(self.block[0])):
                curList = list(self.block[0][j])
                curList = list(reversed(curList))
                currentString = currentString + curList[i]

            newRotation.append(currentString)
            currentString = ""

        block = self.block
        self.block = [newRotation]
        if collCount == 0:
            endLocation = getBlock(self, self.pos)
        if collCount > 0:
            endLocation = getBlock(self, (self.pos[0], self.pos[1] + GRIDWIDTH))
        for location in endLocation:
            if checkCollision(endLocation):
                self.block = block

    def rotateBlock2(self):
        for i in range(3):
            self.rotateBlock()

    def moveRight(self):
        if collCount == 0:
            xcor = self.pos[0]
            xcor += GRIDWIDTH
            testPos = (xcor, self.pos[1])
            endLocation = getBlock(self, testPos)
            for location in endLocation:
                if checkCollision(endLocation):
                    return None
            self.pos = testPos
        if collCount > 0:
            xcor = self.pos[0]
            xcor += GRIDWIDTH
            if collCount != 0:
                testPos = (xcor, self.pos[1] + GRIDWIDTH)
            else:
                testPos = (xcor, self.pos[1])
            endLocation = getBlock(self, testPos)
            for location in endLocation:
                if checkCollision(endLocation):
                    return None
            self.pos = testPos

    def moveLeft(self):
        xcor = self.pos[0]
        xcor -= GRIDWIDTH
        if collCount != 0:
            testPos = (xcor, self.pos[1] + GRIDWIDTH)
        else:
            testPos = (xcor, self.pos[1])
        endLocation = getBlock(self, testPos)
        for location in endLocation:
            if checkCollision(endLocation):
                return None
        self.pos = testPos

    def solidify(self):
        drawTurt.clearstamps()
        solids = getBlock(self, self.pos)
        for i in solids:
            collisionList.append([i, self.color])


# Shape Types

blockS = [["---", "-00", "00-"], "red"]

blockZ = [["---", "00-", "-00"], "green"]

blockI = [["----", "0000", "----", "----"], "light blue"]

blockO = [["----", "-00-", "-00-", "----"], "yellow"]

blockT = [["-0-", "000", "---"], "purple"]

blockL = [["-0-", "-0-", "-00"], "orange"]

blockJ = [["-0-", "-0-", "00-"], "blue"]

blockList = [blockS, blockZ, blockT, blockJ, blockL, blockO, blockI]
bag = blockList[:]


def getRandom():
    global bag, blockList
    if len(bag) == 0:

        bag = blockList[:]
    e = random.choice(bag)
    bag.remove(e)
    return e


currentBlock = tonktrono(getRandom(), (0, 140))
upcomingBlock = tonktrono(getRandom(), (80, 140))
drawTurt = turtle.Turtle()
drawTurt.ht()
drawTurt.shape("square")
drawTurt.turtlesize(0.40)
drawTurt.up()


def correct(e):
    e.setpos(round(e.xcor(), 0), round(e.ycor(), 0))


def getBlock(obj, pos):
    retList = []
    drawTurt.setpos(pos)
    correct(drawTurt)
    if len(obj.block[0]) % 2 == 0:
        offset = 0
    elif len(obj.block[0]) % 2 >= 1:
        offset = 0.5
    drawTurt.setx(drawTurt.xcor() - ((len(obj.block[0]) / 2 + offset) * GRIDWIDTH))
    correct(drawTurt)
    drawTurt.sety(drawTurt.ycor() + ((len(obj.block[0]) / 2 + offset) * GRIDWIDTH))
    correct(drawTurt)
    drawTurt.color(obj.color)
    starter = drawTurt.pos()
    for i in range(len(obj.block[0])):
        curList = list(obj.block[0][i])
        for j in range(len(curList)):
            drawTurt.setx(drawTurt.xcor() + GRIDWIDTH)
            correct(drawTurt)
            if curList[j] == "0":
                retList.append(drawTurt.pos())
        drawTurt.setx(starter[0])
        correct(drawTurt)
        drawTurt.sety(drawTurt.ycor() - GRIDWIDTH)
        correct(drawTurt)
    return retList


def drawBlock(blo):
    for i in blo:
        drawTurt.setpos(i)
        drawTurt.stamp()


def enableControls():
    global speed
    speed = 5
    window.onkey(currentBlock.rotateBlock2, "Up")
    window.onkey(currentBlock.moveLeft, "Left")
    window.onkey(currentBlock.moveRight, "Right")
    window.onkey(downSpeed, "space")
    window.onkey(currentBlock.rotateBlock, "z")
    window.listen()


mainCounter = 0


def checkCollision(blo):
    collideCoords = []
    for lis in collisionList:
        collideCoords.append(lis[0])
    for i in blo:
        i2 = (int(i[0]), int(i[1]))
        if i2 in wallList or i2 in collideCoords:
            return True
    return False


def downSpeed():
    global speed
    if speed == 5:
        speed = 0
    elif speed == 0:
        speed = 5


def remAll(L, item):
    answer = []
    for i in L:
        if i != item:
            answer.append(i)
    return answer


def findFullLines():
    yLineList = []
    for block in collisionList:
        yLineList.append(round(block[0][1], 0))
    for item in yLineList:
        if yLineList.count(item) < 8:
            yLineList = remAll(yLineList, item)
    removeList = []
    for block in collisionList:
        if round(block[0][1], 0) in yLineList:
            if not block in removeList:
                removeList.append(block)
    for item in removeList:
        print(item)
        collisionList.remove(item)


def applyGravity():
    for i in range(4):
        yLineList = []
        for block in collisionList:
            yLineList.append(round(block[0][1], 0))

        yLineList.append(-20)
        for item in yLineList:
            if not yLineList.count(item) < 8:
                yLineList = remAll(yLineList, item)

        for block in collisionList:
            if not block[0][1] - GRIDWIDTH in yLineList:
                block[0] = (block[0][0], block[0][1] - GRIDWIDTH)


speed = 5
collCount = 0


def mainLoop():
    global upcomingBlock
    global currentBlock
    global mainCounter
    global speed
    global collCount
    global upcomingBlock

    findFullLines()
    applyGravity()
    drawTurt.clearstamps()
    yeet = getBlock(currentBlock, currentBlock.pos)
    if checkCollision(yeet):
        drawBlock(
            getBlock(
                currentBlock, (currentBlock.pos[0], currentBlock.pos[1] + GRIDWIDTH)
            )
        )
        if collCount < 20:
            collCount += 1
        else:
            currentBlock.pos = (currentBlock.pos[0], currentBlock.pos[1] + GRIDWIDTH)
            currentBlock.solidify()
            del currentBlock
            currentBlock = tonktrono(upcomingBlock.block, (0, 140))
            upcomingBlock.block = getRandom()
            upcomingBlock.color = upcomingBlock.block[1]
            enableControls()
            collCount = 0
    else:
        collCount = 0
        drawBlock(yeet)
    drawBlock(getBlock(upcomingBlock, upcomingBlock.pos))
    ycor = currentBlock.pos[1]
    if collCount == 0:
        if mainCounter >= speed:
            ycor -= GRIDWIDTH
            mainCounter = 0
    currentBlock.pos = (currentBlock.pos[0], ycor)
    mainCounter += 1

    drawCollisionList()
    turtle.update()
    time.sleep(0.02)


enableControls()
while True:
    mainLoop()
