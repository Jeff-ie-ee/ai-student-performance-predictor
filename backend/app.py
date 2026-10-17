import streamlit as st
import requests
import time


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Student Performance Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(99,102,241,0.10), transparent 30%),
            radial-gradient(circle at 90% 20%, rgba(14,165,233,0.08), transparent 30%),
            #f8fafc;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* ---------- HEADER ---------- */

    .hero {
        padding: 35px 35px 30px 35px;
        border-radius: 24px;
        background: linear-gradient(
            135deg,
            #111827 0%,
            #1e293b 55%,
            #312e81 100%
        );
        color: white;
        box-shadow: 0 15px 40px rgba(15, 23, 42, 0.20);
        margin-bottom: 25px;
        animation: fadeIn 0.8s ease-in-out;
    }

    .hero-title {
        font-size: 44px;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        font-size: 17px;
        color: #cbd5e1;
        line-height: 1.6;
    }

    .hero-badge {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 999px;
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.18);
        font-size: 13px;
        margin-bottom: 15px;
    }

    /* ---------- SECTION HEADERS ---------- */

    .section-title {
        font-size: 25px;
        font-weight: 750;
        color: #111827;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .section-description {
        color: #64748b;
        font-size: 14px;
        margin-bottom: 18px;
    }

    /* ---------- CARDS ---------- */

    .info-card {
        background: rgba(255,255,255,0.85);
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 22px;
        box-shadow: 0 8px 25px rgba(15,23,42,0.06);
        transition: all 0.25s ease;
        height: 100%;
    }

    .info-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 14px 30px rgba(15,23,42,0.10);
    }

    /* ---------- RESULT ---------- */

    .result-card {
        background: linear-gradient(135deg, #ffffff, #f8fafc);
        border: 1px solid #e2e8f0;
        border-radius: 22px;
        padding: 25px;
        box-shadow: 0 12px 35px rgba(15,23,42,0.08);
        text-align: center;
        animation: slideUp 0.7s ease;
    }

    .result-number {
        font-size: 42px;
        font-weight: 800;
        color: #111827;
    }

    .result-label {
        font-size: 14px;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .performance-badge {
        display: inline-block;
        padding: 8px 18px;
        border-radius: 999px;
        font-weight: 700;
        margin-top: 8px;
    }

    .risk-badge {
        display: inline-block;
        padding: 8px 18px;
        border-radius: 999px;
        font-weight: 700;
        margin-top: 8px;
    }

    /* ---------- RECOMMENDATION ---------- */

    .recommendation {
        background: white;
        border-left: 5px solid #6366f1;
        border-radius: 12px;
        padding: 15px 18px;
        margin: 10px 0;
        box-shadow: 0 5px 18px rgba(15,23,42,0.05);
        animation: fadeIn 0.5s ease;
    }

    .recommendation-title {
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 4px;
    }

    .recommendation-text {
        color: #64748b;
        font-size: 14px;
    }

    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        padding: 30px 10px 10px;
        color: #94a3b8;
        font-size: 13px;
    }

    /* ---------- BUTTON ---------- */

    .stButton > button,
    .stFormSubmitButton > button {
        border-radius: 12px;
        font-weight: 700;
        min-height: 50px;
        transition: all 0.25s ease;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(79,70,229,0.20);
    }

    /* ---------- ANIMATIONS ---------- */

    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }

    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes pulse {
        0% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.03);
        }
        100% {
            transform: scale(1);
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🎓 AI Predictor")

    st.markdown(
        """
        <div style="
            padding:15px;
            border-radius:15px;
            background:#f1f5f9;
            margin-bottom:20px;
        ">
        <b>About this system</b><br><br>
        This application uses a Machine Learning model
        to estimate a student's final academic performance
        based on academic, demographic and lifestyle factors.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 📊 Model")

    st.info(
        "Machine Learning Pipeline\n\n"
        "The prediction is generated through the FastAPI backend."
    )

    st.markdown("### ⚡ API Status")

    try:
        health_check = requests.get(
            "http://127.0.0.1:8000/",
            timeout=2
        )

        if health_check.status_code == 200:
            st.success("Backend Online")
        else:
            st.warning("Backend Responding")

    except requests.exceptions.RequestException:
        st.error("Backend Offline")

    st.markdown("---")

    st.caption("AI Student Performance Predictor")
    st.caption("Academic Performance Analysis System")


# ============================================================
# HERO HEADER
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-badge">
            MACHINE LEARNING • ACADEMIC ANALYTICS
        </div>

        <div class="hero-title">
            🎓 AI Student Performance Predictor
        </div>

        <div class="hero-subtitle">
            Predict final academic performance using
            student academic, demographic and lifestyle information.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# INTRODUCTION
# ============================================================

st.markdown(
    """
    <div class="section-title">
        Student Assessment
    </div>

    <div class="section-description">
        Enter the student's information below and let the trained
        Machine Learning model estimate the final grade.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FORM
# ============================================================

with st.form("student_form"):

    # ========================================================
    # STUDENT INFORMATION
    # ========================================================

    st.markdown(
        """
        <div class="section-title">👤 Student Information</div>
        <div class="section-description">
        Basic demographic and family information
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        school = st.selectbox(
            "School",
            ["GP", "MS"]
        )

        sex = st.selectbox(
            "Sex",
            ["M", "F"]
        )

        age = st.number_input(
            "Age",
            min_value=15,
            max_value=25,
            value=18
        )

        address = st.selectbox(
            "Address",
            ["U", "R"],
            help="U = Urban, R = Rural"
        )

        famsize = st.selectbox(
            "Family Size",
            ["GT3", "LE3"],
            help="GT3 = Greater than 3, LE3 = 3 or fewer"
        )

    with col2:

        Pstatus = st.selectbox(
            "Parent Status",
            ["T", "A"],
            help="T = Together, A = Apart"
        )

        Medu = st.slider(
            "Mother Education",
            0,
            4,
            3,
            help="0 = none, 4 = higher education"
        )

        Fedu = st.slider(
            "Father Education",
            0,
            4,
            3,
            help="0 = none, 4 = higher education"
        )

        Mjob = st.selectbox(
            "Mother Job",
            [
                "teacher",
                "health",
                "services",
                "at_home",
                "other"
            ]
        )

        Fjob = st.selectbox(
            "Father Job",
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
                "course",
                "home",
                "reputation",
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
            1
        )

        studytime = st.slider(
            "Study Time",
            1,
            4,
            3
        )

        failures = st.slider(
            "Previous Failures",
            0,
            3,
            0
        )


    st.divider()


    # ========================================================
    # EDUCATION & SUPPORT
    # ========================================================

    st.markdown(
        """
        <div class="section-title">📚 Education & Support</div>
        <div class="section-description">
        Information about educational support and student goals
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        schoolsup = st.selectbox(
            "Extra School Support",
            ["yes", "no"]
        )

        famsup = st.selectbox(
            "Family Support",
            ["yes", "no"]
        )

        paid = st.selectbox(
            "Extra Paid Classes",
            ["yes", "no"]
        )

    with col2:

        activities = st.selectbox(
            "Extra Activities",
            ["yes", "no"]
        )

        nursery = st.selectbox(
            "Attended Nursery",
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

        absences = st.number_input(
            "Absences",
            min_value=0,
            max_value=100,
            value=4
        )


    st.divider()


    # ========================================================
    # LIFESTYLE
    # ========================================================

    st.markdown(
        """
        <div class="section-title">🌱 Lifestyle & Social Information</div>
        <div class="section-description">
        Lifestyle and personal factors used by the prediction model
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        famrel = st.slider(
            "Family Relationship",
            1,
            5,
            4
        )

        freetime = st.slider(
            "Free Time",
            1,
            5,
            3
        )

        goout = st.slider(
            "Going Out",
            1,
            5,
            3
        )

    with col2:

        Dalc = st.slider(
            "Weekday Alcohol Consumption",
            1,
            5,
            1
        )

        Walc = st.slider(
            "Weekend Alcohol Consumption",
            1,
            5,
            1
        )

        health = st.slider(
            "Health",
            1,
            5,
            4
        )

    with col3:

        G1 = st.slider(
            "First Period Grade (G1)",
            0,
            20,
            14
        )

        G2 = st.slider(
            "Second Period Grade (G2)",
            0,
            20,
            15
        )


    st.divider()


    # ========================================================
    # PREDICT BUTTON
    # ========================================================

    submitted = st.form_submit_button(
        "🚀 Predict Student Performance",
        use_container_width=True
    )


# ============================================================
# PREDICTION
# ============================================================

if submitted:

    # --------------------------------------------------------
    # CREATE REQUEST DATA
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
        "absences": absences,

        "G1": G1,
        "G2": G2
    }


    # --------------------------------------------------------
    # LOADING ANIMATION
    # --------------------------------------------------------

    with st.spinner("Analyzing student information..."):

        try:

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json=student_data,
                timeout=30
            )

            time.sleep(0.5)


            # =================================================
            # SUCCESS
            # =================================================

            if response.status_code == 200:

                result = response.json()

                predicted_grade = float(
                    result.get("predicted_grade", 0)
                )

                performance = result.get(
                    "performance",
                    "Unknown"
                )

                risk_level = result.get(
                    "risk_level",
                    "Unknown"
                )


                # ------------------------------------------------
                # NORMALIZE GRADE
                # ------------------------------------------------

                predicted_grade = max(
                    0,
                    min(20, predicted_grade)
                )

                percentage = (
                    predicted_grade / 20
                ) * 100


                # =================================================
                # SUCCESS MESSAGE
                # =================================================

                st.success(
                    "Prediction completed successfully! 🎉"
                )


                st.markdown(
                    """
                    <div class="section-title">
                        📊 Prediction Results
                    </div>

                    <div class="section-description">
                        AI-generated academic performance assessment
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                # =================================================
                # RESULT CARDS
                # =================================================

                r1, r2, r3 = st.columns(3)


                with r1:

                    st.markdown(
                        f"""
                        <div class="result-card">

                            <div class="result-label">
                                Predicted Grade
                            </div>

                            <div class="result-number">
                                {predicted_grade:.2f}
                                <span style="
                                    font-size:20px;
                                    color:#64748b;
                                ">
                                    / 20
                                </span>
                            </div>

                            <div style="
                                color:#64748b;
                                margin-top:5px;
                            ">
                                {percentage:.1f}% estimated score
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                with r2:

                    performance_lower = str(
                        performance
                    ).lower()

                    if "good" in performance_lower:
                        badge_bg = "#dcfce7"
                        badge_text = "#166534"

                    elif "average" in performance_lower:
                        badge_bg = "#fef3c7"
                        badge_text = "#92400e"

                    else:
                        badge_bg = "#fee2e2"
                        badge_text = "#991b1b"


                    st.markdown(
                        f"""
                        <div class="result-card">

                            <div class="result-label">
                                Performance
                            </div>

                            <div style="
                                font-size:32px;
                                font-weight:800;
                                margin-top:18px;
                            ">
                                {performance}
                            </div>

                            <div class="performance-badge"
                                style="
                                    background:{badge_bg};
                                    color:{badge_text};
                                ">
                                {performance}
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                with r3:

                    risk_lower = str(
                        risk_level
                    ).lower()

                    if "low" in risk_lower:
                        risk_bg = "#dcfce7"
                        risk_text = "#166534"

                    elif "medium" in risk_lower:
                        risk_bg = "#fef3c7"
                        risk_text = "#92400e"

                    else:
                        risk_bg = "#fee2e2"
                        risk_text = "#991b1b"


                    st.markdown(
                        f"""
                        <div class="result-card">

                            <div class="result-label">
                                Risk Level
                            </div>

                            <div style="
                                font-size:32px;
                                font-weight:800;
                                margin-top:18px;
                            ">
                                {risk_level}
                            </div>

                            <div class="risk-badge"
                                style="
                                    background:{risk_bg};
                                    color:{risk_text};
                                ">
                                {risk_level} Risk
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                st.write("")


                # =================================================
                # GRADE PROGRESS
                # =================================================

                st.markdown(
                    """
                    <div class="section-title">
                        📈 Academic Performance Indicator
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.progress(
                    percentage / 100
                )

                p1, p2, p3 = st.columns(3)

                with p1:
                    st.caption("0 — Beginning")

                with p2:
                    st.caption("10 — Average")

                with p3:
                    st.caption("20 — Maximum")


                # =================================================
                # STUDENT SNAPSHOT
                # =================================================

                st.divider()

                st.markdown(
                    """
                    <div class="section-title">
                        👤 Student Snapshot
                    </div>

                    <div class="section-description">
                        Key information used during prediction
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                s1, s2, s3, s4 = st.columns(4)

                with s1:
                    st.metric(
                        "Age",
                        age
                    )

                with s2:
                    st.metric(
                        "Study Time",
                        f"{studytime}/4"
                    )

                with s3:
                    st.metric(
                        "Absences",
                        absences
                    )

                with s4:
                    st.metric(
                        "Previous Failures",
                        failures
                    )


                # =================================================
                # ACADEMIC PROFILE
                # =================================================

                st.divider()

                st.markdown(
                    """
                    <div class="section-title">
                        📚 Academic Profile
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                a1, a2, a3 = st.columns(3)

                with a1:

                    st.metric(
                        "G1",
                        f"{G1}/20"
                    )

                with a2:

                    st.metric(
                        "G2",
                        f"{G2}/20"
                    )

                with a3:

                    st.metric(
                        "Predicted G3",
                        f"{predicted_grade:.2f}/20"
                    )


                # =================================================
                # RECOMMENDATIONS
                # =================================================

                st.divider()

                st.markdown(
                    """
                    <div class="section-title">
                        💡 Academic Recommendations
                    </div>

                    <div class="section-description">
                        General suggestions based on the entered profile
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                recommendations = []


                # Study time
                if studytime <= 1:

                    recommendations.append(
                        (
                            "📖 Increase Study Time",
                            "Consider creating a consistent daily study schedule "
                            "and gradually increasing focused study sessions."
                        )
                    )

                elif studytime == 2:

                    recommendations.append(
                        (
                            "📖 Maintain Regular Study",
                            "A structured study routine with regular revision "
                            "can help maintain academic consistency."
                        )
                    )

                else:

                    recommendations.append(
                        (
                            "📖 Strong Study Routine",
                            "Continue maintaining your current study routine "
                            "while focusing on quality and revision."
                        )
                    )


                # Absences
                if absences > 20:

                    recommendations.append(
                        (
                            "🏫 Improve Attendance",
                            "A high number of absences can reduce exposure "
                            "to classroom learning. Try to maintain regular attendance."
                        )
                    )

                elif absences > 10:

                    recommendations.append(
                        (
                            "🏫 Monitor Attendance",
                            "Keep track of attendance and avoid unnecessary "
                            "absences where possible."
                        )
                    )

                else:

                    recommendations.append(
                        (
                            "🏫 Good Attendance Pattern",
                            "The entered absence level is relatively low. "
                            "Continue maintaining regular class participation."
                        )
                    )


                # Previous failures
                if failures > 0:

                    recommendations.append(
                        (
                            "🎯 Focus on Difficult Subjects",
                            "Previous failures indicate areas where additional "
                            "revision, practice or academic support may be useful."
                        )
                    )

                else:

                    recommendations.append(
                        (
                            "🎯 Maintain Consistency",
                            "No previous failures were entered. Continue using "
                            "regular revision and practice to maintain progress."
                        )
                    )


                # G1 / G2
                if G2 > G1:

                    recommendations.append(
                        (
                            "📈 Positive Academic Trend",
                            f"G2 ({G2}) is higher than G1 ({G1}). "
                            "Continue the learning strategies that are helping improvement."
                        )
                    )

                elif G2 < G1:

                    recommendations.append(
                        (
                            "🔎 Review Recent Performance",
                            f"G2 ({G2}) is lower than G1 ({G1}). "
                            "Review recent topics and identify areas that need additional practice."
                        )
                    )

                else:

                    recommendations.append(
                        (
                            "📊 Stable Performance",
                            "G1 and G2 are at the same level. "
                            "Consistent revision can help improve future performance."
                        )
                    )


                for title, description in recommendations:

                    st.markdown(
                        f"""
                        <div class="recommendation">

                            <div class="recommendation-title">
                                {title}
                            </div>

                            <div class="recommendation-text">
                                {description}
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                # =================================================
                # MODEL METRICS
                # =================================================

                st.divider()

                st.markdown(
                    """
                    <div class="section-title">
                        🤖 Model Information
                    </div>

                    <div class="section-description">
                        Performance information from the trained model
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                try:

                    # Try common metric names
                    mae = None
                    rmse = None
                    r2 = None

                    if isinstance(result, dict):

                        mae = result.get("mae")
                        rmse = result.get("rmse")
                        r2 = result.get("r2")

                    if mae is None and isinstance(
                        result, dict
                    ):
                        mae = result.get("MAE")

                    if rmse is None and isinstance(
                        result, dict
                    ):
                        rmse = result.get("RMSE")

                    if r2 is None and isinstance(
                        result, dict
                    ):
                        r2 = result.get("R2")


                    if isinstance(metrics, dict):

                        if mae is None:
                            mae = metrics.get("MAE")

                        if mae is None:
                            mae = metrics.get("mae")

                        if rmse is None:
                            rmse = metrics.get("RMSE")

                        if rmse is None:
                            rmse = metrics.get("rmse")

                        if r2 is None:
                            r2 = metrics.get("R2")

                        if r2 is None:
                            r2 = metrics.get("r2")


                    m1, m2, m3 = st.columns(3)


                    with m1:

                        if mae is not None:

                            st.metric(
                                "MAE",
                                f"{float(mae):.2f}"
                            )

                        else:

                            st.metric(
                                "MAE",
                                "Available"
                            )


                    with m2:

                        if rmse is not None:

                            st.metric(
                                "RMSE",
                                f"{float(rmse):.2f}"
                            )

                        else:

                            st.metric(
                                "RMSE",
                                "Available"
                            )


                    with m3:

                        if r2 is not None:

                            st.metric(
                                "R² Score",
                                f"{float(r2):.2f}"
                            )

                        else:

                            st.metric(
                                "R² Score",
                                "Available"
                            )


                except Exception:

                    st.info(
                        "Model prediction completed successfully."
                    )


                # =================================================
                # RAW API RESPONSE
                # =================================================

                with st.expander(
                    "🔧 View Technical Prediction Response"
                ):

                    st.json(result)


            # =================================================
            # API ERROR
            # =================================================

            else:

                st.error(
                    "Prediction failed."
                )

                st.code(
                    response.text
                )


        # ========================================================
        # CONNECTION ERROR
        # ========================================================

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Cannot connect to the FastAPI backend."
            )

            st.warning(
                "Please start your FastAPI server first."
            )

            st.code(
                "uvicorn backend.main:app --reload"
            )


        # ========================================================
        # TIMEOUT
        # ========================================================

        except requests.exceptions.Timeout:

            st.error(
                "⏱️ The prediction request timed out."
            )

            st.info(
                "Check whether the FastAPI backend and ML model are running correctly."
            )


        # ========================================================
        # GENERAL ERROR
        # ========================================================

        except Exception as e:

            st.error(
                "⚠️ An unexpected error occurred."
            )

            st.exception(e)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        AI Student Performance Predictor
        <br>
        Machine Learning Based Academic Performance Analysis
        <br><br>
        Developed as an Artificial Intelligence / Machine Learning Project

    </div>
    """,
    unsafe_allow_html=True
)