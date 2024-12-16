import streamlit as st
import jwt
import time

# Define the Metabase URL and secret
METABASE_URL = "https://commversion.metabaseapp.com"  # Your Metabase URL
EMBEDDING_SECRET = "f82323238f85ea65a5ba48217c9b16705a97d00e7c0c1711addb418b79ae11a3"  # Your Metabase secret key (you should get this from Metabase Admin)

# Streamlit app layout
st.title("Embed Metabase Dashboard")

# Input field for dynamic account ID (you can replace this with logic to get the client account ID dynamically)
sf_account_id = st.text_input("Enter Client Account ID", value="123")  # Default to "123" for now

# Button to generate the embed URL
if st.button("Generate Embed URL"):
    # Generate the payload for the token
    payload = {
        "resource": {
            "dashboard": 13  # Replace with your actual dashboard ID
        },
        "params": {
            "sf_account_id": sf_account_id  # Pass dynamic parameter (e.g., client account ID)
        },
        "exp": time.time() + 3600  # Token expiration time in seconds (1 hour from now)
    }

    # Generate the signed token
    embed_token = jwt.encode(payload, EMBEDDING_SECRET, algorithm='HS256')

    # Construct the embed URL with the signed token
    embed_url = f"{METABASE_URL}/embed/dashboard/13?token={embed_token}"  # Replace '10' with your actual dashboard ID

    # Display the embed URL in the Streamlit app
    st.write("Embed URL Generated:")
    st.write(embed_url)

    # Embed the Metabase dashboard in an iframe within the Streamlit app
    embed_code = f'<iframe src="{embed_url}" width="1200" height="600" frameborder="0" style="border: none;"></iframe>'
    st.markdown(embed_code, unsafe_allow_html=True)
