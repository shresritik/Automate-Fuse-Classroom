				Automating Fuse Classroom

Disclaimer:
This program is for educational purpose only.


 It is not meant to harm anyone.

Use case:
If you are bored to the manual process of joining the class through Fuse Classroom or
need for the attendance without being present then this bot can be used. This bot
cannot guarantee the full steps of joining the class like doing regularly.

How to use:
Open main.exe file and leave everything to the bot. 

Note:
1. The button in the Fuse Classroom and Zoom to be clicked should be in full screen 
and visible so that the bot can recognize it.

2. Zoom should not be running in the background, if so disable it.

3. The timing of the process is independent of your device/internet (i.e.The process
can be slow/fast or some steps might not work.

4. After the class for the days is finished it is advised to close the program.

How it works:
1. It opens Fuse Classroom's live class schedule webpage in your default browser and 
waits for 10 seconds irresepctive of the complete loading of the webpage.

2. It checks for the "Join Class" button in the page for 10 times, if found then it is clicked
and displays "Joining Class", else "Join Class Not Found" is displayed and it searches
for the button 10 times. After the 10th time it displays 
"Still Class Not Found, so Waiting for 5 mins" and waits for 5 minutes and again step 2 
is processed.

3. After clicking the Join Class button, it waits for 3 seconds and searches for 
"Switch to Zoom" button and if found it displays "Switching to Zoom" and waits for 
20 seconds, else "Cannot Switch to Zoom" and loops for 5 times until it is found.
  
4. After waiting for 20 seconds, it navigates to the Launch zoom webpage and Zoom is 
automatically opened and waits for 3 seconds. If zoom is not automatically opened within
few minutes then manually launch the zoom in the webpage.

5. If zoom is opened, it searches for continue button in "Meeting is being recorded" 
notification, if the button is not found, it searches it for 8 times else it displays
"Cannot launch recording continue button in zoom".

6. If step 5 is successful, then it waits for 3 seconds and searches for 
"Join with audio" button, if found then it is clicked and displays 
"Joining with Audio of Zoom" else displays "Cannot Joining with Audio of Zoom" and loops
for 5 times.

7. It then waits for 2 seconds and searches for the mute button, if it is visible in the
screen then it is pressed and displays "Mute Button Clicked" and shows the current time
along with "Waiting 1:00 hr for Class to Finish" and waits for 1 hour for class to finish, 
else it displays "Cannot Mute button in Zoom" and loops for 5 times.

8. After 1 hour, it checks for the zoom running in the background process, if it is found
then it displays "Zoom in Background is Found" and shows the current time and displays
"Waiting 30 min more for Class to Finish" and waits 30 minutes and loops step 8 for 2 times, and 
if Zoom is not found then it displays "Zoom in Background is Not Found" and opens the
Fuse Classroom's live schedule webpage in the new tab of the browser and step 1 is repeated.

Note: 
1. During the class time, the system waits according to the time of execution of the code 
not the time of the class. The time of exection is displayed with current time.
2. If the class is 1 hour it skips 30 minutes wait of step 8 else loops 2 times for 
30 minutes unitl zoom is running.

If you have any queries, feel free to contact me.

***************************************************************************************

For python developers

python:3.8.5
pip:21.1.2

Modules used:
pyautogui
time
webbrowser
subprocess

Feel free to modify the program and let me know.

***************************************************************************************






