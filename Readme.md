
# Virtual Mouse with gesture control

The project is about controlling cursor movement and actions using gestures. We have used computer vision in this project where the camera would detect the object(s) (finger gloves) and perform operations accordingly. If there are two objects detected then it will control the movement of cursor and if there is one object, it will execute clicking and dragging operations.
Libraries used :
* OpenCV-Python	
* Numpy
* WxPython
* Pynput



## Steps followed

- Color Detection
![Color Detection](Outputs/Color Detection.png)

- Mask filtering
![Filtering Mask](Outputs/Filtering Mask.png)

- Object Tracking
![Object Tracking](Outputs/Object Tracking.png)

- Creating pointer to control cursor
![Pointer Creation](Outputs/Pointer Creation.png)

- Creating boundary to represent screen
![Boundary Screen](Outputs/Boundary Screen.png)

- Moving the cursor (Open gesture)
![Open Gesture](Outputs/Open Gesture.png)

- Preforming click and dragging (Close gesture)
![Close Gesture](Outputs/Close Gesture.png)
![Dragging Operation](Outputs/Dragging Operation.png)

- Fine Tuning
    1) Position Flickering
    2) Coontinuous clicking
    3) Clicking when single object detected

  
