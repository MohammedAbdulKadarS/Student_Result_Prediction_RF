import streamlit as st
import pandas as pd
import joblib
import time

st.markdown("<style> \
.reportview-container {background: linear-gradient(135deg, #23a6d5 0%, #23d5ab 100%);color: #fff;} \
.sidebar .sidebar-content {background: #222428;} \
h1,h2,h3,h4,h5,h6 {color: #fff !important;} \
div.stButton > button:first-child {background-color: #00f2fe;border: none;color: white; \
height: 3em;width: 12em;border-radius: 10px;box-shadow: 0 0 10px #00f2fe, 0 0 20px #4facfe;font-size: 20px;font-weight: bold;\
animation: glow 1.5s infinite;transition: 0.3s;} \
@keyframes glow {0% { box-shadow: 0 0 10px #00f2fe, 0 0 20px #4facfe;} 50% { box-shadow: 0 0 20px #00f2fe, 0 0 40px #4facfe;} 100% { box-shadow: 0 0 10px #00f2fe, 0 0 20px #4facfe;}} \
</style>", unsafe_allow_html=True)

st.title("🎓 Student Performance Prediction App 🚀")
st.markdown('<div style="text-align:center;font-size:28px;">🖥️ Enter Details & Get Instant Results!</div>', unsafe_allow_html=True)

dt = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

# Double-sided input with Streamlit columns
col1, col2 = st.columns(2)

with col1:
    Gender_Male = st.selectbox("Gender", [1, 0], format_func=lambda x: 'Male' if x==1 else 'Female')
    Study_Hours_per_Week = st.slider("Study Hours per Week", 0.0, 40.0, 20.0)
    Attendance_Percentage = st.slider("Attendance Percentage", 0.0, 100.0, 75.0)
    Previous_Sem_Score = st.slider("Previous Sem Score", 0.0, 100.0, 60.0)
    Family_Income = st.slider("Family Income", 10000.0, 100000.0, 55000.0)
    Sleep_Hours = st.slider("Sleep Hours", 4.0, 10.0, 7.0)
    Travel_Time = st.slider("Travel Time", 0.0, 3.0, 1.5)
    Test_Anxiety_Level = st.slider("Test Anxiety Level", 1.0, 10.0, 5.0)

with col2:
    Peer_Influence = st.slider("Peer Influence", 1.0, 10.0, 5.0)
    Motivation_Level = st.slider("Motivation Level", 1.0, 10.0, 6.0)
    Library_Usage_per_Week = st.slider("Library Usage/Week", 0, 9, 5)
    Parental_Education_Postgraduate = st.selectbox("Parental Education: Postgraduate", [1, 0], format_func=lambda x: 'Yes' if x==1 else 'No')
    Internet_Access_Yes = st.selectbox("Internet Access", [1, 0], format_func=lambda x: 'Yes' if x==1 else 'No')
    Tutoring_Classes_Yes = st.selectbox("Tutoring Classes", [1, 0], format_func=lambda x: 'Yes' if x==1 else 'No')
    Sports_Activity_Yes = st.selectbox("Sports Activity", [1, 0], format_func=lambda x: 'Yes' if x==1 else 'No')
    Extra_Curricular_Yes = st.selectbox("Extra Curricular", [1, 0], format_func=lambda x: 'Yes' if x==1 else 'No')
    School_Type_Public = st.selectbox("School Type: Public", [1, 0], format_func=lambda x: 'Public' if x==1 else 'Private')
    Teacher_Feedback_Excellent = st.selectbox("Teacher Feedback: Excellent", [1, 0], format_func=lambda x: 'Yes' if x==1 else 'No')
    Teacher_Feedback_Good = st.selectbox("Teacher Feedback: Good", [1, 0], format_func=lambda x: 'Yes' if x==1 else 'No')
    Teacher_Feedback_Poor = st.selectbox("Teacher Feedback: Poor", [1, 0], format_func=lambda x: 'Yes' if x==1 else 'No')

input_dict = dict(
    Gender_Male=Gender_Male,
    Study_Hours_per_Week=Study_Hours_per_Week,
    Attendance_Percentage=Attendance_Percentage,
    Previous_Sem_Score=Previous_Sem_Score,
    Family_Income=Family_Income,
    Sleep_Hours=Sleep_Hours,
    Travel_Time=Travel_Time,
    Test_Anxiety_Level=Test_Anxiety_Level,
    Peer_Influence=Peer_Influence,
    Motivation_Level=Motivation_Level,
    Library_Usage_per_Week=Library_Usage_per_Week,
    Parental_Education_Postgraduate=Parental_Education_Postgraduate,
    Internet_Access_Yes=Internet_Access_Yes,
    Tutoring_Classes_Yes=Tutoring_Classes_Yes,
    Sports_Activity_Yes=Sports_Activity_Yes,
    Extra_Curricular_Yes=Extra_Curricular_Yes,
    School_Type_Public=School_Type_Public,
    Teacher_Feedback_Excellent=Teacher_Feedback_Excellent,
    Teacher_Feedback_Good=Teacher_Feedback_Good,
    Teacher_Feedback_Poor=Teacher_Feedback_Poor
)

input_df = pd.DataFrame([input_dict])

if st.button("Predict Result"):
    input_df = input_df.reindex(columns=columns, fill_value=0)
    with st.spinner('Predicting Student Performance 🔮...'):
        time.sleep(2)
    result = dt.predict(input_df)[0]
    st.success(f"🎉 Prediction: {result} 🎉")
    st.balloons()
    st.markdown("#### Congrats! Your result is ready. 🚀")

