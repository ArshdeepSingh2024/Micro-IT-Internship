# Python Quiz Game

A comprehensive quiz application with both Command Line Interface (CLI) and Graphical User Interface (GUI) options.

## Overview

This Python Quiz Game allows users to test their knowledge across various categories including Science, History, Geography, and Entertainment. The game features multiple-choice questions, timed responses, score tracking, and detailed performance analysis.

## Features

- **Multiple Question Categories**: Science, History, Geography, and Entertainment
- **Customizable Settings**: Adjust number of questions and time limits
- **Timer**: Limited time to answer each question
- **Score Tracking**: Track correct answers and calculate percentages
- **Category Performance**: See how well you perform in different subject areas
- **Question Review**: Review all questions with correct answers after completing the quiz
- **Two User Interfaces**:
  - Command Line Interface (CLI) for simple terminal-based gameplay
  - Graphical User Interface (GUI) for a more interactive experience

## Requirements

- Python 3.6 or higher
- Tkinter (included in standard Python installations) for the GUI version

## Files

1. `quiz_game_gui.py` - Graphical user interface version of the quiz game

## Installation

No special installation is required beyond Python itself. Simply download the desired file and run it using Python.

```bash


# For GUI version
python quiz_game_gui.py
```

## How to Play

### GUI Version

1. Run the script using Python
2. Click "Start Quiz" on the welcome screen
3. Adjust settings (number of questions, time limit, categories)
4. Answer questions by clicking on your chosen option
5. Review your performance on the results screen


## Customization

### Adding New Questions

To add more questions, modify the `initialize_questions()` method in either version. Each question requires:

```python
self.questions.append(Question(
    "Question text here?",  # Question text
    ["Option 1", "Option 2", "Option 3", "Option 4"],  # Options array
    correct_index,  # Index of correct answer (0-based)
    "Category"  # Question category
))
```

### Adding Categories

To add new categories, simply add questions with the new category name. The system will automatically detect and include the new category.

## Code Highlights


### GUI Version

- Uses Tkinter for the graphical interface
- Implements multiple screens (welcome, settings, quiz, results)
- Features a visual timer with progress bar
- Provides tabbed category review in the results screen
- Uses color-coding to indicate correct and incorrect answers

## Future Enhancements

Potential improvements for future versions:

1. Database integration for storing questions and high scores
2. User accounts and login system
3. Difficulty levels for questions
4. Image-based questions
5. Sound effects and background music
6. Online multiplayer mode
7. Detailed statistics tracking over time

# Python Quiz Game

A comprehensive quiz application with both Command Line Interface (CLI) and Graphical User Interface (GUI) options.

## Overview

This Python Quiz Game allows users to test their knowledge across various categories including Science, History, Geography, and Entertainment. The game features multiple-choice questions, timed responses, score tracking, and detailed performance analysis.

## Features

- **Multiple Question Categories**: Science, History, Geography, and Entertainment
- **Customizable Settings**: Adjust number of questions and time limits
- **Timer**: Limited time to answer each question
- **Score Tracking**: Track correct answers and calculate percentages
- **Category Performance**: See how well you perform in different subject areas
- **Question Review**: Review all questions with correct answers after completing the quiz
- **Two User Interfaces**:
  - Command Line Interface (CLI) for simple terminal-based gameplay
  - Graphical User Interface (GUI) for a more interactive experience

## Requirements

- Python 3.6 or higher
- Tkinter (included in standard Python installations) for the GUI version

## Files

1. `quiz_game_cli.py` - Command line version of the quiz game
2. `quiz_game_gui.py` - Graphical user interface version of the quiz game

## Installation

No special installation is required beyond Python itself. Simply download the desired file and run it using Python.

```bash
# For CLI version
python quiz_game_cli.py

# For GUI version
python quiz_game_gui.py
```

## How to Play

### CLI Version

1. Run the script using Python
2. Choose from the menu options (Start Quiz, Settings, Exit)
3. Answer questions by entering the number corresponding to your choice
4. View your results at the end of the quiz

### GUI Version

1. Run the script using Python
2. Click "Start Quiz" on the welcome screen
3. Adjust settings (number of questions, time limit, categories)
4. Answer questions by clicking on your chosen option
5. Review your performance on the results screen

## Code Structure

### CLI Version (`quiz_game_cli.py`)

```
QuizGame
├── Question Class
│   ├── text (question text)
│   ├── options (possible answers)
│   ├── correct_answer (index of correct option)
│   ├── category
│   ├── user_answer (user's selection)
│   └── time_taken (time to answer)
│
└── QuizGame Class
    ├── initialize_questions()
    ├── shuffle_questions()
    ├── display_question()
    ├── get_answer()
    ├── run_quiz()
    └── display_results()
```

### GUI Version (`quiz_game_gui.py`)

```
QuizGameGUI
├── Question Class (same as CLI version)
│
└── QuizGameGUI Class
    ├── initialize_questions()
    ├── create_frames()
    ├── show_welcome_screen()
    ├── show_settings_screen()
    ├── start_quiz()
    ├── display_current_question()
    ├── update_timer()
    ├── answer_question()
    ├── show_next_button()
    ├── show_results()
    └── add_question_to_review()
```

## Customization

### Adding New Questions

To add more questions, modify the `initialize_questions()` method in either version. Each question requires:

```python
self.questions.append(Question(
    "Question text here?",  # Question text
    ["Option 1", "Option 2", "Option 3", "Option 4"],  # Options array
    correct_index,  # Index of correct answer (0-based)
    "Category"  # Question category
))
```

### Adding Categories

To add new categories, simply add questions with the new category name. The system will automatically detect and include the new category.

## Code Highlights

### CLI Version

- Uses object-oriented design with Question and QuizGame classes
- Implements input validation for user responses
- Features a simple timer system for each question
- Provides detailed statistics and question review

### GUI Version

- Uses Tkinter for the graphical interface
- Implements multiple screens (welcome, settings, quiz, results)
- Features a visual timer with progress bar
- Provides tabbed category review in the results screen
- Uses color-coding to indicate correct and incorrect answers

## Future Enhancements

Potential improvements for future versions:

1. Database integration for storing questions and high scores
2. User accounts and login system
3. Difficulty levels for questions
4. Image-based questions
5. Sound effects and background music
6. Online multiplayer mode
7. Detailed statistics tracking over time

## License

This project is open-source and free to use and modify.

## Credits

Created as a Python programming exercise to demonstrate:
- Object-oriented programming concepts
- GUI development with Tkinter
- Game logic implementation


The README covers:

1. **Overview**: A brief introduction to the quiz game
2. **Features**: All the key functionalities of the game
3. **Requirements**: The software needed to run the application
4. **Installation**: How to install and run the versions
5. **How to Play**: Instructions for  GUI versions
6. **Code Structure**: A breakdown of the classes and methods
7. **Customization**: How to add new questions and categories
8. **Code Highlights**: Technical features of each implementation
9. **Future Enhancements**: Potential improvements for future versions

This README serves as both documentation and a guide for anyone who wants to use, understand, or modify the quiz game code. It's structured in a way that both beginners and experienced developers can follow along and understand the project.

The README is written in Markdown format, which is commonly used on platforms like GitHub, making it ready for sharing as open-source if desired.

photos:
![Screenshot 2025-04-28 130852](https://github.com/user-attachments/assets/a2d0badd-f5fa-40ff-ba2e-0e87eaae26e2)
![Screenshot 2025-04-28 130914](https://github.com/user-attachments/assets/e8ade335-ae1a-4dea-adac-abfce848f182)
![Screenshot 2025-04-28 130926](https://github.com/user-attachments/assets/1e883983-5f48-4852-b7a5-9c48b8af466a)

