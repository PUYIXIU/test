# -*- codeing =utf-8 -*-
# @Time ： 2021/4/4 20:32
# @Author: wsy
# @File:模拟电梯.py
# @Software: PyCharm


import pygame

nowFloor=5#当前楼层
r = 40
k = 13
btnX, btnY , btnW , btnH = 150, 60, 130 , 570
pygame.init()
bX,bY,bW,bH=300,50,400,600

def showBuilding(window): #显示建筑物
    pygame.draw.rect(window,(0,255,0),(bX,bY,bW,bH),1)
    pygame.draw.line(window,(0,255,0),(bX+bW/3-1,bY),(bX+bW/3-1,bY+bH),1)
    pygame.draw.line(window,(0,255,0),(bX+bW*2/3+1,bY),(bX+bW*2/3+1,bY+bH),1)
    pygame.draw.rect(window,(0,255,0),(bX,bY-30,bW/3,30))
    pygame.draw.rect(window, (0, 255, 0), (bX+bW*2/3, bY - 30, bW / 3, 30))
    pygame.draw.rect(window, (0, 255, 0), (bX+bW/3, bY - 30, bW / 3, 10))
    pygame.draw.rect(window,(0,255,0),(bX,bY+bH,bW/3,30))
    pygame.draw.rect(window,(0,255,0),(bX+bW*2/3,bY+bH,bW/3,30))
    pygame.draw.rect(window, (0, 255, 0), (bX+bW/3, bY +bH+20, bW / 3, 10))
    pygame.draw.line(window,(0,0,0),(bX+bW/3, bY),(bX+bW*2/3, bY),1)
    pygame.draw.line(window, (0, 0, 0), (bX + bW / 3, bY+bH-1), (bX + bW * 2 / 3, bY+bH-1), 2)
    # pygame.draw.rect(window,(0,0,0),(bX+bW/3,bY-20,bW/3,21))
    font=pygame.font.Font('font/RocknRoll One.ttf',30)
    for i in range(1,5):
        sX=bX
        sY=eY=bY+i*(bH/5)
        eX=bX+bW
        pygame.draw.line(window,(0,255,0),(sX,sY),(eX,eY),1)
        pygame.draw.line(window,(0,0,0),(bX+bW/3,sY),(bX+bW*2/3,eY),4)
    for i in range(1,6):
        text=font.render("{} F".format(6-i),True,(0,255,0))
        tw,th=text.get_size()
        tx=bX+bW+30
        ty=bY+(bH/5/2)*(2*i-1)-th/2
        window.blit(text,(tx,ty))

def elevatorBtn(window):
    '''
    显示电梯按钮
    '''
    pygame.draw.rect(window,(0,255,0),(btnX,btnY,btnW,btnH),1)
    font=pygame.font.Font('font/RocknRoll One.ttf',30)
    for i in range(1,7):
        x=btnX+btnW/2
        y=k*i+r*(i-1)*2+btnY+r
        pygame.draw.circle(window,(0,255,0),(x,y),r,1)
        if i!=6:
            text=font.render(str(6-i),True,(0,255,0))
        else:
            text=font.render("run",True,(0,255,0))
        tx,ty=text.get_size()
        window.blit(text,(x-tx/2,y-ty/2))
    pass

def btnDown(num,window): #按钮点击事件
    x = btnX + btnW / 2
    y = k * num + r * (num - 1) * 2 + btnY + r
    pygame.draw.circle(window, (0, 255, 0), (x, y), r)
    font=pygame.font.Font('font/RocknRoll One.ttf',30)
    if num!=6:
        text = font.render(str(6-num), True, (0,0,0))
    else:
        text = font.render('run',True, (0, 0, 0))
    tx, ty = text.get_size()
    window.blit(text, (x - tx / 2, y - ty / 2))
    pass

def btnUp(num,window): #按钮松开事件
    x = btnX + btnW / 2
    y = k * num + r * (num - 1) * 2 + btnY + r
    pygame.draw.circle(window, (0, 0, 0), (x, y), r-1)
    font=pygame.font.Font('font/RocknRoll One.ttf',30)
    if num!=6:
        text = font.render(str(6-num), True, (0,255,0))
    else:
        text = font.render('run', True, (0, 255, 0))
    tx, ty = text.get_size()
    window.blit(text, (x - tx / 2, y - ty / 2))
    pass

def elevatorMove(floorList,window): #电梯移动
    global nowFloor
    lx = bX + bW / 3+1
    lw=bW/3-1
    lh=bH/5
    indexFloorList=[]
    n=len(floorList)
    print(floorList)
    for i in range(1,n):
        print('lala',n-i-1)
        for j in range(1,n-i):
            print("dd")
            x=abs(floorList[j]-nowFloor)
            y=abs(floorList[j+1]-nowFloor)
            if y<x:
                print("change")
                temp=floorList[j]
                floorList[j]=floorList[j+1]
                floorList[j+1]=temp

    # floorList.sort(reverse=True)
    print(floorList)
    # for num in floorList:
    # if len(floorList)>1:
    #
    if True:
        num=floorList[0]
        print(num)
        ny=bY+(nowFloor-1)*bH/5
        ly=bY+(num-1)*bH/5
        if nowFloor>num: #上移
          while ny>ly:
            pygame.draw.rect(window,(0,0,0),(lx,ny,lw,lh))
            pygame.draw.line(window,(0,0,0),(lx,ny-1),(lx+lw,ny-1),10)
            pygame.draw.line(window,(0,0,0),(lx,ny+lh+1),(lx+lw,ny+lh+1),10)
            ny-=5
            pygame.draw.line(window,(0,255,0),(lx,ny-1),(lx+lw,ny-1),10)
            pygame.draw.line(window,(0,255,0),(lx,ny+lh+1),(lx+lw,ny+lh+1),10)
            pygame.draw.rect(window,(0,255,0),(lx,ny,lw,lh))
            pygame.draw.rect(window,(0,0,0),(lx+lw/2-2,ny,4,lh))
            pygame.display.update()
            pygame.time.Clock().tick(100)
            pass
          open = lx + lw / 2 - 40
          width = 80
          nowOpen = lx + lw / 2 - 2
          nowWidth = 4
          while nowOpen > open:
              nowOpen -= 1
              nowWidth += 2
              pygame.draw.rect(window, (0, 0, 0), (nowOpen, ny, nowWidth, lh))
              pygame.display.update()
              pygame.time.Clock().tick(100)
        elif nowFloor<num:
            while ny<ly: #下降
                pygame.draw.rect(window, (0, 0, 0), (lx, ny, lw, lh))
                pygame.draw.line(window,(0,0,0),(lx,ny-1),(lx+lw,ny-1),10)
                pygame.draw.line(window,(0,0,0),(lx,ny+lh+1),(lx+lw,ny+lh+1),10)
                ny += 5
                pygame.draw.line(window,(0,255,0),(lx,ny-1),(lx+lw,ny-1),10)
                pygame.draw.line(window,(0,255,0),(lx,ny+lh+1),(lx+lw,ny+lh+1),10)
                pygame.draw.rect(window, (0, 255, 0), (lx, ny, lw, lh))
                pygame.draw.rect(window,(0,0,0),(lx+lw/2-2,ny,4,lh))
                pygame.display.update()
                pygame.time.Clock().tick(100)
            open=lx+lw/2-40
            width=80
            nowOpen=lx+lw/2-2
            nowWidth=4
            while nowOpen>open:
                nowOpen-=1
                nowWidth+=2
                pygame.draw.rect(window,(0,0,0),(nowOpen,ny,nowWidth,lh))
                pygame.display.update()
                pygame.time.Clock().tick(100)
        elif nowFloor==num and len(floorList)>1:
            open=lx+lw/2-2
            width=4
            nowOpen=lx+lw/2-40
            nowWidth=80
            while nowOpen<open:
                pygame.draw.rect(window, (0, 255, 0), (nowOpen,ny+3,nowWidth/2,lh-4))
                pygame.draw.rect(window, (0, 255, 0), (nowOpen+nowWidth/2, ny + 3, nowWidth/2, lh - 4))
                nowOpen+=1
                nowWidth-=2
                pygame.draw.rect(window,(0,0,0),(nowOpen,ny,nowWidth,lh))
                pygame.display.update()
                pygame.time.Clock().tick(100)
            # pygame.draw.rect(window, (0, 255, 0), (lx, ny, lw, lh))
            x = btnX + btnW / 2
            y = k * num + r * (num - 1) * 2 + btnY + r
            pygame.draw.circle(window, (0, 0, 0), (x, y), r - 5, 4)
            floorList.remove(num)
            elevatorMove(floorList,window)
            return floorList
        elif nowFloor==num and len(floorList)==1:
            pygame.draw.line(window,(0,255,0),(lx,ny-1),(lx+lw,ny-1),10)
            pygame.draw.line(window,(0,255,0),(lx,ny+lh+1),(lx+lw,ny+lh+1),10)
            pygame.draw.rect(window, (0, 255, 0), (lx, ny, lw, lh))
            pygame.draw.rect(window,(0,0,0),(lx+lw/2-40,ny,80,lh))
        nowFloor=num
        # delFloorList.append(num)
        x = btnX + btnW / 2
        y = k * num + r * (num - 1) * 2 + btnY + r
        pygame.draw.circle(window, (0, 0, 0), (x, y), r-5,4)
        floorList.remove(num)
        if len(floorList)==0:
            floorList.append(num)
    # for item in delFloorList:
    #     floorList.remove(item)
    return floorList
    pass

window=pygame.display.set_mode((900,700))
elevatorBtn(window)
floorList=[5] #电梯楼层
elevatorMove(floorList,window)
while True:
    showBuilding(window)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mx,my=event.pos
            if mx>btnX+btnW/2-r and mx<btnX+btnW/2+r:
                if my>k*1+r*(1-1)*2+btnY and my<k*1+r*1*2+btnY:
                    floorList.append(1)
                    btnDown(1,window)
                    # print("1")
                elif my>k*2+r*(2-1)*2+btnY and my<k*2+r*2*2+btnY:
                    floorList.append(2)
                    btnDown(2,window)
                    # print("2")
                elif my>k*3+r*(3-1)*2+btnY and my<k*3+r*3*2+btnY:
                    floorList.append(3)
                    btnDown(3,window)
                    # print("3")
                elif my>k*4+r*(4-1)*2+btnY and my<k*4+r*4*2+btnY:
                    floorList.append(4)
                    btnDown(4,window)
                    # print("4")
                elif my>k*5+r*(5-1)*2+btnY and my<k*5+r*5*2+btnY:
                    floorList.append(5)
                    btnDown(5,window)
                    # print("5")
                elif my>k*6+r*(6-1)*2+btnY and my<k*6+r*6*2+btnY:
                    # floorList.append(6)
                    btnDown(6,window)
                    floorList=elevatorMove(floorList,window)
                    # print("run")
        elif event.type==pygame.MOUSEBUTTONUP:
            mx, my = event.pos
            if mx > btnX + btnW / 2 - r and mx < btnX + btnW / 2 + r:
                if my > k * 1 + r * (1 - 1) * 2 + btnY and my < k * 1 + r * 1 * 2 + btnY:
                    btnUp(1, window)
                    # print("1")
                elif my > k * 2 + r * (2 - 1) * 2 + btnY and my < k * 2 + r * 2 * 2 + btnY:
                    btnUp(2, window)
                    # print("2")
                elif my > k * 3 + r * (3 - 1) * 2 + btnY and my < k * 3 + r * 3 * 2 + btnY:
                    btnUp(3, window)
                    # print("3")
                elif my > k * 4 + r * (4 - 1) * 2 + btnY and my < k * 4 + r * 4 * 2 + btnY:
                    btnUp(4, window)
                    # print("4")
                elif my > k * 5 + r * (5 - 1) * 2 + btnY and my < k * 5 + r * 5 * 2 + btnY:
                    btnUp(5, window)
                    # print("5")
                elif my > k * 6 + r * (6 - 1) * 2 + btnY and my < k * 6 + r * 6 * 2 + btnY:
                    btnUp(6, window)
                    # print("run")
    for floor in floorList:
        x = btnX + btnW / 2
        y = k * floor + r * (floor - 1) * 2 + btnY + r
        pygame.draw.circle(window, (0, 255, 0), (x, y), r-5,4)

    pygame.display.update()