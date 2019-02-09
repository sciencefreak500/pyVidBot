from PIL import Image, ImageDraw
import os
import math
import random

#helper functions
def pathjoin(base,current):
    return os.path.join(base,current)


def getMidpointsAndDirection(width,height,limit):
    #left, right up or down?
    direction = 'vertical' if random.randint(0,1) == 0 else 'horizontal'
    horizontal = 'L' if random.randint(0,1) == 0 else 'R'
    vertical = 'U' if random.randint(0,1) == 0 else 'D'
    
    #random mids
    mid = math.floor(limit/2)
    startx,starty = [random.randrange(mid,width-mid), random.randrange(mid,height-mid)]
    endx,endy = [random.randrange(mid,width-mid), random.randrange(mid,height-mid)]

    #print(direction)
    #going left and right
    if direction == 'horizontal':
        if horizontal == 'L':
            startx = mid
            towards = 'L'
            endx = width-mid
            
        if horizontal == 'R':
            startx = width-mid
            endx = mid
            towards = 'R'

    #going up and down
    if direction == 'vertical':
        if vertical == 'U':
            starty = mid
            endy = height-mid
            towards = 'U'
            
        if vertical == 'D':
            starty = height-mid
            endy = mid
            towards = 'D'

    return ((startx,starty),(endx,endy),towards)
    



def getPixelRate(midstart,midend,totalframes):
    #if Up or Down
    midx = midstart[0] - midend[0]
    midy = midstart[1] - midend[1]
    pixelRateX = midx/totalframes
    pixelRateY = midy/totalframes
    return [pixelRateX,pixelRateY]

def getMovingMidpointArray(midstart,slopeX,slopeY):
    currentMidpointX = midstart[0]
    currentMidpointY = midstart[1]
    result = []
    for i in range(totalframes):
        currentMidpointX = math.floor(currentMidpointX + slopeX)
        currentMidpointY = math.floor(currentMidpointY + slopeY)
        result.append((currentMidpointX,currentMidpointY))
    return result


basedir = pathjoin(os.path.dirname(os.path.abspath(__file__)),'images')
#imageList = os.listdir(basedir)
imageList = ['image00005.jpg']

for index,i in enumerate(imageList):
    #makes new directory of images to store
    newdir = pathjoin(basedir,i[0:len(i)-4])
    #os.mkdir(newdir)
    
    #get image (width,height)
    im = Image.open(pathjoin(basedir,i))
    width,height = im.size

    #get 1/2 side of image, make that the crop size
    totalframes = 24*3
    limit = math.floor(min(im.size[0],im.size[1])/2)

    #get the slope, points, and direction
    midstart,midend,direction = getMidpointsAndDirection(width,height,limit)
    slopeX,slopeY = getPixelRate(midstart,midend,totalframes)

    #get the individual midpoints
    movingMidpoint = getMovingMidpointArray(midstart,slopeX,slopeY)

    #get the image crops
    mid = limit/2
    #cropArray = []

    draw = ImageDraw.Draw(im)
    #xy = (movingMidpoint[0][0],movingMidpoint[0][1],movingMidpoint[71][0],movingMidpoint[71][1])
    #draw.line(xy,fill=128,width=3)
    
    
 
    for index,i in enumerate(movingMidpoint):
        #box = (i[0]-mid,i[1]-mid,i[0]+mid,i[1]+mid)
        box = (i[0]-20,i[1]-20,i[0]+20,i[1]+20)
        draw.rectangle(box,fill=128,width=3)
        #region = im.crop(box)
        #cropArray.append(region)
        #region.save(pathjoin(newdir,str(index)+'.jpg'))

    im.show()













    


