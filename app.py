import streamlit as st
from agents import advisor_agent, market_agent, weather_agent, recommender_agent

st.title("🌾 AgroSynapse – AI Farming Advisor")

land_type = st.selectbox("Choose your land type:", ["Loamy", "Clay", "Sandy"])
budget = st.number_input("Enter your budget:", min_value=1000)

if st.button("Get Recommendation"):
    land_info = {"land_type": land_type}
    financial_goals = {"budget": budget}

    advice = advisor_agent.get_advice(land_info, financial_goals)
    market = market_agent.get_top_demand_crops()
    weather = weather_agent.get_forecast()
    final_recommendation = recommender_agent.recommend(advice, market, weather)

    st.success(f"Recommended Crop: {final_recommendation['crop']}")
    st.info(f"Suggested Method: {final_recommendation['method']}")
