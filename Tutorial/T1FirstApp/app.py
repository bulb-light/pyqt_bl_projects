import sys # only needed for access to command line arguments
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    """
    Custom subclass of QMainWindow
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Awesome App")

        button = QPushButton("Press Me")

        # Uncomment the following line for fixed size window
        # self.setFixedSize(QSize(400, 300))

        # Uncomment the following lines to set the max and min size of the window
        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(700, 600))

        # set the central widget of the window
        self.setCentralWidget(button)

#NOTE: You need one (and only one) QApplication instance per application
# Pass in sys.argv to allow command line arguments for your app
# or [] if command line arguments are not going to be used

app = QApplication(sys.argv)

# create a Qt widget, which will be our window.
# any widgets created can be windows
# window = QWidget()
# window = QPushButton("Push me")
# window = QMainWindow()

window = MainWindow()
window.show() #NOTE: windows are hidden by default

# start the event loop
app.exec()

# The application won't reach here until the event loop has finished
print("The Window was closed")
