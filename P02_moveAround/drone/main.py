from djitellopy import Tello

my_drone = Tello()
my_drone.connect()


my_drone.takeoff()

# Die Drohne wird ein Rechteck fliegen.

# Bewegen der Drohne um 20cm nach vorne.
my_drone.move_forward(20)
# Drehen der Drohne um 180 Grad nach rechts.
my_drone.rotate_clockwise(180)
# Bewegen der Drohne um 40cm nach vorne.
my_drone.move_left(40)
# Drehen der Drohne um 90 Grad nach links.
my_drone.rotate_counter_clockwise(90)
# Bewegen der Drohne um 20cm nach rechts.
my_drone.move_right(20)
# Bewegen der Drohne um 40cm nach hinten.
my_drone.move_back(40)
# Drehen der Drohne um 90 Grad nach link.
my_drone.rotate_counter_clockwise(90)

my_drone.land()
