
import os
import glob
import cv2

li = glob.glob('*.png')

start = input("Для старата ведите s: ")
if start == 's':
    print('Будет переделано')
    print(li)

    for i in li:
        image = cv2.imread(f"{i}")
        cv2.imwrite(f"{i.strip('.PNG')}.jpg",image, [int(cv2.IMWRITE_JPEG_QUALITY), 60])
        os.remove(i)
else:
    print("ERROR")

ex = ''

while ex != 'b':
    ex = input("Нажмите b для выхода: ")

