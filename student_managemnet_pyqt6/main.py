import sqlite3
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

import sys


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add New Student")
        self.setFixedWidth(300)
        self.setFixedHeight(250)

        layout = QVBoxLayout()

        # Add student name widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Enter student name")
        layout.addWidget(QLabel("Student Name:"))
        layout.addWidget(self.student_name)

        # Add course combo box
        self.course_box = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics", "Chemistry"]
        self.course_box.addItems(courses)
        layout.addWidget(QLabel("Course:"))
        layout.addWidget(self.course_box)

        # Add mobile number field
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Enter mobile number")
        layout.addWidget(QLabel("Mobile:"))
        layout.addWidget(self.mobile)

        # Add submit button
        button_layout = QHBoxLayout()
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.add_student)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.close)

        button_layout.addWidget(submit_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_box.currentText()
        mobile = self.mobile.text()

        if not name or not mobile:
            QMessageBox.warning(self, "Warning", "Please fill all fields")
            return

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
                       (name, course, mobile))
        connection.commit()
        connection.close()

        QMessageBox.information(self, "Success", "Student added successfully!")
        self.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.insert)  # Connect to insert method
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()
        self.load_data()  # Refresh the table after adding a student

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()


# Create database and table if they don't exist
def initialize_database():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            course TEXT NOT NULL,
            mobile TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()


app = QApplication(sys.argv)
initialize_database()  # Initialize database before creating the main window
age_calculator = MainWindow()
age_calculator.load_data()
age_calculator.show()
sys.exit(app.exec())