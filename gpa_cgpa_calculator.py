import streamlit as st
import pandas as pd

st.title("🎓 GPA & CGPA Calculator (5 Semesters)")

st.write("""
Enter your marks and credit hours for each subject in all semesters.
The app will calculate your **GPA for each semester** and **CGPA** automatically.
""")

# Function to convert marks to grade points
def marks_to_gpa(marks):
    if marks >= 85:
        return 4.0
    elif marks >= 80:
        return 3.7
    elif marks >= 75:
        return 3.3
    elif marks >= 70:
        return 3.0
    elif marks >= 65:
        return 2.7
    elif marks >= 61:
        return 2.3
    elif marks >= 58:
        return 2.0
    elif marks >= 55:
        return 1.7
    elif marks >= 50:
        return 1.0
    else:
        return 0.0

# Function to calculate GPA for a semester
def calculate_gpa(subjects):
    total_quality_points = 0
    total_credits = 0
    for sub in subjects:
        gpa = marks_to_gpa(sub["marks"])
        total_quality_points += gpa * sub["credit"]
        total_credits += sub["credit"]
    return round(total_quality_points / total_credits, 2) if total_credits > 0 else 0.0

# Store GPAs for 5 semesters
semester_gpas = []
semester_data = []

for sem in range(1, 6):
    st.header(f"Semester {sem}")
    num_subjects = st.number_input(f"Enter number of subjects in Semester {sem}", 1, 10, key=f"num_{sem}")
    
    subjects = []
    for i in range(1, num_subjects + 1):
        col1, col2 = st.columns(2)
        with col1:
            marks = st.number_input(f"Subject {i} Marks (0-100)", 0, 100, key=f"marks_{sem}_{i}")
        with col2:
            credit = st.number_input(f"Subject {i} Credit Hours", 1.0, 5.0, step=0.5, key=f"credit_{sem}_{i}")
        subjects.append({"marks": marks, "credit": credit})
    
    gpa = calculate_gpa(subjects)
    semester_gpas.append(gpa)
    semester_data.append(subjects)
    st.success(f"Semester {sem} GPA: {gpa}")

# Calculate CGPA
valid_gpas = [g for g in semester_gpas if g > 0]
cgpa = round(sum(valid_gpas) / len(valid_gpas), 2) if valid_gpas else 0.0

st.subheader("📊 Summary")
for i, gpa in enumerate(semester_gpas, start=1):
    st.write(f"**Semester {i} GPA:** {gpa}")

st.markdown("---")
st.success(f"🎯 **Overall CGPA (up to 5 semesters): {cgpa}**")

# Optional: Display GPA table
if st.checkbox("Show GPA Table"):
    df = pd.DataFrame({
        "Semester": [f"Sem {i}" for i in range(1, 6)],
        "GPA": semester_gpas
    })
    st.dataframe(df)
