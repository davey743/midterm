import streamlit as st
from ttt_logic import create_board, make_move, check_winner

def play_tic_tac_toe():
    st.header("Tic Tac Toe")

    if "board" not in st.session_state:
        st.session_state.board = create_board()
        st.session_state.current_player = "X"
        st.session_state.winner = None

    board = st.session_state.board
    current_player = st.session_state.current_player
    winner = st.session_state.winner

   
    for row in range(3):
        cols = st.columns(3)
        for col in range(3):
            cell = board[row][col]
            if cell == "":
                if cols[col].button(" ", key=f"{row}-{col}"):
                    if make_move(board, row, col, current_player):
                        result = check_winner(board)
                        if result:
                            st.session_state.winner = result
                        else:
                            st.session_state.current_player = "O" if current_player == "X" else "X"
            else:
                cols[col].markdown(f"**{cell}**")

    if winner:
        if winner == "Tie":
            st.success("It's a tie!")
        else:
            st.success(f"🎉 Player {winner} wins!")
        if st.button("Play Again"):
            st.session_state.board = create_board()
            st.session_state.current_player = "X"
            st.session_state.winner = None
