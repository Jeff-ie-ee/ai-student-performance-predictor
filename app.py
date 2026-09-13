import streamlit as st
import requests

st.set_page_config(
    page_title="AI Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Student Performance Predictor")
st.write("Predict a student's final academic performance using Machine Learning.")

st.divider()

with st.form("student_form"):

    st.subheader("Student Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        school = st.selectbox("School", ["GP", "MS"])
        sex = st.selectbox("Sex", ["M", "F"])
        age = st.number_input("Age", 15, 25, 18)
        address = st.selectbox("Address", ["U", "R"])
        famsize = st.selectbox("Family Size", ["GT3", "LE3"])
        Pstatus = st.selectbox("Parent Status", ["T", "A"])
        Medu = st.slider("Mother Education", 0, 4, 3)
        Fedu = st.slider("Father Education", 0, 4, 3)

    with col2:
        Mjob = st.selectbox(
            "Mother Job",
            ["teacher", "health", "services", "at_home", "other"]
        )

        Fjob = st.selectbox(
            "Father Job",
            ["teacher", "health", "services", "at_home", "other"]
        )

        reason = st.selectbox(
            "Reason for Choosing School",
            ["course", "home", "reputation", "other"]
        )

        guardian = st.selectbox(
            "Guardian",
            ["mother", "father", "other"]
        )

        traveltime = st.slider("Travel Time", 1, 4, 1)
        studytime = st.slider("Study Time", 1, 4, 3)
        failures = st.slider("Past Failures", 0, 3, 0)
        absences = st.number_input("Absences", 0, 100, 4)

    with col3:
        schoolsup = st.selectbox("Extra School Support", ["yes", "no"])
        famsup = st.selectbox("Family Support", ["yes", "no"])
        paid = st.selectbox("Extra Paid Classes", ["yes", "no"])
        activities = st.selectbox("Extra Activities", ["yes", "no"])
        nursery = st.selectbox("Attended Nursery", ["yes", "no"])
        higher = st.selectbox("Wants Higher Education", ["yes", "no"])
        internet = st.selectbox("Internet Access", ["yes", "no"])
        romantic = st.selectbox("Romantic Relationship", ["yes", "no"])

    st.subheader("Lifestyle & Academic Information")

    col4, col5, col6 = st.columns(3)

    with col4:
        famrel = st.slider("Family Relationship", 1, 5, 4)
        freetime = st.slider("Free Time", 1, 5, 3)
        goout = st.slider("Going Out", 1, 5, 3)

    with col5:
        Dalc = st.slider("Weekday Alcohol Consumption", 1, 5, 1)
        Walc = st.slider("Weekend Alcohol Consumption", 1, 5, 1)
        health = st.slider("Health", 1, 5, 4)

    with col6:
        G1 = st.slider("First Period Grade (G1)", 0, 20, 14)
        G2 = st.slider("Second Period Grade (G2)", 0, 20, 15)

    st.divider()

    submitted = st.form_submit_button(
        "🚀 Predict Student Performance",
        use_container_width=True
    )


if submitted:

    student_data = {
        "school": school,
        "sex": sex,
        "age": age,
        "address": address,
        "famsize": famsize,
        "Pstatus": Pstatus,
        "Medu": Medu,
        "Fedu": Fedu,
        "Mjob": Mjob,
        "Fjob": Fjob,
        "reason": reason,
        "guardian": guardian,
        "traveltime": traveltime,
        "studytime": studytime,
        "failures": failures,
        "schoolsup": schoolsup,
        "famsup": famsup,
        "paid": paid,
        "activities": activities,
        "nursery": nursery,
        "higher": higher,
        "internet": internet,
        "romantic": romantic,
        "famrel": famrel,
        "freetime": freetime,
        "goout": goout,
        "Dalc": Dalc,
        "Walc": Walc,
        "health": health,
        "absences": absences,
        "G1": G1,
        "G2": G2
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=student_data
        )

        if response.status_code == 200:

            result = response.json()

            st.success("Prediction completed successfully! 🎉")

            st.divider()

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Predicted Grade",
                    f"{result['predicted_grade']} / 20"
                )

            with col2:
                st.metric(
                    "Performance",
                    result["performance"]
                )

            with col3:
                st.metric(
                    "Risk Level",
                    result["risk_level"]
                )

        else:
            st.error("Prediction failed.")
            st.write(response.text)

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Backend API is not running. "
            "Please start FastAPI first."
        )