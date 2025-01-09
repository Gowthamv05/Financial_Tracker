import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to display the dashboard
def display_dashboard():
    st.title("Personal Finance Dashboard")
    st.write("Track your income, expenses, and savings goals effectively.")

    st.sidebar.header("Settings")
    currency = st.sidebar.selectbox("Select Currency", ["₹", "$", "€", "£"], index=0)

    st.header("Income and Expenses Overview")

    # Income Section
    st.subheader("Income")
    total_monthly_salary = st.number_input("Monthly Salary", min_value=0.0, format="%.2f", value=0.0)
    annual_bonus = st.number_input("Annual Bonus", min_value=0.0, format="%.2f", value=0.0)
    interest_investment = st.number_input("Interest from Investments", min_value=0.0, format="%.2f", value=0.0)
    dividend_investment = st.number_input("Dividend from Investments", min_value=0.0, format="%.2f", value=0.0)
    other_income = st.number_input("Other Income (Rent/Prof Fees)", min_value=0.0, format="%.2f", value=0.0)
    cash_in_hand = st.number_input("Cash in hand", min_value=0.0, format="%.2f", value=0.0)

    total_income_monthly = total_monthly_salary + (annual_bonus / 12) + interest_investment + dividend_investment + other_income + cash_in_hand
    total_income_annual = total_monthly_salary * 12

    st.write(f"**Gross Total Income (Monthly):** {currency}{total_income_monthly:.2f}")
    st.write(f"**Gross Total Income (Annual):** {currency}{total_income_annual:.2f}")

    # Expenses Section
    st.header("Expenses")
    st.write("Enter your monthly expenses for each category.")

    # Collapsible sections for categories
    with st.expander("Housing"):
        rent = st.number_input("Rent", min_value=0.0, format="%.2f", value=0.0)
        maintenance = st.number_input("Maintenance", min_value=0.0, format="%.2f", value=0.0)
        repairs = st.number_input("Repairs", min_value=0.0, format="%.2f", value=0.0)
        housing_expenses = rent + maintenance + repairs

    with st.expander("Utilities"):
        groceries = st.number_input("Groceries", min_value=0.0, format="%.2f", value=0.0)
        electricity = st.number_input("Electricity", min_value=0.0, format="%.2f", value=0.0)
        water = st.number_input("Water", min_value=0.0, format="%.2f", value=0.0)
        internet = st.number_input("Internet", min_value=0.0, format="%.2f", value=0.0)
        utilities_expenses = electricity + water + internet + groceries

    with st.expander("Medical"):
        medical_expenses = st.number_input("Medical Expenses", min_value=0.0, format="%.2f", value=0.0)

    with st.expander("Education"):
        education_expenses = st.number_input("Education Expenses", min_value=0.0, format="%.2f", value=0.0)

    with st.expander("Entertainment"):
        entertainment = st.number_input("Entertainment", min_value=0.0, format="%.2f", value=0.0)

    total_expenses = housing_expenses + utilities_expenses + medical_expenses + education_expenses + entertainment
    st.write(f"**Total Monthly Expenses:** {currency}{total_expenses:.2f}")

    # Investments Section
    st.header("Investments")
    st.subheader("MF SIP")
    mf_sip = st.number_input("Monthly MF SIP", min_value=0.0, format="%.2f", value=0.0)
    life_insurance = st.number_input("Life Insurance Premium", min_value=0.0, format="%.2f", value=0.0)
    equity_stocks = st.number_input("Equity / Stocks Investments", min_value=0.0, format="%.2f", value=0.0)
    crypto_investment = st.number_input("Crypto Investment", min_value=0.0, format="%.2f", value=0.0)
    investments_monthly = mf_sip + life_insurance + equity_stocks + crypto_investment
    st.write(f"**Total Monthly Investments:** {currency}{investments_monthly:.2f}")

    # Loan Repayments Section
    st.header("Loan Repayments")
    loan_home = st.number_input("Home Loan Payment", min_value=0.0, format="%.2f", value=0.0)
    loan_personal = st.number_input("Personal Loan Payment", min_value=0.0, format="%.2f", value=0.0)
    loan_property = st.number_input("Property Loan Payment", min_value=0.0, format="%.2f", value=0.0)
    loan_car = st.number_input("Car Loan Payment", min_value=0.0, format="%.2f", value=0.0)
    loan_any_other = st.number_input("Any Other Loan Payment", min_value=0.0, format="%.2f", value=0.0)
    total_loan_repayment = loan_home + loan_personal + loan_property + loan_car + loan_any_other
    st.write(f"**Total Monthly Loan Repayments:** {currency}{total_loan_repayment:.2f}")

    # Savings Section
    st.header("Savings Goals")
    savings_goal = st.number_input("Set Your Savings Goal", min_value=0.0, format="%.2f", value=0.0)
    savings = total_income_monthly - total_expenses - investments_monthly - total_loan_repayment

    if savings < 0:
        st.write("**Your expenses are greater than your income. Please try to increase your income or reduce your expenses.**")
        progress = 0  # No progress when savings are negative
    else:
        st.write(f"**Monthly Savings:** {currency}{savings:.2f}")
        progress = (savings / savings_goal) * 100 if savings_goal > 0 else 0

    st.progress(min(progress / 100, 1.0))
    if savings >= 0:
        st.write(f"Progress towards goal: {progress:.2f}%")

    # Financial Tips Section
    st.header("Financial Tips")
    if total_expenses > total_income_monthly:
        st.warning("Your monthly expenses exceed your income. Consider reducing discretionary spending like entertainment or dining out.")
    elif savings < savings_goal:
        st.info("You are below your savings goal. Try allocating a portion of your bonus or cutting down on non-essential expenses.")

    if investments_monthly < 0.2 * total_income_monthly:
        st.info("Consider increasing your investment allocation to at least 20% of your income for better long-term returns.")

    if total_loan_repayment > 0.4 * total_income_monthly:
        st.warning("Loan repayments are taking a significant portion of your income. Focus on paying off high-interest loans first.")

    if cash_in_hand > 0.2 * total_income_monthly:
        st.success("You have a healthy cash reserve. Consider moving excess cash into investments or savings for higher returns.")

    # Visualization
    st.header("Expense Breakdown")

    labels = [
        "Housing", "Utilities", "Medical", "Education", 
        "Entertainment", "Loan Repayments", "Investments", 
        "Savings", "Cash in Hand"
    ]

    values = [
        max(0, housing_expenses), max(0, utilities_expenses), 
        max(0, medical_expenses), max(0, education_expenses), 
        max(0, entertainment), max(0, total_loan_repayment), 
        max(0, investments_monthly), max(0, savings), 
        max(0, cash_in_hand)
    ]

    if sum(values) == 0:
        st.write("No data available for the chart. Enter values to see the breakdown.")
    else:
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

    # Export Data
    if st.button("Export Summary"):
        data = {
            "Category": labels,
            "Amount": values
        }
        df = pd.DataFrame(data)
        st.download_button(
            label="Download as CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="finance_summary.csv",
            mime="text/csv"
        )

# Run the app
if __name__ == "__main__":
    display_dashboard()
