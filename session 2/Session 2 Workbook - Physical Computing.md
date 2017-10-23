# Session 2 Workbook - Physical Computing

<p align="center">
    <img src="images/ICAHLOGO.png" alt="ICAHLOGO" width="300">
</p>

# How to use this workbook & teams formation

Welcome back to the third session of the Physical Computing theme!

This week, the focus moves firmly to working in teams of 3 to 4 and doing exercises in your workbook together. All exercises happen on the actual Raspberry Pis, so unless you have the means to connect the Pis up to a screen, keyboard and mouse at home, there won't be any homework.

Having formed teams, let's jump right in at the deep end!

# May we introduce...

So we've been busy this last week to assemble you a little vehicle. May we introduce the **ICAH-101 bot**. It is very heavily based on Imperial College Robotics Society's [Robotics 101 course](http://101.icrs.io/), which you should definitely read up on here if you want to find out more about how it all works "under the bonnet".

<p align="center">
    <img src="images/bot.png" alt="ICAH-101 bot" width="800">
    <figcaption align="center">The ICAH-101 bot</figcaption>
</p>

For the rest of this theme, you will be working with this robot.

It has the following capabilities:

* **Driving around!** The two wheels on either side can be independently controlled, so you can make it go forward, backward and steer left or right, with either just one wheel spinning, or both spinning in opposite direction.

* **Blinking an LED!** (Yay...) This is a good way to check the functioning of the GPIO pins in general. We'll get to that in the first exercise.

* **Detecting a forward-facing distance.** This uses the HC-SR04 ultrasound sensor we met in the last session. Note that it detects a distance straight ahead of the robot.

* **Detecting brightness changes in the floor surface**, using 2 TCRT5000 **line sensors**. Why are they called line sensors? Because a natural application for reading brightness changes is to follow a black line on bright ground.

We won't be focussed on the electronic setup of the robot in this session, but if you want to find out more about how we actually control the motors, do have a look at the [explanation in the 101 course](http://101.icrs.io/lesson-2) ("Motor Driver").

# Exercises

1. <p align="center"><img src="images/led.png" alt="LED layout" width="800"><figcaption align="center">The LED connection on the robot</figcaption></p> Have a look at your robot and [the Raspberry Pi pin layout](http://gpiozero.readthedocs.io/en/stable/_images/pin_layout.svg) (the bottom is where the USB ports are, and it is also on your desktop background). Find out which pin the LED is connected to and get it to blink. If you're stuck, look back at the first session's workbook!

2. Driving the robot around.
 gpiozero makes it very easy to drive the robot around. (Remember the reason from last session why we use software libraries in the first place!) Look at the below sample code:
   
   ```python
   from gpiozero import Robot
   
   leftPins = (21, 16)
   rightPins = (12, 1)
   
   my_robot = Robot(left=leftPins, right=rightPins)
   
   # move around
   my_robot.forward()
   sleep(2)
   my_robot.backward()
   sleep(2)
   my_robot.left()
   sleep(1)
   my_robot.forward()
   sleep(2)
   my_robot.right()
   sleep(1)
   my_robot.backward()
   ```

   The above creates an instance of gpiozero's `Robot` object, called `my_robot`. As we create it, we tell it the correct GPIO pins for controlling the left and the right motor.

   Armed with this knowledge, `my_robot` knows exactly what signals to put out onto the pins if it is asked to move the robot forward, backward, left or right. The great thing is that we can leave the nitty-gritty of _how_ to move in either direction to the internal workings of the gpiozero library. It just presents us with handy shortcut commands called left(), right(), forward() and backward().

   To do a motion at less than full speed, you can give it a speed parameter. For example `my_robot.forward(0.5)` moves the robot forward at half of the full speed.

   You can find all the commands that you can send to the Robot object [here](http://gpiozero.readthedocs.io/en/stable/api_boards.html?highlight=robot#robot). Note that there is a handy `stop()` function that saves you from writing things like `my_robot.forward(0)`.

3. Moving out of the way when there is an obstacle in front of the robot.
 In this exercise, we stop the robot when there is an obstacle in front of it, using the ultrasonic distance sensor. Optionally, you can set it on a new course until it detects another obstacle, thus going on until its battery is depleted.

   Remember [the distance sensing code from last time](https://github.com/till-h/ICAHHorizons_Y2PhysComp/blob/master/session%201/Session%201%20Workbook%20-%20Physical%20Computing.md#using-an-ultrasonic-distance-sensor)? You will first need to wire up the sensor, including the voltage divider, as per the last session's instructions. We will once more give you a "large" and a "small" resistor to build the voltage divider.  
   We have a bigger breadboard this time to set things up on, and the front part of it is left empty for you to set up the wires for the distance sensor.

   You will be using the pins <TODO> for the Trig signal, and <TODO> for the Echo signal. A sample flowchart for the robot control is shown below - but do try out your own ideas!

   <p align="center">
      <img src="images/obstacle_flowchart.png" alt="Obstacle avoidance" width="600">
      <figcaption align="center">A possible way to deal with obstacles.</figcaption>
   </p>

4. Stopping the robot when it crosses a black line.
 <p align="center"><img src="images/TCRT5000.jpg" alt="The TCRT5000 line sensor module" width="300"><figcaption align="center">The TCRT5000 line sensor module</figcaption></p>
 Instead of the ultrasonic sensor, you can use what's called a line sensor to detect an abrupt change in brightness of the ground. If we use this together with a black marker tape stuck onto a white paper, or similar, it is the perfect way to detect markings on the ground. Let's use it to stop if our robot crosses a black line! 
 In order to use the line sensor, you need to import the `LineSensor` object from gpiozero.

   ```python
   from gpiozero import LineSensor
   
   sensor = LineSensor(21) # if we connect the sensor's data pin to GPIO pin 21
   
   while True:
   	 if sensor.pin.state:
   	 	 print("No line detected.")
   	 else:
   	     print("Line detected.")
   ```

   Physically, you connect it up as follows:

   * Connect the sensor's VCC to a 3V3 pin on the Pi.
   * Connect the sensor's GND to a Ground pin on the Pi.
   * Connect the sensor's OUT to a free GPIO pin on the Pi.

   Again, feel free to change this to a more interesting behaviour, if you have time.

5. Driving the robot around in a black square.
Finally, you can use the previous exercise to drive the robot around within a box. Can you make it go as closely as possible around the inside of the perimeter? I.e., constantly keep probing to one side?