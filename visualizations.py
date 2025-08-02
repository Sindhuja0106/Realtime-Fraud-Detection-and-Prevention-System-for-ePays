import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def data_plots():
    st.title("Data Visualization Dashboard")

    # Generate sample data for visualizations
    np.random.seed(42)
    n_samples = 1000
    
    # Create synthetic transaction data
    step = np.random.randint(1, 100, n_samples)
    amount = np.random.uniform(100, 100000, n_samples)
    oldbalanceOrg = np.random.uniform(0, 200000, n_samples)
    newbalanceOrig = oldbalanceOrg - amount
    oldbalanceDest = np.random.uniform(0, 200000, n_samples)
    newbalanceDest = oldbalanceDest + amount
    isFlaggedFraud = np.random.choice([0, 1], n_samples, p=[0.95, 0.05])
    
    # Create fraud labels based on rules
    fraud_labels = np.zeros(n_samples)
    for i in range(n_samples):
        fraud_score = 0
        if amount[i] > 50000:
            fraud_score += 1
        if abs(newbalanceOrig[i] - oldbalanceOrg[i]) > 40000:
            fraud_score += 1
        if oldbalanceDest[i] == 0 and newbalanceDest[i] == 0:
            fraud_score += 1
        if isFlaggedFraud[i] == 1:
            fraud_score += 1
        if fraud_score >= 2:
            fraud_labels[i] = 1
    
    # Create DataFrame
    df = pd.DataFrame({
        'step': step,
        'amount': amount,
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest,
        'newbalanceDest': newbalanceDest,
        'isFlaggedFraud': isFlaggedFraud,
        'fraud': fraud_labels
    })

    # Section 1: Data Exploration
    st.subheader("Data Exploration")

    # Dropdown to select which plot to display
    plot_selection = st.selectbox(
        'Select Plot to Display:',
        [
            'Transaction Amount Distribution',
            'Fraud vs. Flagged Fraud',
            'Percentage of Fraud by Hour',
            'KDE Plot of Amount by Class'
        ]
    )

    # Display the selected plot
    if plot_selection == 'Transaction Amount Distribution':
        fig = px.histogram(df, x='amount', nbins=50, 
                          title='Transaction Amount Distribution',
                          labels={'amount': 'Transaction Amount', 'count': 'Frequency'})
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        
    elif plot_selection == 'KDE Plot of Amount by Class':
        fig = px.histogram(df, x='amount', color='fraud', 
                          title='Transaction Amount Distribution by Fraud Class',
                          labels={'amount': 'Transaction Amount', 'count': 'Frequency'},
                          color_discrete_map={0: 'green', 1: 'red'})
        st.plotly_chart(fig, use_container_width=True)
        
    elif plot_selection == 'Fraud vs. Flagged Fraud':
        # Create pie chart
        fraud_counts = df['fraud'].value_counts()
        flagged_counts = df['isFlaggedFraud'].value_counts()
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig1 = px.pie(values=fraud_counts.values, names=['Not Fraud', 'Fraud'],
                         title='Fraud Detection Results')
            st.plotly_chart(fig1, use_container_width=True)
            
        with col2:
            fig2 = px.pie(values=flagged_counts.values, names=['Not Flagged', 'Flagged'],
                         title='System Flagged Transactions')
            st.plotly_chart(fig2, use_container_width=True)
            
    elif plot_selection == 'Percentage of Fraud by Hour':
        # Convert step to hour (assuming 24-hour cycle)
        df['hour'] = df['step'] % 24
        fraud_by_hour = df.groupby('hour')['fraud'].mean() * 100
        
        fig = px.bar(x=fraud_by_hour.index, y=fraud_by_hour.values,
                     title='Percentage of Fraud by Hour',
                     labels={'x': 'Hour of Day', 'y': 'Percentage of Fraud (%)'})
        st.plotly_chart(fig, use_container_width=True)

    # Section 2: Outliers
    st.subheader("Outliers")

    outlier_plot = st.selectbox(
        'Select Plot to Display:',
        [
            'Outliers Detection',
            'Handle outliers'
        ],
        key='outliers'
    )

    if outlier_plot == 'Outliers Detection':
        # Box plot for amount outliers
        fig = px.box(df, y='amount', title='Transaction Amount Outliers')
        st.plotly_chart(fig, use_container_width=True)
        
    elif outlier_plot == 'Handle outliers':
        # Remove outliers using IQR method
        Q1 = df['amount'].quantile(0.25)
        Q3 = df['amount'].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        df_clean = df[(df['amount'] >= lower_bound) & (df['amount'] <= upper_bound)]
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig1 = px.histogram(df, x='amount', title='Original Data (with outliers)')
            st.plotly_chart(fig1, use_container_width=True)
            
        with col2:
            fig2 = px.histogram(df_clean, x='amount', title='Cleaned Data (outliers removed)')
            st.plotly_chart(fig2, use_container_width=True)

    # Section 3: Visualization
    st.subheader("Visualization")

    viz_plot = st.selectbox(
        'Select Plot to Display:',
        [
            'Correlation Matrix',
            'Transaction Amount Distribution'
        ],
        key='visualization'
    )

    if viz_plot == 'Correlation Matrix':
        # Calculate correlation matrix
        corr_matrix = df[['step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 
                         'oldbalanceDest', 'newbalanceDest', 'isFlaggedFraud', 'fraud']].corr()
        
        fig = px.imshow(corr_matrix, 
                       title='Correlation Matrix',
                       color_continuous_scale='RdBu',
                       aspect='auto')
        st.plotly_chart(fig, use_container_width=True)
        
    elif viz_plot == 'Transaction Amount Distribution':
        # Create subplots
        fig = make_subplots(rows=2, cols=2, 
                           subplot_titles=('Amount Distribution', 'Fraud by Amount',
                                          'Balance Changes', 'Fraud vs Flagged'))
        
        # Amount distribution
        fig.add_trace(go.Histogram(x=df['amount'], name='All Transactions'), row=1, col=1)
        
        # Fraud by amount
        fraud_amounts = df[df['fraud'] == 1]['amount']
        non_fraud_amounts = df[df['fraud'] == 0]['amount']
        fig.add_trace(go.Box(y=fraud_amounts, name='Fraud', marker_color='red'), row=1, col=2)
        fig.add_trace(go.Box(y=non_fraud_amounts, name='Not Fraud', marker_color='green'), row=1, col=2)
        
        # Balance changes
        balance_change = df['oldbalanceOrg'] - df['newbalanceOrig']
        fig.add_trace(go.Histogram(x=balance_change, name='Balance Changes'), row=2, col=1)
        
        # Fraud vs Flagged
        fraud_vs_flagged = pd.crosstab(df['fraud'], df['isFlaggedFraud'])
        fig.add_trace(go.Bar(x=['Not Fraud', 'Fraud'], y=fraud_vs_flagged[0], name='Not Flagged'), row=2, col=2)
        fig.add_trace(go.Bar(x=['Not Fraud', 'Fraud'], y=fraud_vs_flagged[1], name='Flagged'), row=2, col=2)
        
        fig.update_layout(height=600, title_text="Transaction Analysis Dashboard")
        st.plotly_chart(fig, use_container_width=True)

# Entry point
if __name__ == "__main__":
    data_plots() 