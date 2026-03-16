import streamlit as st

st.set_page_config(page_title="Streamlit 요소 샘플", page_icon="🎨", layout="wide")

st.title("🎈 Streamlit 요소 샘플 페이지")
st.write("아래는 Streamlit에서 자주 쓰는 주요 UI 요소 예시입니다.")

# 사이드바
st.sidebar.header("사이드바 예시")
st.sidebar.write("사이드바에서 상태를 제어할 수 있습니다.")
show_chart = st.sidebar.checkbox("차트 표시")
option = st.sidebar.selectbox("옵션 선택", ["A", "B", "C"])

# 입력 위젯
st.header("🧩 입력 위젯")
text_input = st.text_input("텍스트 입력", value="안녕하세요")
number = st.number_input("숫자 입력", min_value=0, max_value=100, value=42)
slider = st.slider("슬라이더", min_value=0, max_value=100, value=25)

st.write("입력값 확인:", text_input, number, slider, option)

# 버튼과 상태
if st.button("눌러보기 버튼"):
    st.success("버튼이 눌렸습니다!")

if st.checkbox("이 체크박스를 체크하면 메시지 보이기"):
    st.info("체크가 활성화되었습니다.")

# 멀티미디어
st.header("🎥 멀티미디어")
st.image("https://static.streamlit.io/examples/dog.jpg", caption="예시 이미지", use_column_width=True)

# 차트
import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.subheader("차트 예시")
if show_chart:
    st.line_chart(data)
    st.bar_chart(data)
    st.area_chart(data)

# 멀티 컬럼 레이아웃
st.header("🧱 레이아웃")
col1, col2, col3 = st.columns(3)
col1.metric("온도", "22°C", "+3°C")
col2.metric("습도", "60%", "-5%")
col3.metric("속도", "120 km/h", "+8 km/h")

# 코드, 데이터 표시
st.header("🧾 텍스트 / 코드 / 데이터")
st.code("print('Hello Streamlit')")
st.json({"name": "Streamlit", "type": "Web app"})

st.dataframe(data)

# 진행 표시
st.header("⏳ 진행 상태")
progress = st.progress(0)
for i in range(101):
    progress.progress(i)

# 사용자 입력 기반 알림
if st.button("리셋 진행 상태"):
    st.experimental_rerun()
