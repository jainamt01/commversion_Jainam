import streamlit as st

# Title of the app
st.title("Metabase Dashboard Embedding")

# Embed Metabase Dashboard
metabase_url = "https://commversion.metabaseapp.com/dashboard/13-client-dashboard?text=0018d00000Mh0CHAAZ&time_based_filtering="
st.markdown(f'<iframe src="{metabase_url}" width="800" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)
