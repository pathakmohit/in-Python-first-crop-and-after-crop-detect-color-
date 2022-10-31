# this loops to exit use "ESC"buttons 
from platform import node
from unicodedata import name
import cv2
import pandas as pd 
import numpy as nd
from PIL import ImageFilter
from soupsieve import select



img_path = r'Test2.jpg'
img =cv2.imread(img_path)
rows,cos,_=img.shape
print("Rows",rows)
print("Cols",cos)
cut_image = img[300:440,197:1050]
clicked = False
r = g = b = x_pos = y_pos = 0
index = ["colors", "color_name", "hex","R", "G" , "B"]
csv = pd.read_csv('colors.csv',names=index , header = None)



def get_clor_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
         d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
         if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

def draw_function(cut, x, y, flags, param):
      if cut == cv2.EVENT_LBUTTONDBLCLK:
          global r,g,b,x_pos,y_pos,clicked
          clicked = True
          x_pos = x
          y_pos = y
          b, g, r = img[y, x]
          b = int(b)
          g = int(g)
          r = int(r)
          
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)
cv2.imshow("image",img)


while True:
        cv2.imshow("image", cut_image)
        if clicked:

          cv2.rectangle(cut_image, (20, 20), (750, 60), (b, g, r), -1)
          text = get_clor_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
          cv2.putText(cut_image, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
          if r + g + b >= 600:
                cv2.putText(cut_image, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False
        if cv2.waitKey(20) & 0xFF == 27:
            break

cv2.destroyAllWindows()

    
