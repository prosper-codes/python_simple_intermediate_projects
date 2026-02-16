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

        # Create menu items
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")

        # Add Student action
        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        # About action
        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        # Search action
        search_action = QAction("Search", self)
        search_action.triggered.connect(self.search)
        edit_menu_item.addAction(search_action)

        # Create table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        # Create toolbar
        toolbar = self.addToolBar("Toolbar")
        toolbar.setMovable(False)

        # Add search box to toolbar
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search by name...")
        self.search_box.textChanged.connect(self.search_students)  # Real-time search
        toolbar.addWidget(self.search_box)

        # Add search button to toolbar
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_students)
        toolbar.addWidget(search_button)

        # Add clear search button
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_search)
        toolbar.addWidget(clear_button)

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()
        self.load_data()  # Refresh the table after adding a student

    def load_data(self):
        """Load all students from database"""
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def search(self):
        """Open search dialog"""
        dialog = SearchDialog(self)
        dialog.exec()

    def search_students(self):
        """Search students by name (real-time)"""
        search_text = self.search_box.text().strip()

        if search_text:
            # Search with wildcards for partial matching
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM students WHERE name LIKE ?", (f'%{search_text}%',))
            results = cursor.fetchall()

            self.table.setRowCount(0)
            for row_number, row_data in enumerate(results):
                self.table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            connection.close()
        else:
            # If search box is empty, show all students
            self.load_data()

    def clear_search(self):
        """Clear search box and show all students"""
        self.search_box.clear()
        self.load_data()


class SearchDialog(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Search Students")
        self.setFixedWidth(300)
        self.setFixedHeight(150)

        layout = QVBoxLayout()

        # Search input
        layout.addWidget(QLabel("Enter student name:"))
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Name...")
        layout.addWidget(self.search_input)

        # Buttons
        button_layout = QHBoxLayout()
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.perform_search)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.close)

        button_layout.addWidget(search_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def perform_search(self):
        search_text = self.search_input.text().strip()

        if search_text:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM students WHERE name LIKE ?", (f'%{search_text}%',))
            results = cursor.fetchall()

            # Clear and update the main window's table
            self.main_window.table.setRowCount(0)
            for row_number, row_data in enumerate(results):
                self.main_window.table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.main_window.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            if not results:
                QMessageBox.information(self, "No Results", f"No students found with name '{search_text}'")

            connection.close()
            self.close()
        else:
            QMessageBox.warning(self, "Warning", "Please enter a search term")


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