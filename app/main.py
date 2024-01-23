# main.py in app package
import sys
sys.path.append('/Users/roshan1610/Desktop/language-mastery-app')

from tkinter import Tk, Label, Button, Scale, messagebox
from datetime import datetime
from notifications import Notifications
from word_api import WordAPI
import plyer
from tkinter import simpledialog
from shared.words_api_logic import get_word_data


class LearnWordApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Learn_Word App")

        self.label = Label(self.root, text="Welcome to Learn_Word!")
        self.label.pack()

       # Difficulty Level Scale
        self.difficulty_scale_label = Label(self.root, text="Set Difficulty Level:", foreground="black")
        self.difficulty_scale = Scale(self.root, from_=1, to=5, orient="horizontal", length=200)
        self.difficulty_scale_label.pack()
        self.difficulty_scale.pack()

        # Set Notification Time Button
        self.notification_button = Button(self.root, text="Set Notification Time", command=self.set_notification_time)
        self.notification_button.pack()

        # Get Word of the Day Button
        self.word_button = Button(self.root, text="Get Word of the Day", command=self.get_word_of_the_day)
        self.word_button.pack()

    def set_notification_time(self):
         # Ask the user for notification time
        notification_time = simpledialog.askstring(
            "Set Notification Time", "Enter notification time (HH:MM:SS):"
        )

        if notification_time:
            # Schedule a notification
            plyer.notification.schedule(
                title="Learn_Word Notification",
                message="It's time to learn a new word!",
                timeout=10,  # Notification will be shown for 10 seconds
                ticker="Learn_Word",
                app_icon=None,  # e.g., 'path/to/app_icon.ico'
                toast=False,  # Whether to use Windows Toast Notifications
                toast_once=True,  # Show the toast only once
                cronstring=f"0 {notification_time.split(':')[1]} {notification_time.split(':')[0]} * *"
            )
        

    def get_word_of_the_day(self):
        # Get a new word and its meaning from the API
        api_response = WordAPI().get()

        # Print API response for debugging
        print("API Response:", api_response)
        word = api_response["word"]
        meaning = api_response["meaning"]

        

        # Show word dialogue with meaning
        Notifications.show_word_dialogue(word, meaning)
   
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = LearnWordApp()
    app.run()
