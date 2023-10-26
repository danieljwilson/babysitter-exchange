import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import folium
from streamlit_folium import folium_static
import pandas as pd
from streamlit_extras.app_logo import add_logo
from streamlit_extras.buy_me_a_coffee import button


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

add_logo("media/exchange60.png", height=100)

# Sidebar Buttons
# Add custom CSS styles

with st.sidebar:
        st.markdown(
                    f'<a href="https://forms.gle/RmjNdkbu2pBzpLeNA" style="display: inline-block; padding: 6px 30px; background-color: #5B9A8B; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;"><b>Join Us!</b></a>',
                    unsafe_allow_html=True
        )
        st.warning('⚠️ The Babysitters Exchange is for PARENTS ONLY')

# Title
# st.markdown('## Parents Babysitter Exchange')

# Add text
#st.divider()
'''
#### 👨‍👨‍👦‍👦 The Parents Babysitting Exchange 
**An informal group of Montreal parents with the goal of helping one another go on (more) affordable evening outings (sans kids).**
'''
# st.divider()
col1, col2, col3 = st.columns(3)
with col2:
        st.markdown(
                        f'<a href="https://forms.gle/RmjNdkbu2pBzpLeNA" style="display: inline-block; padding: 6px 30px; background-color: #5B9A8B; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;"><b>Join Us!</b></a>',
                        unsafe_allow_html=True
                )
st.divider()
st.info('Once signed up go to 🔍 Find Echange Partner to locate an exchange', icon="👈")

'''
##### How it Works
The idea of the **Babysitter Exchange** is to have a nearby parent come over AFTER YOUR KIDS HAVE GONE TO SLEEP to be around in case anything happens, and in the meantime they can do some work or reading or internetting, etc. Then on another evening you or your partner will do the same for them.

Once you sign up you will be given a password to access the map of other neighborhood parents interested in exchanging.
'''
st.markdown('**For more info see our <a href="/FAQs" target="_self">FAQ page</a>**', unsafe_allow_html=True)

st.warning('This has just been launched so if you are not finding a good fit now, please check back soon. Also if the map is temporarily not working please check back the next day!')
st.divider()

st.image('media/art_d_pic.jpg', caption="Our little gang", width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

# col1, col2, col3 = st.columns(3)
# with col2:
#         st.markdown('##### Support the site! 👇')
#         st.markdown(
#                     f'<a href="https://www.buymeacoffee.com/danieljwilson" style="display: inline-block; padding: 6px 20px; background-color: #96B6C5; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">☕  Buy me a coffee</a>',
#                     unsafe_allow_html=True
#         )
