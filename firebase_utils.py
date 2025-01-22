# firebase_utils.py

import firebase_admin
from PyQt5.uic.properties import QtCore
from firebase_admin import credentials, db
import uuid  # To generate unique IDs for employees

def initialize_firebase():
    # Init
    cred = credentials.Certificate('secret key.json')  # Tutaj klucz do firebase trzeba umiescic
    firebase_admin.initialize_app(cred, {
        'databaseURL': "URL to database"
    })
    print("Firebase initialized successfully.")

def get_database_reference(path):
    # Zwraca referencje do db dla sciezki
    return db.reference(path)


def add_employee(name, department, access_rooms):
    # Dodajemy pracownika
    employee_id = str(uuid.uuid4())  # Generator ID
    ref = db.reference(f'employees/{employee_id}')
    ref.set({
        'name': name,
        'department': department,
        'access_rooms': access_rooms
    })
    print(f"Employee {name} added with ID: {employee_id}")

def get_all_employees():
    ref = db.reference('employees')
    employees = ref.get()
    if employees:
        for employee_id, details in employees.items():
            print(f"ID: {employee_id}, Name: {details['name']}, Department: {details['department']}")
    else:
        print("No employees found.")
    return employees

def update_employee(employee_id, updated_data):
    ref = db.reference(f'employees/{employee_id}')
    ref.update(updated_data)
    print(f"Employee {employee_id} updated.")

def delete_employee(employee_id):

    ref = db.reference(f'employees/{employee_id}')
    ref.delete()
    print(f"Employee {employee_id} deleted.")

def add_log(name, status):
    # Dodajemy logi
    log_id = str(uuid.uuid4())  # Generator ID
    ref = db.reference(f'logs/{log_id}')
    ref.set({
        'timestamp': QtCore.QDateTime.currentDateTime().toString(QtCore.Qt.ISODate),
        'name': name,
        'status': status
    })
    print(f"Log added: {name} - {status}")

def get_logs():
    # Zczytujemy logi
    ref = db.reference('logs')
    logs = ref.get()
    if logs:
        for log_id, details in logs.items():
            print(f"Log ID: {log_id}, Name: {details['name']}, Status: {details['status']}, Timestamp: {details['timestamp']}")
    else:
        print("No logs found.")
    return logs
