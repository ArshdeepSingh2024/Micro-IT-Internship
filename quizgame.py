import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
from typing import List, Dict, Any

class Question:
    def __init__(self, text: str, options: List[str], correct_answer: int, category: str):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer  # Index of the correct answer
        self.category = category
        self.user_answer = None
        self.time_taken = 0

class QuizGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Game")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Set icon (optional)
        # self.root.iconbitmap("quiz_icon.ico")
        
        self.questions = []
        self.current_question_index = 0
        self.score = 0
        self.total_time = 0
        self.question_history = []
        self.category_stats = {}
        self.time_limit = 15  # Default time limit in seconds
        self.num_questions = 5  # Default number of questions
        self.remaining_time = 0
        self.timer_running = False
        self.timer_id = None
        
        # Initialize questions
        self.initialize_questions()
        
        # Create frames
        self.create_frames()
        
        # Show welcome screen
        self.show_welcome_screen()
    
    def initialize_questions(self):
        """Add questions to the quiz."""
        # Science questions
        self.questions.append(Question(
            "What is the chemical symbol for gold?",
            ["Go", "Au", "Ag", "Gd"],
            1,
            "Science"
        ))
        self.questions.append(Question(
            "Which planet is known as the Red Planet?",
            ["Venus", "Jupiter", "Mars", "Saturn"],
            2,
            "Science"
        ))
        self.questions.append(Question(
            "What is the hardest natural substance on Earth?",
            ["Titanium", "Platinum", "Gold", "Diamond"],
            3,
            "Science"
        ))
        
        # History questions
        self.questions.append(Question(
            "In which year did World War II end?",
            ["1943", "1945", "1947", "1950"],
            1,
            "History"
        ))
        self.questions.append(Question(
            "Who was the first President of the United States?",
            ["Thomas Jefferson", "John Adams", "George Washington", "Benjamin Franklin"],
            2,
            "History"
        ))
        self.questions.append(Question(
            "Which ancient civilization built the Machu Picchu?",
            ["Aztecs", "Mayans", "Incas", "Olmecs"],
            2,
            "History"
        ))
        
        # Geography questions
        self.questions.append(Question(
            "What is the capital of Australia?",
            ["Sydney", "Melbourne", "Canberra", "Perth"],
            2,
            "Geography"
        ))
        self.questions.append(Question(
            "Which is the longest river in the world?",
            ["Amazon", "Nile", "Yangtze", "Mississippi"],
            1,
            "Geography"
        ))
        self.questions.append(Question(
            "Which country has the largest population?",
            ["India", "United States", "Russia", "China"],
            0,
            "Geography"
        ))
        
        # Entertainment questions
        self.questions.append(Question(
            "Who directed the movie 'Inception'?",
            ["Steven Spielberg", "James Cameron", "Christopher Nolan", "Quentin Tarantino"],
            2,
            "Entertainment"
        ))
        self.questions.append(Question(
            "Which band performed the album 'Dark Side of the Moon'?",
            ["The Beatles", "Led Zeppelin", "Pink Floyd", "The Rolling Stones"],
            2,
            "Entertainment"
        ))
        self.questions.append(Question(
            "Who wrote the Harry Potter series?",
            ["J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "Stephen King"],
            1,
            "Entertainment"
        ))
    
    def create_frames(self):
        """Create the main frames for the GUI."""
        # Welcome frame
        self.welcome_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.welcome_frame.pack(fill="both", expand=True)
        
        # Settings frame
        self.settings_frame = tk.Frame(self.root, bg="#f0f0f0")
        
        # Quiz frame
        self.quiz_frame = tk.Frame(self.root, bg="#f0f0f0")
        
        # Results frame
        self.results_frame = tk.Frame(self.root, bg="#f0f0f0")
    
    def show_welcome_screen(self):
        """Display the welcome screen."""
        # Clear any existing widgets
        for widget in self.welcome_frame.winfo_children():
            widget.destroy()
        
        # Title
        title_label = tk.Label(
            self.welcome_frame, 
            text="Python Quiz Game", 
            font=("Arial", 24, "bold"), 
            bg="#f0f0f0", 
            fg="#333333"
        )
        title_label.pack(pady=(100, 20))
        
        # Description
        desc_label = tk.Label(
            self.welcome_frame, 
            text="Test your knowledge with multiple-choice questions\nfrom various categories!",
            font=("Arial", 14),
            bg="#f0f0f0",
            fg="#555555"
        )
        desc_label.pack(pady=(0, 50))
        
        # Start button
        start_button = tk.Button(
            self.welcome_frame,
            text="Start Quiz",
            command=self.show_settings_screen,
            font=("Arial", 14),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            relief=tk.FLAT,
            activebackground="#45a049"
        )
        start_button.pack(pady=(0, 20))
        
        # Exit button
        exit_button = tk.Button(
            self.welcome_frame,
            text="Exit",
            command=self.root.quit,
            font=("Arial", 14),
            bg="#f44336",
            fg="white",
            padx=20,
            pady=10,
            relief=tk.FLAT,
            activebackground="#d32f2f"
        )
        exit_button.pack()
    
    def show_settings_screen(self):
        """Display the settings screen."""
        # Hide welcome frame
        self.welcome_frame.pack_forget()
        
        # Configure settings frame
        self.settings_frame.pack(fill="both", expand=True)
        
        # Clear any existing widgets
        for widget in self.settings_frame.winfo_children():
            widget.destroy()
        
        # Title
        title_label = tk.Label(
            self.settings_frame, 
            text="Quiz Settings", 
            font=("Arial", 20, "bold"), 
            bg="#f0f0f0"
        )
        title_label.pack(pady=(50, 30))
        
        # Settings container
        settings_container = tk.Frame(self.settings_frame, bg="#f0f0f0")
        settings_container.pack(pady=20)
        
        # Number of questions
        question_label = tk.Label(
            settings_container,
            text="Number of Questions:",
            font=("Arial", 12),
            bg="#f0f0f0"
        )
        question_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.question_var = tk.StringVar(value=str(self.num_questions))
        question_scale = tk.Scale(
            settings_container,
            from_=1,
            to=len(self.questions),
            orient=tk.HORIZONTAL,
            length=200,
            variable=self.question_var,
            font=("Arial", 10),
            bg="#f0f0f0"
        )
        question_scale.grid(row=0, column=1, padx=10, pady=10)
        
        # Time limit
        time_label = tk.Label(
            settings_container,
            text="Time per Question (seconds):",
            font=("Arial", 12),
            bg="#f0f0f0"
        )
        time_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        self.time_var = tk.StringVar(value=str(self.time_limit))
        time_scale = tk.Scale(
            settings_container,
            from_=5,
            to=60,
            orient=tk.HORIZONTAL,
            length=200,
            variable=self.time_var,
            font=("Arial", 10),
            bg="#f0f0f0"
        )
        time_scale.grid(row=1, column=1, padx=10, pady=10)
        
        # Categories frame
        categories_frame = tk.LabelFrame(
            self.settings_frame,
            text="Categories",
            font=("Arial", 12),
            bg="#f0f0f0",
            padx=10,
            pady=10
        )
        categories_frame.pack(pady=20)
        
        # Get unique categories
        categories = list(set(q.category for q in self.questions))
        
        # Category checkbuttons
        self.category_vars = {}
        for i, category in enumerate(categories):
            var = tk.BooleanVar(value=True)
            self.category_vars[category] = var
            
            cb = tk.Checkbutton(
                categories_frame,
                text=category,
                variable=var,
                font=("Arial", 11),
                bg="#f0f0f0"
            )
            cb.grid(row=i//2, column=i%2, padx=10, pady=5, sticky="w")
        
        # Buttons frame
        buttons_frame = tk.Frame(self.settings_frame, bg="#f0f0f0")
        buttons_frame.pack(pady=30)
        
        # Start button
        start_button = tk.Button(
            buttons_frame,
            text="Start Quiz",
            command=self.start_quiz,
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            padx=15,
            pady=8,
            relief=tk.FLAT
        )
        start_button.grid(row=0, column=0, padx=10)
        
        # Back button
        back_button = tk.Button(
            buttons_frame,
            text="Back to Menu",
            command=lambda: (self.settings_frame.pack_forget(), self.show_welcome_screen()),
            font=("Arial", 12),
            bg="#2196F3",
            fg="white",
            padx=15,
            pady=8,
            relief=tk.FLAT
        )
        back_button.grid(row=0, column=1, padx=10)
    
    def start_quiz(self):
        """Start the quiz with selected settings."""
        # Get settings values
        try:
            self.num_questions = int(self.question_var.get())
            self.time_limit = int(self.time_var.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for settings.")
            return
        
        # Filter questions by selected categories
        selected_categories = [cat for cat, var in self.category_vars.items() if var.get()]
        if not selected_categories:
            messagebox.showerror("No Categories", "Please select at least one category.")
            return
        
        filtered_questions = [q for q in self.questions if q.category in selected_categories]
        if not filtered_questions:
            messagebox.showerror("No Questions", "No questions available for selected categories.")
            return
        
        # Shuffle questions and take required number
        random.shuffle(filtered_questions)
        self.quiz_questions = filtered_questions[:self.num_questions]
        
        # Reset quiz state
        self.current_question_index = 0
        self.score = 0
        self.total_time = 0
        self.question_history = []
        self.category_stats = {}
        
        # Initialize category stats
        for question in self.quiz_questions:
            if question.category not in self.category_stats:
                self.category_stats[question.category] = {"correct": 0, "total": 0}
        
        # Hide settings frame and show quiz frame
        self.settings_frame.pack_forget()
        self.quiz_frame.pack(fill="both", expand=True)
        
        # Start displaying questions
        self.display_current_question()
    
    def display_current_question(self):
        """Display the current question."""
        # Clear quiz frame
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()
        
        # Get current question
        question = self.quiz_questions[self.current_question_index]
        
        # Question number and category
        header_frame = tk.Frame(self.quiz_frame, bg="#f0f0f0")
        header_frame.pack(fill="x", pady=(20, 0))
        
        question_num_label = tk.Label(
            header_frame,
            text=f"Question {self.current_question_index + 1}/{len(self.quiz_questions)}",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0"
        )
        question_num_label.pack(side="left", padx=20)
        
        category_label = tk.Label(
            header_frame,
            text=f"Category: {question.category}",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#555555"
        )
        category_label.pack(side="right", padx=20)
        
        # Timer
        self.timer_frame = tk.Frame(self.quiz_frame, bg="#f0f0f0")
        self.timer_frame.pack(pady=10)
        
        self.timer_label = tk.Label(
            self.timer_frame,
            text=f"Time Remaining: {self.time_limit} seconds",
            font=("Arial", 12),
            bg="#f0f0f0"
        )
        self.timer_label.pack()
        
        # Progress bar
        self.timer_progress = ttk.Progressbar(
            self.timer_frame,
            orient="horizontal",
            length=300,
            mode="determinate",
            maximum=self.time_limit
        )
        self.timer_progress.pack(pady=5)
        
        # Question text
        question_label = tk.Label(
            self.quiz_frame,
            text=question.text,
            font=("Arial", 16, "bold"),
            wraplength=700,
            justify="center",
            bg="#f0f0f0"
        )
        question_label.pack(pady=(30, 40))
        
        # Options frame
        options_frame = tk.Frame(self.quiz_frame, bg="#f0f0f0")
        options_frame.pack(pady=10)
        
        # Option buttons
        self.option_buttons = []
        option_letters = ["A", "B", "C", "D"]
        
        for i, option in enumerate(question.options):
            button_frame = tk.Frame(options_frame, bg="#f0f0f0")
            button_frame.pack(pady=8, fill="x")
            
            btn = tk.Button(
                button_frame,
                text=f"{option_letters[i]}. {option}",
                font=("Arial", 14),
                bg="#e0e0e0",
                activebackground="#d0d0d0",
                relief=tk.FLAT,
                width=40,
                command=lambda idx=i: self.answer_question(idx)
            )
            btn.pack()
            self.option_buttons.append(btn)
        
        # Start timer
        self.remaining_time = self.time_limit
        self.timer_running = True
        self.update_timer()
    
    def update_timer(self):
        """Update the timer display."""
        if not self.timer_running:
            return
        
        if self.remaining_time <= 0:
            self.timer_label.config(text="Time's up!")
            self.timer_progress["value"] = 0
            self.time_up()
            return
        
        self.timer_label.config(text=f"Time Remaining: {self.remaining_time} seconds")
        self.timer_progress["value"] = self.remaining_time
        
        self.remaining_time -= 1
        self.timer_id = self.root.after(1000, self.update_timer)
    
    def time_up(self):
        """Handle time up event."""
        # Disable option buttons
        for btn in self.option_buttons:
            btn.config(state=tk.DISABLED)
        
        # Highlight correct answer
        correct_idx = self.quiz_questions[self.current_question_index].correct_answer
        self.option_buttons[correct_idx].config(bg="#4CAF50", fg="white")
        
        # Record that user didn't answer
        question = self.quiz_questions[self.current_question_index]
        question.user_answer = None
        question.time_taken = self.time_limit
        
        # Update category stats
        self.category_stats[question.category]["total"] += 1
        
        # Add to history
        self.question_history.append(question)
        
        # Add time to total
        self.total_time += question.time_taken
        
        # Show message
        tk.Label(
            self.quiz_frame,
            text="Time's up! You didn't answer in time.",
            font=("Arial", 12, "bold"),
            fg="#f44336",
            bg="#f0f0f0"
        ).pack(pady=10)
        
        # Next question button
        self.show_next_button()
    
    def answer_question(self, answer_idx):
        """Process the user's answer."""
        # Stop timer
        self.timer_running = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        
        # Calculate time taken
        time_taken = self.time_limit - self.remaining_time
        
        # Record answer
        question = self.quiz_questions[self.current_question_index]
        question.user_answer = answer_idx
        question.time_taken = time_taken
        
        # Update category stats
        self.category_stats[question.category]["total"] += 1
        
        # Add to history
        self.question_history.append(question)
        
        # Add time to total
        self.total_time += time_taken
        
        # Disable option buttons
        for btn in self.option_buttons:
            btn.config(state=tk.DISABLED)
        
        # Check if answer is correct
        correct = answer_idx == question.correct_answer
        
        if correct:
            # Highlight correct answer
            self.option_buttons[answer_idx].config(bg="#4CAF50", fg="white")
            
            # Update score
            self.score += 1
            
            # Update category stats
            self.category_stats[question.category]["correct"] += 1
            
            # Show correct message
            tk.Label(
                self.quiz_frame,
                text="Correct!",
                font=("Arial", 14, "bold"),
                fg="#4CAF50",
                bg="#f0f0f0"
            ).pack(pady=10)
        else:
            # Highlight user's wrong answer
            self.option_buttons[answer_idx].config(bg="#f44336", fg="white")
            
            # Highlight correct answer
            self.option_buttons[question.correct_answer].config(bg="#4CAF50", fg="white")
            
            # Show incorrect message
            tk.Label(
                self.quiz_frame,
                text=f"Incorrect! The correct answer was: {question.options[question.correct_answer]}",
                font=("Arial", 12, "bold"),
                fg="#f44336",
                bg="#f0f0f0"
            ).pack(pady=10)
        
        # Next question button
        self.show_next_button()
    
    def show_next_button(self):
        """Show the next question button."""
        button_text = "Next Question" if self.current_question_index < len(self.quiz_questions) - 1 else "Finish Quiz"
        button_command = self.next_question if self.current_question_index < len(self.quiz_questions) - 1 else self.show_results
        
        next_button = tk.Button(
            self.quiz_frame,
            text=button_text,
            command=button_command,
            font=("Arial", 12),
            bg="#2196F3",
            fg="white",
            padx=15,
            pady=8,
            relief=tk.FLAT
        )
        next_button.pack(pady=20)
    
    def next_question(self):
        """Move to the next question."""
        self.current_question_index += 1
        self.display_current_question()
    
    def show_results(self):
        """Show the quiz results."""
        # Hide quiz frame
        self.quiz_frame.pack_forget()
        
        # Show results frame
        self.results_frame.pack(fill="both", expand=True)
        
        # Clear any existing widgets
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        
        # Results title
        title_label = tk.Label(
            self.results_frame,
            text="Quiz Results",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0"
        )
        title_label.pack(pady=(50, 30))
        
        # Score summary
        score_frame = tk.Frame(self.results_frame, bg="#f0f0f0")
        score_frame.pack(pady=10)
        
        score_percentage = (self.score / len(self.question_history)) * 100
        
        score_label = tk.Label(
            score_frame,
            text=f"Final Score: {self.score}/{len(self.question_history)} ({score_percentage:.1f}%)",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0"
        )
        score_label.pack()
        
        avg_time = self.total_time / len(self.question_history)
        time_label = tk.Label(
            score_frame,
            text=f"Average Time Per Question: {avg_time:.2f} seconds",
            font=("Arial", 12),
            bg="#f0f0f0"
        )
        time_label.pack(pady=5)
        
        # Category performance
        category_frame = tk.LabelFrame(
            self.results_frame,
            text="Performance by Category",
            font=("Arial", 14),
            bg="#f0f0f0",
            padx=15,
            pady=10
        )
        category_frame.pack(pady=20, padx=50, fill="x")
        
        for category, stats in self.category_stats.items():
            if stats["total"] > 0:
                percentage = (stats["correct"] / stats["total"]) * 100
                category_label = tk.Label(
                    category_frame,
                    text=f"{category}: {stats['correct']}/{stats['total']} ({percentage:.1f}%)",
                    font=("Arial", 12),
                    bg="#f0f0f0",
                    anchor="w"
                )
                category_label.pack(fill="x", pady=2)
        
        # Create a notebook for questions review
        review_notebook = ttk.Notebook(self.results_frame)
        review_notebook.pack(pady=20, padx=50, fill="both", expand=True)
        
        # All questions tab
        all_tab = tk.Frame(review_notebook, bg="#f0f0f0")
        review_notebook.add(all_tab, text="All Questions")
        
        # Category tabs
        category_tabs = {}
        for category in self.category_stats.keys():
            tab = tk.Frame(review_notebook, bg="#f0f0f0")
            review_notebook.add(tab, text=category)
            category_tabs[category] = tab
        
        # Add scrollable frame for questions
        all_canvas = tk.Canvas(all_tab, bg="#f0f0f0")
        all_scrollbar = ttk.Scrollbar(all_tab, orient="vertical", command=all_canvas.yview)
        all_scrollable_frame = tk.Frame(all_canvas, bg="#f0f0f0")
        
        all_scrollable_frame.bind(
            "<Configure>",
            lambda e: all_canvas.configure(scrollregion=all_canvas.bbox("all"))
        )
        
        all_canvas.create_window((0, 0), window=all_scrollable_frame, anchor="nw")
        all_canvas.configure(yscrollcommand=all_scrollbar.set)
        
        all_canvas.pack(side="left", fill="both", expand=True, padx=(10, 0))
        all_scrollbar.pack(side="right", fill="y")
        
        # Add questions to all tab
        for i, question in enumerate(self.question_history):
            self.add_question_to_review(all_scrollable_frame, question, i)
        
        # Add category scrollable frames
        for category, tab in category_tabs.items():
            canvas = tk.Canvas(tab, bg="#f0f0f0")
            scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
            scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")
            
            scrollable_frame.bind(
                "<Configure>",
                lambda e, c=canvas: c.configure(scrollregion=c.bbox("all"))
            )
            
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            canvas.pack(side="left", fill="both", expand=True, padx=(10, 0))
            scrollbar.pack(side="right", fill="y")
            
            # Add category-specific questions
            question_index = 0
            for i, question in enumerate(self.question_history):
                if question.category == category:
                    self.add_question_to_review(scrollable_frame, question, question_index)
                    question_index += 1
        
        # Buttons frame
        buttons_frame = tk.Frame(self.results_frame, bg="#f0f0f0")
        buttons_frame.pack(pady=20, padx=20, fill="x")
        
        # New game button
        new_game_button = tk.Button(
            buttons_frame,
            text="New Quiz",
            command=lambda: (self.results_frame.pack_forget(), self.show_settings_screen()),
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            padx=15,
            pady=8,
            relief=tk.FLAT
        )
        new_game_button.pack(side="left", padx=(50, 10))
        
        # Main menu button
        menu_button = tk.Button(
            buttons_frame,
            text="Main Menu",
            command=lambda: (self.results_frame.pack_forget(), self.show_welcome_screen()),
            font=("Arial", 12),
            bg="#2196F3",
            fg="white",
            padx=15,
            pady=8,
            relief=tk.FLAT
        )
        menu_button.pack(side="left", padx=10)
        
        # Exit button
        exit_button = tk.Button(
            buttons_frame,
            text="Exit Game",
            command=self.root.quit,
            font=("Arial", 12),
            bg="#f44336",
            fg="white",
            padx=15,
            pady=8,
            relief=tk.FLAT
        )
        exit_button.pack(side="right", padx=(10, 50))
    
    def add_question_to_review(self, parent_frame, question, index):
        """Add a question to the review tab."""
        # Question frame
        question_frame = tk.LabelFrame(
            parent_frame,
            text=f"Question {index + 1}",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            padx=10,
            pady=10
        )
        question_frame.pack(pady=10, padx=10, fill="x")
        
        # Question text and category
        text_frame = tk.Frame(question_frame, bg="#f0f0f0")
        text_frame.pack(fill="x", pady=5)
        
        question_text = tk.Label(
            text_frame,
            text=question.text,
            font=("Arial", 12),
            wraplength=600,
            justify="left",
            bg="#f0f0f0"
        )
        question_text.pack(side="left")
        
        category_label = tk.Label(
            text_frame,
            text=f"Category: {question.category}",
            font=("Arial", 10),
            fg="#555555",
            bg="#f0f0f0"
        )
        category_label.pack(side="right")
        
        # Options
        for i, option in enumerate(question.options):
            option_frame = tk.Frame(question_frame, bg="#f0f0f0")
            option_frame.pack(fill="x", pady=2)
            
            # Determine background color
            bg_color = "#f0f0f0"
            text_color = "#000000"
            
            if i == question.correct_answer:
                bg_color = "#c8e6c9"  # Light green for correct answer
                text_color = "#2e7d32"
            elif question.user_answer is not None and i == question.user_answer and i != question.correct_answer:
                bg_color = "#ffcdd2"  # Light red for wrong answer
                text_color = "#c62828"
            
            option_label = tk.Label(
                option_frame,
                text=f"{i+1}. {option}",
                font=("Arial", 11),
                bg=bg_color,
                fg=text_color,
                padx=5,
                pady=2,
                anchor="w"
            )
            option_label.pack(fill="x")
        
        # Status
        status_frame = tk.Frame(question_frame, bg="#f0f0f0")
        status_frame.pack(fill="x", pady=5)
        
        if question.user_answer is None:
            status_text = "No answer (Time's up)"
            status_color = "#f44336"
        elif question.user_answer == question.correct_answer:
            status_text = "Correct"
            status_color = "#4CAF50"
        else:
            status_text = f"Incorrect (Chose: {question.options[question.user_answer]})"
            status_color = "#f44336"
        
        # Status label completion
        status_label = tk.Label(
            status_frame,
            text=status_text,
            font=("Arial", 11, "bold"),
            fg=status_color,
            bg="#f0f0f0"
        )
        status_label.pack(side="left")
        
        # Time taken
        time_label = tk.Label(
            status_frame,
            text=f"Time taken: {question.time_taken:.1f} seconds",
            font=("Arial", 10),
            fg="#555555",
            bg="#f0f0f0"
        )
        time_label.pack(side="right")

def main():
    """Main function to run the quiz game."""
    root = tk.Tk()
    app = QuizGameGUI(root)
    
    # Set a custom style for ttk widgets
    style = ttk.Style()
    style.configure("TProgressbar", thickness=20, troughcolor="#e0e0e0", background="#2196F3")
    
    # Center the window on screen
    window_width = 800
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    # Prevent window from being resized too small
    root.minsize(700, 500)
    
    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()