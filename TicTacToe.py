from turtle import *
from freegames import line

def grid():
    """Draw tic-tac-toe grid."""
    # MODIFICACIÓN: pencolor mantiene el color del tablero igual durante el juego. 
    pencolor('black') 
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    """Draw X player."""
    # MODIFICACIÓN: Cambio el color de las X a rojo.
    pencolor('red')
    
    # MODIFICACIÓN: Añado un margen para que la X quede centrada en sus cuadros.
    line(x + 26, y + 26, x + 107, y + 107)
    line(x + 26, y + 107, x + 107, y + 26)

def drawo(x, y):
    """Draw O player."""
    # MODIFICACIÓN: Cambio el color de las Os a azul.
    pencolor('blue')
    up()
    
    # MODIFICACIÓN: Modifico la posición de las Os en sus cuadros para que se mantenga centrada.
    goto(x + 67, y + 27)
    down()
    
    # MODIFICACIÓN: Cambio el radio del círculo.
    circle(40)

def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200

state = {'player': 0}
players = [drawx, drawo]

def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
