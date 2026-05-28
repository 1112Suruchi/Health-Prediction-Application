import sqlite3

# Database connection
conn = sqlite3.connect('patients.db', check_same_thread=False)
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    dob TEXT,
    email TEXT,
    glucose REAL,
    haemoglobin REAL,
    cholesterol REAL,
    remarks TEXT
)
''')

conn.commit()

# Insert patient

def add_patient(name, dob, email, glucose, haemoglobin, cholesterol, remarks):
    cursor.execute('''
    INSERT INTO patients
    (name, dob, email, glucose, haemoglobin, cholesterol, remarks)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, dob, email, glucose, haemoglobin, cholesterol, remarks))

    conn.commit()

# View patients

def view_patients():
    cursor.execute('SELECT * FROM patients')
    return cursor.fetchall()

# Update patient

def update_patient(id, name, dob, email, glucose, haemoglobin, cholesterol, remarks):
    cursor.execute('''
    UPDATE patients
    SET name=?, dob=?, email=?, glucose=?, haemoglobin=?, cholesterol=?, remarks=?
    WHERE id=?
    ''', (name, dob, email, glucose, haemoglobin, cholesterol, remarks, id))

    conn.commit()

# Delete patient

def delete_patient(id):
    cursor.execute('DELETE FROM patients WHERE id=?', (id,))
    conn.commit()