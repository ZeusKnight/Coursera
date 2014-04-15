# template for "Stopwatch: The Game"
import simplegui
# define global variables
message = "Python is Fun!"
position = [130, 275]
width = 500
height = 500
interval = 100
decisecond = 0
start = False
attempt = 0
success = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(decisecond):
    A = str(int(round(decisecond / 600)))
    D = str(decisecond % 10)
    BC = str(((decisecond - int(D)) / 10) % 60)
    if len(BC) < 2:
        BC = "0" + BC
    
    return A + ":" + BC + "." + D 
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global start
    start = True
    
def stop_handler():
    global start, attempt, success
    if start:
        attempt = attempt + 1
        if decisecond % 10 == 0:
            success = success + 1
        start = False
    
def reset_handler():
    global start, decisecond, attempt, success
    start = False
    decisecond = 0
    attempt = 0
    success = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    if start:
        global decisecond
        decisecond = decisecond + 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(decisecond), position, 100, "Red")
    canvas.draw_text(str(success) + "/" + str(attempt), [400, 50], 50, "Green")
    
# create frame
frame = simplegui.create_frame("Home", width, height)

# register event handlers
frame.set_draw_handler(draw)
start = frame.add_button("Start", start_handler, 100)
stop = frame.add_button("Stop", stop_handler, 100)
reset = frame.add_button("Reset", reset_handler, 100)
timer = simplegui.create_timer(interval, tick)

start = False
# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric
