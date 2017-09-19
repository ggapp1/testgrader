import cv2
import numpy as np
import matplotlib.pyplot as plt

def getOption(x):
	if x in range(50,60) or x in range(380,390):
		return 'A'
	if x in range(95,105) or x in range(425,435):
		return 'B'
	if x in range(140,150) or x in range(470,480):
		return 'C'
	if x in range(185,190) or x in range(515,525):
		return 'D'
	if x in range(230,245) or x in range(560,570):
		return 'E'
	

def getAnswer(x,y):
#	print x
	#line 1
	if y in range(3,13):
		if x > 300:
			return 16
		else:
			return 1
			
	#line 2
	if y in range(25,35):
		if x > 300:
			return 17
		else:
			return 2
			
	#line 3
	if y in range(47,57):
		if x > 300:
			return 18
		else:
			return 3
	#line 4
	if y in range(67,77):
		if x > 300:
			return 19
		else:
			return 4
	#line 5
	if y in range(93,103):
		if x > 300:
			return 20
			
		else:
			return 5
	#line 6
	if y in range(115,125):
		if x > 300:
			return 21
		else:
			return 6
	#line 7
	if y in range(138,148):
		if x > 300:
			return 22
		else:
			return 7
	#line 8
	if y in range(160,170):
		if x > 300:
			return 23
			
		else:
			return 8
	#line 9
	if y in range(185,195):
		if x > 300:
			return 24
		else:
			return 9
			
	#line 10
	if y in range(207,217):
		if x > 300:
			return 25
		else:
			return 10
	#line 11
	if y in range(228,238):
		if x > 300:
			return 26
		else:
			return 11
	#line 12
	if y in range(252,262):
		if x > 300:
			return 27
		else:
			return 12
	#line 13
	if y in range(275,285):
		if x > 300:
			return 28
		else:
			return 13
	#line 14
	if y in range(300,310):
		if x > 300:
			return 29
		else:
			return 14
	#line 15
	if y in range(320,330):	
		if x > 300:
			return 30
		else:
			return 15


image = cv2.imread('dados/pattern_0001_scan.png');
image = cv2.resize(image,(960,1080))
image = image[330:680,193:804]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 75, 200)

thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

cnts = cnts[1]
questionCnts = []
i = 0
lista = [': Branco'] * 31

for c in cnts:
	x,y,w,h = cv2.boundingRect(c)
	ar = w / float(h)
	mask = np.zeros(thresh.shape, dtype="uint8")
	cv2.drawContours(mask, [c], -1, 255, -1)

	mask = cv2.bitwise_and(thresh, thresh, mask=mask)
	total = cv2.countNonZero(mask)

	if w >= 10 and h >= 10 and ar >= 1.5 and ar <= 10.1:
		if total > 270:
			if(lista[getAnswer(x,y)] == ': Branco'):
				lista[getAnswer(x,y)] = ': ' + getOption(x)
			else:
				lista[getAnswer(x,y)] = ': Nulo'
			cv2.drawContours(image, [c], -1, 255, -1)


for i in range(31):
	print str(i) + " " + lista[i]
plt.imshow(image)
plt.show()
	