import streamlit as st
from final2 import amazon, flipkart

def main():
    st.title("Price Locator")

    # Input field for the product name
    product_name = st.text_input("Enter product name: ")

    if st.button("Search"):
        with st.spinner("Searching......."):
            # Fetch data from amazon and flipkart
            amazon_details = amazon(product_name)
            flipkart_details = flipkart(product_name)

        # Create two columns
        col1, col2 = st.columns(2)

        # Show Amazon details in the left column
        with col1:
            st.subheader("Amazon Details")
            for i in amazon_details:
                st.write(i)

        # Show Flipkart details in the right column
        with col2:
            st.subheader("Flipkart Details")
            for i in flipkart_details:
                st.write(i)

if __name__ == "__main__":
    main()
