# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets # type: ignore
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
import serial
import threading
from rfid_reader import rfidRead

from firebase_utils import *

class EmployeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_connections()

        # Initialize Firebase here or earlier during app setup
        initialize_firebase()
        # self.db_ref = get_database_reference('Database reference')
        # print(self.db_ref.get())

        self.employeeButtons = []


        # Serial port setup
        self.serial_port = None
        self.serial_thread = None
        self.is_listening = False  # Flaga kontrolująca nasłuchiwanie
        self.card_read = "Brak"


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

        # Zakładki (Rejestracja, Pracownicy, Logi Dostępów, Przypisz kartę)
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
        self.tabWidget.addTab(self.tabRegister, "Rejestracja Pracownika")

        # Zakładka Pracownicy
        self.tabEmployees = QtWidgets.QWidget()
        self.verticalLayoutEmployees = QtWidgets.QVBoxLayout(self.tabEmployees)
        self.tableEmployees = QtWidgets.QTableWidget(0, 4, self.tabEmployees)
        self.tableEmployees.setHorizontalHeaderLabels(["Id", "Imię i Nazwisko", "Dział", "Uprawnienia"])
        self.verticalLayoutEmployees.addWidget(self.tableEmployees)
        self.tabWidget.addTab(self.tabEmployees, "Pracownicy")

        # Zakładka Logi Dostępów
        self.tabAccessLogs = QtWidgets.QWidget()
        self.verticalLayoutLogs = QtWidgets.QVBoxLayout(self.tabAccessLogs)
        self.tableLogs = QtWidgets.QTableWidget(0, 3, self.tabAccessLogs)
        self.tableLogs.setHorizontalHeaderLabels(["Data i Czas", "Imię i Nazwisko", "Status"])
        self.verticalLayoutLogs.addWidget(self.tableLogs)
        self.tabWidget.addTab(self.tabAccessLogs, "Logi Dostępów")

        # Zakładka Przypisz Kartę
        self.tabAssignCard = QtWidgets.QWidget()
        self.verticalLayoutAssignCard = QtWidgets.QVBoxLayout(self.tabAssignCard)

        # Lista pracowników (radiobuttony)
        self.groupBoxEmployees = QtWidgets.QGroupBox("Lista Pracowników", self.tabAssignCard)
        self.verticalLayoutEmployeesList = QtWidgets.QVBoxLayout(self.groupBoxEmployees)
        self.scrollArea = QtWidgets.QScrollArea(self.groupBoxEmployees)
        self.scrollArea.setWidgetResizable(True)
        self.scrollWidget = QtWidgets.QWidget()
        self.scrollLayout = QtWidgets.QVBoxLayout(self.scrollWidget)
        self.scrollArea.setWidget(self.scrollWidget)
        self.verticalLayoutEmployeesList.addWidget(self.scrollArea)
        self.verticalLayoutAssignCard.addWidget(self.groupBoxEmployees)

        # Pole na kartę do przypisania
        self.labelCardToAssign = QtWidgets.QLabel("Karta do przypisania: Brak", self.tabAssignCard)
        self.verticalLayoutAssignCard.addWidget(self.labelCardToAssign)

        # Ostrzeżenie o nadpisaniu karty
        self.warningLabel = QtWidgets.QLabel("", self.tabAssignCard)
        self.warningLabel.setStyleSheet("color: red;")
        self.verticalLayoutAssignCard.addWidget(self.warningLabel)

        # Przycisk przypisz kartę
        self.buttonAssignCard = QtWidgets.QPushButton("Przypisz kartę", self.tabAssignCard)
        self.buttonAssignCard.clicked.connect(self.assign_card)
        self.verticalLayoutAssignCard.addWidget(self.buttonAssignCard)

        # Dodajemy przycisk do usunięcia karty
        self.buttonRemoveCard = QtWidgets.QPushButton("Usuń aktualną kartę", self.tabAssignCard)
        self.buttonRemoveCard.clicked.connect(self.remove_card)
        self.verticalLayoutAssignCard.addWidget(self.buttonRemoveCard)

        self.tabWidget.addTab(self.tabAssignCard, "Przypisz Kartę")



        # Przyciski główne
        self.buttonExit = QtWidgets.QPushButton("Wyjście", self.centralwidget)
        self.verticalLayout.addWidget(self.buttonExit)

    def setup_connections(self):
        # Podłączanie przycisków do odpowiednich funkcji.
        self.buttonSave.clicked.connect(self.register_employee)
        self.buttonExit.clicked.connect(self.close)

        # Obsługa zmiany zakładek
        self.tabWidget.currentChanged.connect(self.on_tab_changed)

    def assign_card(self):
        selected_employee = None
        for button in self.employeeButtons:
            if button.isChecked():
                selected_employee = button.text()
                break

        if selected_employee:
            if "Karta: Brak" not in selected_employee:
                self.warningLabel.setText("Pracownik już posiada kartę! Usuń starą kartę przed przypisaniem nowej.")
            else:
                self.warningLabel.setText("")
                if self.card_read and self.card_read != "Brak":
                    # Sprawdź, czy karta już ma przypisanego właściciela
                    # card_owner = get_card_owner(self.card_read)  # Funkcja do sprawdzania właściciela karty
                    # if card_owner:
                        # Usuń pole owner_id z tej karty
                    remove_employee_from_card(self.card_read)
                    # QtWidgets.QMessageBox.information(
                    #     self, "Karta Przypisana",
                    #     f"Karta {self.card_read} została usunięta od poprzedniego użytkownika."
                    # )

                    # Przypisz kartę do wybranego pracownika
                    employee_id = selected_employee.split(",")[0].split(":")[1].strip()
                    assign_card_to_employee(employee_id, self.card_read)  # Funkcja przypisująca kartę
                    self.warningLabel.setText("")
                    QtWidgets.QMessageBox.information(
                        self, "Sukces", f"Karta {self.card_read} została przepisana do pracownika."
                    )
                    self.load_employees_and_cards_assigned()







    def remove_card(self):
        selected_employee = None
        selected_card_id = None
        for button in self.employeeButtons:
            if button.isChecked():
                selected_employee = button.text()
                # Wyciągamy ID karty z tekstu przycisku (przykład: "Karta: 12345")
                if "Karta: Brak" not in selected_employee:
                    selected_card_id = selected_employee.split("Karta: ")[1].strip()
                break

        if selected_employee:
            if selected_card_id:
                # Usuwamy kartę pracownikowi
                remove_employee_from_card(selected_card_id)  # Funkcja usuwająca kartę z bazy danych
                self.warningLabel.setText("")
                self.labelCardToAssign.setText("Karta do przypisania: Brak")
                QtWidgets.QMessageBox.information(self, "Sukces", "Karta została usunięta!")
                self.load_employees_and_cards_assigned()
            else:
                self.warningLabel.setText("Pracownik nie ma przypisanej karty!")
        else:
            self.warningLabel.setText("Proszę wybrać pracownika.")


    def start_serial_listener(self):
        """Rozpocznij nasłuchiwanie portu szeregowego."""

        if self.is_listening:
            return  # Jeśli nasłuchiwanie już trwa, nic nie rób

        self.is_listening = True
 #       port = "COM9"  # Ustaw odpowiedni port
 #       baudrate = 9600  # Ustaw odpowiednią prędkość transmisji

  #      try:
  #          self.serial_port = serial.Serial(port, baudrate, timeout=1)
  #          QtWidgets.QMessageBox.information(self, "Sukces", f"Połączono z portem: {port}")

            # Uruchom wątek do nasłuchiwania
        self.serial_thread = threading.Thread(target=self.listen_serial_data)
        self.serial_thread.daemon = True
        self.serial_thread.start()

   #     except serial.SerialException as e:
   #         QtWidgets.QMessageBox.critical(self, "Błąd", f"Błąd połączenia z portem szeregowym: {e}")

#    def listen_serial_data(self):
        # Nasłuchiwanie danych z portu szeregowego.
#       while True:
#            if self.serial_port and self.serial_port.in_waiting > 0:
#                data = self.serial_port.readline().decode('utf-8').strip()
#                if data:
#                    # Wykonaj akcję z danymi, np. wyświetlenie ich w oknie
#                    # QtCore.QMetaObject.invokeMethod(self, "update_ui_with_serial_data", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, data))
#                    print(data)
#                    self.card_read = data
#                    self.labelCardToAssign.setText(f"Karta do przypisania: {data}")

    def listen_serial_data(self):

        data = rfidRead()
        self.card_read = data
        self.labelCardToAssign.setText(f"Karta do przypisania: {data}")
        

 

    # def update_ui_with_serial_data(self, data):
    #     """Aktualizowanie UI danymi z portu szeregowego."""
    #     print(f"Odebrane dane: {data}")


    def on_tab_changed(self, index):
        if self.tabWidget.tabText(index) == "Pracownicy":
            self.load_employees()
        elif self.tabWidget.tabText(index) == "Przypisz Kartę":


            self.start_serial_listener()

            self.load_employees_and_cards_assigned()
            self.card_read = "Brak"
            self.labelCardToAssign.setText(f"Karta do przypisania: Brak")



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
            add_employee(name, department, access_rooms)
            QtWidgets.QMessageBox.information(self, "Sukces", "Dane zostały zapisane!")

    def load_employees(self):
        self.tableEmployees.setRowCount(0)
        print("Ładowanie listy pracowników...")
        employees = get_all_employees()
        for id, f_name, dep, accesses in employees:
            self.add_row(id, f_name, dep, accesses)


    def load_employees_and_cards_assigned(self):
        # Czyszczenie widżetu
        for i in reversed(range(self.scrollLayout.count())):
            widget_to_remove = self.scrollLayout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.deleteLater()

        # Usuwanie starych przycisków z listy
        self.employeeButtons.clear()

        employees = get_all_employees_and_their_cards()


        # Tworzenie RadioButtonów dla każdego pracownika
        for employee in employees:
            card_status = f"Karta: {employee['card']}" if employee['card'] else "Karta: Brak"
            radio_text = f"ID: {employee['id']}, Imię: {employee['name']}, Dział: {employee['department']}, Dostępy: {employee['access']}, {card_status}"
            radio_button = QtWidgets.QRadioButton(radio_text)
            self.scrollLayout.addWidget(radio_button)
            self.employeeButtons.append(radio_button)  # Dodaj przycisk do listy



    def add_row(self, id, full_name, department, accesses):
        row_position = self.tableEmployees.rowCount()
        self.tableEmployees.insertRow(row_position)

        self.tableEmployees.setItem(row_position, 0, QTableWidgetItem(id))
        self.tableEmployees.setItem(row_position, 1, QTableWidgetItem(full_name))
        self.tableEmployees.setItem(row_position, 2, QTableWidgetItem(department))
        self.tableEmployees.setItem(row_position, 3, QTableWidgetItem(str(accesses)))

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
