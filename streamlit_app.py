import streamlit as st

st.set_page_config(page_title="나를 소개하는 페이지", page_icon="👋", layout="wide")

st.title("👋 안녕하세요! 제 소개 페이지")
st.write("여기는 당신의 이름, 연락처, 스킬과 프로젝트를 소개하는 Streamlit 웹 페이지입니다.")

# 👉 사용자 입력으로 자기소개 글 생성
st.subheader("📝 자기소개 내용 입력")
name = st.text_input("이름", "박예진")
age = st.number_input("나이", min_value=0, max_value=120, value=23)
major = st.text_input("전공", "인천대학교 수학교육과")
year = st.selectbox("학번", ["20학번", "21학번", "22학번", "23학번", "24학번"], index=3)
grade = st.selectbox("학년", ["1학년", "2학년", "3학년", "4학년"], index=3)
about = st.text_area("자기소개", "안녕하세요! 저는 인천대학교 수학교육과에 재학 중인 23학번 박예진입니다. 현재 4학년이고, 수학 교육에 열정을 가지고 있으며 Streamlit을 통해 웹 앱을 만들고 있습니다.")

st.write("---")
st.subheader("📌 소개 요약")
st.markdown(f"""**이름:** {name}
**나이:** {age}
**전공:** {major}
**학번:** {year}
**학년:** {grade}""")
st.write(about)

st.write("---")

# 링크, 배지, 이미지 예시
st.subheader("🌐 연락 및 프로필")
col1, col2, col3 = st.columns(3)
col1.write("[LinkedIn](https://www.linkedin.com)")
col2.write("[GitHub](https://github.com)")
col3.write("[포트폴리오](https://example.com)")

st.image("https://static.streamlit.io/examples/dog.jpg", caption="프로필 사진 자리", use_column_width=False)

st.write("---")

# 기술 스택
st.subheader("🛠️ 기술 스택")
skills = st.multiselect("보유 기술 선택", ["Python", "JavaScript", "React", "Streamlit", "Docker", "AWS"], default=["Python", "Streamlit"])
st.write("선택한 기술:", ", ".join(skills))

st.write("---")

# 간단한 인사 버튼
if st.button("인사하기"):
    st.success(f"안녕하세요, {name}님! 만나서 반갑습니다.\n이 페이지는 Streamlit으로 만들어졌어요.")

st.write("===")

st.header("🎈 아래는 이전 Streamlit 요소 샘플이 이어집니다")

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
