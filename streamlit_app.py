import streamlit as st
import mymodel as m

st.write("""
        #Sales Model Test
         Below are our sales predictions for this customer.
         """)

st.write(m.run(window=15))

