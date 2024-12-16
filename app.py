import streamlit as st

# Title of the app
st.title("Metabase Dashboard Embedding")

# Embed Metabase Dashboard
metabase_url = "https://commversion.metabaseapp.com/public/dashboard/b0ae71a8-1beb-4d14-87df-eab23e66b76f"
st.markdown(f'<iframe src="{metabase_url}" width="800" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)
