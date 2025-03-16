import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")
st.markdown(
    """
    <style>
        .stApp {
            background-color: #ADD8E6; 
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='color:blue;'>🔒 Password Strength Checker</h1>", unsafe_allow_html=True)
st.markdown("""
 ## Welcome to the ultimate password strength checker!🙋‍♀️
Check the strength of your password with our Tool! Get instant feedback and suggestions to create a **secure** and **unique password**.""") 

password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password: 
    if len(password) >= 8:
        score += 1
    else : 
        feedback.append("❌Password should be atleast 8 characters long.")
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]' , password):
        score += 1   
    else:
        feedback.append("❌Password should contain both upper and lower case.")

    if re.search(r'\d', password):
        score += 1
    else :
        feedback.append("❌Password should contain atleast one digit.")
    if re.search(r'[!@#$%&*]' , password):
        score += 1
    else: 
        feedback.append("❌Password should contain at least one special character(!@#$%&*).")
    if score == 4:
        feedback.append("✅ Strong!👍")     
    elif score == 3:
        feedback.append("🟡 Medium!")
    else:
        feedback.append("🔴 Weak!")    

    if feedback:
        st.markdown("## Improvements Suggested")    
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please Enter Your Password To Get Started.")            
