import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QLabel, QVBoxLayout, QWidget

# connecting widgets together directly

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()

        self.input = QLineEdit()
        # connects textChanged signal from input to the label directly
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # set the central widget of the window
        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
