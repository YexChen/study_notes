#-*- coding : utf-8 -*-
import common
def run(screen):
	return  Surface(screen)

class Surface(object):
	def __init__(self,screen):
		self.screen = screen
		self.intializeGraphic()
		self.bindEvent(1,2,3,4,5)
	def intializeGraphic(self):
		self.renderBackground()
		self.renderTopic()
		self.renderStartBtn()
		self.renderConfigBtn()
	def bindEvent(self,sx,sy,ex,ey,fn):
		def returnFn():
			print("loop fn running!")
			if(event.type == MOUSEBUTTONDOWN):
				print("get mouse down!")
		common.registeventFn(returnFn)
	#接下来是一些UI细节函数			
	def renderBackground(self):
		pass
	def renderTopic(self):
		pass
	def renderStartBtn(self):
		pass
	def renderConfigBtn(self):
		pass

