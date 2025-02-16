# employee-identification-system

# Employee Identification System

The **Employee Identification System** is an application designed to manage employees and their assigned RFID cards for access control within a company. The system utilizes a graphical interface built with PyQt5 and stores data about employees and their access permissions in Firebase Firestore.

This system allows easy management of employee information, RFID card assignments, and tracking of access logs, all of which can be controlled through a simple, intuitive interface.

## Features

- **Employee Registration**: Add new employees to the system by entering their personal details, department, and access rights.
- **Manage Employees**: View the list of all employees along with their assigned RFID cards and access permissions.
- **Access Logs**: Track employee access to various rooms and facilities in real time.
- **RFID Card Assignment**: Assign RFID cards to employees for access control, with the ability to remove or update assignments.

## Requirements

To run this application, you need the following:

- Python 3.x
- PyQt5 (for GUI)
- Firebase Admin SDK for Python (`firebase-admin`)
- PySerial (for handling serial ports and RFID data reading)

## Installation

### Step 1: Install Dependencies

You can install all required libraries by running the following command in your terminal:

```bash
pip install -r requirements.txt
