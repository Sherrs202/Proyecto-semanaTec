"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')

# Create 8 pairs for a 4x4 board
tiles = list(range(8)) * 2

# Initialize the counter for discovered pairs
state = {'mark': None, 'pairs': 0}

# Initialize the 16 tiles as hidden
hide = [True] * 16

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""

    # Adjust coordinates for the 4x4 board
    return int((x + 100) // 50 + ((y + 100) // 50) * 4)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""

    # Position tiles in a centered 4x4 grid
    return (count % 4) * 50 - 100, (count // 4) * 50 - 100

def tap(x, y):
    """Update mark and hidden tiles based on tap."""

    # Ignore clicks outside the 4x4 board
    if not (-100 <= x < 100 and -100 <= y < 100):
        return

    spot = index(x, y)

    # Ignore tiles that have already been revealed
    if not hide[spot]:
        return

    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

        # Increase the counter when two matching tiles are found
        state['pairs'] += 1

        # Display the total number of discovered pairs
        print("Pares descubiertos:", state['pairs'])

        # Check whether all tiles have been revealed
        if not any(hide):
            print("¡Felicidades! Has descubierto todos los pares.")
            print("¡Juego terminado!")

def draw():
    """Draw image and tiles."""

    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Draw the 16 tiles of the 4x4 board
    for count in range(16):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)

setup(420, 420, 370, 0)

addshape(car)

hideturtle()

tracer(False)

onscreenclick(tap)

draw()

done()
