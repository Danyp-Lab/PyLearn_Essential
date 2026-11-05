import ast
import math
import operator
import sys
from functools import partial

from PyQt6.QtWidgets import QApplication, QGridLayout, QLineEdit, QPushButton, QWidget

_SAFE_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
    ast.Pow: operator.pow,
}

_SAFE_FUNCS = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "sqrt": math.sqrt,
}


def safe_math_eval(expr: str):
    tree = ast.parse(expr.strip(), mode="eval")

    def _eval(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        elif isinstance(node, ast.BinOp) and type(node.op) in _SAFE_OPS:
            return _SAFE_OPS[type(node.op)](_eval(node.left), _eval(node.right))
        elif isinstance(node, ast.UnaryOp) and type(node.op) in _SAFE_OPS:
            return _SAFE_OPS[type(node.op)](_eval(node.operand))
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in _SAFE_FUNCS:
            args = [_eval(a) for a in node.args]
            return _SAFE_FUNCS[node.func.id](*args)
        raise ValueError("Unsupported expression")

    return _eval(tree.body)


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
                result = str(safe_math_eval(self.line_edit.text()))
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
