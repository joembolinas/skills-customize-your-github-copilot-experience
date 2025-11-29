
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a playable Hangman game in Python that uses strings, loops, and user input to let players guess letters of a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️	Core Game Mechanics

#### Description
Implement the main Hangman gameplay: select a random word, accept letter guesses, reveal correct letters, track remaining attempts, and determine win/lose outcomes.

#### Requirements
Completed program should:

- Choose a random word from a predefined list
- Display progress as underscores for unknown letters (e.g., `_ _ _ _`)
- Accept single-letter input and validate it (alphabetic, not previously guessed)
- Reveal all occurrences of correctly guessed letters
- Track and display incorrect guesses and attempts remaining
- End the game when the word is fully guessed or attempts reach zero
- Show clear win/lose messages and the final word


### 🛠️	User Experience & Features

#### Description
Enhance the game with helpful feedback and optional features to improve usability and replayability.

#### Requirements
Completed program should:

- Show a list of letters already guessed (correct and incorrect)
- Handle edge cases (empty input, multiple characters, non-letters)
- Provide a simple menu or prompt to play again without restarting the program
- Keep the word list easily editable in code (e.g., a `WORDS` list)
- Optional: Draw a basic text-based hangman/attempts meter
- Optional: Support case-insensitive input
