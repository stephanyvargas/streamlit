
import streamlit as st

import numpy as np
import pandas as pd

@st.cache
def get_area_chart data():
    print('get_area_chart called')
    return pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c']
        )

def run():

    with st.echo():
        chart_data = get_area_chart data()

        st.area_chart(chart_data)
