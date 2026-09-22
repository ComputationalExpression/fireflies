"""Fireflies at Bousson.

CMPSC 100: Computational Expression, Lab 3

A June night at the college's Bousson Environmental Research Reserve, counting
fireflies at the pond edge. Your Pico 2 W's built-in LED is your lantern, and
the fireflies answer a lantern the way they answer each other: in patterns.
Every stage repeats something, and a loop is how you say it once.

Every message this program prints is yours to word, and the story is yours to
change. The automated checks read only the field log at the end.

Author: TODO
"""

from machine import Pin
import time


def main():
    led = Pin("LED", Pin.OUT)

    print("=" * 50)
    print("FIREFLIES AT BOUSSON")
    print("=" * 50)

    # ===== Stage One: The Call =====

    # TODO 1: ask the user's name, save it to a variable called `name`

    # TODO 2: ask how many flashes to send toward the pond edge (1-10), save
    # the answer to a variable called `flashes`, and convert it to an int

    # TODO 3: keep `flashes` between 1 and 10 with an if/elif
    # if it is more than 10: set it to 10 and print a message
    # elif it is less than 1: set it to 1 and print a message

    # TODO 4: print a message that uses `name`, then flash the lantern
    # `flashes` times with a for loop over range(1, flashes + 1)
    # On every trip: print the flash number, then led.on(), time.sleep(0.2),
    # led.off(), time.sleep(0.2)

    # ===== Stage Two: Waiting for Dark =====

    print()

    # TODO 5: ask what the light meter reads (0-100), save it to `reading`,
    # and convert it to an int

    # TODO 6: fireflies start once the meter reads 20 or lower. Set a variable
    # called `checks` to 0, then write a while loop that runs as long as
    # `reading` is more than 20. On every trip: print the reading, subtract 10
    # from `reading`, and add 1 to `checks`
    # After the loop, print that it is dark enough

    # ===== Stage Three: The Answer =====

    print()

    # TODO 7: ask how many flashes are in the pattern (1-12), save it to
    # `pattern`, and convert it to an int

    # TODO 8: every third flash is held long. Set a variable called
    # `long_flashes` to 0, then loop over range(1, pattern + 1)
    # On every trip, an if/else decides the flash:
    # if the flash number divided by 3 leaves no remainder (use %): print that
    #     it is held long, led.on(), time.sleep(0.6), led.off(), and add 1 to
    #     `long_flashes`
    # else: print the flash number, led.on(), time.sleep(0.2), led.off()
    # After the if/else, still inside the loop, time.sleep(0.2)
    # After the loop, print that the fireflies answer

    # ===== Stage Four: SOS =====

    print()
    print("You look up from the count. The trail markers you followed in are gone in the dark.")

    # TODO 9: ask how many times to send SOS toward the road (1-5), save it to
    # `repeats`, and convert it to an int

    # TODO 10: SOS is three short flashes, three long, three short. Write an
    # outer for loop over range(1, repeats + 1) that prints which attempt this
    # is. Inside it, three more for loops, each over range(3):
    # the first: led.on(), time.sleep(0.2), led.off(), time.sleep(0.2)
    # the second: led.on(), time.sleep(0.6), led.off(), time.sleep(0.2)
    # the third: the same as the first
    # Put a time.sleep(0.4) between the letters and a time.sleep(1.0) after the
    # third, still inside the outer loop
    # After the outer loop, print what happens when someone sees the signal

    print()
    print("=" * 50)

    # TODO 11: print the field log, one line each, in this order:
    # "FIELD LOG: {name}", then a line of 50 "=" characters, then
    # "Flashes sent: {flashes}", "Checks until dark: {checks}",
    # "Long flashes: {long_flashes}", and "SOS repeats: {repeats}"
    # Print each value any way you like: commas, + with str(), or an f-string


if __name__ == "__main__":
    main()
