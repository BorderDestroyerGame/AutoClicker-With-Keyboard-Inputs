# Autoclicker With Keyboard Inputs
This is an autoclicker program that has built in functionality for keyboard inputs. The `KeyCodes.py` file was taken from [DougDoug's Twitch Plays](https://github.com/DougDougGithub/TwitchPlays) code. 

All of the rest of the code was written by Nathaniel (BorderDestroyer) Davies.



Feel free to use the code and alter it however you want! If you do, credit would be nice and appreciated!

## Setup
1) This program uses Python 3.10.11, so if you don't have that installed, you can find it here! (https://www.python.org/downloads/release/python-31011/)

2) Run `python -m pip install -r requirements.txt` in the project folder to install all packages needed.

## Running The Application
1) Change the main variables to what you desire (found starting at `line 8`)
   - `SETUP_TIME` Is how long until the autoclicker begins after starting the program
   - `PRESS_TIME` Is how long to wait in between inputs (in milliseconds)
   - `PRESS_AMOUNT` Is how many times you want the specified input to happen

2) Set the specified input you want to be repeated (`line 32/33`). The following methods are how you do so:
   - `HoldAndReleaseKey(button, duration)` Is what allows for keyboard inputs, with button being one of the variables found in 'KeyCodes.py' and duration being how long until the keyboard input is released
   - `pydirectinput.mouseDown(button, duration)` Is what allows for mouse button inputs, with button being what mouse button you want pressed (defaults to left click) and duration being how long until the mouse button is released

**NOTE: Autoclickers can be messy, if for some reaon the code will not stop running and you can't manually close it there is a failsafe written into the code! If this happens, just press the F8 key on your keyboard and it will automatically close the code for you! This key can be changed in `main.py` at `line 17`!**
