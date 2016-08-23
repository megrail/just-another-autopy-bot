#!/usr/bin/python
# -*- coding: utf-8 -*-

import autopy
import time
import random
import math
import numpy as np
from scipy.special import binom
import glob




def move_mouse_randomly(xf, yf):
    def Bernstein(n, k):
        """Bernstein polynomial.

        """
        coeff = binom(n, k)

        def _bpoly(x):
            return coeff * x ** k * (1 - x) ** (n - k)

        return _bpoly

    def Bezier(points, num=200):
        """Build Bézier curve from points.

        """
        N = len(points)
        t = np.linspace(0, 1, num=num)
        curve = np.zeros((num, 2))
        for ii in range(N):
            curve += np.outer(Bernstein(N - 1, ii)(t), points[ii])
        return curve

    pos = autopy.mouse.get_pos()
    pos_list = []
    pos_list.append(pos)
    num = int(max(math.fabs(pos[0]-xf), math.fabs(pos[1]-yf)))

    N = random.randint(1 , 3)
    for i in xrange(N):
        x = int(random.uniform(pos[0], xf))
        y = int(random.uniform(pos[1], yf))
        pos_list.append([x, y])
    pos_list.append([xf, yf])
    l = Bezier(pos_list, num).T

    z = zip(l[0], l[1])
    for x, y in zip(l[0], l[1]):
  #      print(x, y)
        autopy.mouse.move(int(x), int(y))
        time.sleep(random.uniform(0.0002, 0.001))

def find_possition_bitmap_screenshot(bmp):

 #   screenshot = autopy.bitmap.Bitmap.open('screen.png')
    pos = screenshot.find_bitmap(bmp)
    return pos

def click_mouse_randomly(pos, bmp):
    pos1 = []
    pos1.append(int(random.uniform(pos[0] + 1,  pos[0] + bmp.width - 5)))
    pos1.append(int(random.uniform(pos[1] + 1,  pos[1] + bmp.height - 6)))
    move_mouse_randomly(*pos1)
    autopy.mouse.toggle(True)
    time.sleep(random.uniform(0.2, 0.5))
    autopy.mouse.toggle(False)




if __name__ == '__main__':

    bmp_path_list = glob.glob('*.png')
#    screen_list = glob.glob('tmp/*.png')

#    print screen_list
#    bmps = [ autopy.bitmap.Bitmap.open(x) for x in bmp_path_list ]
 #   screens = [autopy.bitmap.Bitmap.open(x) for x in screen_list]
 #   bmps = [autopy.bitmap.Bitmap.open('1hour.png')]
   #  move_mouse_randomly(0, 400)
  #  find_bitmap_screenshot()

    # for screen in screens:
    #     for bmp in bmps:
    #         pos = screen.find_bitmap(bmp, 0.6)
    #         print pos
    while 1:
        screenshot = autopy.bitmap.capture_screen()
  #      screenshot.save('tmp/'+ str(time.clock()) + '.png')
        for path in bmp_path_list:
            bmp = autopy.bitmap.Bitmap.open(path)
            pos = screenshot.find_bitmap(bmp, 0.6)
      #      print(pos)
            if pos:
                print(pos, path)
                click_mouse_randomly(pos, bmp)
                move_mouse_randomly(1,1)
                time.sleep(random.uniform(5, 200))
        time.sleep(random.uniform(10, 20))
