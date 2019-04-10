# Pyrosim: Objects

## Notes:
* Objects are beholden to the laws of physics, which are applied to the objects automatically by the simulator
* [Link Assignment](https://www.reddit.com/r/ludobots/wiki/pyrosim/objects)

## Instructions
1. Copy empty.py and rename the copied file objects.py. Throughout, we will create copies of our previous work so that if we ever get stuck we can return to a file that we know works.

2. Between lines 10 and 11 of the previous project, add this line:
    `sim.send_cylinder( length=1.0 , radius=0.1 )`

3. When you run objects.py now, you should see a cylinder with a length of 1u and a radius of 0.1u rocket up through the floor during the first few time steps of the simulation. (In this simulation, distances are not in meters or feet, but in arbitrary (u)nits, which we shall simply refer to as u.) Let’s slow things down so we can observe the cylinder in more detail.

4. Modify line 10 from the previous project as follows:

    `sim = pyrosim.Simulator( play_paused = True )`

5. Now when you run the program again, the simulation starts in paused mode. You should see a cylinder partly embedded in the ground (Fig. 2a). Take a screenshot of this (or take a photo using your phone) and save the resulting file.

6. You can unpause the simulation by pressing `Ctrl-p`. You should now see the cylinder rocket up from the floor again.

7. Run the program again, but this time press `Ctrl-o`. This will advance the simulation one time step at a time. This allows you to carefully observe how your simulation behaves.

8. You can also inspect your simulation by moving about in it. You are in fact viewing the simulation through a virtual camera hanging in space. You can manipulate the camera using a mouse or a trackpad. Left-clicking and dragging the mouse changes the direction in which the camera points. Right-clicking and dragging changes the position of the camera. Trying moving the camera to view your cylinder from different angles.

9. Why does the cylinder behave like this? Each object has a default position, which is x = 0, y = 0, and z = 0. This position happens to be in the middle of the floor. One function of a physical simulator is collision detection and collision resolution. At each time step of the simulation, the simulator determines whether any two objects are in contact with one one another. In this case, there are two such objects: the cylinder and the floor. If there is an object pair in contact with one another, the simulator will apply a small force to push them apart so that they do not interpenetrate each other. In this case, the simulation keeps pushing on the cylinder, causing it to fly upward.

10. Let’s set the initial position of the object so that this does not happen. Add the following arguments to line 3:

    `sim.send_cylinder( x=0 , y=0 , z=0.6 , length=1.0 , radius=0.1 )`

11. This should now cause the cylinder to start standing on the ground (Fig. 2b) because we moved the object upward by 0.6u. Notice that the cylinder has two hemispherical caps to it, so we needed to move the object up by one half of its length (0.5u) plus its radius (0.1u). Take a screenshot of this (or take a photo using your phone) and save the resulting file.

12. The coordinate system in this simulator is as follows:

    (a) negative x values place objects to the left;

    (b) positive x values place objects to the right;

    (c) negative y values place objects ‘out’ of the screen;

    (d) positive y values place objects ‘into’ the computer screen;

    (e) negative z values place objects below the ground;

    (f) positive z values place objects above the ground (Fig 1.2c).

13. Explore this coordinate system by changing the object’s initial position and rerunning the simulation. Did the object appear where you thought it would?

14. Let us now place the object at a fair distance above the ground...

    `sim.send_cylinder( x=0 , y=0 , z=1.5 , length=1.0 , radius=0.1 )`

15. And tell the simulation to run for 1000 time steps. (By default, the simulation only runs for 100 time steps):

    `sim = pyrosim.Simulator( play_paused=True , eval_time=1000 )`

16. When you run the program now and unpause it now, you should see the cylinder fall to the ground yet remain upright. (It will take a while for the simulation to end because we extended its running time. You can end it early with command-Q on Macs and closing the window in Linux or Windows). The cylinder does not fall over because, unlike the real world, there are no small random forces acting on the object like wind or a slightly uneven floor.

17. Let us add a second object to our simulator. Before we do however, reset the position of the first object so that it starts on the ground (z = 0.6). We are also going to 'capture' the ID number generated for this object into the variable whiteObject. Whenever an object is created in Pyrosim, a new ID number is assigned to it. You can store this ID number in a variable for later use. (We will see how these ID numbers are used in the next assignment.)

    `whiteObject = sim.send_cylinder( x=0 , ...)`

    a. You can see the ID number by adding this line
    `print(whiteObject)`

    b. right after capturing the ID number in this variable. Go ahead and do so. When you run your code now, you should see 0 printed the screen.

    c. Go ahead and remove line 23c now.

18. Now we can add a second object to the simulation after adding the first one...
    `whiteObject = sim.send_cylinder( x=0 , ...)`

    `redObject = sim.send_cylinder( x=-0.2 , y=0 , z=0.6 )`

19. ...but we will put it just to the left of the first one (x = −0.2) and capture its ID number. (This object is not yet red, but we will make it so shortly.)

    a. print the value of *redObject* and run your code to validate that this object has been assigned an ID number of 1.

    b. Delete this print statement from your code.

20. Let us also change the color of the second object, so that we can distinguish between them. This requires adding another three arguments: the (r)ed, (g)reen, and (b)lue components of the object’s color:

    `redObject = sim.send_cylinder( ... r=1, g=0, b=0)`

21. When you run your program now, you should see two objects next to one another (Fig. 2d). Take a screenshot of this (or take a photo using your phone) and save the resulting file.

22. In addition to setting an object’s shape and position, we can also set its initial orientation. That is, in the case of a cylinder, what direction the cylinder ‘points’ in when the simulation starts. We do this by dictating a three-dimensional vector—the rotational vector—along which the cylinder’s long axis will initially lie.

23. Let’s get the second cylinder to point into the screen by setting this rotation vector to x = r1 = 0, y = r2 = 1, z = r3 = 0. (To understand why this causes the cylinder to point into the screen, refer to Fig. 2b.) We do this by adding three more arguments:

    `sim.send_cylinder( ... r1=0 , r2=1, r3=0 ... )`

24. Your simulation should now look like Fig. 2e. Take a screenshot of this (or take a photo using your phone) and save the resulting file.

25. Let us now move the red cylinder so that its back end intersects with the top end of the white cylinder as shown in Fig. 2f. Before we do so however, let us draw the two cylinders in 3D as shown in Fig. 3. Re-draw this figure on a piece of paper or in a drawing program (such as Google Draw) so that you can easily add and remove information from it as you go (hint: use a pencil). What should the new coordinates of the second object’s position be so that you get Fig. 2f? Type those coordinates into your program and run it. If you got the position wrong, try again until your simulation matches Fig. 2f. Take a screenshot of this (or take a photo using your phone) and save the resulting file.

26. Make sure to keep the drawing you made for the next project because you will be annotating it.
