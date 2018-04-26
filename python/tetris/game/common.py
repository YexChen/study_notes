# -*- coding : utf-8 -*-
#这个文件用来存放共有变量,和变量对应的方法(多文件真是个大坑啊)

#这里是注册方法,如果需求跨界面运行进程的话,需要使用更高级的监听者模式
loopfns = []
def registFn(fn):
	loopfns.append(fn)

def flushFn():
	loopfns = []

#eventloop 这是注册事件的循环,把fn传入里面即可
eventloopfns = []
def registeventFn(fn):
	eventloopfns.append(fn)

def flusheventFn():
	eventloopfns = []
