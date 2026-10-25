import sys
from functools import partial

from PyQt6.QtWidgets import QApplication, QGridLayout, QLineEdit, QPushButton, QWidget


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.initUI()

    def initUI(self):
        # Create grid layout
        gridLayout = QGridLayout()

        # Create line edit for input and output
        self.line_edit = QLineEdit()
        gridLayout.addWidget(self.line_edit, 0, 0, 1, 4)

        # Create buttons
        buttons = {
            "sin": (1, 0),
            "cos": (1, 1),
            "tan": (1, 2),
            "cot": (1, 3),
            "log": (2, 0),
            "sqrt": (2, 1),
            "C": (2, 2),
            "=": (2, 3),
        }

        for btnText, pos in buttons.items():
            button = QPushButton(btnText)
            button.clicked.connect(partial(self.onButtonClick, btnText))
            gridLayout.addWidget(button, pos[0], pos[1])

        # Set layout
        self.setLayout(gridLayout)

    def onButtonClick(self, button_text):
        if button_text == "C":
            self.line_edit.clear()
        elif button_text == "=":
            try:
                result = str(eval(self.line_edit.text()))
                self.line_edit.setText(result)
            except Exception:
                self.line_edit.setText("Error")
        elif button_text == "cot":
            self.line_edit.insert("1/tan(")
        else:
            self.line_edit.insert(f"{button_text}(")


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CalculatorApp()
    ex.show()
    sys.exit(app.exec())
