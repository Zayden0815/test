import streamlit as st
import pandas as pd

st.title("선박 적재 현황")

data = pd.DataFrame({
    '선박명' : ['슈팅스타', '골드', '깨방정', '잘달림'],
    '현재 적재량(%)' :[30, 40, 11, 2] ,
    '운송 컨티션' : ['좋음', '나쁨', '피곤함', '평균'],
    '인지도(%)' : [25, 20, 1, 10]
})

st.dataframe(data, use_container_width=True)

#edited_date = st.data_editor(data)
#st.write(edited_date)

st.bar_chart(data.set_index('선박명')['인지도(%)'])  #선택을 해옴
st.line_chart(data.set_index('선박명')['현재 적재량(%)']) 


fig = data.plot.pie(
    y = "인지도(%)",
    labels = data["선박명"],
    autopct = "%1.1f%%",
    figsize = (5,5),
    legend = False,
    title = "선박 별 인지도"
    ).get_figure()
st.pyplot(fig)