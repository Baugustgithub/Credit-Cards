# rotating_bonus.py

import streamlit as st

def update_rotating_bonuses(cards):
    st.header("Update Rotating Bonuses (Quarterly)")

    # Common popular rotating categories
    common_categories = [
        "Gas Stations", "Grocery Stores", "Restaurants", "Amazon",
        "PayPal", "Digital Wallets", "Streaming Services", "Drugstores",
        "Home Improvement Stores", "Department Stores", "Transit",
        "Select Travel", "Movie Theaters", "Entertainment", "Wholesale Clubs"
    ]

    for card in cards:
        if "freedom" in card["name"].lower() or "discover" in card["name"].lower() or "nusenda" in card["name"].lower():
            st.subheader(f"Rotating categories for {card['name']}")

            selected_common = st.multiselect(
                f"Select common rotating categories for {card['name']}",
                common_categories,
                key=f"common_{card['name']}"
            )

            custom_input = st.text_input(
                f"Enter any additional custom categories for {card['name']} (comma-separated)",
                key=f"custom_{card['name']}"
            )

            # Combine selections
            rotating = [s.lower() for s in selected_common]

            if custom_input:
                custom_list = [c.strip().lower() for c in custom_input.split(",") if c.strip()]
                rotating.extend(custom_list)

            card["rotating_bonuses"] = rotating