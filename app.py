import streamlit as st,time
from math import log
from joblib import load
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# MAIN PAGE
# heading
st.set_page_config(layout="wide")
colT1,colT2 = st.columns([3,8])
with colT2:
    st.title('Predicting Spotify Popularity')
# display of popularity meter and number
colT1,colT2 = st.columns([6,8])
with colT2:
    with st.spinner('Wait for it...'):
        time.sleep(2)
    popularity_number = st.text("")
st.text('')
st.markdown('###### Use the options below to predict the popularity of any song on Spotify.')
st.text('')

with st.container():

    col1, col2,col3,col4,col5= st.columns((2,0.5,1,1,0.75))
    with col1:
# widgets for user to select values for features
        danceability = st.slider('Danceability', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        energy = st.slider('Energy', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        speechiness = st.slider('Speechiness', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        valence = st.slider('Valence', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        loudness = st.slider('Loudness', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        acousticness=st.slider('Acousticness', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    with col2:
        st.text('')
        st.text('')


    with col3:
        st.markdown('###### Looking for Explicit Songs?')
        st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        explicit_label = st.radio('explicit', ('Yes', 'No'),index=1)
        explicit = 1 if explicit_label == 'Yes' else 0
    with col4:    
        
        st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        dance_electronic_label = st.radio('Dance-Electro', ('Yes', 'No'),index=1)
        dance_electronic = 1 if dance_electronic_label == 'Yes' else 0

        st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        hip_hop_label = st.radio('HipHop', ('Yes', 'No'),index=1)
        hip_hop = 1 if hip_hop_label == 'Yes' else 0
   
        st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        metal_label = st.radio('Metal', ('Yes', 'No'),index=1)
        metal = 1 if hip_hop_label == 'Yes' else 0
     
    
    with col5:
        st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        rock_label = st.radio('Rock', ('Yes', 'No'),index=1)
        rock = 1 if rock_label == 'Yes' else 0

        st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        r_b_label = st.radio('R&B', ('Yes', 'No'),index=1)
        r_b = 1 if r_b_label == 'Yes' else 0

       
# predict popularity
model = load('Machine_Learning_Models/final_model.pkl')
features = np.array([explicit,rock,danceability,loudness,acousticness,energy,metal,hip_hop,dance_electronic,speechiness,r_b,valence])
popularity = model.predict(features.reshape(1, -1))
popularity_number.subheader(f'{ "Your Song is Popular" if int(popularity[0])==1 else "Sorry Not Popular" }')


