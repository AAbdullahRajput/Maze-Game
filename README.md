# 🧩 Maze Game

> A maze navigation game built with OpenGL/GLUT where the player moves through a grid maze collecting yellow coins for points while avoiding colorful triangular enemies. Features lives system, score tracking, a timer, and a green goal cell to reach for victory.

---

## 🎮 Gameplay Preview

```
█████████████████████████████
█ P  █     █     █     █   █
█ █████ ██ █ ██ ██ ██ █ █ ██
█       █     █       █   ░ █
█████████████████████████████
  Player(🔴) → Goal(🟩)
```

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🔴 Player | Move through the maze using arrow keys |
| 🟡 Coins | Collect yellow coins to earn points (+10 each) |
| 🔺 Enemies | Avoid colorful triangular enemies that move randomly |
| 🟩 Goal | Reach the green cell to win |
| ❤️ Lives | You have 3 lives — lose them all and it's game over |
| ⏱️ Timer | Track how fast you complete the maze |
| 🔄 Restart | Press `R` to restart at any time |

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Graphics:** OpenGL / GLUT / GLU
- **Library:** PyOpenGL

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/AAbdullahRajput/maze-game.git
cd maze-game
```

### 2. Install dependencies
```bash
py -m pip install PyOpenGL PyOpenGL_accelerate
```

### 3. Run the game
```bash
py project.py
```

---

## 🕹️ Controls

| Key | Action |
|-----|--------|
| ⬆️ Arrow Up | Move Up |
| ⬇️ Arrow Down | Move Down |
| ⬅️ Arrow Left | Move Left |
| ➡️ Arrow Right | Move Right |
| `R` | Restart Game |
| `ESC` | Quit Game |

---

## 🗺️ Game Elements

```
🔵 Blue Cells     →  Walls (cannot pass through)
⬜ White Cells    →  Walkable paths
🔴 Red Square     →  Player
🟡 Yellow Circle  →  Collectible coin (+10 points)
🔺 Colored Triangle → Enemy (avoid!)
🟩 Green Square   →  Goal (reach to win!)
```

---

## 📊 Scoring

- **+10 points** for each coin collected
- **-1 life** for each enemy collision
- **Game Over** when lives reach 0
- **You Win** when you reach the green goal cell

---

## 📁 Project Structure

```
maze-game/
│
├── project.py        # Main game file
└── README.md         # Project documentation
```

---

## 🚀 Requirements

- Python 3.x
- PyOpenGL
- PyOpenGL_accelerate
- Windows / Linux / macOS

---

## 👨‍💻 Author

Made with ❤️ for Computer Graphics & HCI Subject
© 2025 — All rights reserved
