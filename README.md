# 🔍 **Clustering Analysis with K-Means and Hierarchical Clustering**  

This project demonstrates clustering techniques using **K-Means** and **Hierarchical Clustering** on synthetic data generated with three distinct clusters. It highlights the key steps in implementing, visualizing, and evaluating the performance of these clustering algorithms.

---

## 📊 **Project Overview**  

1. **Synthetic Data Generation**:  
   - Generated data points with 3 distinct clusters using `make_blobs` from scikit-learn.  

2. **Clustering Techniques**:  
   - **K-Means Clustering**:  
     - Performed clustering using 3 clusters and analyzed the results over multiple iterations.  
   - **Hierarchical Clustering**:  
     - Calculated cluster means and mapped data points to their respective cluster centers.

3. **Evaluation Metrics**:  
   - Mean Squared Error (MSE) was used to evaluate the performance of clustering methods.

---

## 🔧 **Technologies and Libraries Used**  

- **Programming Language**: Python  
- **Libraries**:  
  - `numpy` for numerical operations.  
  - `matplotlib` for data visualization.  
  - `scikit-learn` for clustering algorithms and evaluation metrics.  

---

## 🛠️ **Steps and Key Features**  

1. **Data Visualization**:  
   - Plotted initial data points to visualize the clusters.  

2. **K-Means Clustering**:  
   - Initialized with random centroids.  
   - Visualized initial clusters with centroids.  
   - Iterated to refine clusters and plotted final results.  
   - Calculated **Mean Squared Error (MSE)** for performance evaluation.

3. **Hierarchical Clustering**:  
   - Mapped data points to their respective cluster centers based on cluster means.  
   - Computed and displayed MSE for hierarchical clustering.  

---

## 📈 **Results**  

### K-Means Clustering  
- **Final Clusters**: Plotted after convergence.  
- **Centroids**: Highlighted initial and final cluster centers.  
- **Iterations**: Displayed the number of epochs for convergence.  
- **MSE**: Quantified clustering accuracy.  

### Hierarchical Clustering  
- **Cluster Means**: Computed based on labeled data.  
- **MSE**: Evaluated the error by mapping points to cluster means.

---

## 🚀 **Visual Outputs**  

- **Initial Data Points**: Scatter plot of the synthetic dataset.  
- **K-Means Initial and Final Clusters**: Visualized clusters with centroids.  
- **Hierarchical Clustering Results**: Evaluated using MSE.  

---

## 🧮 **How to Run the Project**  

1. Ensure you have Python installed along with the required libraries:  
   ```bash
   pip install numpy matplotlib scikit-learn

---
