import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# Signal and slot first example
# connect button clicked signal to a user-defined slot
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button_is_checked = True

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        # button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)

        # set the central widget of the window
        self.setCentralWidget(button)

    # def the_button_was_clicked(self):
    #     print("Clicked!")

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked

        print("Clicked?", self.button_is_checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
