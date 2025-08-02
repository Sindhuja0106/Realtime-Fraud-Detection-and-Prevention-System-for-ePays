import streamlit as st
import streamlit.components.v1 as components
import front6
import visualizations
import csv_utils

# Set the page config FIRST
st.set_page_config(page_title="Online Payment Fraud Detection System", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            color: #fff;
            background-color: #1E1E2F;
        }

        .sidebar .sidebar-content {
            background-color: #2A2A3C;
        }
        .sidebar .sidebar-content div div ul li span {
            color: white;
        }
        .sidebar .sidebar-content div div ul li:hover {
            background-color: #4A4A5F;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #00BFFF;
        }
        .search-bar {
            display: flex;
            justify-content: flex-end;
            margin-bottom: 20px;
        }
        .search-bar input[type="text"] {
            width: 300px;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #00BFFF;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App title and sidebar
st.sidebar.title("FRAUD DETECTION AND PREVENTION SYSTEM FOR EPAY")
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Sidebar Navigation
if st.sidebar.button("Home"):
    st.session_state.page = 'home'
if st.sidebar.button("Overview"):
    st.session_state.page = 'overview'
if st.sidebar.button("Fraud Insights"):
    st.session_state.page = 'fraud_insights'

# Model Development Sidebar
st.sidebar.subheader("Model Development")
if st.sidebar.button("Visualization"):
    st.session_state.page = 'Visualizations'
if st.sidebar.button("Model Details"):
    st.session_state.page = 'model_details'

st.sidebar.subheader("Application")
if st.sidebar.button("About"):
    st.session_state.page = 'About'
if st.sidebar.button("Getting Started"):
    st.session_state.page = 'getting_started'
if st.sidebar.button("Bulk Upload"):
    st.session_state.page = 'bulk_upload'

# Display content based on selection

if st.session_state.page == 'home':
    st.title("FRAUD DETECTION AND PREVENTION SYSTEM FOR EPAY")
    st.subheader("About the Application")
    st.markdown(
        "This application predicts fraudulent transactions in online payment systems using advanced machine learning techniques. "
        "Designed for real-time fraud detection and prevention, it empowers financial institutions and e-commerce platforms to identify suspicious activities instantly."
    )
if st.session_state.page == 'overview':
    st.title("Overview")
    
    st.subheader("About the Application")
    st.markdown(
        "The Online Payments Fraud Detection application predicts fraudulent transactions in online payment systems using advanced machine learning techniques."
        " With the growing risk of online payment fraud, this model helps financial institutions and e-commerce platforms identify suspicious transactions in real-time."
    )
    
    st.subheader("🎯 Objective")
    st.markdown(
    "To enable **ePay** to detect and block fraudulent transactions in real-time, thereby:\n\n"
    "- ✅ Enhancing user trust and platform credibility\n"
    "- 💸 Reducing financial losses\n"
    "- 🛡️ Complying with regulatory security standards"
)

    st.subheader("Features")
    st.markdown(
        "1. **Real-Time Fraud Detection**\n"
        "    - Detects fraud during transaction processing by analyzing transaction features like amount, origin, and time.\n"
        "    - Provides immediate feedback to help prevent fraudulent activities.\n"
        "2. **Interactive Interface**\n"
        "    - Powered by Streamlit, users can easily input transaction details to get predictions.\n"
        "    - Designed for accessibility and user-friendliness, ensuring a seamless experience.\n"
        "3. **Comprehensive Feature Engineering**\n"
        "    - Implements advanced preprocessing steps to clean and optimize transaction data.\n"
    )

    st.subheader("How It Works")
    st.markdown(
    "The application leverages the **Random Forest** machine learning model to detect fraudulent transactions based on transaction attributes. Here's how it operates:\n"
    
    "### ⚙️ Key Components:\n"
    
    "- **Data Preprocessing**\n"
    "    - Cleaning and transforming transaction data for analysis, including handling missing values, scaling amounts, and encoding categorical variables.\n"
    
    "- **Exploratory Data Analysis (EDA)**\n"
    "    - Visualizing feature distributions, correlations, and class imbalances (fraud vs. legit).\n"
    
    "- **Outlier Detection & Removal**\n"
    "    - Using Z-Score and IQR methods to remove anomalies that may skew model performance.\n"
       
    "- **Modeling with Random Forest**\n"
    "    - Training the Random Forest classifier to distinguish between fraudulent and non-fraudulent transactions using labeled historical data.\n"
    
    "- **Evaluation Metrics**\n"
    "    - Measuring performance with precision, recall, F1-score, and AUC-ROC to ensure high fraud detection accuracy while minimizing false positives.\n"
       
    "- **Prediction:** The trained Random Forest model evaluates transaction details to classify them as genuine or fraudulent.\n\n"

)


    st.subheader("Key Highlights")
    st.markdown(
        "- **Machine Learning Backbone:** Powered by RandomForest, renowned for its accuracy and efficiency in handling imbalanced datasets.\n"
        "- **AUC-ROC Performance:** Achieves a score of **0.9556**, demonstrating its reliability in fraud detection.\n"
        "- **Seamless Integration:** Can be embedded into existing payment systems for real-time fraud analysis."
    )
    
elif st.session_state.page == 'fraud_insights':
    st.title("Fraud Insights")
    st.subheader("Understanding Fraud Patterns")
    st.markdown(
        "Fraudulent transactions often exhibit distinct patterns that can help identify them. By analyzing transaction data, we can uncover insights that reveal common characteristics of fraudulent activities, such as:\n"
        "\n- **Unusually High Transaction Amounts:** Fraudulent transactions often involve abnormally large amounts."
        "\n- **Time-Based Trends:** Spikes in fraudulent activities during specific hours or days."
    )

    st.subheader("Key Insights")
    st.markdown(
        "1. **Transaction Amount Analysis**\n"
        "    - Transactions exceeding the 95th percentile often indicate suspicious activity.\n"
        "    - Low-value transactions are sometimes used to test stolen card details.\n"
        "2. **Frequency of Transactions**\n"
        "    - Rapid successive transactions from the same account or card.\n"
        "    - Repeated declines followed by successful attempts.\n"
        "3. **Time-Based Transactions**\n"
        "    - Fraudsters may initiate multiple transactions within short, consistent time intervals to exploit system vulnerabilities.\n"
        "    - Fraudulent transactions may be spread out over an extended period to evade detection."
        "\n**Fraud Trends Over Time**\n"
        "- Track year-on-year analysis to see how fraud patterns evolve.\n"
        "- Adaptable models ensure the system stays ahead of emerging threats."
        "\n**Conclusion**\n"
        "- By leveraging advanced analytics and machine learning, we enhance security and reduce financial risks."
    )


elif st.session_state.page == 'Visualizations':
    visualizations.data_plots()  

elif st.session_state.page == 'model_details':
    st.title("Model Details")
    st.markdown(
        "### Random Forest Model\n"
        "- **Algorithm:** Random Forest (Ensemble of Decision Trees)\n"
        "- **Library:** Implemented using scikit-learn's `RandomForestClassifier`\n"
        "- **AUC-ROC Score:** 0.9556\n"
        "- **Features Used:**\n"
        "  - `step`: Time step of the transaction\n"
        "  - `amount`: Transaction amount\n"
        "  - `oldbalanceOrg`: Original balance in the origin account before the transaction\n"
        "  - `newbalanceOrig`: New balance in the origin account after the transaction\n"
        "  - `oldbalanceDest`: Original balance in the destination account before the transaction\n"
        "  - `newbalanceDest`: New balance in the destination account after the transaction\n"
         "  - `isFlaggedFraud`: Indicates whether the transaction was internally flagged as potentially fraudulent (1 = flagged, 0 = not flagged).\n"
        "- **Hyperparameters:**\n"
        "  - `n_estimators`: 45 (number of trees in the forest, adjustable based on performance)\n"
        "  - `max_depth`: 4 (maximum depth of each tree, prevents overfitting)\n"
        "  - `min_samples_split`: 100 (minimum samples required to split a node)\n"
        "  - `min_samples_leaf`: 30 (minimum samples required at a leaf node)\n"
        "  - `random_state`: 42 (for reproducibility)\n"
        "- **Preprocessing:**\n"
        "  - **Data Cleaning:** Removed or handled missing values and outliers in the dataset.\n"
        "  - **Feature Engineering:** Modifying or Selecting input features (Random Forest is robust to selected features).\n"
        "  - **Prediction:** The trained model analyses incoming transactions to predict whether they are fraudulent or not.\n"
        "- **Training Details:**\n"
        "  - Trained on a labeled dataset with approximately 6.36 million transactions.\n"
        "  - Used a 80-20 train-test split for model evaluation.\n"
        "  - Balanced the dataset using techniques like SMOTE or class weighting due to the imbalanced nature of fraud data (few fraud cases).\n"
        "- **Performance Metrics:**\n"
        "  - **Accuracy:** ~96% on the test set\n"
        "  - **Precision:** High for fraud detection to minimize false negatives(~49%)\n"
        "  - **Recall:** Optimized to capture most fraudulent transactions\n"
        "  - **F1-Score:** Balanced measure of precision and recall(~65%)\n"
        "- **Advantages:**\n"
        "  - Robust to overfitting due to ensemble averaging.\n"
        "  - Handles non-linear relationships and feature interactions effectively.\n"
        "  - Provides feature importance scores for interpretability.\n"
        "- **Limitations:**\n"
        "  - Computationally intensive with large datasets and many trees.\n"
        "  - Less interpretable than a single decision tree.\n"
        "- **Model File:** Saved as 'rf_model3.pkl' using joblib for deployment."
    )
    
elif st.session_state.page == 'About':    
    st.subheader("Welcome to the Online Payment Fraud Detection and Prevention App!")
    st.markdown(
        "This guide will walk you through the steps to set up and use the Online Payment Fraud Detection application effectively."
    )

    st.subheader("Prerequisites")
    st.markdown(
        "Before you begin, ensure you have the following installed on your system: Python 3.7+ as the application is built using Python,a code editor such as VS Code or PyCharm for editing the code (optional), and basic knowledge of terminal commands to execute the setup and run commands."
    )

    st.subheader("Running the Application")
    st.markdown(
        "Once the setup is complete, you can launch the application: Start the Streamlit App by running streamlit run app.py in the terminal which will start the web server and provide a URL typically http://localhost:8501, and Access the App by opening your web browser and navigating to the provided URL to interact with the app."
    )

    st.subheader("Using the Application")
    st.markdown(
        "Here's how to use the app to detect fraudulent transactions: Input Transaction Details by entering the required transaction data such as step, amount, and balances, Analyze Transactions by clicking the buttons to detect or prevent fraud based on the input, and View Results as the app will display whether the transaction is fraudulent or legitimate."
    )


elif st.session_state.page == 'getting_started':
    front6.main()
elif st.session_state.page == 'bulk_upload':
    st.title("📁 Bulk Transaction Analysis")
    st.markdown("Upload a CSV file with transaction data to analyze multiple transactions at once.")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])
    
    if uploaded_file is not None:
        csv_utils.render_bulk_check(uploaded_file)
    else:
        st.info("Please upload a CSV file with the following columns: step, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, isFlaggedFraud")
        
        # Show sample data
        st.subheader("📋 Sample Data Format")
        st.markdown("Your CSV should look like this:")
        st.code("""step,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,isFlaggedFraud
1,1500,2000,500,0,0,0
2,22000,21000,3000,5000,27000,1
3,5600,6000,400,2000,7600,0""")
        
        # Download sample files
        col1, col2 = st.columns(2)
        with col1:
            with open('sample_bulk_transactions.csv', 'r') as f:
                st.download_button(
                    label="📥 Download Sample Transactions",
                    data=f.read(),
                    file_name="sample_bulk_transactions.csv",
                    mime="text/csv"
                )
        with col2:
            with open('obvious_fraud_transactions.csv', 'r') as f:
                st.download_button(
                    label="📥 Download Fraud Sample",
                    data=f.read(),
                    file_name="obvious_fraud_transactions.csv",
                    mime="text/csv"
                ) 