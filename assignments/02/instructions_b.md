# Pyrosim: Joints.
## Notes:
* In this project you will add a joint to the simulation. Joints, like your knees or elbows, connect parts of the robot’s body together and allow them to rotate relative to one another.
* [Link Assignment](https://www.reddit.com/r/ludobots/wiki/pyrosim/joints)

## Instructions
1. Start by making a copy of objects.py and naming the copy joints.py.

2. Run joints.py and unpause it using Ctrl-P. You should see the red object fall to the ground as in Fig. 1a, because the two objects are not attached together.

3. Capture a screenshot like Fig. 1a and save it for submission later.

4. We are now ready to connect these two objects by placing a line just after the creation ofthe two objects:

    `whiteObject = ...`

    `redObject = ...`

    `joint = sim.send_hinge_joint( first_body_id = whiteObject , second_body_id = redObject )`

5. This creates a joint that connects the two cylinders together.

6. When you run joints.py now and unpause it, you should see that the two objects are connected:the robot ‘falls’ forward as shown in Fig. 1b.

7. Capture a screenshot like Fig. 1b and save it for submission later.

8. We need to specify some more parameters of the joint however to get the two objects to rotate relative to another, like your knee allows your lower leg to rotate relative to your upper leg.

9. To begin, we need to determine where this joint should be placed: this position is known as the joint’s anchor. We will put it at the place where the two objects intersect, as shown by the blue dots in Fig. 2. Add this dot to your drawing from the last project.

10. Calculate what the position of this joint should be by replacing the question marks in Fig.2a with the correct position on your drawing.

11. Now add these arguments to Send Joint to specify where the joint should be positioned:

    `sim.send_hinge_joint( ... x=..., y=..., z=...)`

12. When you run the program now, you should see no change. This is because we still need to specify the joint’s axis: the axis dictates the plane through which the two objects will rotate relative to one another. Consult Fig. 2b, and imagine the red cylinder rotating downward about the joint’s anchor until it hits the white cylinder. As you can see, this would cause the red cylinder to rotate through the plane defined by the y and z axes in Fig.2b. This is the plane through which we want the objects to rotate relative to one another.

13. Imagine sticking a vector through this plane such that the vector is normal to the plane:this vector is the joint’s axis. Since we want the objects to rotate through the yz plane,one such vector is the x = −1, y = 0, z = 0 vector shown in Fig. 2c. Add this normal to the joint with the three additional parameters n1 = x, n2 = y, and n3 = z ('n' stands for(n)ormal):

    `sim.send_hinge_joint( ... n1 = -1 , n2 = 0 , n3 = 0 )`

14. When you run your code now, you should see the red cylinder rotate down toward the whitecylinder as in Fig. 1c. (The magnitude of a joint axis does not matter, so n1 = −100, n2 = 0,n3 = 0 and n1 = +1, n2 = 0, n3 = 0 would also work fine.)

15. Hint: It may be difficult to see this rotation when you unpause your simulation because it runs so quickly. To slow down your simulation during debugging, you can run your code and then hit ctrl-o to step the simulation forward [o]ne small increment at a time. By repeatedly hitting ctrl-o you can slowly step through your simulation.

16. Capture a screenshot of your simulation toward its end, when the two cylinders have visibly rotated toward one another. In other words, the angle between them is less then 90 degrees.Save the image for submission later.

17. We are now going to modify our robot a bit to help you become more comfortable with setting joint normals. We will start by temporarily removing the joint.

18. You can always remove components from a simulation simply by commenting out the line corresponding to that component. For example, comment out the joint by placing the pound sign in front of it:

    `# joint = ...`

19. Rerun your code. You should now see the red cylinder fall as in Fig. 1a, because no joint is sent to the simulator.

20. Change the position and rotation of the red cylinder so that it points to the right, as in Fig. 1d.

30. Hint: In addition to modifying the red cylinder's position, you will also have to modify its orientation by modifying its r1, r2, and/or r3 arguments.

31. Capture a screenshot of this and save it for submission later.

32. Now uncomment the joint and rerun your program. The two objects should act as if they are welded together and fall together to the right, because although the joint’s anchor is still in the right position, its normal (made up of n1, n2, and n3) is now incorrect. (See Fig. 1e).

33. Capture a screenshot of this robot and save it for later submission.

34. We want the red object to rotate relative to the white object through the xz plane. This is the plane that is parallel to your computer screen, and the one shown in Fig. 2a. We need to now select a vector that is normal to the xz plane. What might such a vector be? It should be a vector that points ‘toward’ you out of the screen, or away from you into the screen. Take one of these joint normals and change n1, n2 and/or n3 accordingly in your code.

35. When you run your code now, you should see the red cylinder rotate clockwise and downward toward the white object, through the xz plane, as in Fig. 1f.

36. Capture a screenshot of this robot and save it for later submission.

37. Now, revert the joint and red cylinder back to just before step 20 so that the red cylinderagain points ‘into the screen’ and rotates through the yz plane.

38. We are going to make one last change to the joint: its range of motion. The default range of motion for a joint is to rotate inward by π/4 radians or outward by π/4 radians. These are known as the joint’s low and high stops, respectively (the low stop should always be more negative than the high stop). Let us expand the joint’s range of motion by changing the low and high stops to −π/2 and +π/2 radians respectively:

    `sim.send_hinge_joint( ... lo=-3.14159/2 , hi=3.14159/2 )`

39. The red cylinder should now rotate almost all the way to the white cylinder, but is stopped just short by the forward rotation of the whole robot, as shown in Fig. 1g. In some cases it may rotate always toward and in to the white object, causing both to fall forward. This is fine too.
