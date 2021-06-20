
# Virtual Mouse with gesture control

The project is about controlling cursor movement and actions using gestures. We have used computer vision in this project where the camera would detect the object(s) (finger gloves) and perform operations accordingly. If there are two objects detected then it will control the movement of cursor and if there is one object, it will execute clicking and dragging operations.
Libraries used :
* OpenCV-Python	
* Numpy
* WxPython
* Pynput



## Steps followed

- Color Detection<br><br>
![Color Detection](https://github.com/DV821/Virtual-Mouse-with-Object-Tracking/blob/main/Outputs/Color%20Detection.png)

- Mask filtering<br><br>
![Filtering Mask](https://github.com/DV821/Virtual-Mouse-with-Object-Tracking/blob/main/Outputs/Filtering%20Mask.png)

- Object Tracking<br><br>
![Object Tracking](https://github.com/DV821/Virtual-Mouse-with-Object-Tracking/blob/main/Outputs/Object%20Tracking.png)

- Creating pointer to control cursor <br><br>
![Pointer Creation](https://github.com/DV821/Virtual-Mouse-with-Object-Tracking/blob/main/Outputs/Pointer%20Creation.png)

- Creating boundary to represent screen<br><br>
![Boundary Screen](https://github.com/DV821/Virtual-Mouse-with-Object-Tracking/blob/main/Outputs/Boundary%20Screen.png)

- Moving the cursor (Open gesture)<br><br>
![Open Gesture](https://github.com/DV821/Virtual-Mouse-with-Object-Tracking/blob/main/Outputs/Open%20Gesture.png)

- Preforming click and dragging (Close gesture)<br><br>
![Close Gesture](https://github.com/DV821/Virtual-Mouse-with-Object-Tracking/blob/main/Outputs/Close%20Gesture.png)<br><br>
![Dragging Operation](https://github.com/DV821/Virtual-Mouse-with-Object-Tracking/blob/main/Outputs/Dragging%20Operation.png)

- Fine Tuning
    1) Position Flickering
    2) Coontinuous clicking
    3) Clicking when single object detected

  
