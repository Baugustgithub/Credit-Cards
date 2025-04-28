# app.py

import streamlit as st
import pandas as pd
from cards_db import cards_data
from cheat_sheet import show_cheat_sheet
from rotating_bonus import update_rotating_bonuses
from optimizer_engine import find_best_card
import datetime

# Track last update time
if 'last_update' not in st.session_state:
    st.session_state['last_update'] = datetime.datetime.now()

st.title("Credit Card Spend Optimizer (Custom Built)")

# Sidebar
show_cheat_sheet()

st.sidebar.markdown("### Update Rotating Bonuses")
update_rotating_bonuses(cards_data)

# Reminder after 90 days
days_since_update = (datetime.datetime.now() - st.session_state['last_update']).days
if days_since_update > 90:
    st.warning("⚡ Reminder: It's been over 90 days since you updated rotating bonuses!")

# Spend Input
st.header("Enter Your Estimated Monthly Spend")

spend_categories = ['Gas', 'Groceries', 'Dining', 'Amazon', 'Travel', 'Retail', 'Bills', 'Streaming', 'Other']
spend = {}

for category in spend_categories:
    spend[category] = st.number_input(f"{category} Spend ($)", min_value=0.0, step=10.0)

# Results
st.header("Optimization Results")

results = []
cashback_per_card = {}

total_cashback = 0

for category, amount in spend.items():
    if amount > 0:
        best_card, rate = find_best_card(cards_data, category)
        cashback = amount * (rate / 100)
        total_cashback += cashback
        results.append({
            "Category": category,
            "Best Card": best_card,
            "Cashback Rate (%)": rate,
            "Expected Cashback ($)": cashback
        })
        cashback_per_card[best_card] = cashback_per_card.get(best_card, 0) + cashback

results_df = pd.DataFrame(results)
st.dataframe(results_df)

st.subheader("Total Estimated Cashback")
st.write(f"Monthly: **${total_cashback:.2f}**")
st.write(f"Yearly: **${total_cashback * 12:.2f}**")

# Cashback by Card Summary
st.subheader("Estimated Cashback by Card This Month")
cashback_card_df = pd.DataFrame([
    {"Card": card, "Cashback Earned ($)": earned}
    for card, earned in cashback_per_card.items()
])
st.dataframe(cashback_card_df)
