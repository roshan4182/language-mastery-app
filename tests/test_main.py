import unittest
from unittest.mock import patch, Mock
from notifications import Notifications
from app.main import LearnWordApp

class TestNotifications(unittest.TestCase):
    @patch('tkinter.messagebox.showinfo')
    def test_show_word_dialogue(self, mock_showinfo):
        Notifications.show_word_dialogue("Test Word", "Test Definition")
        mock_showinfo.assert_called_once_with(
            "Word of the Day", "Word: Test Word\ndefinition: Test Definition"
        )

class TestLearnWordApp(unittest.TestCase):
    @patch('tkinter.simpledialog.askstring', return_value='12:00:00')
    @patch('plyer.notification.schedule')
    def test_set_notification_time(self, mock_schedule, mock_askstring):
        app = LearnWordApp()
        app.set_notification_time()
        mock_askstring.assert_called_once_with(
            "Set Notification Time", "Enter notification time (HH:MM:SS):"
        )
        mock_schedule.assert_called_once_with(
            title="Learn_Word Notification",
            message="It's time to learn a new word!",
            timeout=10,
            ticker="Learn_Word",
            app_icon=None,
            toast=False,
            toast_once=True,
            cronstring="0 0 12 * *"
        )

    @patch('app.LearnWordApp.get_word_of_the_day')
    def test_button_click(self, mock_get_word_of_the_day):
        app = LearnWordApp()
        app.word_button.invoke()
        mock_get_word_of_the_day.assert_called_once()

if __name__ == '__main__':
    unittest.main()
