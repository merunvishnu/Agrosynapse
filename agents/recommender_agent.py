def recommend(advisor_suggestion, market_trends, weather):
    if advisor_suggestion['crop'] in market_trends:
        return advisor_suggestion
    else:
        return {'crop': market_trends[0], 'method': advisor_suggestion['method']}
