#-*- coding : UTF-8 -*-
#参数设置,这里定义一些信号变量
scene = 1
surface_background_url = "surface_background.jpg"
game_background_url = "game_background.jpg"
cong_background_url = "cong.jpg"
surface_font = ""
screen_resolution = (640,480)
theme_color = (33,33,33)
block_color = (254,67,101)
pause = False
point = "00000000"
highPoint = "00000000"
import pygame
import time
import copy
from random import randint
from pygame.locals import *

#初始化游戏和视窗
pygame.init()
screen = pygame.display.set_mode(screen_resolution)

#加载图片
surface_background = pygame.image.load(surface_background_url).convert()
game_background = pygame.image.load(game_background_url).convert()
cong_background = pygame.image.load(cong_background_url).convert()

#调整图片细节
surface_background = pygame.transform.scale(surface_background,screen_resolution)
game_background = pygame.transform.scale(game_background,screen_resolution)
cong_background = pygame.transform.scale(cong_background,screen_resolution)

#添加文字
start_game = pygame.font.SysFont("comicsansms",50)
start_game_surface = start_game.render("START GAME!",False,(66,66,66),(222,222,222))


pause_btn = pygame.font.SysFont("comicsansms",50)
pause_btn_surface = pause_btn.render("Pause",False,(66,66,66),(222,222,222))

restart_btn = pygame.font.SysFont("comicsansms",50)
restart_btn_surface = restart_btn.render("Restart",False,(66,66,66),(222,222,222))

point_show = pygame.font.SysFont("comicsansms",50)

cong_show = pygame.font.SysFont("comicsansms",50)
#这里来定义几个类,用来制作游戏
#第一个就是我们的游戏类,就是一个矩阵
class gameBody(object):
	def __init__(self,row_pix,column_pix):
		self.matrix = [[0]*12 for i in range(15)]
		self.existObj = False
		self.row_pix = row_pix
		self.col_pix = column_pix
	def render(self):
		for rindex,rows in enumerate(self.matrix):
			for cindex,col in enumerate(rows):
				if col == 1:
					pygame.draw.rect(screen,block_color,((cindex * self.col_pix,self.row_pix * rindex),(self.col_pix,self.row_pix)))
				else:
					pygame.draw.rect(screen,theme_color,((cindex * self.col_pix,self.row_pix * rindex),(self.col_pix,self.row_pix)))
#move接收从方块收到的坐标,判断是否能移动,如果可以的话,
	def move(self):
		bcoors = self.movingObj.clearBefore()
		#clear before position
		for coor in bcoors:
			self.matrix[coor[0]][coor[1]] = 0
		coors = self.movingObj.move()
		for coor in coors:
			self.matrix[coor[0]][coor[1]] = 1
		#here to judge that if obj touches the button
		for coor in coors:
			if coor[0] > 12:
				self.createObj()
				break
		#bounce detect
		for coor in self.getbottom(coors):
			if self.matrix[coor[0]+1][coor[1]] == 1:
				self.createObj()
				if coor[0] < 3:
					global pause
					pause = True
				break
		#if a whole row  are  1, clean that row and all down 1
		for rindex,rows in enumerate(self.matrix):
			for cindex,col in enumerate(rows):
				if col == 0:
					break
				if cindex == len(rows)-1:
					self.clean(rindex)
	def clean(self,cleanindex):
		del self.matrix[cleanindex]
		self.matrix[:0] = [[0]*12]
		global point
		point = str(int(point)+1000).zfill(8)

	def delta(self,x):
		#clear previous one
		bcoors = self.movingObj.clearBefore()
		for coor in bcoors:
			self.matrix[coor[0]][coor[1]] = 0
		coors = self.movingObj.delta(x)
		for coor in coors:
			self.matrix[coor[0]][coor[1]] = 1
	def transform(self):
		bcoors = self.movingObj.clearBefore()
		for coor in bcoors:
			self.matrix[coor[0]][coor[1]] = 0
		coors = self.movingObj.transform()
		for coor in coors:
			self.matrix[coor[0]][coor[1]] = 1
	def getbottom(self,coors):
		rv =[]
		bottom = 0
		for coor in coors:
			if coor[0] > bottom:
				bottom = coor[0]
		for coor in coors:
			if(coor[0] == bottom):
				rv.append(coor)
		return rv

#创造物体方法,创造一个downObject类
	def createObj(self):
		self.movingObj = downObject()
		self.existObj = True
	#restart method
	def restart(self):
		self.matrix = [[0] * 12 for i in range(15)]
		self.createObj()
		global pause
		if pause == True:
			pause = False
		global point
		global highPoint
		if point > highPoint:
			highPoint = point
		point = "00000000"
#第二个就是我们的下落方块类,就是一个数组,记录了每一个部分所在矩阵位置
#type 1 方块
#type 2 凸字
#type 3 L形
#type 4 I形
#type 5 凹字形
#type 6 超长I形
#type 7 加长凸字形
class downObject(object):
	def __init__(self):
		self.positions = self.getPosition()
	def getPosition(self):
		self.type = type = self.getType()
		self.status = 0
		delta = self.randomPosition()
		if(type == 1):
			return [[0,delta],[0,delta+1],[1,delta],[1,delta+1]]
		elif(type == 2):
			self.statusMatrix = [[[1, -1], [1, 1], [0, 0], [-1, -1]],
								 [[1, 1], [-1, 1], [0, 0], [1, -1]],
								 [[-1, 1], [-1, -1], [0, 0], [1, 1]],
								 [[-1, -1], [1, -1], [0, 0], [-1, 1]]]
			return [[0,delta+1],[1,delta],[1,delta+1],[1,delta+2]]
		elif(type == 3):
			self.statusMatrix = [[[1, 1], [0, 2], [-1, 1], [-2, 0]],
								 [[0, 1], [-1, 0], [0, -1], [1, -2]],
								 [[-1, -1], [0, -2], [1, -1], [2, 0]],
								 [[0, -1], [1, 0], [0, 1], [-1, 2]]]
			return [[0,delta+1],[1,delta+1],[1,delta+2],[1,delta+3]]
		elif(type == 4):
			self.statusMatrix = [[[0,0],[1,-1],[2,-2],[3,-3]],
								 [[0,0],[-1,1],[-2,2],[-3,3]]]
			return [[0,delta],[0,delta+1],[0,delta+2],[0,delta+3]]
		elif(type == 5):
			return [[0,delta],[0,delta+2],[1,delta],[1,delta+1],[1,delta+2]]
		elif(type == 6):
			return [[0,delta],[0,delta+1],[0,delta+2],[0,delta+3],[0,delta+4],[0,delta+5]]
		elif(type == 7):
			return [[0,delta+1],[1,delta+1],[2,delta],[2,delta+1],[2,delta+2]]
#move 函数丝毫不考虑碰撞问题,碰撞应该是game主题考虑的事,如果可以走再触发方块中的move函数
	def move(self):
		for position in self.positions:
			position[0] = position[0]+1
		return self.positions
	def clearBefore(self):
		return self.positions
	def getType(self):
		return randint(1,4)
	def randomPosition(self):
		return randint(1,5)
	def delta(self,x):
		for position in self.positions:
			if position[1] < 11:
				position[1] = position[1]+x
		return self.positions
	def transform(self):
		if self.type == 1:
			return self.positions
		for i,position in enumerate(self.positions):
			position[0] += self.statusMatrix[self.status][i][0]
			position[1] += self.statusMatrix[self.status][i][1]
		self.status += 1
		if self.status > len(self.statusMatrix)-1:
			self.status = 0
		return self.positions

def createpointtext():
	return point_show.render(point, False, (66, 66, 66), (222, 222, 222))

def createhighpointtext():
	return point_show.render(highPoint, False, (66, 66, 66), (222, 222, 222))


#主循环
while True:
	#这里定义一些公有的信号变量
	screenWidth,screenHeight = pygame.display.get_surface().get_size()
	#这里是场景1的私有信号变量
	text_area = (screenWidth/2-start_game_surface.get_width()/2,screenHeight/2-start_game_surface.get_height()/2)
	pause_btn_position = (480,180)
	restart_btn_position = (480,250)
	#sign variable of scene2
	point_position = (440,100)
	highpoint_position = (440,50)
	#事件处理
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
		#append keyboard detection to scene2
		if event.type == KEYDOWN and scene == 2:
			if event.key == K_LEFT:
				gamebody.delta(-1)
			if event.key == K_RIGHT:
				gamebody.delta(1)
			if event.key == K_UP:
				gamebody.transform()
			if event.key == K_DOWN:
				pass
		#判断是否点击到游戏开始,切换到场景2
		if event.type == MOUSEBUTTONDOWN and scene == 1:
			tx,ty = event.pos
			if(screenWidth/2-start_game_surface.get_width()/2<tx and tx < screenWidth/2+start_game_surface.get_width()/2 and ty>screenHeight/2-start_game_surface.get_height()/2 and ty<screenHeight/2+start_game_surface.get_height()/2):
				scene = 2
		#game pause
		if event.type == MOUSEBUTTONDOWN and scene == 2:
			tx,ty = event.pos
			if pause_btn_position[0]<tx and tx < pause_btn_position[0]+pause_btn_surface.get_width() and ty>pause_btn_position[1] and ty<pause_btn_position[1]+pause_btn_surface.get_height():
				pause = not pause
			if restart_btn_position[0]<tx and tx < restart_btn_position[0]+restart_btn_surface.get_width() and ty>restart_btn_position[1] and ty<restart_btn_position[1]+restart_btn_surface.get_height():
				gamebody.restart()
	#场景1:进入游戏
	if(scene == 1):
		screen.blit(surface_background,(0,0))
		screen.blit(start_game_surface,text_area)
	#场景2:游戏开始
	if(scene == 2):
		try :
			print(gamebody)
		except:
			gamebody = gameBody(34,34)
		#绘制主要框架(每一帧重复绘制)
		screen.blit(game_background,(0,0))
		pygame.draw.rect(screen,theme_color,[0,0,400,600])
		pygame.draw.rect(screen,theme_color,[420,50,200,100])
		#绘制文字
		screen.blit(pause_btn_surface,pause_btn_position)
		screen.blit(restart_btn_surface,restart_btn_position)
		screen.blit(createpointtext(),point_position)
		screen.blit(createhighpointtext(), highpoint_position)
		#主游戏部分
		if(gamebody.existObj == False):
			gamebody.createObj()
		if(pause == False):
			gamebody.move()
		gamebody.render()
		time.sleep(0.3)
	# scene3 : game over
	#if (scene == 3):
		#screen.blit(cong_background, (0, 0))
		#screen.blit(createendpointtext(), text_area)
	pygame.display.update()
