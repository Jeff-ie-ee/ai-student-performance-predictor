import streamlit as st
import pandas as pd
import joblib


# ============================================================
# LOAD TRAINED MODEL AND METRICS
# ============================================================

model = joblib.load("student_performance_pipeline.pkl")
metrics = joblib.load("model_metrics.pkl")


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .recommendation {
        padding: 12px;
        margin: 8px 0;
        border-radius: 10px;
        background-color: #f5f5f5;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🎓 AI Student Performance Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning powered academic performance prediction'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# STUDENT INFORMATION
# ============================================================

st.header("👨‍🎓 Student Information")

col1, col2, col3 = st.columns(3)


with col1:

    school = st.selectbox(
        "School",
        ["GP", "MS"]
    )

    sex = st.selectbox(
        "Sex",
        ["F", "M"]
    )

    age = st.number_input(
        "Age",
        min_value=15,
        max_value=22,
        value=17
    )

    address = st.selectbox(
        "Address",
        ["U", "R"],
        help="U = Urban, R = Rural"
    )

    famsize = st.selectbox(
        "Family Size",
        ["LE3", "GT3"],
        help="LE3 = 3 or fewer, GT3 = greater than 3"
    )


with col2:

    Pstatus = st.selectbox(
        "Parent Status",
        ["T", "A"],
        help="T = Together, A = Apart"
    )

    Medu = st.slider(
        "Mother's Education",
        0,
        4,
        2
    )

    Fedu = st.slider(
        "Father's Education",
        0,
        4,
        2
    )

    Mjob = st.selectbox(
        "Mother's Job",
        [
            "teacher",
            "health",
            "services",
            "at_home",
            "other"
        ]
    )

    Fjob = st.selectbox(
        "Father's Job",
        [
            "teacher",
            "health",
            "services",
            "at_home",
            "other"
        ]
    )


with col3:

    reason = st.selectbox(
        "Reason for Choosing School",
        [
            "home",
            "reputation",
            "course",
            "other"
        ]
    )

    guardian = st.selectbox(
        "Guardian",
        [
            "mother",
            "father",
            "other"
        ]
    )

    traveltime = st.slider(
        "Travel Time",
        1,
        4,
        2
    )

    studytime = st.slider(
        "Weekly Study Time",
        1,
        4,
        2
    )

    failures = st.number_input(
        "Previous Failures",
        min_value=0,
        max_value=4,
        value=0
    )


# ============================================================
# EDUCATION & SUPPORT
# ============================================================

st.divider()

st.header("📚 Education & Support")

col1, col2, col3 = st.columns(3)


with col1:

    schoolsup = st.selectbox(
        "Extra Educational Support",
        ["yes", "no"]
    )

    famsup = st.selectbox(
        "Family Educational Support",
        ["yes", "no"]
    )

    paid = st.selectbox(
        "Extra Paid Classes",
        ["yes", "no"]
    )


with col2:

    activities = st.selectbox(
        "Extra-curricular Activities",
        ["yes", "no"]
    )

    nursery = st.selectbox(
        "Attended Nursery School",
        ["yes", "no"]
    )

    higher = st.selectbox(
        "Wants Higher Education",
        ["yes", "no"]
    )


with col3:

    internet = st.selectbox(
        "Internet Access",
        ["yes", "no"]
    )

    romantic = st.selectbox(
        "Romantic Relationship",
        ["yes", "no"]
    )


# ============================================================
# LIFESTYLE & HEALTH
# ============================================================

st.divider()

st.header("❤️ Lifestyle & Health")

col1, col2, col3 = st.columns(3)


with col1:

    famrel = st.slider(
        "Family Relationship Quality",
        1,
        5,
        3
    )

    freetime = st.slider(
        "Free Time",
        1,
        5,
        3
    )


with col2:

    goout = st.slider(
        "Going Out",
        1,
        5,
        3
    )

    Dalc = st.slider(
        "Weekday Alcohol Consumption",
        1,
        5,
        1
    )


with col3:

    Walc = st.slider(
        "Weekend Alcohol Consumption",
        1,
        5,
        1
    )

    health = st.slider(
        "Current Health",
        1,
        5,
        3
    )

    absences = st.number_input(
        "School Absences",
        min_value=0,
        max_value=100,
        value=5
    )


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.divider()

predict_button = st.button(
    "🔮 Predict Student Performance",
    use_container_width=True
)


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    # --------------------------------------------------------
    # CREATE STUDENT INPUT
    # --------------------------------------------------------

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
        "absences": absences
    }


    # --------------------------------------------------------
    # CONVERT INPUT TO DATAFRAME
    # --------------------------------------------------------

    student_df = pd.DataFrame([student_data])


    # --------------------------------------------------------
    # PREDICTION
    # --------------------------------------------------------

    prediction = model.predict(student_df)[0]

    prediction = max(0, min(20, prediction))


    # ========================================================
    # PERFORMANCE CATEGORY
    # ========================================================

    if prediction >= 16:

        category = "Excellent 🌟"

    elif prediction >= 14:

        category = "Very Good 🟢"

    elif prediction >= 10:

        category = "Average 🟡"

    else:

        category = "Needs Improvement 🔴"


    # ========================================================
    # RISK LEVEL
    # ========================================================

    if prediction >= 14:

        risk = "Low Risk 🟢"

    elif prediction >= 10:

        risk = "Medium Risk 🟡"

    else:

        risk = "High Risk 🔴"


    # ========================================================
    # MODEL PERFORMANCE
    # ========================================================

    st.divider()

    st.header("📈 Model Performance")

    metric_col1, metric_col2, metric_col3 = st.columns(3)


    with metric_col1:

        st.metric(
            "MAE",
            f"{metrics['MAE']:.3f}"
        )


    with metric_col2:

        st.metric(
            "RMSE",
            f"{metrics['RMSE']:.3f}"
        )


    with metric_col3:

        st.metric(
            "R² Score",
            f"{metrics['R2']:.3f}"
        )


    st.caption(
        "These metrics were calculated using the held-out test dataset."
    )


    # ========================================================
    # PREDICTION RESULT
    # ========================================================

    st.divider()

    st.header("📊 Prediction Result")

    result_col1, result_col2, result_col3 = st.columns(3)


    with result_col1:

        st.metric(
            "Predicted Performance",
            f"{prediction:.2f} / 20"
        )


    with result_col2:

        st.metric(
            "Performance Category",
            category
        )


    with result_col3:

        st.metric(
            "Academic Risk",
            risk
        )


    # ========================================================
    # PERFORMANCE PROGRESS
    # ========================================================

    st.subheader("📈 Performance Level")

    progress = prediction / 20

    st.progress(progress)

    st.write(
        f"Predicted score: **{prediction:.2f} / 20**"
    )


    # ========================================================
    # PERSONALIZED RECOMMENDATIONS
    # ========================================================

    st.divider()

    st.header("💡 Personalized Recommendations")

    recommendations = []


    if studytime <= 2:

        recommendations.append(
            "📚 Increase weekly study time and follow a consistent study schedule."
        )


    if failures > 0:

        recommendations.append(
            "⚠️ Focus on subjects where you previously struggled "
            "and consider additional academic support."
        )


    if absences > 10:

        recommendations.append(
            "🏫 Try to reduce school absences and maintain regular attendance."
        )


    if freetime >= 4:

        recommendations.append(
            "⏰ Balance free time with revision and academic activities."
        )


    if goout >= 4:

        recommendations.append(
            "🎯 Maintain a healthy balance between social activities "
            "and study time."
        )


    if famrel <= 2:

        recommendations.append(
            "❤️ A supportive family environment may help improve academic focus."
        )


    if health <= 2:

        recommendations.append(
            "💪 Pay attention to your health, sleep and daily routine."
        )


    if absences <= 5:

        recommendations.append(
            "✅ Your attendance level is currently good. Keep maintaining it."
        )


    if studytime >= 3:

        recommendations.append(
            "🌟 Your study-time commitment is good. Continue maintaining consistency."
        )


    if not recommendations:

        recommendations.append(
            "🌟 Your current profile looks balanced. "
            "Continue maintaining your study habits."
        )


    for recommendation in recommendations:

        st.markdown(
            f"""
            <div class="recommendation">
                {recommendation}
            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # MODEL INSIGHTS
    # ========================================================

    st.divider()

    st.header("🧠 Model Insights")

    st.write(
        "These features were considered important by the "
        "trained Random Forest model."
    )


    try:

        # Get pipeline components

        trained_preprocessor = model.named_steps["preprocessor"]

        trained_model = model.named_steps["model"]


        # Get transformed feature names

        feature_names = (
            trained_preprocessor
            .get_feature_names_out()
        )


        # Get feature importance

        importances = (
            trained_model
            .feature_importances_
        )


        # Create dataframe

        importance_df = pd.DataFrame(
            {
                "Feature": feature_names,
                "Importance": importances
            }
        )


        # Sort by importance

        importance_df = importance_df.sort_values(
            by="Importance",
            ascending=False
        )


        # Top 10

        top_features = importance_df.head(10)


        # Chart

        st.subheader(
            "📊 Top 10 Important Features"
        )

        chart_data = (
            top_features
            .set_index("Feature")["Importance"]
        )

        st.bar_chart(chart_data)


        # Table

        display_df = top_features.copy()


        display_df["Importance"] = (
            display_df["Importance"] * 100
        ).round(2)


        display_df = display_df.rename(
            columns={
                "Importance": "Importance (%)"
            }
        )


        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )


    except Exception as e:

        st.warning(
            "Model insights could not be displayed."
        )

        st.caption(str(e))


    # ========================================================
    # DISCLAIMER
    # ========================================================

    st.divider()

    st.caption(
        "⚠️ This prediction is generated by a machine-learning "
        "model and should be used for educational guidance only. "
        "It is not a definitive assessment of a student's future performance."
    )