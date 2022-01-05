#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install opencv-python


# In[ ]:





# In[3]:


#importing cv library
import cv2

#defining video capture object
vid = cv2.VideoCapture(0)

while True:
    #capture video frame
    #by frame
    ret, frame = vid.read()
    
    #displaying result frame
    cv2.imshow('frame',frame)
    
    #defining button to quit
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
        
#capturing the obj
vid.release()
#destroying all window
cv2.destroyAllWindows()

