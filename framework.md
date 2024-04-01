# Framework Documentation

## Introduction

Welcome to the documentation for the AI/ML Model Training Framework! This document provides a comprehensive guide for utilizing the framework effectively. The framework is designed to simplify the training and fine-tuning of AI/ML models, specifically focusing on BERT models for classification and NER (Named Entity Recognition). Additionally, it seamlessly integrates with Optuna and Ray Tune for hyperparameter optimization and MLflow for experiment tracking and artifact storage.

## Getting Started

### Installation

To begin, install the framework via pip:

```bash
pip install ai-ml-training-framework
```

### Setting Up Your Use Case

1. Create a directory for your specific use case under the `use_cases` directory.
2. Store your dataset within the created use case directory under `Datasets`.
3. Place your configuration file (`config.json`) under `Configurations` within the use case directory.

### Running the Framework

Execute the `main.py` file with the path to your configuration file as an argument:

```bash
python main.py path/to/config.json
```

## Framework Components

The framework comprises several key components:

- `BertTrainerTorch`: Class for training BERT models.
- `NERTrainer`: Class for training NER models.
- `OptunaTuner`: Class for hyperparameter optimization using Optuna.
- `RayTuner`: Class for hyperparameter optimization using Ray Tune.

## Model Training

### Training

- The `BertTrainerTorch` class trains a BERT model for classification.
- Upon training completion, the model is stored in the `TrainedModels` folder.
- If the model outperforms existing models in the `OptimumModels` folder, it is also stored there.

### Retraining

- When the performance of the optimum model on new datasets falls below a threshold, the retraining mechanism is triggered.
- The optimum model is retrained on the new dataset, or if not available, the base model (retrained BERT model) is utilized.

## Hyperparameter Tuning

### Why Hyperparameter Tuning?

Hyperparameter tuning is crucial for optimizing the performance of machine learning models. Different combinations of hyperparameters can significantly impact the model's performance, and finding the optimal set manually is time-consuming and inefficient. Automated hyperparameter tuning techniques, such as those provided by Optuna and Ray Tune, help search the hyperparameter space efficiently and find the best configuration for the model.

### How the Framework Helps with Hyperparameter Tuning

- The framework integrates with Optuna and Ray Tune for hyperparameter optimization.
- Users can specify hyperparameter search spaces and objectives in the configuration file.
- OptunaTuner and RayTuner classes facilitate hyperparameter search and store the best parameters in dedicated folders (`Optuna` and `RayTune`).

## MLflow Integration

MLflow is an open-source platform for managing the end-to-end machine learning lifecycle. It enables tracking experiments, packaging code into reproducible runs, and sharing and deploying models.

### What is MLflow?

- MLflow helps organize and track machine learning experiments.
- It provides APIs and UIs for logging parameters, metrics, and artifacts.
- MLflow supports various machine learning libraries and frameworks.

### How the Framework Utilizes MLflow

- The framework seamlessly integrates with MLflow for experiment tracking and artifact storage.
- Experiment artifacts, including trained models, hyperparameters, metrics, and logs, are stored under `outputs/mlflow/Artifacts` with a directory structure based on the use case and experiment name.

## Model Storage

### Trained Models and Optimum Models

- Trained models are stored in the `TrainedModels` folder under `outputs`.
- Optimum models, which are models that outperform existing models, are also stored in the `TrainedModels` folder.
- The directory structure for storing models follows a pattern based on the use case and experiment name.

### Optuna and Ray Tune Outputs

- Hyperparameter optimization outputs from Optuna and Ray Tune are stored in dedicated folders (`Optuna` and `RayTune`) under `outputs`.
- These folders contain information about the hyperparameter search process and the best parameters found.

## Additional Details

- The base model used for BERT is `Bert_base_uncased`.
- The framework is implemented using PyTorch.
- The `BertTrainerTorch` class is the parent class of the `OptunaTuner` and `RayTuner`.

## Framework Structure

The framework directory structure is organized as follows:

- `bin/run.sh`: Shell script to run the framework.
- `outputs`: Directory for storing all outputs, including trained models, optimum models, hyperparameter optimization outputs, and MLflow artifacts.
- `pretrained_models`: Directory for storing pretrained models.
- `src/train`: Directory containing class files for model training.
- `use_cases`: Directory for storing use case-specific datasets and configuration files.
- `utils`: Directory containing helper files, including model loaders, data loaders, and general utility functions (`helper.py`).

## Conclusion

This documentation provides a detailed overview of the AI/ML Model Training Framework, including model training, hyperparameter tuning, MLflow integration, and framework structure. By following the guidelines outlined here, users can effectively leverage the framework for developing and optimizing machine learning models. For further assistance or inquiries, please refer to the documentation or contact the framework maintainers. Happy training!