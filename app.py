import json
import pandas as pd
import streamlit as st
import requests
from get_results import *

# load json data to show initial data
response = open('./json/response.json')
data = json.load(response)
utterances = data['utterances']
# save speaker label utterances data to dataframe for ease of visualization
utterances_df = pd.DataFrame(utterances)
utterances_df['start_str'] = utterances_df['start'].apply(convertMillis)
# variable to track whether to show initial json data or data from an uploaded file
uploaded = False

## body
st.title('Speaker Diarization Demo')

uploaded_file = st.file_uploader('Upload a local file for speaker diarization.')

if uploaded_file is not None:
    polling_endpoint = upload_to_AssemblyAI(uploaded_file)
    # status of file submitted to AAI for transcription
    status = 'submitted'

    while status != 'completed':
        uploaded = True
        polling_response = requests.get(polling_endpoint, headers=headers)
        status = polling_response.json()['status']

        # display speaker label data when transcription is completed
        if status == 'completed':
            st.subheader('Turn-by-Turn Conversation Recap')
            utterances = polling_response.json()['utterances']
            utterances_df = pd.DataFrame(utterances)
            utterances_df['start_str'] = utterances_df['start'].apply(convertMillis)

            for index, row in utterances_df.iterrows():
                st.markdown(f'#### Speaker {row["speaker"]} - __{row["start_str"]}__')
                st.markdown(f'{row["text"]}')

# displays data from static json file when page first loads
if uploaded == False:
    st.video('https://youtu.be/Da3SBwlgcDc')

    st.title('Turn-by-Turn Conversation Recap')

    # display speaker label data
    for index, row in utterances_df.iterrows():
        st.markdown(f'#### Speaker {row["speaker"]} - __{row["start_str"]}__')
        st.markdown(f'{row["text"]}')
