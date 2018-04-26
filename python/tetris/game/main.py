#-*- coding : utf-8 -*-
# 进程控制文件:
# 职责:
# 1.控制各个界面的执行状况,收到各种界面的切换请求,并移交相应界面进行处理(类)
# 2.收取game.py文件的指令,运行游戏

#引入各种库
from surface import *
import body
import config
import sound
import util
import pygame
import common
from pygame.locals import *


#主入口文件
def run():
	pygame.init()
	#这里应该添加初始化文件,初始化相关绑定要素
	screen = pygame.display.set_mode((1024,768))
	Surface(screen)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
			#事件循环轮询
			print (common.eventloopfns)
			for fn in common.eventloopfns:
				fn()
		#公有函数轮询
		for fn in common.loopfns:
			fn()
		pygame.display.update()

#loop里面是一个主函数,里面的代码在主循环中运行
#如果进程返回False的话,就清除函数
def loop():
	for fn in common.loopfns:
		fn()
#eventloop 用来查询事件
def eventloop():
	for fn in common.eventloopfns:
		fn()
