import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class AdvancedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Advanced Calculator')
        self.setGeometry(100, 100, 400, 600)
        self.setStyleSheet("background-color: #2E2E2E; color: #FFFFFF;")  # Dark background with white text

        # Create main layout
        vbox = QVBoxLayout()

        # Display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(60)
        self.display.setFont(QFont('Arial', 20))
        self.display.setStyleSheet("background-color: #1E1E1E; border: 1px solid #444444; padding: 10px;")
        vbox.addWidget(self.display)

        # Button layout
        grid = QGridLayout()
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', 'x', '(',
            '1', '2', '3', '-', ')',
            '0', '.', '=', '+', 'sqrt',
            'sin', 'cos', 'tan', 'log'
        ]

        row, col = 0, 0
        for button in buttons:
            btn = QPushButton(button)
            btn.setFont(QFont('Arial', 16))
            if button == 'C':
                btn.setStyleSheet("background-color: #FF4C4C; border: none; color: #FFFFFF; padding: 15px;")
            else:
                btn.setStyleSheet("background-color: #444444; border: none; color: #FFFFFF; padding: 15px;")
            btn.clicked.connect(self.on_button_click)
            grid.addWidget(btn, row, col, 1, 1)
            col += 1
            if col > 4:
                col = 0
                row += 1

        vbox.addLayout(grid)
        self.setLayout(vbox)

    def on_button_click(self):
        sender = self.sender().text()
        current_text = self.display.text()

        if sender == 'C':
            self.display.clear()
        elif sender == '=':
            try:
                result = str(eval(current_text))
                self.display.setText(result)
            except Exception as e:
                self.display.setText("Error")
        elif sender == 'sqrt':
            try:
                value = float(current_text)
                result = str(math.sqrt(value))
                self.display.setText(result)
            except Exception as e:
                self.display.setText("Error")
        elif sender == 'sin':
            try:
                value = float(current_text)
                result = str(math.sin(math.radians(value)))
                self.display.setText(result)
            except Exception as e:
                self.display.setText("Error")
        elif sender == 'cos':
            try:
                value = float(current_text)
                result = str(math.cos(math.radians(value)))
                self.display.setText(result)
            except Exception as e:
                self.display.setText("Error")
        elif sender == 'tan':
            try:
                value = float(current_text)
                result = str(math.tan(math.radians(value)))
                self.display.setText(result)
            except Exception as e:
                self.display.setText("Error")
        elif sender == 'log':
            try:
                value = float(current_text)
                result = str(math.log10(value))
                self.display.setText(result)
            except Exception as e:
                self.display.setText("Error")
        else:
            self.display.setText(current_text + sender)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = AdvancedCalculator()
    calc.show()
    sys.exit(app.exec_())
