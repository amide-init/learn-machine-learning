#Load image in opencv


#import numpy as np
#import cv2
#from matplotlib import pyplot as plt
#
#img = cv2.imread('elon.jpg')
#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAWllindows()


#load video in opencv

#import numpy as np
#import cv2
#
#cap = cv2.VideoCapture(0)
#while (True):
#    ret, frame = cap.read()
#    cv2.putText(frame, 'Amin Uddin', (20, 140),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#    cv2.imshow('frame', frame)
#    
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
#cap.release()
#cap.destroyAllWindows()


#line draw on image

#import numpy as np
#import cv2
#from matplotlib import pyplot as plt
#
#img = cv2.imread('elon.jpg')
#cv2.line(img, (0,0), (150, 150), (255, 0, 255), 15)
#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAWllindows()



#draw a rectnagle on  image

#import numpy as np
#import cv2
#from matplotlib import pyplot as plt
#
#img = cv2.imread('elon.jpg')
#cv2.rectangle(img, (10, 25), (200, 150), (0, 255, 0), 10)
#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#cirlce on image

#import numpy as np
#import cv2
#from matplotlib import pyplot as plt
#
#img = cv2.imread('elon.jpg')
#cv2.circle(img, (100, 65), 55, (0, 0, 255), -1)
#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#FONT ON IMAGE
#import numpy as np
#import cv2
#from matplotlib import pyplot as plt
#
#img = cv2.imread('elon.jpg')
#cv2.putText(img, 'Elon Here', (20, 140),cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 155, 140), 2)
#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()



#image operation
import numpy as np
import cv2

img  = cv2.imread('alia.jpg')

img[206:236, 224:313] = [255,255,255]
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()














