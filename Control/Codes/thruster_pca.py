import pygame

pygame.init()
pygame.joystick.init()
joy = pygame.joystick.Joystick(0)
joy.init()

while True:
    pygame.event.pump()
    pressed = [i for i in range(joy.get_numbuttons()) if joy.get_button(i)]
    axes = {i: round(joy.get_axis(i), 2) for i in range(joy.get_numaxes()) if abs(joy.get_axis(i)) > 0.2}
    if pressed or axes:
        print("Buttons:", pressed, "Axes:", axes)
