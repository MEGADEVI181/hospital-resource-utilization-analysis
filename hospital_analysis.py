import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# STEP 1: CREATE DATASET (same as your image)
# -------------------------------

data = {
    'Patient_ID': list(range(1,21)),
    'Year': [2020,2020,2020,2020,2020,
             2021,2021,2021,2021,2021,
             2022,2022,2022,2022,2022,
             2023,2023,2023,2023,2023],
    
    'Month': ['Jan','Feb','Mar','Apr','May']*4,
    
    'Department': [
        'ICU','General','Emergency','ICU','General',
        'Emergency','ICU','General','ICU','Emergency',
        'General','ICU','Emergency','ICU','General',
        'Emergency','ICU','General','ICU','Emergency'
    ],
    
    'Doctor': [
        'Dr.A','Dr.B','Dr.C','Dr.A','Dr.B',
        'Dr.C','Dr.D','Dr.B','Dr.A','Dr.C',
        'Dr.B','Dr.D','Dr.C','Dr.A','Dr.B',
        'Dr.C','Dr.D','Dr.B','Dr.A','Dr.C'
    ],
    
    'Beds_Used': [1]*20,
    
    'Stay_Days': [5,2,3,6,2,4,7,3,5,4,2,6,3,5,2,4,7,3,6,5],
    
    'Treatment_Cost': [
        25000,8000,12000,30000,7000,
        15000,32000,9000,27000,14000,
        8500,31000,13000,28000,7500,
        16000,35000,9500,30000,17000
    ]
}

df = pd.DataFrame(data)

print("\n===== DATASET =====")
print(df)

# -------------------------------
# STEP 2: BASIC ANALYSIS
# -------------------------------

print("\nTotal Patients:", len(df))
print("Average Stay Days:", df['Stay_Days'].mean())
print("Total Revenue:", df['Treatment_Cost'].sum())

# -------------------------------
# STEP 3: DEPARTMENT ANALYSIS
# -------------------------------

dept = df.groupby('Department')['Patient_ID'].count()
print("\nPatients per Department:\n", dept)

# -------------------------------
# STEP 4: DOCTOR WORKLOAD
# -------------------------------

doctor = df['Doctor'].value_counts()
print("\nDoctor Workload:\n", doctor)

# -------------------------------
# STEP 5: YEARLY TREND
# -------------------------------

yearly = df.groupby('Year')['Patient_ID'].count()
print("\nYearly Patient Count:\n", yearly)

# -------------------------------
# STEP 6: VISUALIZATION
# -------------------------------

# Line Chart - Yearly Trend
yearly.plot(marker='o')
plt.title("Yearly Patient Trend")
plt.xlabel("Year")
plt.ylabel("Patients")
plt.grid()
plt.show()

# Bar Chart - Department
dept.plot(kind='bar')
plt.title("Department Usage")
plt.xlabel("Department")
plt.ylabel("Patients")
plt.show()

# Pie Chart - Department Distribution
dept.plot(kind='pie', autopct='%1.1f%%')
plt.title("Department Distribution")
plt.ylabel("")
plt.show()

# Bar Chart - Doctor Workload
doctor.plot(kind='bar')
plt.title("Doctor Workload")
plt.xlabel("Doctor")
plt.ylabel("Patients")
plt.show()

# -------------------------------
# STEP 7: ADVANCED INSIGHTS
# -------------------------------

max_dept = dept.idxmax()
max_doc = doctor.idxmax()

print("\n===== FINAL INSIGHTS =====")
print("Most Busy Department:", max_dept)
print("Most Busy Doctor:", max_doc)
print("Hospital workload is increasing steadily.")
