import streamlit as st
from module import get_computer_choice, determine_winner

st.title("Rock, Paper, Scissors")

# Initialize score tracking 
if "wins" not in st.session_state:
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.ties = 0


user_choice = st.radio("Choose your move:", ["rock", "paper", "scissors"])

if st.button("Play"):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    # Score updater
    if result == "You win!":
        st.session_state.wins += 1
    elif result == "Computer wins!":
        st.session_state.losses += 1
    else:
        st.session_state.ties += 1



    # Results
    st.write(f"Computer chose: {computer_choice}")
    st.subheader(result)

# Display score
st.write(f"🏆 Wins: {st.session_state.wins} | ❌ Losses: {st.session_state.losses} | 🤝 Ties: {st.session_state.ties}")

