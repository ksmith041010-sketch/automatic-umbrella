A simple Python number guessing game with a “hot and cold” feedback system and progressive hint tracking. Built as a learning project to practice loops, conditionals, randomness, and user interaction in Python.

---

## 🎯 How the Game Works

The computer secretly chooses a number between **0 and 50**.

You have **5 attempts** to guess it.

After each guess, the game tells you how close you are:

- 🔥 Very hot (very close)
- 🌡️ Warm
- 🧊 Cold
- 🥶 Freezing (far away)

---

## 📈 Bonus Feature: Hotter / Colder Tracking

After your first guess, the game tracks whether you're:

- 📈 Getting hotter (closer than your previous guess)
- 📉 Getting colder (farther than your previous guess)
- ➡️ Staying the same distance

This helps guide your strategy instead of relying on random guessing.

---

## 🧠 What I Practiced Building This

- `while` loops and `for` loops
- Conditionals (`if / elif / else`)
- Random number generation
- User input handling
- Game state tracking
- Basic logic comparison (distance system)

---

## ▶️ How to Run the Game

Make sure you have Python installed, then run:

```bash
python guessing_game.py
