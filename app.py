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

# Grouped Categories
st.subheader("🛒 Shopping / Retail")
amazon_spend = st.number_input("Amazon Spend ($)", min_value=0.0, step=10.0)
retail_spend = st.number_input("Retail Spend ($)", min_value=0.0, step=10.0)
online_retail_spend = st.number_input("Online Retail Spend ($)", min_value=0.0, step=10.0)
electronic_store_spend = st.number_input("Electronic Store Spend ($)", min_value=0.0, step=10.0)

st.subheader("🍽️ Food and Dining")
groceries_spend = st.number_input("Groceries Spend ($)", min_value=0.0, step=10.0)
dining_spend = st.number_input("Dining Spend ($)", min_value=0.0, step=10.0)

st.subheader("✈️ Transportation and Travel")
gas_spend = st.number_input("Gas Spend ($)", min_value=0.0, step=10.0)
travel_spend = st.number_input("Travel Spend ($)", min_value=0.0, step=10.0)
fitness_spend = st.number_input("Fitness Clubs Spend ($)", min_value=0.0, step=10.0)

st.subheader("⚡ Bills and Services")
bills_spend = st.number_input("Bills Spend ($)", min_value=0.0, step=10.0)
streaming_spend = st.number_input("Streaming Spend ($)", min_value=0.0, step=10.0)
cell_phone_spend = st.number_input("Cell Phone Spend ($)", min_value=0.0, step=10.0)
utilities_spend = st.number_input("Utilities Spend ($)", min_value=0.0, step=10.0)

st.subheader("🔮 Other")
other_spend = st.number_input("Other Spend ($)", min_value=0.0, step=10.0)

# Spend dictionary
spend = {
    "amazon": amazon_spend,
    "retail": retail_spend,
    "online retail": online_retail_spend,
    "electronic store": electronic_store_spend,
    "groceries": groceries_spend,
    "dining": dining_spend,
    "gas": gas_spend,
    "travel": travel_spend,
    "fitness clubs": fitness_spend,
    "bills": bills_spend,
    "streaming": streaming_spend,
    "cell phone": cell_phone_spend,
    "utilities": utilities_spend,
    "other": other_spend
}

# Which categories require Wallet Cards
wallet_required_categories = {"gas", "groceries", "dining", "travel", "retail"}

# Results
st.header("Optimization Results")

results = []
cashback_per_card = {}
wallet_cards_used = set()
drawer_cards_used = set()
total_cashback = 0

for category, amount in spend.items():
    if amount > 0:
        prefer_wallet = category in wallet_required_categories
        existing_cards = wallet_cards_used.union(drawer_cards_used)

        best_card, rate = find_best_card(
            cards=cards_data,
            category=category,
            prefer_wallet_cards=prefer_wallet,
            minimize_switching=True,
            existing_wallet_cards=existing_cards
        )

        if best_card:
            # Track cards used
            for card in cards_data:
                if card['name'] == best_card:
                    if card.get('wallet_card', False):
                        wallet_cards_used.add(best_card)
                    else:
                        drawer_cards_used.add(best_card)

            cashback = amount * (rate / 100)
            total_cashback += cashback

            results.append({
                "Category": category.capitalize(),
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

# Wallet vs Drawer card display
st.subheader("Cards You Need to Carry")
st.write(", ".join(sorted(wallet_cards_used)))

st.subheader("Cards You Can Leave at Home (Drawer Cards)")
st.write(", ".join(sorted(drawer_cards_used)))