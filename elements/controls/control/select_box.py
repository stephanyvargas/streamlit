
import streamlit as st

import numpy as np
import pandas as pd

def title():
    return 'Select box, multi select'

@st.cache
def get_data():
    print('get_data select box called')
    return pd.DataFrame({
          'first column': list(range(1, 11)),
          'second column': np.arange(10, 101, 10)
        })

def run():

    with st.echo():
        df = get_data()

        option = st.selectbox('Select a line to filter', df['first column'])

        filtered_df = df[df['first column'] == option]

        st.write(filtered_df)