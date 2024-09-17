from PySide6.QtWidgets import QApplication
from GUI.gui import DocuFlareGUI
import sys

def main():
    """
    Entry point for the DocuFlare application.
    Initializes and starts the PySide6 GUI.
    """
    app = QApplication(sys.argv)
    window = DocuFlareGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
