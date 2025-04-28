# optimizer_engine.py

def find_best_card(cards, category, prefer_wallet_cards=True, minimize_switching=True, existing_wallet_cards=set()):
    best_card = None
    best_rate = 0.0

    for card in cards:
        rate = card['base_rate']
        card_name = card['name']

        # Check rotating bonuses first
        if category.lower() in card.get('rotating_bonuses', []):
            rate = 5.0
        # Check static bonuses
        elif category.lower() in card.get('static_bonuses', {}):
            rate = card['static_bonuses'][category.lower()]

        # Skip Drawer cards if category must be wallet (gas, groceries, dining, travel, retail)
        if prefer_wallet_cards and not card.get('wallet_card', False):
            continue

        # Prefer reusing an existing card within 1% margin
        if minimize_switching and best_card in existing_wallet_cards:
            if rate >= (best_rate - 1.0):
                best_card = card_name
                best_rate = rate
        else:
            if rate > best_rate:
                best_card = card_name
                best_rate = rate

    return best_card, best_rate