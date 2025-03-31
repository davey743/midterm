import streamlit as st
from module import get_computer_choice, determine_winner

st.title("Rock, Paper, Scissors")

user_choice = st.radio("Choose your move:", ["rock", "paper", "scissors"])

if st.button("Play"):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    st.write(f"Computer chose: {computer_choice}")
    st.subheader(result)
