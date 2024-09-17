from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox, QProgressBar
from PySide6.QtCore import Qt
import sys
from Utils.file_handler import FileHandler

class DocuFlareGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DocuFlare - File to PDF Converter')
        self.setGeometry(300, 300, 500, 300)

        self.layout = QVBoxLayout()

        self.file_label = QLabel("No files selected.")
        self.file_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.file_label)

        self.select_file_button = QPushButton('Select Files to Convert')
        self.select_file_button.clicked.connect(self.select_files)
        self.layout.addWidget(self.select_file_button)

        self.output_label = QLabel("No output folder selected.")
        self.output_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.output_label)

        self.select_output_button = QPushButton('Select Output Folder')
        self.select_output_button.clicked.connect(self.select_output_folder)
        self.layout.addWidget(self.select_output_button)

        self.convert_button = QPushButton('Convert to PDF')
        self.convert_button.setEnabled(False)
        self.convert_button.clicked.connect(self.convert_files)
        self.layout.addWidget(self.convert_button)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.progress_bar)

        self.setLayout(self.layout)
        self.setContentsMargins(20, 20, 20, 20)

        self.selected_files = []
        self.output_folder = ""

    def select_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, 'Select Files', '',
                                                'Documents (*.docx *.pptx *.xlsx *.txt *.md);;Images (*.jpg *.png);;ZIP Files (*.zip)')
        if files:
            self.selected_files = files
            self.file_label.setText(f"{len(files)} files selected.")
            self.convert_button.setEnabled(True)
        else:
            self.file_label.setText("No files selected.")
            self.convert_button.setEnabled(False)

    def select_output_folder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select Output Folder')
        if folder:
            self.output_folder = folder
            self.output_label.setText(f"Output folder: {self.output_folder}")
        else:
            self.output_label.setText("No output folder selected.")

    def convert_files(self):
        if not self.output_folder:
            self.show_message("Error", "Please select an output folder!", QMessageBox.Warning)
            return

        self.convert_button.setEnabled(False)
        self.progress_bar.setValue(0)

        total_files = len(self.selected_files)
        for idx, file in enumerate(self.selected_files, start=1):
            suggested_name = f"converted_{idx}.pdf"
            output_path, _ = QFileDialog.getSaveFileName(self, 'Save PDF As',
                                                         f"{self.output_folder}/{suggested_name}",
                                                         'PDF Files (*.pdf)')
            if not output_path:
                self.show_message("Error", f"Output file not specified for {file}", QMessageBox.Warning)
                continue

            handler = FileHandler(file, output_path)
            success, message = handler.convert_file()

            if success:
                self.progress_bar.setValue(int((idx / total_files) * 100))
            else:
                self.show_message("Error", f"Failed to convert {file}: {message}", QMessageBox.Critical)

        self.convert_button.setEnabled(True)
        self.show_message("Success", "All files converted successfully!", QMessageBox.Information)

    def show_message(self, title, message, icon_type):
        msg_box = QMessageBox(self)
        msg_box.setIcon(icon_type)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DocuFlareGUI()
    window.show()
    sys.exit(app.exec())
