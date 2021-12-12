import cv2
import numpy as np
import xlrd
from matplotlib import pyplot as plt

workbook = xlrd.open_workbook(r'E:\H.xlsx')
tablica = workbook.sheet_by_index(0)

kap = cv2.imread(r'E:\kap100.jpg')
kap_gray = cv2.cvtColor(kap, cv2.COLOR_BGR2GRAY)
kap_smooth = cv2.GaussianBlur(kap_gray, (3, 3), 2, 2)

kap_canny = cv2.Canny(kap_smooth, 128, 255)
kap_canny = cv2.dilate(kap_canny, None, iterations=1)
kap_canny = cv2.erode(kap_canny, None, iterations=1)

contours = cv2.findContours(kap_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[1]

c = max(contours, key = cv2.contourArea)
trazenaKontura = np.zeros(kap_canny.shape, np.uint8)

height, width = trazenaKontura.shape[:2]

extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])

cv2.drawContours(trazenaKontura, [c], -1, 255, -1)

pxPromjer_De = extRight[0] - extLeft[0]

red_Ds = extTop[1] + pxPromjer_De
red_igle = extTop[1] + 2*pxPromjer_De

brBijelih = 0
x1 = 0
x2 = 0
a1 = 0
a2 = 0

for i in range(width):
    if trazenaKontura[red_Ds][i] == 255 and brBijelih == 0:
        brBijelih = 1
        x1 = i
    elif trazenaKontura[red_Ds][i] == 255:
        x2 = i

pxPromjer_Ds = x2 - x1

brBijelih2 = 0

for i in range(width):
    if trazenaKontura[red_igle][i] == 255 and brBijelih2 == 0:
        brBijelih2 = 1
        a1 = i
    elif trazenaKontura[red_igle][i] == 255:
        a2 = i


sirina_kapilare = a2 - a1
   
mjerilo = 0.133/sirina_kapilare #pretpostavka da je sirina kapilare 0.133 cm , [cm/px]
promjer_De = pxPromjer_De*mjerilo
promjer_Ds = pxPromjer_Ds*mjerilo
g = 980.4

delta_gustoca = 0.9882-0.655 #pretpostavljena gustoće vode 0.9882 g/cm3, heksana 0.655 gm/cm3
omjerS = promjer_Ds/promjer_De
omjerS3 = round(omjerS, 3)

H = 0

for i in range(tablica.nrows):
     if omjerS3 == tablica.cell_value(i,0):
         H = tablica.cell_value(i, 1)

medjuPovrsinska_napetost = g*delta_gustoca*promjer_De**2*H
medjuPovrsinska_napetost_mNm = medjuPovrsinska_napetost*1000

cv2.circle(trazenaKontura, extLeft, 3, (0, 255, 0), -1)
cv2.circle(trazenaKontura, extRight, 3, (0, 255, 0), -1)
cv2.circle(trazenaKontura, extTop, 3, (0, 255, 0), -1)

print('delta_gustoca' ,delta_gustoca)
print('red_Ds', red_Ds)
print('red_igle', red_igle)
print('extLeft', extLeft)
print('extTop', extTop[1])
print('extRight', extRight)
print('a2', a2)
print('a1', a1)
print('x1', x1)
print('x2', x2)
print('pxPromjer_Ds', pxPromjer_Ds)
print('pxPromjer_De', pxPromjer_De)
print('omjer ds/de', omjerS3)
print('promjer_De', promjer_De)
print('promjer_De', promjer_De)
print('promjer_Ds', promjer_Ds)
print('H', H)
print('medjuPovrsinska_napetost mN/m', medjuPovrsinska_napetost)
cv2.imwrite(r'E:\kapfinal.jpg', trazenaKontura)
cv2.imwrite(r'E:\kapy.jpg', kap_canny)
plt.imshow(trazenaKontura, interpolation = 'bicubic')
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
	    
    


