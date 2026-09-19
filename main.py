from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from game_logic import NumberGuessGame


class GuessNumberRoot(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = dp(24)
        self.spacing = dp(16)
        self.game = NumberGuessGame(1, 100)

        self.title_label = Label(
            text="Guess the Number",
            font_size="30sp",
            size_hint_y=None,
            height=dp(60),
        )
        self.add_widget(self.title_label)

        self.instructions_label = Label(
            text="I chose a number from 1 to 100.\nEnter your guess below.",
            font_size="19sp",
            halign="center",
            valign="middle",
        )
        self.instructions_label.bind(size=self._update_text_size)
        self.add_widget(self.instructions_label)

        self.number_input = TextInput(
            hint_text="Enter a number (1-100)",
            multiline=False,
            input_filter="int",
            font_size="24sp",
            halign="center",
            size_hint_y=None,
            height=dp(58),
        )
        self.number_input.bind(on_text_validate=self.check_guess)
        self.add_widget(self.number_input)

        self.guess_button = Button(
            text="Guess",
            font_size="22sp",
            size_hint_y=None,
            height=dp(58),
        )
        self.guess_button.bind(on_release=self.check_guess)
        self.add_widget(self.guess_button)

        self.result_label = Label(
            text="Good luck!",
            font_size="22sp",
            halign="center",
            valign="middle",
        )
        self.result_label.bind(size=self._update_text_size)
        self.add_widget(self.result_label)

        self.attempts_label = Label(
            text="Attempts: 0",
            font_size="17sp",
            size_hint_y=None,
            height=dp(42),
        )
        self.add_widget(self.attempts_label)

        self.new_game_button = Button(
            text="New Game",
            font_size="20sp",
            size_hint_y=None,
            height=dp(54),
        )
        self.new_game_button.bind(on_release=self.new_game)
        self.add_widget(self.new_game_button)

    @staticmethod
    def _update_text_size(widget, size):
        widget.text_size = size

    def check_guess(self, *_args):
        raw_value = self.number_input.text.strip()

        if not raw_value:
            self.result_label.text = "Please enter a number from 1 to 100."
            return

        try:
            value = int(raw_value)
            result = self.game.guess(value)
        except ValueError:
            self.result_label.text = "Please enter a whole number from 1 to 100."
            return

        self.attempts_label.text = f"Attempts: {self.game.attempts}"

        if result == "higher":
            self.result_label.text = "Too low — try a HIGHER number."
            self.number_input.select_all()
        elif result == "lower":
            self.result_label.text = "Too high — try a LOWER number."
            self.number_input.select_all()
        else:
            self.result_label.text = (
                f"Correct! The number was {self.game.secret_number}.\n"
                f"You found it in {self.game.attempts} attempts."
            )
            self.guess_button.disabled = True
            self.number_input.disabled = True

    def new_game(self, *_args):
        self.game.reset()
        self.number_input.disabled = False
        self.guess_button.disabled = False
        self.number_input.text = ""
        self.result_label.text = "New number chosen. Good luck!"
        self.attempts_label.text = "Attempts: 0"
        self.number_input.focus = True


class GuessNumberApp(App):
    def build(self):
        self.title = "Guess the Number"
        Window.softinput_mode = "below_target"
        return GuessNumberRoot()


if __name__ == "__main__":
    GuessNumberApp().run()
