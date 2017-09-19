import cv2
import numpy as np
import matplotlib.pyplot as plt

def getAnswer(x,y):
#	print x
	#line 1
	if y in range(3,13):
		if x > 300:
			print 16
		else:
			print 1
	#line 2
	if y in range(25,35):
		if x > 300:
			print 17
		else:
			print 2
	#line 3
	if y in range(47,57):
		if x > 300:
			print 18
		else:
			print 3
	#line 4
	if y in range(67,77):
		if x > 300:
			print 19
		else:
			print 4
	#line 5
	if y in range(93,103):
		if x > 300:
			print 20
		else:
			print 5
	#line 6
	if y in range(115,125):
		if x > 300:
			print 21
		else:
			print 6
	#line 7
	if y in range(138,148):
		if x > 300:
			print 22
		else:
			print 7
	#line 8
	if y in range(160,170):
		if x > 300:
			print 23
		else:
			print 8
	#line 9
	if y in range(185,195):
		if x > 300:
			print 24
		else:
			print 9
	#line 10
	if y in range(207,217):
		if x > 300:
			print 25
		else:
			print 10
	#line 11
	if y in range(228,238):
		if x > 300:
			print 26
		else:
			print 11
	#line 12
	if y in range(252,262):
		if x > 300:
			print 27
		else:
			print 12
	#line 13
	if y in range(275,285):
		if x > 300:
			print 28
		else:
			print 13
	#line 14
	if y in range(300,310):
		if x > 300:
			print 29
		else:
			print 14
	#line 15
	if y in range(320,330):	
		if x > 300:
			print 30
		else:
			print 15































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
lista = []
print cnts
for c in cnts:
	x,y,w,h = cv2.boundingRect(c)
	ar = w / float(h)
	mask = np.zeros(thresh.shape, dtype="uint8")
	cv2.drawContours(mask, [c], -1, 255, -1)

	mask = cv2.bitwise_and(thresh, thresh, mask=mask)
	total = cv2.countNonZero(mask)

	if w >= 10 and h >= 10 and ar >= 1.5 and ar <= 10.1:
		if total > 270:
			#print total, x,y
			lista.append(y)
			getAnswer(x,y)
			cv2.drawContours(image, [c], -1, 255, -1)

lista.sort()
#print lista
plt.imshow(image)
plt.show()
	