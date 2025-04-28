# optimizer_engine.py

def find_best_card(cards, category):
    best_card = None
    best_rate = 0.0

    for card in cards:
        rate = card['base_rate']
        # Check rotating bonuses first
        if category.lower() in card.get('rotating_bonuses', []):
            rate = 5.0
        # Check static bonuses next
        elif category.lower() in card.get('static_bonuses', {}):
            rate = card['static_bonuses'][category.lower()]
        
        if rate > best_rate:
            best_card = card['name']
            best_rate = rate

    return best_card, best_rate