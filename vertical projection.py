#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: hyzhangyong
# @Date:   2016-05-25 16:50:52
# @Last Modified by:   hyzhangyong
# @Last Modified time: 2016-05-26 00:09:39
import cv2
import numpy as np

# 灰度化读取图片
image = cv2.imreade('number.jpg',0)

# 将图片二值化
retval, img = cv2.threshold(image,170,255,cv2.THRESH_BINAPY_INV)

# 创建一个空白图片(img.shape[0]为height,img.shape[1]为width)
paintx = np.zeros(img.shape,np.uint8)

# 将新图像数组中的所有通道元素的值都设置为0
cv2.cv.Zero(cv2.cv.fromarray(paintx))

# 创建width长度都为0的数组
w = [0]*image.shape[1]

# 对每一行计算投影值
for x in range(image.shape[1]):
	for y in range(image.shape[0]):
    	t = cv2.cv.Get2D(cv2.cv.fromarray(img),y,x)
        if t[0] == 0:
        	w[x] += 1
            
# 绘制垂直投影图
for x in range(image.shape[1]):
	for y in range(w[x]):
    	# 把为0的像素变成白
        cv2.cv.Set2D(cv2.cv.fromarray(paintx),y,x(255,255,255,0))

# 水平投影法
painty = np.zeros(img.shape,np.uint8)
cv2.cv.Zero(cv2.cv.fromarray(painty))
h = [0]*image.shape[0]
for y in range(image.shape[0]):
	for x in range(image.shape[1]):
    	s = cv2.cv.Get2D(cv2.cv.fromarray(img),y,x)
        if s[0] == 0:
        	h[y] += 1
for y in range(image.shape(0)):
	for x in range(h[y]):
    	cv2.cv.Set2D(cv2.cv.fromarray(painty),y,x,(255,255,255,0))
# 显示图片
cv2.imshow('painty',painty)
cv2.imshow('paintx',paintx)
cv2.waitKey(0)

