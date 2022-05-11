from turtle import onclick
import streamlit as st
import pandas as pd
import numpy as np
import random

st.title('Proyecto de clasificación de tweets violentos')

df = pd.read_csv('preds.tsv', sep='\t')
#votes = pd.DataFrame(index=[0], columns=['tweet','vote'])
votes = pd.read_csv('votes.csv', sep ='\t')

current_tweet = df['text'].iloc[random.randint(0,len(df))]

def vote_violent_callback():
  votes.loc[votes.shape[0]] = [current_tweet,1]
  votes.to_csv('votes.csv',index=False,sep='\t')
  return None

def vote_non_violent_callback():
  votes.loc[votes.shape[0]] = [current_tweet,0]
  votes.to_csv('votes.csv',index=False,sep='\t')
  return None

def vote_mysoginist_callback():
  votes.loc[votes.shape[0]] = [current_tweet,2]
  votes.to_csv('votes.csv',index=False,sep='\t')
  return None




with st.container(): 
  st.subheader('Tweet de muestra')
  st.write(current_tweet)
  st.button(label='Violento',key='violent_button', on_click=vote_violent_callback)
  st.button(label='Violento y misógino',key='mysoginist_button', on_click=vote_mysoginist_callback)
  st.button(label='No violento',key='not_violence_button',on_click=vote_non_violent_callback)