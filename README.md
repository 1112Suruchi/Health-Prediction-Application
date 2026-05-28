🏥 Health Prediction Application

A simple AI/ML-based Health Prediction Application built using Python, Streamlit, and SQLite.
The application allows users to manage patient records and predict possible health risks based on blood test values.

📌 Features
Add New Patient Records
View Patient Records
Update Existing Records
Delete Patient Records
AI/ML-based Health Risk Prediction
Input Validation
SQLite Database Storage
Clean and User-Friendly Interface
🛠️ Technologies Used
Technology	Purpose
Python	Backend Logic
Streamlit	Frontend UI
SQLite	Database
Pandas	Data Handling
Scikit-learn	ML Support
📂 Project Structure
health-prediction-app/
│
├── app.py
├── database.py
├── model.py
├── requirements.txt
├── README.md
└── patients.db
⚙️ Installation Steps
1. Clone Repository
git clone YOUR_GITHUB_REPOSITORY_LINK
2. Navigate to Project Folder
cd health-prediction-app
3. Install Dependencies
pip install -r requirements.txt
4. Run Application
python -m streamlit run app.py
🚀 Application Workflow
User enters patient details
Input validation is performed
Health prediction logic runs
Result is stored in database
Records can be viewed, updated, and deleted
🧠 AI/ML Prediction Logic

The application predicts possible health risks using blood test values.

Condition	Prediction
Glucose > 140	Possible Diabetes Risk
Haemoglobin < 12	Possible Anemia
Cholesterol > 240	Possible Heart Disease Risk
Otherwise	Healthy
📋 CRUD Operations
CREATE

Add new patient records.

READ

View all patient records.

UPDATE

Modify existing patient information.

DELETE

Remove patient records.

✅ Input Validation

The application validates:

Valid email format
Date of birth cannot be future date
Numeric blood test values
💾 Database

SQLite database is used for persistent storage of patient records.

Database File:

patients.db
🎯 Why This Technology Stack?
Streamlit provides fast and easy UI development using Python only.
SQLite is lightweight and beginner-friendly.
Python simplifies backend and ML integration.
The project demonstrates CRUD operations and AI workflow effectively.
📸 Screenshots

Add application screenshots here.

Example:

screenshots/homepage.png
🎥 Demo Video

Add your demo video link here.

Example:

https://drive.google.com/your-demo-video-link
🔮 Future Improvements
Login Authentication
Real ML Model Integration
Data Visualization Charts
CSV Export
Search Functionality
Cloud Deployment
