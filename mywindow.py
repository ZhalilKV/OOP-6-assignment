from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('bmi.ui', self)

        # Connect signals
        self.btn_calculate.clicked.connect(self.calculate_bmi)
        self.actionExit.triggered.connect(self.close)
        self.actionClear.triggered.connect(self.clear_fields)
        self.actionAbout.triggered.connect(self.show_about)

    def calculate_bmi(self):
        try:
            weight = float(self.edit_weight.text())
            height = float(self.edit_height.text())

            if self.radio_metric.isChecked():
                bmi = weight / (height ** 2)
            else:
                # Convert imperial to metric
                weight *= 0.453592
                height *= 0.0254
                bmi = weight / (height ** 2)

            self.label_result.setText(f'BMI: {bmi:.2f}')

            if bmi < 18.5:
                status = 'Underweight'
            elif 18.5 <= bmi < 25:
                status = 'Normal'
            elif 25 <= bmi < 30:
                status = 'Overweight'
            else:
                status = 'Obese'
            self.label_status.setText(f'Status: {status}')

        except ValueError:
            QMessageBox.warning(self, 'Error', 'Please enter valid numbers!')

    def clear_fields(self):
        self.edit_weight.clear()
        self.edit_height.clear()
        self.label_result.setText('BMI: ')
        self.label_status.setText('Status: ')

    def show_about(self):
        QMessageBox.information(self, 'Help',
                                'Enter your weight and height in selected units\n'
                                'Click Calculate to get your BMI and status.')