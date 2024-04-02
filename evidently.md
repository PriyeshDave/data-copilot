# Model Monitoring Framework Documentation

## Introduction
Model monitoring is a crucial aspect of any machine learning system to ensure that deployed models continue to perform effectively over time. As data evolves and environments change, it's essential to monitor models for potential drift and degradation in performance. To facilitate this process, we have developed a comprehensive model monitoring framework using Evidently, a Python library for ML observability.

## Why Model Monitoring?
Model monitoring helps in maintaining the performance and reliability of machine learning models in production environments. By continuously monitoring models, organizations can:

- Identify and mitigate data drift to ensure model accuracy and fairness.
- Detect changes in data quality to prevent degradation in model performance.
- Understand how models behave over time and in different contexts.
- Improve model interpretability and trustworthiness.

## Framework Overview
Our model monitoring framework is designed to handle two types of data: tabular and textual. It provides various capabilities tailored to each data type, including:

### For Textual Data
1. **Data Drift Detection**: Identify shifts in the distribution of text data over time.
2. **Embeddings Drift Detection**: Detect changes in semantic representations of text using word embeddings.
3. **Text Descriptors**: Provide statistics such as text length, word count, and sentence count.
4. **N-gram Analysis**: Analyze n-grams (up to decagrams) to understand text patterns.
5. **Word Cloud Visualization**: Visualize token/word distributions using word clouds.

### For Tabular Data
1. **Data Quality Reports**: Identify issues such as missing data and provide data quality test reports.
2. **Data Drift Reports**: Detect drift at different quantiles (0.25, 0.5, 0.75) to understand changes in data distribution.

## Framework Usage
To use our model monitoring framework, follow these steps:

1. **Clone Repository**: Clone the repository containing the framework.
   ```bash
   git clone https://github.com/your/repository.git
   ```

2. **Set Up Virtual Environment**: Create a virtual environment and activate it.
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

3. **Install Required Packages**: Install all required packages listed in `ml_observability_requirements.txt`.
   ```bash
   pip install -r ml_observability_requirements.txt
   ```

4. **Run Application**: Execute the `app.py` file using Streamlit to access the interactive UI for model monitoring.
   ```bash
   streamlit run app.py
   ```

## Key Concepts
### Evidently
[Evidently](https://github.com/evidentlyai/evidently) is a Python library that provides tools for monitoring machine learning models. It offers various functionalities for model observability, including drift detection, feature importance analysis, and model performance evaluation.

### Data Drift
Data drift refers to the phenomenon where the statistical properties of data change over time. For example, consider a model trained on historical sales data. If the consumer behavior shifts due to economic changes, the model may experience data drift, leading to decreased prediction accuracy.

### Embeddings Drift
Embeddings drift occurs when the semantic meaning of text changes over time. For instance, consider a sentiment analysis model trained on social media data. If the usage of certain slang terms evolves over time, the model may fail to accurately capture the sentiment, indicating embeddings drift.

### Statistical Tests for Drift Detection
Evidently uses various statistical tests to detect drift in data and embeddings, including:

- Kolmogorov-Smirnov test for comparing distributions
- Chi-square test for independence
- T-test for comparing means
- Mann-Whitney U test for comparing medians
- KL-divergence for measuring divergence between distributions

## Conclusion
Our model monitoring framework powered by Evidently provides a comprehensive solution for monitoring machine learning models in production environments. By leveraging advanced techniques for data and embeddings drift detection, along with data quality assessment, users can ensure the reliability and performance of their models over time.

For more information and detailed usage instructions, refer to the documentation and examples provided in the repository.