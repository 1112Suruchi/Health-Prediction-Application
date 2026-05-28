import streamlit as st
import pandas as pd
import re

from datetime import date

from database import (
    add_patient,
    view_patients,
    update_patient,
    delete_patient
)

from model import predict_health

st.set_page_config(page_title="Health Prediction App", layout="wide")

st.title("Health Prediction Application")

menu = ["Add Patient", "View Patients", "Update Patient", "Delete Patient"]
choice = st.sidebar.selectbox("Menu", menu)

# Add Patient
if choice == "Add Patient":

    st.subheader("Add New Patient")
    name = st.text_input("Full Name")
    from datetime import date

    dob = st.date_input(
    "Date of Birth",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)
    email = st.text_input("Email")

    glucose = st.number_input("Glucose")
    haemoglobin = st.number_input("Haemoglobin")
    cholesterol = st.number_input("Cholesterol")

    if st.button("Submit"):

        # Email validation
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(pattern, email):
            st.error("Invalid Email")

        elif dob > date.today():
            st.error("DOB cannot be future date")

        else:
            remarks = predict_health(glucose, haemoglobin, cholesterol)

            add_patient(
                name,
                str(dob),
                email,
                glucose,
                haemoglobin,
                cholesterol,
                remarks
            )

            st.success("Patient Added Successfully")
            st.write("Prediction:", remarks)

# View Patients
elif choice == "View Patients":

    st.subheader("Patient Records")

    result = view_patients()

    df = pd.DataFrame(result, columns=[
        "ID",
        "Name",
        "DOB",
        "Email",
        "Glucose",
        "Haemoglobin",
        "Cholesterol",
        "Remarks"
    ])

    st.dataframe(df)

# Update Patient
elif choice == "Update Patient":

    st.subheader("Update Patient")

    result = view_patients()

    patient_ids = [row[0] for row in result]

    selected_id = st.selectbox("Select Patient ID", patient_ids)

    selected_patient = None
    for row in result:
        if row[0] == selected_id:
            selected_patient = row

    if selected_patient:

        name = st.text_input("Full Name", selected_patient[1])
        dob = st.text_input("DOB", selected_patient[2])
        email = st.text_input("Email", selected_patient[3])

        glucose = st.number_input("Glucose", value=float(selected_patient[4]))
        haemoglobin = st.number_input("Haemoglobin", value=float(selected_patient[5]))
        cholesterol = st.number_input("Cholesterol", value=float(selected_patient[6]))

        if st.button("Update"):

            remarks = predict_health(glucose, haemoglobin, cholesterol)

            update_patient(
                selected_id,
                name,
                dob,
                email,
                glucose,
                haemoglobin,
                cholesterol,
                remarks
            )

            st.success("Patient Updated Successfully")

# Delete Patient
elif choice == "Delete Patient":

    st.subheader("Delete Patient")

    result = view_patients()

    patient_ids = [row[0] for row in result]

    selected_id = st.selectbox("Select Patient ID to Delete", patient_ids)

    if st.button("Delete"):

        delete_patient(selected_id)

        st.success("Patient Deleted Successfully")
