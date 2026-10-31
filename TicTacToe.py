from turtle import *
from freegames import line

def grid():
    """Draw tic-tac-toe grid."""
    pencolor('black') 
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    """Draw X player."""
    pencolor('red')
    
    line(x + 26, y + 26, x + 107, y + 107)
    line(x + 26, y + 107, x + 107, y + 26)

def drawo(x, y):
    """Draw O player."""
    pencolor('blue')
    up()
    goto(x + 67, y + 27)
    down()
    
    circle(40)

def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200

    ### Modificación asistida con IA :P
# MODIFICACIÓN: Se reemplaza el estado "Ocupado" con Board.
# Board permite rastrear las casillas ocupadas, y quén las ocupa.
# Se añade también el booleano game_over.
state = {'player': 0, 'board': {}, 'game_over': False}
players = [drawx, drawo]

# MODIFICACIÓN: Función para mostrar el resultado del juego en pantalla.
def display_message(msg):
    """Write the end game message across the center of the board."""
    up()
    goto(0, -20)  # Posiciona el texto cerca del centro de la pantalla.
    pencolor('green')
    write(msg, align='center', font=('Arial', 40, 'bold'))

# MODIFICATION: Evaluación de las posibles posiciones donde hay una victoria.
def check_win(player):
    """Check if the current player has three marks in a row."""
    win_lines = [
        # Columnas
        [(-200, -200), (-200, -67), (-200, 66)],
        [(-67, -200), (-67, -67), (-67, 66)],
        [(66, -200), (66, -67), (66, 66)],
        # Filas
        [(-200, -200), (-67, -200), (66, -200)],
        [(-200, -67), (-67, -67), (66, -67)],
        [(-200, 66), (-67, 66), (66, 66)],
        # Diagonales
        [(-200, -200), (-67, -67), (66, 66)],
        [(-200, 66), (-67, -67), (66, -200)]
    ]
    
    # Evalúa si un jugador ocupa las casillas de una línea que le dé la victoria.
    for line in win_lines:
        if all(state['board'].get(pos) == player for pos in line):
            return True
    return False

def tap(x, y):
    """Draw X or O in tapped square."""
    # MODIFICACIÓN: Si el juego ha terminado, se ignoran nuevos clicks.
    if state['game_over']:
        return
        
    x = floor(x)
    y = floor(y)
    
    # MODIFICACIÓN: Ignora selección de casillas que ya están ocupadas.
    if (x, y) in state['board']:
        return
        
    player = state['player']
    
    # MODIFICACIÓN: Marca la casilla disponible seleccionada con un "ID" del jugador que la seleccionó.
    state['board'][(x, y)] = player
    
    draw = players[player]
    draw(x, y)
    
    # MODIFICACIÓN: Evalúa empate o victoria tras cada turno.
    if check_win(player):
        # El jugador acaba de seleccionar una casilla ganadora.
        state['game_over'] = True
        winner_name = 'X' if player == 0 else 'O'
        display_message(f"Ganan las {winner_name} :)")
    elif len(state['board']) == 9:
        # Todas las casillas están seleccionadas pero no hay un ganador.
        state['game_over'] = True
        display_message("Empate :P")
    else:
        # El jeugo no se ha definido, sigue el juego.
        state['player'] = not player

    update()

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
