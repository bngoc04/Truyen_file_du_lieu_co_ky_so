import sys
from PyQt5.QtWidgets import QApplication
from app import FileTransferApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Load stylesheet
    try:
        with open('assets/styles.css', 'r') as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Warning: styles.css not found")
    
    window = FileTransferApp()
    window.show()
    sys.exit(app.exec_())