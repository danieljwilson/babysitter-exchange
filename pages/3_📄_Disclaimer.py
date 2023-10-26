import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import folium
from streamlit_folium import folium_static
import pandas as pd
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Disclaimer", page_icon="📄")

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
    st.warning('⚠️ The Babysitters Exchange is for PARENTS ONLY')
    st.markdown(
                f'<a href="https://forms.gle/RmjNdkbu2pBzpLeNA" style="display: inline-block; padding: 6px 30px; background-color: #5B9A8B; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;"><b>Join Us!</b></a>',
                unsafe_allow_html=True
    )
        

st.markdown('#### The Babysitter Exchange Disclaimer')
'''
Please read this disclaimer ("Disclaimer") carefully before using **The Babysitter Exchange** ("the Site"), operated by Daniel Wilson ("us," "we," or "our").

1.  **Introduction**

    The Site provides a platform that informally connects parents to exchange babysitting services ("Services"). By using the Site, you understand and agree to this Disclaimer. If you disagree with any part of this Disclaimer, please do not use the Site.

2.  **No Liability**

    a. No Endorsement or Verification: We do not endorse, certify, or verify any user of the Site, including those offering or receiving babysitting services. We encourage users to conduct their own due diligence in selecting other users with whom to engage.

    b. No Responsibility for Actions of Users: We are not responsible for any actions, conduct, or decisions made by users of the Site. Any disputes, incidents, or issues that arise between users are solely the responsibility of those users.

    c. No Guarantee of Service: We do not guarantee or warrant the quality, safety, legality, or appropriateness of any babysitting services exchanged through the Site.

3.  **Indemnification**

    You agree to indemnify, defend, and hold harmless us and our subsidiaries, affiliates, officers, directors, employees, and agents from and against any claims, liabilities, damages, losses, costs, expenses, or fees (including reasonable attorney's fees) that arise from or relate to your use or misuse of the Site, violation of this Disclaimer, or violation of any rights of a third party.

4.  **Limitation of Liability**

    In no event shall we be liable to you or any third party for any direct, indirect, special, punitive, incidental, exemplary, or consequential damages, or any loss or damages whatsoever, even if we have been previously advised of the possibility of such damages, whether in an action under contract, negligence, or any other theory arising out of or in connection with the use, inability to use, or performance of the information, services, products, and materials available from the Site.

5.  **Governing Law & Jurisdiction**

    This Disclaimer shall be governed by and construed in accordance with the laws of Quebec. Any dispute arising from this Disclaimer will be resolved in the courts of Quebec.

6.  **Changes to Disclaimer**

    We reserve the right to change this Disclaimer at any time. Any changes will be posted on this page, and it is your responsibility to review this page regularly.

7.  **Contact Information**

    For any questions regarding this Disclaimer, please contact us at daniel.j.wilson <at> gmail <dot> com.

'''