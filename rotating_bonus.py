# rotating_bonus.py

import streamlit as st

def update_rotating_bonuses(cards):
    st.header("Update Rotating Bonuses (Quarterly)")

    for card in cards:
        if "freedom" in card["name"].lower() or "discover" in card["name"].lower() or "nusenda" in card["name"].lower():
            bonuses = st.text_input(f"Rotating categories for {card['name']} (separate by commas)", key=card["name"])
            if bonuses:
                card["rotating_bonuses"] = [b.strip().lower() for b in bonuses.split(",")]