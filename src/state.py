from enum import Enum


# Class for state of a dialog.
class State(Enum):
    first_image_waiting = "first_image_waiting"
    second_image_waiting = "second_image_waiting"
    sending_image = "sending_image"
    stop = "stop"
