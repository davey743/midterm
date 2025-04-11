import streamlit as st
from rps import play_rps
from ttt import play_tic_tac_toe

st.title("🎮 Game Hub")

game_choice = st.selectbox("Choose a game to play:", ["Rock, Paper, Scissors", "Tic Tac Toe"])

if game_choice == "Rock, Paper, Scissors":
    play_rps()
elif game_choice == "Tic Tac Toe":
    play_tic_tac_toe()
