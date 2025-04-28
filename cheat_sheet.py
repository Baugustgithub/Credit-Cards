# cheat_sheet.py

import streamlit as st

def show_cheat_sheet():
    with st.sidebar.expander("When to Use Each Card (Cheat Sheet)", expanded=True):
        st.markdown("""
        - **Gas**: Ducks Unlimited (5%), Cash+ (5% if selected)
        - **Groceries**: Bread AAA (5%), Blue Cash Everyday (3%)
        - **Dining**: Altitude Go (4%), Freedom Flex (3%), Barclays View (3%)
        - **Streaming**: US Bank Cash+ (5%), Altitude Go (2%)
        - **Travel**: Wells Fargo Autograph (3%)
        - **General Spending**: Citi Double Cash (2%), FNBO Evergreen (2%)
        - **Amazon**: Chase Prime Visa (5%)
        - **Other**: Use fallback 2% cards
        """)
