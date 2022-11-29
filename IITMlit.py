import streamlit as st

st.title('IITM Graded Assignment')

choice1 = st.number_input('Enter First number')
choice2 = st.number_input('Enter Second number')
choice3 = st.number_input('Enter Third number')

string = f'Maximum value is {max(choice1,choice2,choice3)}'

st.write(string)
