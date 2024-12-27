import streamlit as st

st.title('사용자 입력 받기')

in_name = st.text_input('선적(도착) 할 국가를 입력하세요.')
time = st.number_input("소요 날짜를 입력", min_value = 1, max_value = 300)

options = ["FOB", "CIF", "CLF", "FAS"]
selected = st.selectbox("선적 방식 입력", options)

r_options = ["항공", "해상", "육로", "그 외"]
choice = st.radio("운송 방식", r_options)


selected_many = st.multiselect("운송 방식이 여러개라면?", r_options)

checked = st.checkbox("개인정보 제공 동의")

if st.button("입력 성공!") :
    st.write(f'선적 방식은?{in_name}')
    st.write(f'도착항까지 소요되는 시간은?{time}')
    st.write(f'선적 방식?{selected}')
    st.write(f'운송 방식?{choice}')
    st.write(f'운송 방식이 여러개?{selected_many}')
    st.write(f'운송 방식은은?{choice}')
    st.write(f'개인 정보 동의해?{checked}')
    st.write(f'입력하신 선적 방신은 {in_name}{selected}이며, 총 소요 시간은 {time}입니다.')