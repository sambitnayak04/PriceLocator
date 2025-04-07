# pip install streamlit
import streamlit as st
from final2 import amazon,flipkart


def main():
    st.title("Price Locator")

    product_name=st.text_input("Enter product name : ")

    if st.button("Search"):
        with st.spinner("Sreaching......."):
            amazon_details=amazon(product_name)
            flipkart_details=flipkart(product_name)
        
        st.subheader("Amazon Details")
        for i in amazon_details:
            st.write(i)

        st.subheader("Flipkart Details")
        for i in flipkart_details:
            st.write(i)

if __name__=="__main__":
    main()