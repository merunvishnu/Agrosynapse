def get_advice(land_info, financial_goals):
    if land_info['land_type'] == 'Loamy' and financial_goals['budget'] > 5000:
        return {'crop': 'Wheat', 'method': 'Drip Irrigation'}
    else:
        return {'crop': 'Millet', 'method': 'Sprinkler Irrigation'}
