import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import folium
from streamlit_folium import folium_static
import pandas as pd
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Find Exchange", page_icon="🔍")

# Function to read Google Sheet
def read_google_sheet(sheet_url, creds_path):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_url(sheet_url)
    # select specific worksheet (1st sheet)
    worksheet = sheet.get_worksheet(0) # 0 refers to the first worksheet
    data = worksheet.get_all_records()
    return pd.DataFrame(data)

# Function to create map with points
def create_map(data):
    m = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()],
                   tiles='openstreetmap',
                   zoom_start=14)
    for i, row in data.iterrows():
        if row['Currently looking for exchange'] == 'Yes': # Only show popup if the value in 'Currently looking for exchange' column is 'yes'
            popup_content = f"""
            <h4>{row['First Name']}</h4>
            <p><b>Number of Kids</b>: {row['Number of Kids']}<br>
            <b>Sleep Time</b>: {row['Time kids are asleep?']}</p>
            <p><b>Email</b>: {row['Email Address']}</p>
            """
            popup = folium.Popup(popup_content, max_width=300)
        else:
            popup = None
        icon = folium.Icon(color=row['Color for Looking'], icon='home')
        folium.Marker([row['Latitude'], row['Longitude']], popup=popup, icon=icon).add_to(m)
    return m

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

# Title
#st.markdown("## <span style='color:#7C9D96'>Parents Babysitting Exchange 🔄</span>", unsafe_allow_html=True)

## Sidebar
# st.sidebar.image(image="media/exchange.png", width=50)
add_logo("media/exchange60.png", height=100)

# # Password protection
password = st.sidebar.text_input(label='Password', type="password")
st.sidebar.divider()
# Sidebar Buttons
with st.sidebar:
        st.markdown(
                    f'<a href="https://forms.gle/RmjNdkbu2pBzpLeNA" style="display: inline-block; padding: 6px 30px; background-color: #5B9A8B; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;"><b>Join Us!</b></a>',
                    unsafe_allow_html=True
        )
        st.warning('⚠️ The Babysitters Exchange is for PARENTS ONLY')
if password not in st.secrets['map_passwords']:
    st.info('Enter password in sidebar to view the map please...', icon="⚠️")
    st.stop()

# Read data from Google Sheet
sheet_url = 'https://docs.google.com/spreadsheets/d/1x23hsLL4ogyLHrRfv3liYj-g-XNdwiEv3epX6bs7Bno/edit#gid=1508967770'
creds_path = 'creds/babysit-exchange-d3319b91f667.json'
data = read_google_sheet(sheet_url, creds_path)


# Create and display the map
m = create_map(data)
folium_static(m)

# To access the Google Sheet programmatically, you'll need to create a service account and share the sheet with the service account's email address. 
# Follow these instructions to create a service account and download the credentials file: https://docs.gspread.org/en/latest/oauth2.html

# Replace 'URL_OF_YOUR_GOOGLE_SHEET' with the actual URL of your Google Sheet, and 'PATH_TO_YOUR_CREDENTIALS_JSON_FILE' with the path to your downloaded credentials JSON file. 
# Change 'YourPasswordHere' to the password you want to use.

# Note
# You'll need to ensure that the Google Sheet has the appropriate columns for latitude, longitude, and additional information.
# The password protection implemented here is not highly secure and should not be used for sensitive information. For better security, consider implementing proper authentication.

# You can run the app using the following command in your terminal:
# streamlit run app.py
# Just make sure your code is saved in a file named app.py.
