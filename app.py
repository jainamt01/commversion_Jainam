import streamlit as st

# Title of the app
st.title("Metabase Dashboard Embedding")

# Embed Metabase Dashboard
metabase_url = "https://commversion.metabaseapp.com/collection/10-client-dashboard-2-facts-v2"
st.markdown(f'<iframe src="{metabase_url}" width="800" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)
