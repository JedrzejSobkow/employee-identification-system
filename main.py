# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets # type: ignore
from PyQt5.QtCore import Qt

from firebase_utils import *

class EmployeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_connections()

        # Initialize Firebase here or earlier during app setup
        initialize_firebase()
        self.db_ref = get_database_reference('Database reference')
        print(self.db_ref.get())

    def setup_ui(self):
        # Inicjalizacja
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Tytuł aplikacji
        self.labelTitle = QtWidgets.QLabel("System Identyfikacji Pracowników", self.centralwidget)
        self.labelTitle.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.labelTitle)

        # Zakładki (Rejestracja, Pracownicy, Logi Dostępów)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.verticalLayout.addWidget(self.tabWidget)

        # Zakładka Rejestracja
        self.tabRegister = QtWidgets.QWidget()
        self.formLayoutRegister = QtWidgets.QFormLayout(self.tabRegister)
        self.labelName = QtWidgets.QLabel("Imię i Nazwisko:", self.tabRegister)
        self.lineEditName = QtWidgets.QLineEdit(self.tabRegister)
        self.formLayoutRegister.addRow(self.labelName, self.lineEditName)
        self.labelDepartment = QtWidgets.QLabel("Dział:", self.tabRegister)
        self.lineEditDepartment = QtWidgets.QLineEdit(self.tabRegister)
        self.formLayoutRegister.addRow(self.labelDepartment, self.lineEditDepartment)

        # Sekcja Dostęp do sal
        self.labelAccess = QtWidgets.QLabel("Dostęp do sal:", self.tabRegister)
        self.formLayoutRegister.addRow(self.labelAccess)
        self.groupBoxAccess = QtWidgets.QGroupBox(self.tabRegister)
        self.verticalLayoutAccess = QtWidgets.QVBoxLayout(self.groupBoxAccess)
        self.checkBoxSala1 = QtWidgets.QCheckBox("Sala 1", self.groupBoxAccess)
        self.checkBoxSala2 = QtWidgets.QCheckBox("Sala 2", self.groupBoxAccess)
        self.checkBoxSala3 = QtWidgets.QCheckBox("Sala 3", self.groupBoxAccess)
        self.checkBoxSala4 = QtWidgets.QCheckBox("Sala 4", self.groupBoxAccess)
        self.checkBoxSala5 = QtWidgets.QCheckBox("Sala 5", self.groupBoxAccess)
        self.checkBoxSala6 = QtWidgets.QCheckBox("Sala 6", self.groupBoxAccess)
        self.verticalLayoutAccess.addWidget(self.checkBoxSala1)
        self.verticalLayoutAccess.addWidget(self.checkBoxSala2)
        self.verticalLayoutAccess.addWidget(self.checkBoxSala3)
        self.verticalLayoutAccess.addWidget(self.checkBoxSala4)
        self.verticalLayoutAccess.addWidget(self.checkBoxSala5)
        self.verticalLayoutAccess.addWidget(self.checkBoxSala6)
        self.formLayoutRegister.addRow(self.groupBoxAccess)

        # Przyciski
        self.buttonSave = QtWidgets.QPushButton("Zapisz", self.tabRegister)
        self.formLayoutRegister.addWidget(self.buttonSave)
        self.tabWidget.addTab(self.tabRegister, "Rejestracja")

        # Zakładka Pracownicy
        self.tabEmployees = QtWidgets.QWidget()
        self.verticalLayoutEmployees = QtWidgets.QVBoxLayout(self.tabEmployees)
        self.tableEmployees = QtWidgets.QTableWidget(0, 2, self.tabEmployees)
        self.tableEmployees.setHorizontalHeaderLabels(["Imię i Nazwisko", "Dział"])
        self.verticalLayoutEmployees.addWidget(self.tableEmployees)
        self.tabWidget.addTab(self.tabEmployees, "Pracownicy")

        # Zakładka Logi Dostępów
        self.tabAccessLogs = QtWidgets.QWidget()
        self.verticalLayoutLogs = QtWidgets.QVBoxLayout(self.tabAccessLogs)
        self.tableLogs = QtWidgets.QTableWidget(0, 3, self.tabAccessLogs)
        self.tableLogs.setHorizontalHeaderLabels(["Data i Czas", "Imię i Nazwisko", "Status"])
        self.verticalLayoutLogs.addWidget(self.tableLogs)
        self.tabWidget.addTab(self.tabAccessLogs, "Logi Dostępów")

        # Przyciski główne
        self.buttonExit = QtWidgets.QPushButton("Wyjście", self.centralwidget)
        self.verticalLayout.addWidget(self.buttonExit)

    def setup_connections(self):
        # Podłączanie przycisków do odpowiednich funkcji.
        self.buttonSave.clicked.connect(self.register_employee)
        self.buttonExit.clicked.connect(self.close)

    def register_employee(self):
        # Tutaj zrobić POSTA do bazurki
        name = self.lineEditName.text()

        if not name:
            QtWidgets.QMessageBox.critical(self, "Błąd", "Wprowadź imię i nazwisko!")
        else:
            
            department = self.lineEditDepartment.text()
            access_rooms = [self.checkBoxSala1.isChecked(),
                            self.checkBoxSala2.isChecked(),
                            self.checkBoxSala3.isChecked(),
                            self.checkBoxSala4.isChecked(),
                            self.checkBoxSala5.isChecked(),
                            self.checkBoxSala6.isChecked()]
            print(f"Rejestracja: {name}, {department}, Dostęp: {access_rooms}")
            # Nie wiem jeszcze jak to będzie wyglądało, ale pewnie jakieś
            # add_employee(name, department, access_rooms)
            QtWidgets.QMessageBox.information(self, "Sukces", "Dane zostały zapisane!")

    def load_employees(self):
        print("Ładowanie listy pracowników...")
        # get_all_employees()
        # Aktualizacja tabeli self.tableEmployees

    def load_logs(self):
        print("Ładowanie logów...")
        # logs = get_logs()
        # Aktualizacja tabeli self.tableLogs





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = EmployeeApp()
    window.show()
    sys.exit(app.exec_())
