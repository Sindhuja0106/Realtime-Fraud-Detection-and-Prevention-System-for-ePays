import streamlit as st
import pandas as pd
import joblib
import altair as alt

# Load trained model
rf_model = joblib.load('rf_model3.pkl')

# Feature list
features = ['step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'isFlaggedFraud']

# Detect fraud and determine where (origin/destination)
def detect_fraud(transaction):
    step, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, isFlaggedFraud = transaction
    reasons = []
    issues = {'origin': False, 'destination': False}

    if oldbalanceDest == 0 and newbalanceDest == 0:
        reasons.append("Destination balance anomaly")
        issues['destination'] = True
    if round(newbalanceOrig, 2) != round(oldbalanceOrg - amount, 2):
        reasons.append("Origin balance mismatch")
        issues['origin'] = True
    if oldbalanceDest != 0 and round(newbalanceDest, 2) != round(oldbalanceDest + amount, 2):
        reasons.append("Destination balance mismatch")
        issues['destination'] = True

    if reasons:
        return 1, "; ".join(reasons), issues

    transaction_df = pd.DataFrame([transaction], columns=features)
    prediction = int(rf_model.predict(transaction_df)[0])
    return prediction, "ML model prediction: Fraud" if prediction == 1 else "ML model prediction: Not Fraud", issues

# Prevention logic
def prevent_fraud(transaction):
    step, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, isFlaggedFraud = transaction
    actions = []

    if isFlaggedFraud == 1:
        actions.append("⚠️ WARNING: Transaction is flagged as fraud and may not be safe.")
    if amount > 50000:
        actions.append("🚨 High transaction amount")
    if oldbalanceOrg < amount:
        actions.append("🚨 Insufficient origin balance")
    if oldbalanceDest == 0 and newbalanceDest == 0:
        actions.append("🚨 Destination balance anomaly")

    ml_result, _, _ = detect_fraud(transaction)
    if ml_result == 1:
        actions.append("🚨 detected fraud")

    return "✅ ALLOWED" if not actions else " | ".join(actions)

# Main Streamlit UI
def main():
    st.title("🛡️ Fraud Detection and Prevention System")

    if "show_results" not in st.session_state:
        st.session_state.show_results = False
    if "transactions" not in st.session_state:
        st.session_state.transactions = []

    if not st.session_state.show_results:
        n = st.number_input('🔢 Number of transactions to check:', min_value=1, step=1)
        transactions = []

        for i in range(n):
            st.markdown(f"---\n### Transaction {i+1}")
            step = st.number_input('Step (Time Step)', min_value=0, key=f'step_{i}')
            amount = st.number_input('Transaction Amount', min_value=0.0, key=f'amount_{i}')
            oldbalanceOrg = st.number_input('Old Balance (Origin)', min_value=0.0, key=f'oldbalanceOrg_{i}')
            newbalanceOrig = st.number_input('New Balance (Origin)', min_value=0.0, key=f'newbalanceOrig_{i}')
            oldbalanceDest = st.number_input('Old Balance (Destination)', min_value=0.0, key=f'oldbalanceDest_{i}')
            newbalanceDest = st.number_input('New Balance (Destination)', min_value=0.0, key=f'newbalanceDest_{i}')
            isFlaggedFraud = st.selectbox('Is Transaction Flagged as Fraud?', [0, 1], key=f'isFlaggedFraud_{i}')

            transaction = [step, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, isFlaggedFraud]
            transactions.append(transaction)

        if st.button("🚨 Detect Fraud and View Results"):
            st.session_state.transactions = transactions
            st.session_state.show_results = True

    else:
        st.markdown("## 🔎 Fraud Detection Results")

        df = pd.DataFrame(st.session_state.transactions, columns=features)

        fraud_results = df[features].apply(lambda row: detect_fraud(row.tolist()), axis=1)
        df['FraudDetected'] = fraud_results.apply(lambda x: x[0])
        df['FraudReason'] = fraud_results.apply(lambda x: x[1])
        df['FraudIssue'] = fraud_results.apply(lambda x: x[2])
        df['PreventionAction'] = df[features].apply(lambda row: prevent_fraud(row.tolist()), axis=1)

        for idx, row in df.iterrows():
            issues = row['FraudIssue']
            st.markdown(f"---\n### 📄 Transaction {idx + 1}")
            st.write(f"**Step:** {row['step']}")
            st.write(f"**Amount:** {row['amount']}")
            st.write(f"**Origin Balance:** {row['oldbalanceOrg']} → {row['newbalanceOrig']}")
            st.write(f"**Destination Balance:** {row['oldbalanceDest']} → {row['newbalanceDest']}")
            st.write(f"**Flagged by System:** {'✅ Yes' if row['isFlaggedFraud'] == 1 else '❌ No'}")
            
            if row['FraudDetected'] == 1:
                st.error(f"**Fraud Status:** ❌ FRAUD")
            else:
                st.success(f"**Fraud Status:** ✅ Not Fraud")
            
            st.write(f"**Reason:** {row['FraudReason']}")
            st.warning(f"**Prevention Advice:** {row['PreventionAction']}")

        # Visualization
        st.markdown("### 📊 Visualize Fraud Detection")
        df["FlaggedStr"] = df["isFlaggedFraud"].map({0: "Not Flagged", 1: "Flagged"})

        chart = alt.Chart(df).mark_point(size=100).encode(
            x=alt.X('step:Q', title='Step'),
            y=alt.Y('amount:Q', title='Amount'),
            color=alt.Color('FraudDetected:N', scale=alt.Scale(domain=[0, 1], range=['green', 'red']),
                            legend=alt.Legend(title='Fraud Detected')),
            shape=alt.Shape('FlaggedStr:N', scale=alt.Scale(domain=['Not Flagged', 'Flagged'],
                            range=['circle', 'triangle']), legend=alt.Legend(title='User Flagged')),
            tooltip=['step', 'amount', 'FraudDetected', 'FlaggedStr']
        ).properties(
            width=700, height=400,
            title="Fraud Detection (ML Prediction & Flag Status)"
        )

        st.altair_chart(chart, use_container_width=True)

        if st.button("🔄 Check New Transactions"):
            st.session_state.show_results = False
            st.rerun()

if __name__ == "__main__":
    main() 