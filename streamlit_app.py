import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Kiran P, EMBA')

st.info('BI/BA Analyst, Knowledge Builder with an interest in Data Science & Analysis')

icon_size = 20


st_button('medium', 'https://https://kiran1-paudel2.medium.com/', 'Read my Blogs', icon_size)

st_button('linkedin', 'https://www.linkedin.com/in/paudelkiran/', 'Follow me on LinkedIn', icon_size)

st_button('strikingly', 'https://paudel7.mystrikingly.com/', 'Visit my profile', icon_size)

#st_button('cup', 'https://www.buymeacoffee.com/toupdate/', 'Buy me a Coffee', icon_size)
