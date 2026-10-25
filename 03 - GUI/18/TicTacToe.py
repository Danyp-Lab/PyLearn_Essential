import sys
from functools import partial

from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QRadioButton,
    QWidget,
)


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.player_turn = True
        self.board = ["" for _ in range(9)]
        self.winner = None
        self.score = {"X": 0, "O": 0, "Draw": 0}

    def initUI(self):
        self.setWindowTitle("Tic Tac Toe")
        self.gridLayout = QGridLayout()
        self.createBoard()
        self.createScoreboard()
        self.createGameOptions()
        self.setLayout(self.gridLayout)

    def createBoard(self):
        for i in range(3):
            for j in range(3):
                button = QPushButton("")
                button.setFixedSize(100, 100)
                button.clicked.connect(partial(self.onButtonClick, i, j))
                self.gridLayout.addWidget(button, i, j)

    def createScoreboard(self):
        self.scoreboard = QLabel("X: 0 - O: 0 - Draws: 0")
        self.gridLayout.addWidget(self.scoreboard, 3, 0, 1, 3)

    def createGameOptions(self):
        self.newGameButton = QPushButton("New Game")
        self.newGameButton.clicked.connect(self.newGame)
        self.gridLayout.addWidget(self.newGameButton, 4, 0, 1, 3)

        self.playerVsPlayer = QRadioButton("Player vs Player")
        self.playerVsPlayer.setChecked(True)
        self.playerVsCpu = QRadioButton("Player vs CPU")
        self.gameModeLayout = QHBoxLayout()
        self.gameModeLayout.addWidget(self.playerVsPlayer)
        self.gameModeLayout.addWidget(self.playerVsCpu)
        self.gridLayout.addLayout(self.gameModeLayout, 5, 0, 1, 3)

        self.aboutButton = QPushButton("About")
        self.aboutButton.clicked.connect(self.showAbout)
        self.gridLayout.addWidget(self.aboutButton, 6, 0, 1, 3)

    def onButtonClick(self, i, j):
        # Game logic here
        pass

    def newGame(self):
        # Reset the game
        pass

    def showAbout(self):
        QMessageBox.information(self, "About", "Tic Tac Toe Game created with PyQt6.")

    def checkWinner(self):
        # Check for winner or draw
        pass

    def updateScoreboard(self):
        self.scoreboard.setText(
            f"X: {self.score['X']} - O: {self.score['O']} - Draws: {self.score['Draw']}"
        )


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TicTacToe()
    ex.show()
    sys.exit(app.exec())
