# 🎓 AI Student Performance Predictor

An end-to-end **Machine Learning web application** that predicts student academic performance based on academic and behavioral factors.

The project combines **Python, Machine Learning, Pandas, Scikit-learn, and Streamlit** to provide an interactive prediction interface.

---

## 🚀 Features

* 📊 Student performance prediction using Machine Learning
* 🤖 Trained ML model saved as a `.pkl` file
* 🧠 Automated prediction pipeline
* 🌐 Interactive Streamlit web interface
* 📈 Student performance analysis
* ⚡ Fast local predictions
* 🧩 Modular project structure
* 🔄 Separate training and prediction scripts

---

## 🛠️ Tech Stack

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Core programming language |
| Pandas        | Data processing           |
| NumPy         | Numerical operations      |
| Scikit-learn  | Machine Learning          |
| Streamlit     | Web application           |
| Joblib/Pickle | Model serialization       |
| Git & GitHub  | Version control           |

---

## 🧠 Machine Learning Workflow

```text
Student Dataset
      ↓
Data Preprocessing
      ↓
Feature Selection
      ↓
Train/Test Split
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Save Trained Model
      ↓
Streamlit Application
      ↓
Student Input
      ↓
Performance Prediction
```

---

## 📂 Project Structure

```text
ai-student-performance-predictor/
│
├── app.py
├── train_model.py
├── predict.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   └── student_performance_model.pkl
│
└── frontend/
    └── ...
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jeff-ie-ee/ai-student-performance-predictor.git
```

### 2. Navigate to the project

```bash
cd ai-student-performance-predictor
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Train the model

```bash
python train_model.py
```

This trains the Machine Learning model and saves the trained model inside:

```text
models/student_performance_model.pkl
```

### Test prediction

```bash
python predict.py
```

### Launch the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

## 📊 Prediction Pipeline

The application accepts relevant student information as input and passes it through the trained Machine Learning model.

```text
User Input
    ↓
Input Validation
    ↓
Feature Processing
    ↓
Trained ML Model
    ↓
Prediction
    ↓
Performance Result
```

---

## 🎯 Project Objective

The main objective of this project is to demonstrate how Machine Learning can be applied to **educational data** to identify patterns and predict student academic performance.

Such systems can potentially help educators identify students who may require additional academic support.

---

## 🔮 Future Improvements

* 📈 Add interactive performance dashboards
* 📊 Add feature-importance visualization
* 🧠 Compare multiple ML algorithms
* 🎯 Improve prediction accuracy
* 👨‍🎓 Add student performance categories
* 📋 Add downloadable prediction reports
* ☁️ Deploy the application to the cloud
* 🔐 Add authentication
* 🗄️ Add database support
* 📱 Improve mobile responsiveness

---

## 📸 Screenshots

Add screenshots of the Streamlit application here after completing the UI.

```text
screenshots/
├── home.png
├── prediction.png
└── results.png
```

---

## 💡 Skills Demonstrated

This project demonstrates practical experience with:

* Python Programming
* Data Preprocessing
* Exploratory Data Analysis
* Machine Learning
* Model Training
* Model Evaluation
* Model Serialization
* Streamlit
* Git & GitHub
* End-to-End ML Application Development

---

## 👨‍💻 Author

**Jeffrin John**

BSc Computer Applications
Aspiring AI Engineer

GitHub: `Jeff-ie-ee`

---

## ⭐ Project Status

**Status:** 🚧 Active Development

The core Machine Learning pipeline and Streamlit application are implemented. UI improvements, documentation, testing, and deployment can be added as the project evolves.
