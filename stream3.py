import streamlit as st
from final3 import amazon, flipkart

def main():
    st.title("Price Locator")

    # Input field for the product name
    product_name = st.text_input("Enter product name:")

    # Initialize amazon_details and flipkart_details
    amazon_details = None
    flipkart_details = None

    if st.button("Search"):
        with st.spinner("Searching..."):
            try:
                # Fetch data from Amazon and Flipkart
                amazon_details = amazon(product_name)
                flipkart_details = flipkart(product_name)

                if not amazon_details:
                    st.write("No Amazon results found.")
                if not flipkart_details:
                    st.write("No Flipkart results found.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

        # Create two columns for Amazon and Flipkart details
        col1, col2 = st.columns(2)

        # Display Amazon details
        with col1:
            st.subheader("Amazon Results")
            if amazon_details:
                for name, price, img_url in amazon_details:
                    st.image(img_url, width=150)
                    st.write(f"**Product**: {name}")
                    st.write(f"**Price**: ₹{price}")
            else:
                st.write("No results found for Amazon.")

        # Display Flipkart details
        with col2:
            st.subheader("Flipkart Results")
            if flipkart_details:
                for name, price, img_url in flipkart_details:
                    st.image(img_url, width=150)
                    st.write(f"**Product**: {name}")
                    st.write(f"**Price**: ₹{price}")
            else:
                st.write("No results found for Flipkart.")

if __name__ == "__main__":
    main()
