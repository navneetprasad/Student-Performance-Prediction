import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('student_model.pkl')

st.set_page_config(layout="wide")
st.title("Comprehensive Student Performance Predictor")
st.write("Provide complete student details to predict their final math grade accurately.")

# Hardcoded factorization mappings from the training data
mappings = {
    'school': {'GP': 0, 'MS': 1}, 'sex': {'F': 0, 'M': 1}, 'address': {'U': 0, 'R': 1},
    'famsize': {'GT3': 0, 'LE3': 1}, 'Parrent_status': {'A': 0, 'T': 1},
    'Mother_job': {'at_home': 0, 'health': 1, 'other': 2, 'services': 3, 'teacher': 4},
    'Father_job': {'teacher': 0, 'other': 1, 'services': 2, 'health': 3, 'at_home': 4},
    'reason_to_chose_school': {'course': 0, 'other': 1, 'home': 2, 'reputation': 3},
    'guardian': {'mother': 0, 'father': 1, 'other': 2},
    'extra_edu_supp': {'yes': 0, 'no': 1}, 'family_edu_supp': {'no': 0, 'yes': 1},
    'extra_paid_class': {'no': 0, 'yes': 1}, 'extra_curr_activities': {'no': 0, 'yes': 1},
    'nursery': {'yes': 0, 'no': 1}, 'Interested_in_higher_edu': {'yes': 0, 'no': 1},
    'internet_access': {'no': 0, 'yes': 1}, 'romantic_relationship': {'no': 0, 'yes': 1}
}

col1, col2 = st.columns(2)

with col1:
    st.subheader("Demographics & Family")
    school = st.selectbox("School", ['GP', 'MS'])
    sex = st.selectbox("Sex", ['F', 'M'])
    age = st.slider("Age", 15, 22, 16)
    address = st.selectbox("Address (U = Urban, R = Rural)", ['U', 'R'])
    famsize = st.selectbox("Family Size", ['GT3', 'LE3'])
    Pstatus = st.selectbox("Parent Cohabitation Status", ['A', 'T'])
    Medu = st.slider("Mother's Education (0=None, 4=Higher Edu)", 0, 4, 2)
    Fedu = st.slider("Father's Education (0=None, 4=Higher Edu)", 0, 4, 2)
    Mjob = st.selectbox("Mother's Job", ['at_home', 'health', 'other', 'services', 'teacher'])
    Fjob = st.selectbox("Father's Job", ['teacher', 'other', 'services', 'health', 'at_home'])
    guardian = st.selectbox("Guardian", ['mother', 'father', 'other'])
    famrel = st.slider("Family Quality Relationship (1-5)", 1, 5, 4)

with col2:
    st.subheader("Academic & Lifestyle")
    reason = st.selectbox("Reason for Choosing School", ['course', 'other', 'home', 'reputation'])
    traveltime = st.slider("Travel Time (1=<15min, 4=>1hour)", 1, 4, 1)
    studytime = st.slider("Weekly Study Time (1=<2hrs, 4=>10hrs)", 1, 4, 2)
    failures = st.slider("Past Class Failures", 0, 4, 0)
    schoolsup = st.selectbox("Extra Educational Support", ['yes', 'no'])
    famsup = st.selectbox("Family Educational Support", ['no', 'yes'])
    paid = st.selectbox("Extra Paid Classes", ['no', 'yes'])
    activities = st.selectbox("Extra-Curricular Activities", ['no', 'yes'])
    nursery = st.selectbox("Attended Nursery School", ['yes', 'no'])
    higher = st.selectbox("Wants to Pursue Higher Education", ['yes', 'no'])
    internet = st.selectbox("Internet Access at Home", ['no', 'yes'])
    romantic = st.selectbox("In a Romantic Relationship", ['no', 'yes'])

st.subheader("Social & Health")
col3, col4, col5 = st.columns(3)
with col3:
    freetime = st.slider("Free Time After School (1-5)", 1, 5, 3)
    goout = st.slider("Going Out with Friends (1-5)", 1, 5, 3)
with col4:
    Dalc = st.slider("Workday Alcohol Consumption (1-5)", 1, 5, 1)
    Walc = st.slider("Weekend Alcohol Consumption (1-5)", 1, 5, 1)
with col5:
    health = st.slider("Health Status (1-5)", 1, 5, 3)
    absences = st.slider("Number of Absences", 0, 93, 0)

if st.button("Predict Final Grade", type="primary"):
    input_data = {
        'school': mappings['school'][school],
        'sex': mappings['sex'][sex],
        'age': age,
        'address': mappings['address'][address],
        'famsize': mappings['famsize'][famsize],
        'Parrent_status': mappings['Parrent_status'][Pstatus],
        'Mother_edu': Medu,
        'Father_edu': Fedu,
        'Mother_job': mappings['Mother_job'][Mjob],
        'Father_job': mappings['Father_job'][Fjob],
        'reason_to_chose_school': mappings['reason_to_chose_school'][reason],
        'guardian': mappings['guardian'][guardian],
        'traveltime': traveltime,
        'weekly_studytime': studytime,
        'failures': failures,
        'extra_edu_supp': mappings['extra_edu_supp'][schoolsup],
        'family_edu_supp': mappings['family_edu_supp'][famsup],
        'extra_paid_class': mappings['extra_paid_class'][paid],
        'extra_curr_activities': mappings['extra_curr_activities'][activities],
        'nursery': mappings['nursery'][nursery],
        'Interested_in_higher_edu': mappings['Interested_in_higher_edu'][higher],
        'internet_access': mappings['internet_access'][internet],
        'romantic_relationship': mappings['romantic_relationship'][romantic],
        'Family_quality_reln': famrel,
        'freetime_after_school': freetime,
        'goout_with_friends': goout,
        'workday_alcohol_consum': Dalc,
        'weekend_alcohol_consum': Walc,
        'health_status': health,
        'absences': absences
    }
    
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    
    st.success(f"Predicted Final Grade: {prediction[0]:.1f} / 20")