import matplotlib.pyplot as plt
import streamlit as st

fig, ax = plt.subplots()

c1 = st.sidebar.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'purple', 'orange'])
s1 = st.sidebar.radio('선의 스타일을 선택하시오', ['-', '--', ':', '-.'])
m1 = st.sidebar.radio('마커의 스타일을 선택하시오', ['^','o','s','p'])

a = st.number_input('a 값을 입력하시오', value = 2.0, step=1.0)
b = st.number_input('b 값을 입력하시오', value = -1.0, step=1.0)
c = st.number_input('c 값을 입력하시오', value = 15.0, step=1.0)
d = st.number_input('d 값을 입력하시오', value = 2000.0, step=100.0)



love = []
y1 = []
y2 = []
for i in range(-29,30,3):
    love.append(i)
    y1.append(a*i*i + b*i + c)
    y2.append(d/i)



#plt.plot(x, y, 'r:^')
plt.plot(love, y1, y2, color = c1, linestyle = s1, marker = m1)

st.pyplot(fig)


import sys
sys.exit()
