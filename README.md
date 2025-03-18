# Customer Segmentation Using K-Means Clustering

## 📌 Project Overview
This project applies **K-Means Clustering** to segment customers based on their purchasing behavior. It involves:
- Data Cleaning and Preprocessing
- Applying K-Means Clustering Algorithm
- Visualizing Customer Segments

## 🛠 Technologies Used
- **Python** (pandas, seaborn, matplotlib, sklearn, numpy)
- **Jupyter Notebook / GitHub Codespaces**

## 📂 Dataset
We use a **Customer Purchase Dataset**:
- **Columns include**: CustomerID, Age, Gender, Annual Income, Spending Score
- **Goal**: Identify distinct customer groups for better marketing strategies.

## 🔧 Installation & Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/Customer-Segmentation.git
   cd Customer-Segmentation
   ```
2. **Install Required Libraries:**
   ```bash
   pip install pandas numpy seaborn matplotlib scikit-learn
   ```
3. **Run the Script:**
   ```bash
   python Customer_Segmentation.py
   ```

## 📊 Data Analysis & Clustering
### 1️⃣ Data Preprocessing
- Handle missing values
- Standardize numerical features

### 2️⃣ K-Means Clustering
- Determine the optimal number of clusters using the **Elbow Method**
  ```python
  from sklearn.cluster import KMeans
  wcss = []
  for i in range(1, 11):
      kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
      kmeans.fit(df)
      wcss.append(kmeans.inertia_)
  ```

- Fit the K-Means model
  ```python
  kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
  df['Cluster'] = kmeans.fit_predict(df[['Annual Income', 'Spending Score']])
  ```

### 3️⃣ Data Visualization
- **Customer Segments:**
  ```python
  sns.scatterplot(x=df['Annual Income'], y=df['Spending Score'], hue=df['Cluster'], palette='viridis')
  ```

## ✅ Results & Insights
- **Customers were grouped** into 3 distinct segments based on spending behavior.
- **High spenders** and **low spenders** were identified for targeted marketing.
- **Future improvements** can involve hierarchical clustering or deep learning.

## 📜 License
This project is open-source and free to use.

## 📬 Contact
For queries, contact **your-email@example.com** or visit **your GitHub profile**.

