# new file
import time
from djitellopy import Tello
import cv2
from codetiming import Timer

count = 1
start = time.time()
t = Timer(name="time1")
t.start()

tello = Tello()
distance = 0
maxDistance = 500
observedDistance = 0
tello.connect()
print(tello.get_battery())
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(0)
print("Preflight check parameters " + (str(t.stop()) + " seconds"))

t.start()
tello.takeoff()
t.stop()

t.start()
tello.set_speed(100)
# tello.move_down(50)
# tello.move_up(50)
t.stop()

pad = tello.get_mission_pad_id()
print("The Mission Pad Number is: " + str(pad))
time.sleep(.25)


while observedDistance < maxDistance:

    t.start()
    if pad == -1:
        print("No Mission Pad Detected")
        distance = 25
        tello.move_forward(distance)

    observedDistance = observedDistance + distance
    print("Distance traveled is " + str(observedDistance))
    pad = tello.get_mission_pad_id()
    t.stop()

    while pad == 3:
        if count < 1:
            t.start()
            print("The Mission Pad Number is: " + str(pad))
            tello.move_down(50)
            pad = tello.get_mission_pad_id()
            tello.move_forward(distance)
            observedDistance = observedDistance + distance
            print("Distance traveled is " + str(observedDistance))
            count = count + 1
            t.stop()

        elif count < 2:
            t.start()
            print("The Mission Pad Number is: " + str(pad))
            tello.move_down(50)
            pad = tello.get_mission_pad_id()
            tello.move_forward(distance)
            observedDistance = observedDistance + distance
            print("Distance traveled is " + str(observedDistance))
            count = count + 1
            t.stop()

        else:
            t.start()
            print("The Mission Pad Number is: " + str(pad))
            tello.send_command_with_return("downvision 1")
            tello.streamon()
            img = tello.get_frame_read().frame
            cv2.imshow("Bottom View", img)
            cv2.waitKey(5)
            tello.land()
            t.stop()
            break

if observedDistance >= 500:
    end = time.time()
    print("Range is out of bounds!")
    print("Total elapsed time was " + str(end - start))

else:
    end = time.time()
    print("Total distance traveled was " + str(observedDistance))
    print("Total elapsed time was " + str(end - start))
tello.end()
quit()
