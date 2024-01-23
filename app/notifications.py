from tkinter import messagebox

class Notifications:
    @staticmethod
    def show_word_dialogue(word, meaning):
        messagebox.showinfo("Word of the Day", f"Word: {word}\nMeaning: {meaning}")
