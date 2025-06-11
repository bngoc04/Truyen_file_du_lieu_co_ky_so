from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, 
                            QPushButton)

class VerifyWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.file_path = ""
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        self.title = QLabel("XÁC THỰC CHỮ KÝ")
        self.title.setStyleSheet("font-size: 18px; font-weight: bold;")
        
        self.file_label = QLabel("File: ")
        self.status_label = QLabel("Chữ ký số: ")
        
        self.signer_label = QLabel("Thông tin người ký:")
        self.signer_name = QLabel("- Tên: ")
        self.signer_org = QLabel("- Tổ chức: ")
        self.signer_serial = QLabel("- Serial: ")
        self.signer_time = QLabel("- Thời gian ký: ")
        
        self.algo_label = QLabel("Thuật toán: ")
        self.provider_label = QLabel("Nhà cung cấp: ")
        
        self.close_btn = QPushButton("Đóng")
        self.close_btn.clicked.connect(lambda: self.parent.switch_to_main())
        
        self.export_btn = QPushButton("Xuất báo cáo")
        
        layout.addWidget(self.title)
        layout.addWidget(self.file_label)
        layout.addWidget(self.status_label)
        layout.addWidget(self.signer_label)
        layout.addWidget(self.signer_name)
        layout.addWidget(self.signer_org)
        layout.addWidget(self.signer_serial)
        layout.addWidget(self.signer_time)
        layout.addWidget(self.algo_label)
        layout.addWidget(self.provider_label)
        layout.addWidget(self.close_btn)
        layout.addWidget(self.export_btn)
        
        self.setLayout(layout)
    
    def set_file(self, file_path):
        self.file_path = file_path
        self.file_label.setText(f"File: {file_path}")
        # Giả lập thông tin xác thực
        self.status_label.setText("Chữ ký số: Hợp lệ")
        self.signer_name.setText("- Tên: Nguyễn Văn A")
        self.signer_org.setText("- Tổ chức: Công ty ABC")
        self.signer_serial.setText("- Serial: 1234-5678-90AB")
        self.signer_time.setText("- Thời gian ký: 10:30 20/11/2023")
        self.algo_label.setText("Thuật toán: RSA-256")
        self.provider_label.setText("Nhà cung cấp: VNPT-CA")