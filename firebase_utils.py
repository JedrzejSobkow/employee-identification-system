# firebase_utils.py

from PyQt5.uic.properties import QtCore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import uuid

"""
To bedzie trzeba mocno zedytowac
Jak narazie zrobilem tak na sucho 
Pewnie kolumny beda mialy inne nazwy, nie wszystko moze git dzialac - trzeba bedzie debugowac jak sie podlaczy
"""

db = None

def initialize_firebase():
    cred = credentials.Certificate('firebase-credentials.json')  # Tutaj klucz do firebase trzeba umiescic
    firebase_admin.initialize_app(cred)
    global db
    db = firestore.client()
    print("Firebase działa!.")

# def get_database_reference(path):
#     return db.reference(path)


def add_employee(full_name, department, access_rooms):
    global db
    employee_id = str(uuid.uuid4())  # Generator ID
    ref = db.collection('users').document(employee_id)
    ref.set({
        'full_name': full_name,
        'department': department,
        'access_rooms': bools_to_decimal(access_rooms[::-1])
    })
    print(f"Employee {full_name} added with ID: {employee_id}")

def get_all_employees():
    employees = db.collection('users').stream()
    # employees = ref.get()
    employees_for_return = []
    if employees:
        for employee in employees:
            details = employee.to_dict()
            print(details)
            print(f"ID: {employee.id}, Name: {details['full_name']}, Department: {details['department']}")
            employees_for_return.append([employee.id, details['full_name'], details['department'], details["access_rooms"]])
    else:
        print("No employees found.")
    return employees_for_return

def update_employee(employee_id, updated_data):
    ref = db.reference(f'employees/{employee_id}')
    ref.update(updated_data)
    print(f"Employee {employee_id} updated.")

def delete_employee(employee_id):

    ref = db.reference(f'employees/{employee_id}')
    ref.delete()
    print(f"Employee {employee_id} deleted.")

def add_log(name, status):
    log_id = str(uuid.uuid4())  # Generator ID
    ref = db.reference(f'logs/{log_id}')
    ref.set({
        'timestamp': QtCore.QDateTime.currentDateTime().toString(QtCore.Qt.ISODate),
        'name': name,
        'status': status
    })
    print(f"Log added: {name} - {status}")

def get_logs():
    ref = db.reference('logs')
    logs = ref.get()
    if logs:
        for log_id, details in logs.items():
            print(f"Log ID: {log_id}, Name: {details['name']}, Status: {details['status']}, Timestamp: {details['timestamp']}")
    else:
        print("No logs found.")
    return logs


def bools_to_decimal(bool_array):
    binary_str = ''.join(['1' if b else '0' for b in bool_array])
    return int(binary_str, 2)
