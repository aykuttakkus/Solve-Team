# 🧬 Breast Cancer Diagnostic Profiling: Methodological Benchmarking of Neural Architectures

## 📌 Project Objective (Academic Scope)
This project is developed as a strict methodological comparison of linear and non-linear classification algorithms. Bypassing subjective "real-world scenario" narratives, the core objective is to mathematically benchmark **Logistic Regression** against varying capacities of **Multi-Layer Perceptrons (MLPs)** on the exact same isolated data foundation. 

Our focus is entirely on:
- Exploring **Multicollinearity** impacts on non-regularized deep architectures.
- Visualizing **Overfitting Gaps** and resolving them via Weight Decay and Early Stopping.
- Utilizing robust threshold-agnostic evaluation metrics (**ROC Curve, AUC, Recall/F1-Score**) to combat intrinsic Class Imbalance.

---

## 📊 Dataset Specifications
- **Name:** Breast Cancer Wisconsin (Diagnostic)
- **Dimensions:** 569 Samples | 30 Continuous Numerical Features
- **Class Distribution:** 357 Benign (63%) | 212 Malignant (37%)
- **Target:** Binary Classification (Malignant detection prioritization to minimize False Negatives).

---

## 🏗️ Evaluated Models (Curriculum Mapping)
We strictly map our models to the theoretical foundations provided in the course curriculum:

1. **Logistic Regression** (Baseline - Week 2): Demonstrating the raw power of the Sigmoid activation on linearly separable data.
2. **Plain MLP** (Week 3): 2-Hidden-Layer neural network (ReLU) demonstrating unchecked capacity.
3. **MLP + L2 Regularization** (Week 4): Implementing Weight Penalty to resolve feature redundancy.
4. **MLP + Early Stopping** (Week 4): Implementing a patience mechanism to halt memorization.

---

## 🚀 Execution Order
The workflow is distributed across 5 sequential Jupyter Notebooks, guaranteeing zero **Data Leakage** (StandardScaler is strictly fitted to the training set).

To reproduce our numerical findings and figures, execute the notebooks in this exact order:
1. `notebooks/step1_data_understanding.ipynb` (EDA, Correlation Heatmaps, Scaling)
2. `notebooks/step2_logistic_regression.ipynb` (Baseline Establishment)
3. `notebooks/step3_mlp.ipynb` (Overfitting Visualization)
4. `notebooks/step4_regularization_experiments.ipynb` (Overfitting Correction)
5. `notebooks/step5_evaluation_and_comparison.ipynb` (Final Metric Aggregation, ROC/AUC)

---

## 🏆 Summary of Technical Findings
1. **The Overfitting Paradox:** Despite its massive parameter count, the Plain MLP (Week 3) failed to generalize compared to the simple Logistic Regression. The unconstrained MLP over-relied on multicollinear features (`+0.99` correlations), causing a distinct divergence in Training vs Validation loss curves.
2. **Recall Focus:** Due to the severe medical context, dropping Accuracy as the primary metric revealed that the Plain MLP generated dangerous **False Negatives** (Recall dropped to `98.1%`).
3. **Regularization Victory:** Applying **L2 Weight Decay** (`alpha=0.1`) and **Early Stopping** successfully closed the overfitting gap, restoring the network's Recall to the absolute `98.8%` baseline limit.
4. **ROC/AUC Confirmation:** Our bonus ROC analysis established that all regularized mathematical equations produced an identical **`~0.999 AUC`**, proving that Logistic Regression was sufficiently powerful for this dataset's geometric simplicity.

---

## 📁 Repository Structure
```text
Solve-Team/
│
├── notebooks/                              # Core execution sequence
│   ├── step1_data_understanding.ipynb
│   ├── step2_logistic_regression.ipynb
│   ├── step3_mlp.ipynb
│   ├── step4_regularization_experiments.ipynb
│   └── step5_evaluation_and_comparison.ipynb
│
├── outputs/                                # Dynamically generated outputs
│   ├── figures/                            # Loss curves, ROC curves, Matrices
│   └── tables/                             # CSV metric aggregations
│
├── Slides/                                 # Markdown drafting for team presentation
│   ├── slayt_1.md (Member 1)
│   ├── slayt_2.md (Member 2)
│   ├── slayt_3.md (Member 3)
│   ├── slayt_4.md (Member 4)
│   └── slayt_5.md (Member 5)
│
├── data_utils.py                           # Seed-locked Stratified Splitter
├── requirements.txt                        # Environment dependencies
└── README.md                               # This methodological documentation
```
