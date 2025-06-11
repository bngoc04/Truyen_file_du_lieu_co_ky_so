from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from ui.login_ui import LoginWindow
from ui.main_ui import MainWindow
from ui.sign_ui import SignWindow
from ui.verify_ui import VerifyWindow

class FileTransferApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ứng dụng Truyền File có Ký Số")
        self.resize(800, 600)
        
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        self.login_window = LoginWindow(self)
        self.main_window = MainWindow(self)
        self.sign_window = SignWindow(self)
        self.verify_window = VerifyWindow(self)
        
        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.main_window)
        self.stacked_widget.addWidget(self.sign_window)
        self.stacked_widget.addWidget(self.verify_window)
        
        self.stacked_widget.setCurrentWidget(self.login_window)
    
    def switch_to_main(self):
        self.stacked_widget.setCurrentWidget(self.main_window)
    
    def switch_to_sign(self, file_path):
        self.sign_window.set_file(file_path)
        self.stacked_widget.setCurrentWidget(self.sign_window)
    
    def switch_to_verify(self, file_path):
        self.verify_window.set_file(file_path)
        self.stacked_widget.setCurrentWidget(self.verify_window)