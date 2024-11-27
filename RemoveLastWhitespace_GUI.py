import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout, QFileDialog

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Remove Last Whitespace GUI')
        self.setGeometry(100, 100, 400, 200)

        # Create layout
        layout = QVBoxLayout()

        # Create button to select file
        self.file_button = QPushButton('Select Text File', self)
        self.file_button.clicked.connect(self.load_file)
        layout.addWidget(self.file_button)

        # Create button to process file
        self.process_button = QPushButton('Remove Last Whitespace', self)
        self.process_button.clicked.connect(self.remove_last_whitespace)
        layout.addWidget(self.process_button)

        self.setLayout(layout)

    def load_file(self):
        # Open file dialog to select a text file
        options = QFileDialog.Options()
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Select Text File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if self.file_path:
            QMessageBox.information(self, 'File Selected', f'Selected: {self.file_path}')

    def remove_last_whitespace(self):
        if not hasattr(self, 'file_path') or not os.path.isfile(self.file_path):
            QMessageBox.warning(self, 'Warning', 'No valid file selected.')
            return
        
        output_file = 'output.txt'
        
        with open(self.file_path, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
            lines = f_in.readlines()
            for line in lines:
                f_out.write(line.rstrip() + '\n')
        
        QMessageBox.information(self, 'Success', f'Processed file saved as {output_file}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())