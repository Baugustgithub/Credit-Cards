# cheat_sheet.py

import streamlit as st

def show_cheat_sheet():
    with st.sidebar.expander("When to Use Each Card (Cheat Sheet)", expanded=True):
        st.markdown("""
        ### Core Strategy:
        - **Gas**: Ducks Unlimited (5%), US Bank Cash+ (5% if selected)
        - **Groceries**: Bread AAA (5%), Blue Cash Everyday (3%)
        - **Dining**: Altitude Go (4%), Citi Custom Cash (5%), Freedom Flex (3%)
        - **Streaming**: Cash+, Altitude Go, Barclays View
        - **Online Retail**: Blue Cash Everyday (3%)
        - **Travel**: Wells Fargo Autograph (3%)
        - **Bills, Cell Phone, Utilities**: Elan Max Cash (5% if selected), Barclays View
        - **Amazon**: Chase Prime Visa (5%)
        - **General Spend**: Citi Double Cash (2%), FNBO Evergreen (2%)
        """)