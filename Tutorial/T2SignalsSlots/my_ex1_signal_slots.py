import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

# creating the mainwindow object
class MainWindow(QMainWindow):
    
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My example App")
        self.mainwindow_title = ""

        ## left side of the app ##
        self.label_left = QLabel()
        self.label_left.setText("Name")
        
        self.label_name = QLabel()
        self.input_name = QLineEdit()
        # connect textChanged signal from input_name to the label directly
        self.input_name.textChanged.connect(self.label_name.setText)

        self.confirm_name_btn = QPushButton()
        self.confirm_name_btn.setText("Confirm")
        self.confirm_name_btn.setCheckable(True)
        self.confirm_name_btn.clicked.connect(self.confirm_name_btn_clicked)

        layout_left = QVBoxLayout()
        layout_left.addWidget(self.label_left)
        layout_left.addWidget(self.input_name)
        layout_left.addWidget(self.label_name)
        layout_left.addWidget(self.confirm_name_btn)

        ## right side of the app ##
        self.label_right = QLabel()
        self.label_right.setText("Age")
        
        self.label_age = QLabel()
        self.input_age = QLineEdit()
        # connect textChanged signal from input_age to its label directly
        self.input_age.textChanged.connect(self.label_age.setText)

        self.confirm_age_btn = QPushButton()
        self.confirm_age_btn.setText("Confirm")
        self.confirm_age_btn.setCheckable(True)
        self.confirm_age_btn.clicked.connect(self.confirm_age_btn_clicked)

        layout_right = QVBoxLayout()
        layout_right.addWidget(self.label_right)
        layout_right.addWidget(self.input_age)
        layout_right.addWidget(self.label_age)
        layout_right.addWidget(self.confirm_age_btn)

        # create a general layout
        layout = QHBoxLayout()

        # create left side widget
        container_left = QWidget()
        container_left.setLayout(layout_left)

        # create right side widget
        container_right = QWidget()
        container_right.setLayout(layout_right)
        
        # place the left and right side widgets
        layout.addWidget(container_left)
        layout.addWidget(container_right)

        # create container
        container = QWidget()
        container.setLayout(layout)
        
        # set the central widget of the window
        self.setCentralWidget(container)

    def confirm_name_btn_clicked(self, clicked):
        print(f"Confirm Name Button clicked?: {clicked}")
        self.mainwindow_title = f"{self.input_name.text()}-{self.input_age.text()}"
        self.setWindowTitle(self.mainwindow_title)

    def confirm_age_btn_clicked(self, clicked):
        print(f"Confirm Age Button clicked?: {clicked}")
        self.mainwindow_title = f"{self.input_name.text()}-{self.input_age.text()}"
        self.setWindowTitle(self.mainwindow_title)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
