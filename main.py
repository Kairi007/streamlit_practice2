
import streamlit as st
import time
from PIL import Image


st.title("streamlit超入門")

st.write('プログレスバーの表示')

interaption =st.empty()
bar =st.progress(0)

for i in range(100):
    interaption.text(f'Iteration{i+1}')
    bar.progress(i +1)
    time.sleep(0.1)


expander =st.expander('FAQ')
expander.write('ANSWER')

