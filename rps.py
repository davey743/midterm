import pygame
import streamlit as st
from module import get_computer_choice, determine_winner

def play_rps():
    # Initialize pygame mixer for sound
    pygame.mixer.init()

    # Load sound files
    win_sound = pygame.mixer.Sound("win_sound.mp3")
    lose_sound = pygame.mixer.Sound("lose_sound.mp3")
    tie_sound = pygame.mixer.Sound("tie_sound.mp3")  
    win_sound.set_volume(0.1)
    lose_sound.set_volume(0.1)

    st.header("Rock, Paper, Scissors")

    # Initialize score tracking
    if "wins" not in st.session_state:
        st.session_state.wins = 0
        st.session_state.losses = 0
        st.session_state.ties = 0

    image_dict = {
        "rock": "rock.jpg",
        "paper": "paper.png",
        "scissors": "scissors.png",
        "lizard": "lizard.png",
        "spock": "spock.png"}

    user_choice = st.radio("Choose your move:", ["rock", "paper", "scissors", "lizard", "spock"])

    if st.button("Play"):
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        if result == "You win!":
            st.session_state.wins += 1
            win_sound.play()  
        elif result == "Computer wins!":
            st.session_state.losses += 1
            lose_sound.play()  
        else:
            st.session_state.ties += 1
            tie_sound.play()  

        st.write("You chose:")
        st.image(image_dict[user_choice], width=150)

        st.write("Computer chose:")
        st.image(image_dict[computer_choice], width=150)

        st.subheader(result)

    st.write(f"🏆 Wins: {st.session_state.wins} | ❌ Losses: {st.session_state.losses} | 🤝 Ties: {st.session_state.ties}")
