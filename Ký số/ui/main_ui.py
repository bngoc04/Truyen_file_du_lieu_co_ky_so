from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, 
                            QListWidget, QLabel, QPushButton, QFileDialog)

class MainWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.init_ui()
    
    def init_ui(self):
        main_layout = QHBoxLayout()
        
        # Left panel - File list
        left_panel = QVBoxLayout()
        self.file_list = QListWidget()
        self.file_list.itemDoubleClicked.connect(self.show_file_info)
        
        self.add_file_btn = QPushButton("Thêm File")
        self.add_file_btn.clicked.connect(self.add_file)
        
        left_panel.addWidget(QLabel("DANH SÁCH FILE"))
        left_panel.addWidget(self.file_list)
        left_panel.addWidget(self.add_file_btn)
        
        # Right panel - File info
        right_panel = QVBoxLayout()
        self.file_info_label = QLabel("THÔNG TIN FILE")
        self.file_name = QLabel("Tên file: ")
        self.file_type = QLabel("Loại file: ")
        self.file_size = QLabel("Kích thước: ")
        self.file_date = QLabel("Ngày tạo: ")
        self.file_status = QLabel("Trạng thái: ")
        
        self.sign_btn = QPushButton("Ký số")
        self.sign_btn.clicked.connect(self.sign_file)
        self.send_btn = QPushButton("Gửi")
        
        right_panel.addWidget(self.file_info_label)
        right_panel.addWidget(self.file_name)
        right_panel.addWidget(self.file_type)
        right_panel.addWidget(self.file_size)
        right_panel.addWidget(self.file_date)
        right_panel.addWidget(self.file_status)
        right_panel.addWidget(self.sign_btn)
        right_panel.addWidget(self.send_btn)
        
        main_layout.addLayout(left_panel, 60)
        main_layout.addLayout(right_panel, 40)
        
        self.setLayout(main_layout)
    
    def add_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Chọn file")
        if file_path:
            self.file_list.addItem(file_path)
    
    def show_file_info(self, item):
        file_path = item.text()
        self.file_name.setText(f"Tên file: {file_path}")
    
    def sign_file(self):
        selected_items = self.file_list.selectedItems()
        if selected_items:
            file_path = selected_items[0].text()
            self.parent.switch_to_sign(file_path)