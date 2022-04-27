import streamlit as st
import pandas as pd
import random

st.title('Proyecto de clasificación de tweets violentos')


df = pd.read_csv('preds.tsv', sep='\t')


with st.container():
    st.subheader('Tweet de muestra',)
    st.write(df['text'].iloc[random.randint(0,len(df))])
    st.button(label='Violento')
    st.button(label='Violento y misógino')
    st.button(label='No violento')


#matrix = pd.merge(pd.DataFrame(df['label'].value_counts()),
  #  pd.DataFrame(df['predicted_label'].value_counts()),
  #  right_index=True,left_index=True) 




