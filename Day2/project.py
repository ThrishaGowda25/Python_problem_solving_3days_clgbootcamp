import streamlit as st
st.title("password validation and encryption")
password=st.text_input("enter the password",type="password")
if st.button("Validate and Encrypt"):
    if password=="":
        st.warning("Please enter the password")
    elif len(password)<=8:
        st.error("password must be atleast 8")
    elif password[4] not in "12345":
        st.error("The fifth character must be in the range 1-5")
    elif not password.isalnum():
        st.error("must contain alphabet and numeric")
    else:
        has_upper=any(ch.isupper() for ch in password)
        has_lower=any(ch.islower() for ch in password)
        if not (has_upper and has_lower):
            st.error("Must contain 1 upper and 1 lower")
        else:
            encrypted_password=password.replace("A","@")
            encrypted_password=password.replace("a","B")
            encrypted_password=password.replace("b","1")
            
            st.success("thank for entering valid password")
            st.write("the encrypted password is")
            st.code(encrypted_password)