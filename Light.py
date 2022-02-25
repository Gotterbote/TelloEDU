# new file
from djitellopy import Tello
from time import sleep

tello = Tello()
distance = 0
maxDistance = 500
observedDistance = 0
tello.connect()
print(tello.get_battery())
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(0)
tello.takeoff()
sleep(1)
tello.set_speed(25)

pad = tello.get_mission_pad_id()
print("The Mission Pad Number is: " + str(pad))


while observedDistance < maxDistance:

    #   if pad == -1:
    print("No Mission Pad Detected")
    print("I'll keep searching")
    distance = 25
    tello.move_forward(distance)

    observedDistance = observedDistance + distance
    print("Distance traveled is " + str(distance))
    pad = tello.get_mission_pad_id()

    # if pad == 1:
    #     print("The Mission Pad Number is: " + str(pad))
    #     tello.move_forward(100)
    #     distance = distance + 1
    #     sleep(3)
    #     print("Distance traveled is " + str(distance))
    #     pad = tello.get_mission_pad_id()
    #
    # if pad == 2:
    #     print("The Mission Pad Number is: " + str(pad))
    #     tello.move_forward(100)
    #     distance = distance + 1
    #     sleep(3)
    #     print("Distance traveled is " + str(distance))
    #     pad = tello.get_mission_pad_id()

    if pad == 3:
        print("The Mission Pad Number is: " + str(pad))
        print("Time to take a little break!")
        tello.land()
        # sleep(1)
        # tello.takeoff()
        # tello.rotate_clockwise(180)
        # sleep(1)
        # tello.move_forward(100)
        # distance = distance + 1
        # sleep(3)
        # print("Distance traveled is " + str(distance))
        # pad = tello.get_mission_pad_id()

    # if pad == 4:
    #     print("MISSION SUCCESSFUL")
    #     tello.send_command_with_return("downvision 1")
    #     img = tello.get_frame_read().frame
    #     img = cv2.resize(img(360, 240))
    #     cv2.imshow("Success", img)
    #     cv2.waitKey(1)
    #
    #     print("Shutting system down")
    #     tello.disable_mission_pads()
    #     telloland()

if observedDistance >= 500:
    print("Range is out of bounds!")
    print("Abort mission and land now!")

else:
    print("Total distance traveled is " + str(observedDistance))

tello.end()
