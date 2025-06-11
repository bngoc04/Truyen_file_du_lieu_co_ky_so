from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, 
                            QLineEdit, QPushButton, QCheckBox)

class LoginWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        self.title = QLabel("ĐĂNG NHẬP")
        self.title.setStyleSheet("font-size: 20px; font-weight: bold;")
        
        self.username_label = QLabel("Tên đăng nhập:")
        self.username_input = QLineEdit()
        
        self.password_label = QLabel("Mật khẩu:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        
        self.use_cert_check = QCheckBox("Sử dụng chứng thư số")
        
        self.login_btn = QPushButton("Đăng nhập")
        self.login_btn.clicked.connect(self.parent.switch_to_main)
        
        self.exit_btn = QPushButton("Thoát")
        self.exit_btn.clicked.connect(self.parent.close)
        
        layout.addWidget(self.title)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.use_cert_check)
        layout.addWidget(self.login_btn)
        layout.addWidget(self.exit_btn)
        
        self.setLayout(layout)