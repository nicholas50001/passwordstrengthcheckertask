import streamlit as st
import re


def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    common_passwords = ["password", "123456", "qwerty", "password123"]
    if password not in common_passwords:
        score += 1

    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"


st.title('Password Strength Checker')

password = st.text_input('Enter your password:', type='password')

if st.button('Check Strength'):
    if password:
        strength = check_password_strength(password)
        st.write(f'Your password strength is: **{strength}**')
    else:
        st.write('Please enter a password.')
