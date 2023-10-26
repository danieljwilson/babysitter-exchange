import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import folium
from streamlit_folium import folium_static
import pandas as pd
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Cibtact", page_icon="✍️")

add_logo("media/exchange60.png", height=100)

st.markdown("""
        <style>
               .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)


# Sidebar Buttons
with st.sidebar:
        st.markdown(
                    f'<a href="https://forms.gle/RmjNdkbu2pBzpLeNA" style="display: inline-block; padding: 6px 30px; background-color: #5B9A8B; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;"><b>Join Us!</b></a>',
                    unsafe_allow_html=True
        )
        st.warning('⚠️ The Babysitters Exchange is for PARENTS ONLY')

        

st.markdown('#### Contact')
'''
Questions, problems, suggestions?
'''
st.markdown('Please feel free to <a href="mailto:daniel.j.wilson+babysittingexchange@gmail.com">contact me</a>.', unsafe_allow_html=True)