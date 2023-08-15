import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import folium
from streamlit_folium import folium_static
import pandas as pd
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="FAQs", page_icon="❓")

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
with st.sidebar:
        st.markdown(
                    f'<a href="https://forms.gle/RmjNdkbu2pBzpLeNA" style="display: inline-block; padding: 6px 30px; background-color: #5B9A8B; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;"><b>Join Us!</b></a>',
                    unsafe_allow_html=True
        )
        st.error('⚠️ The Babysitters Exchange is for PARENTS ONLY')

# Title
st.markdown("## FAQs")

'''
**What do I do if I want to join?**
1. Click on the [Join Us!](https://forms.gle/RmjNdkbu2pBzpLeNA)") link to fill out the Google form with your info.
2. We will be alerted when you join and activate your profile as well as send you the password for the exchange map.
3. Once you have the password go to the "Find Exchange" page and enter it. You will see a map that indicates the approximate location of all the other potential exchange partners.
4. If you see someone close by with a :green[**green**] icon (this means they are looking for exchanges) then click on the icon and you will see info on their name, number of kids, the bedtime of their kids, age range, and email address.
5. Send an email indicating that you are part of the babysitter exchange and interested in exchanging with them.
6. We recommend meeting in person with your kids beforehand so that in the event that there **is** a nightime wakeup the kids have already met the parent who will be babysitting them.

**What if I have an issue with another parent? Can you help with this?**  
This is something that you will have to handle on your own (please read the Disclaimer). As a working parent (you may be familiar) my bandwith is extremely limited. It is up to you to handle your own screening and relationships with other parents.

**What if I want to update my info after signing up?**  
Just use the same link as above. It will indicate that you have already signed up but there will be a link to edit your responses.

**What if I have enough exchange partners for the moment and don't want additional people to contact me?**  
Just change the info on your sign up form (see the question above) to indicate that you are not currently looking for an exchange. This will turn your icon on the map :red[**red**], and your info will no longer appear. 

**Where did you get the idea for this?**  
We lived in a community in Vancouver near UBC where there were a LOT of young families. At the park one day I was complaining about how there was quite a bit of friction when going out as when you walked out the door you had basically already spent $150 dollars (Uber and babysitter) and hadn't even done anything yet. They mentioned that they acutally lived just across the street from us and we started exchanging sitting for date nights.

**What if I am a single parent?**  
We appreciate that this doesn't really work for single parents since you can't go out to look after someone else's kids and leave your own unattended. We do include an option when signing up for two parent families to indicate if they are open to occasional non-reciprocal sits for single parent families. People that are open to this are indicated on the map.

**What if I need help with my kids during the day?**  
The idea is that this is for evening exchanges when watching kids generally requires no real "work". However, if you develop a relationship with another family through the exchange and want to do this, great!

**Can I join if I am a babysitter?**  
Sorry, this is for parents only.

**Can I support you/this site?**  
Sure, that would be really appreciated. Just click on the "Buy me a Coffee" below! 🙏
'''
col1, col2, col3 = st.columns(3)
with col2:
        st.markdown(
                f'<a href="https://www.buymeacoffee.com/danieljwilson" style="display: inline-block; padding: 6px 20px; background-color: #96B6C5; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">☕  Buy me a coffee</a>',
                unsafe_allow_html=True
)