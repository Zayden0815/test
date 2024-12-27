import streamlit as st

st.title("무역 실무 : ")

st.header('오늘은 무역 실무에서 사용하는 인코텀즈의 종류에 대해서 알아보겠습니다.')

st.subheader("정형거래조건(International commercial terms)은 국제상업회의소가 국제 물품 매매 계약을 위하여 제정한 규칙이다. 약칭인 인코텀즈(Incoterms)로 주로 사용된다. 오늘날 쓰이고 있는 규칙은 인코텀즈 2020이라고 불리며, 이것은 여러 차례의 개정을 걸친 것이다. 보통 10년에 한 번씩 개정된다.")

my_site = st.text_input('확인 하고 싶은 인코텀즈 >',)
st.write(my_site)

if st.button(f'{my_site} 접속하기') :            #True False의 상태를 가짐
    st.success(f'{my_site}원하시는 종류의 인코텀즈를 확인하는 중입니다.🐨🐨🐨', icon = '💕')