from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time
import math

maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,0,1,0,1,0,1,0,1,0,1,1],
    [1,0,1,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,1,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,0,1,1,1,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,1,0,1],
    [1,0,1,0,1,1,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,0,1,0,1,1,1,1,0,1],
    [1,0,0,0,0,1,0,1,0,1,0,0,0,0,1],
    [1,0,1,1,0,1,0,0,0,1,0,1,1,0,1],
    [1,0,0,1,0,0,0,1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

rows, cols = len(maze), len(maze[0])
cell_size = 35

player_pos = [1, 1]
goal_pos = [13, 13]
score = 0
lives = 3
start_time = None
game_over = False
game_won = False

collectibles = []
enemies = []
enemy_colors = []

num_collectibles = 10
num_enemies = 3

def reset_game():
    global player_pos, score, lives, start_time, game_over, game_won, collectibles, enemies, enemy_colors
    player_pos = [1, 1]
    score = 0
    lives = 3
    start_time = time.time()
    game_over = False
    game_won = False
    collectibles = []
    enemies = []
    enemy_colors = []
    for _ in range(num_collectibles):
        while True:
            r, c = random.randint(1, rows-2), random.randint(1, cols-2)
            if maze[r][c] == 0 and [r, c] != player_pos and [r, c] != goal_pos:
                collectibles.append([r, c])
                break
    for _ in range(num_enemies):
        while True:
            r, c = random.randint(1, rows-2), random.randint(1, cols-2)
            if maze[r][c] == 0 and [r, c] != player_pos and [r, c] != goal_pos:
                enemies.append([r, c])
                enemy_colors.append((random.random(), random.random(), random.random()))  # Random color for each enemy
                break

def draw_square(x, y, color):
    glColor3fv(color)
    glBegin(GL_QUADS)
    glVertex2f(x * cell_size, y * cell_size)
    glVertex2f((x + 1) * cell_size, y * cell_size)
    glVertex2f((x + 1) * cell_size, (y + 1) * cell_size)
    glVertex2f(x * cell_size, (y + 1) * cell_size)
    glEnd()

def draw_circle(x, y, radius_ratio, color):
    glColor3fv(color)
    segments = 20
    cx = (x + 0.5) * cell_size
    cy = (y + 0.5) * cell_size
    radius = (cell_size / 2) * radius_ratio
    glBegin(GL_POLYGON)
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        glVertex2f(cx + radius * math.cos(angle), cy + radius * math.sin(angle))
    glEnd()

def draw_triangle(x, y, color):
    glColor3fv(color)
    cx = (x + 0.5) * cell_size
    cy = (y + 0.5) * cell_size
    size = (cell_size / 2) * 0.8
    glBegin(GL_TRIANGLES)
    glVertex2f(cx, cy - size)
    glVertex2f(cx - size, cy + size)
    glVertex2f(cx + size, cy + size)
    glEnd()

def draw_maze():
    for i in range(rows):
        for j in range(cols):
            color = (0.2, 0.2, 0.8) if maze[i][j] == 1 else (0.9, 0.9, 0.9)
            draw_square(j, i, color)
    draw_square(goal_pos[1], goal_pos[0], (0.0, 0.9, 0.0))  # Goal (Green)

def draw_collectibles():
    for c in collectibles:
        draw_circle(c[1], c[0], 0.3, (1.0, 1.0, 0.0))  # Small yellow circles (Coins)

def draw_enemies():
    for idx, e in enumerate(enemies):
        draw_triangle(e[1], e[0], enemy_colors[idx])  # Multicolor triangles (Enemies)

def draw_player():
    draw_square(player_pos[1], player_pos[0], (1.0, 0.0, 0.0))

def draw_text(x, y, text, size=GLUT_BITMAP_HELVETICA_18):
    glColor3f(1, 1, 1)
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(size, ord(ch))

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_maze()
    draw_collectibles()
    draw_enemies()
    draw_player()

    elapsed_time = int(time.time() - start_time) if start_time else 0
    draw_text(10, 20, f"Score: {score}  Time: {elapsed_time}s  Lives: {lives}")

    if game_won:
        draw_text(80, 300, f"🎉 You Win! Score: {score}  Time: {elapsed_time}s", GLUT_BITMAP_HELVETICA_18)
        draw_text(80, 330, "Press 'R' to Restart", GLUT_BITMAP_HELVETICA_18)
    elif game_over:
        draw_text(80, 300, "💀 Game Over!", GLUT_BITMAP_HELVETICA_18)
        draw_text(80, 330, "Press 'R' to Restart", GLUT_BITMAP_HELVETICA_18)

    glutSwapBuffers()

def move_player(dx, dy):
    global score, game_won, game_over, lives
    if game_over or game_won:
        return

    new_x = player_pos[0] + dy
    new_y = player_pos[1] + dx
    if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] == 0:
        player_pos[0], player_pos[1] = new_x, new_y

        for c in collectibles:
            if c == player_pos:
                collectibles.remove(c)
                score += 10
                break

        for e in enemies:
            if e == player_pos:
                lives -= 1
                if lives <= 0:
                    game_over = True
                break

        if player_pos == goal_pos:
            game_won = True

    glutPostRedisplay()

def move_enemies():
    global lives, game_over
    if game_over or game_won:
        return

    for e in enemies:
        dx, dy = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        new_x, new_y = e[0] + dy, e[1] + dx
        if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] == 0:
            e[0], e[1] = new_x, new_y
            if e == player_pos:
                lives -= 1
                if lives <= 0:
                    game_over = True
    glutPostRedisplay()

def special_keys(key, x, y):
    if key == GLUT_KEY_UP:
        move_player(0, -1)
    elif key == GLUT_KEY_DOWN:
        move_player(0, 1)
    elif key == GLUT_KEY_LEFT:
        move_player(-1, 0)
    elif key == GLUT_KEY_RIGHT:
        move_player(1, 0)

def keyboard(key, x, y):
    if key == b'\x1b':
        try:
            glutLeaveMainLoop()
        except:
            exit()
    elif key == b'r' or key == b'R':
        reset_game()
        glutPostRedisplay()

def enemy_timer(value):
    move_enemies()
    glutTimerFunc(500, enemy_timer, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(cols * cell_size, rows * cell_size)
    glutCreateWindow(b"Maze Game with Multicolor Triangular Enemies")
    gluOrtho2D(0, cols * cell_size, rows * cell_size, 0)
    glutDisplayFunc(display)
    glutSpecialFunc(special_keys)
    glutKeyboardFunc(keyboard)
    glClearColor(0.1, 0.1, 0.1, 1)
    reset_game()
    glutTimerFunc(500, enemy_timer, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
