# 🎯 Number Guessing Game  

A simple **Python console game** where the player has to guess a random number between **1 and 100** within **10 chances**.  
The game provides feedback whether the guessed number is **too high** or **too low**, and uses the **Colorama library** to display colorful text in the terminal.  

---

## 🚀 Features  
- Random number between **1–100**  
- **10 chances** to guess the number  
- Tells you if your guess is **too high** or **too low**  
- Shows **remaining chances** after each attempt  
- Displays a **congratulations message** when guessed correctly  
- If the player loses, the correct number is revealed  
- **Replay option** to play multiple rounds  
- **Colorful console output** using `colorama`  

---

## 🛠️ Requirements  
Make sure you have Python installed (>=3.6 recommended).  
Install the required library:  

```bash
pip install colorama
```

---

## ▶️ How to Run  
1. Clone this repository or copy the script.  
2. Open a terminal in the project folder.  
3. Run the script:  

```bash
python main.py
```

---

## 🎮 Game Rules  
1. The computer randomly selects a number between **1–100**.  
2. You have **10 chances** to guess it.  
3. After each guess, the program tells you whether your guess is:  
   - Too high 📈  
   - Too low 📉  
4. If you guess correctly → 🎉 You win!  
5. If you run out of chances → ❌ You lose (the correct number will be shown).  
6. After the game ends, you can choose to **play again** or exit.  

---

## 📸 Example Gameplay  

```
 Welcome To Number Guessing Game 

You have to guess number between 1 to 100.
You have to guess in 10 chances.

Guess the number: 50
Try Again! You guessed too high
Remaining chances: 9

Guess the number: 25
Try Again! You guessed too low
Remaining chances: 8

Guess the number: 30
Congratulations! you guess in 3 chances
```

---

## 📂 Project Structure  

```
number-guessing-game/
│-- main.py                   # Main game script
│-- README.md                 # Project documentation
```

---

## ✨ Future Improvements  
- Add difficulty levels (easy/medium/hard with different chances).  
- Add a scoreboard for tracking attempts across rounds.  
- Create a GUI version with `tkinter` or `pygame`.  
