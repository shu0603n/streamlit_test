import streamlit as st
import numpy as np
import pandas as pd

st.title('テストタイトル_修正済み')

st.write('文字をかけるよ')

df = pd.DataFrame({
	'1列': [1 ,2 , 3,4 ],
	'2列': [10 ,20 ,30 ,40 ]
})

st.write(df)
st.dataframe(df,width=100,height=100)
st.dataframe(df.style.highlight_max(axis=0))
st.dataframe(df.style.highlight_max(axis=1))
st.dataframe(df.style.highlight_min(axis=0))
st.table(df)