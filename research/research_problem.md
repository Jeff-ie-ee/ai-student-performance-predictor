# AI Student Performance Research Predictor

## Research Problem

Educational institutions often identify academically struggling students only
after poor examination results have already occurred.

This project investigates whether machine learning can use previously available
student information to predict future academic performance and identify
students who may require early academic support.

## Primary Research Question

Can machine learning models accurately predict student academic performance
using historical academic, behavioral, and educational features?

## Secondary Research Questions

1. Which features contribute most to academic performance prediction?
2. Which machine learning model performs best?
3. Can explainable AI provide meaningful explanations for individual predictions?
4. Can an early-warning model identify potentially at-risk students?
5. How reliable are the model's predictions across different student groups?

## Objectives

- Analyze student academic-performance data.
- Perform data cleaning and exploratory data analysis.
- Engineer meaningful predictive features.
- Compare multiple machine learning algorithms.
- Evaluate models using appropriate statistical metrics.
- Apply Explainable AI using SHAP.
- Develop an early-warning risk prediction system.
- Generate personalized, data-driven recommendations.
- Deploy the final model through an API and dashboard.

## Important Research Principle

The system is intended to support educators and students rather than make
high-stakes decisions automatically.

Predictions represent estimated risk and should not be treated as definitive
judgments about a student's ability or future.


Absence Analysis:

The relationship between student absences and final academic performance
was not strictly linear. Students with 6–10 absences showed the highest
average final grade (11.40), while students with 11–20 absences had a
lower average (10.12). The 21+ absence group contained only 15 students,
limiting the reliability of conclusions for this category.

Therefore, absences should be considered as one predictive feature among
multiple academic, behavioral, and demographic variables rather than as
an independent causal determinant of performance.