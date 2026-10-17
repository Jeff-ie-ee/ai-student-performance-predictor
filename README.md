# AI Student Performance Predictor

An end-to-end Machine Learning web application that predicts student academic performance using student academic, family, and behavioral information.

The project uses **Python, Pandas, Scikit-learn, Streamlit, and FastAPI** to provide an interactive dashboard and a prediction API.

## Features

- Predict student performance on a scale of 0â€“20.
- Interactive Streamlit dashboard.
- FastAPI REST API for predictions.
- Machine learning pipeline for processing student information.
- Performance categories: Excellent, Good, Average, and Needs Improvement.
- Risk categories: Low, Medium, and High.
- Separate model training, prediction, and application components.

> **Note:** Predictions are estimates from a machine learning model and should not be used as the sole basis for academic decisions.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning pipeline |
| Streamlit | Interactive dashboard |
| FastAPI | Prediction API |
| Uvicorn | API server |
| Joblib | Saving and loading the trained model |
| Git and GitHub | Version control |

## Machine Learning Workflow

```text
Student Dataset
      |
Data Preprocessing
      |
Feature Selection
      |
Model Training and Evaluation
      |
Saved ML Pipeline
      |
FastAPI Prediction Endpoint
      |
Streamlit Dashboard
      |
Predicted Student Performance
```

## Project Structure

```text
ai-student-performance-predictor/
â”œâ”€â”€ app.py
â”œâ”€â”€ main.py
â”œâ”€â”€ train_model.py
â”œâ”€â”€ predict.py
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ README.md
â”œâ”€â”€ backend/
â”‚   â”œâ”€â”€ app.py
â”‚   â”œâ”€â”€ main.py
â”‚   â”œâ”€â”€ requirements.txt
â”‚   â””â”€â”€ student_performance_pipeline.pkl
â”œâ”€â”€ data/
â”‚   â””â”€â”€ student-mat.csv
â”œâ”€â”€ models/
â”‚   â””â”€â”€ student_performance_model.pkl
â”œâ”€â”€ notebooks/
â”œâ”€â”€ research/
â””â”€â”€ src/
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jeff-ie-ee/ai-student-performance-predictor.git
cd ai-student-performance-predictor
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Open two terminals in the project directory and activate the virtual environment in each.

### Terminal 1: Start the FastAPI backend

```bash
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

Health check:

```text
http://127.0.0.1:8000/health
```

### Terminal 2: Start the Streamlit dashboard

```bash
python -m streamlit run app.py
```

The dashboard communicates with the local API at `http://127.0.0.1:8000/predict`.

Start the backend before making predictions through the dashboard.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API information |
| GET | `/health` | Check API health |
| POST | `/predict` | Predict student performance |

You can test the API interactively using the Swagger documentation at `/docs`.

## Prediction Results

The API returns a predicted grade, a performance category, and a risk category. The categories are determined by thresholds defined in the application.

These results are estimates and do not guarantee a student's actual academic outcome.

## Dataset

The project includes a student mathematics performance dataset named `student-mat.csv`. The application uses selected student attributes as model inputs.

## Skills Demonstrated

- Python programming
- Data preprocessing and feature selection
- Machine learning pipelines
- Model training and serialization
- REST API development with FastAPI
- Interactive applications with Streamlit
- Git and GitHub
- Integrating a trained model into a web application

## Future Improvements

- Add feature-importance visualizations.
- Compare multiple machine learning algorithms.
- Improve validation and evaluation reporting.
- Add downloadable prediction reports.
- Deploy the application to a cloud platform.
- Add automated tests and continuous integration.
- Improve dashboard accessibility and mobile responsiveness.

## Author

**Jeffrin John**
BSc Computer Applications | Aspiring AI/ML Engineer

GitHub: [Jeff-ie-ee](https://github.com/Jeff-ie-ee)
