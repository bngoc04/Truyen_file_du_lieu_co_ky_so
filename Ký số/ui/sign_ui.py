from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, 
                            QComboBox, QLineEdit, QPushButton)

class SignWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.file_path = ""
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        self.title = QLabel("KÝ SỐ FILE")
        self.title.setStyleSheet("font-size: 18px; font-weight: bold;")
        
        self.file_label = QLabel("File: ")
        self.size_label = QLabel("Kích thước: ")
        
        self.cert_label = QLabel("Chọn chứng thư số:")
        self.cert_combo = QComboBox()
        self.cert_combo.addItems(["Chứng thư cá nhân - VNPT-CA", "Chứng thư doanh nghiệp - CA2"])
        
        self.pass_label = QLabel("Mật khẩu chứng thư:")
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)
        
        self.algo_label = QLabel("Thuật toán ký:")
        self.algo_combo = QComboBox()
        self.algo_combo.addItems(["RSA-256", "RSA-512", "ECDSA"])
        
        self.view_cert_btn = QPushButton("Xem trước chứng thư")
        
        self.sign_btn = QPushButton("Ký số")
        self.sign_btn.clicked.connect(self.sign_file)
        
        self.cancel_btn = QPushButton("Hủy")
        self.cancel_btn.clicked.connect(lambda: self.parent.switch_to_main())
        
        layout.addWidget(self.title)
        layout.addWidget(self.file_label)
        layout.addWidget(self.size_label)
        layout.addWidget(self.cert_label)
        layout.addWidget(self.cert_combo)
        layout.addWidget(self.pass_label)
        layout.addWidget(self.pass_input)
        layout.addWidget(self.algo_label)
        layout.addWidget(self.algo_combo)
        layout.addWidget(self.view_cert_btn)
        layout.addWidget(self.sign_btn)
        layout.addWidget(self.cancel_btn)
        
        self.setLayout(layout)
    
    def set_file(self, file_path):
        self.file_path = file_path
        self.file_label.setText(f"File: {file_path}")
    
    def sign_file(self):
        print(f"Ký số file: {self.file_path}")
        self.parent.switch_to_main()