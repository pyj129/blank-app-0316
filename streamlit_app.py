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
hobby = st.text_input("취미", "넷플릭스 보기")
about = st.text_area("자기소개", "안녕하세요! 저는 인천대학교 수학교육과에 재학 중인 23학번 박예진입니다. 현재 4학년이고, 수학 교육에 열정을 가지고 있으며 Streamlit을 통해 웹 앱을 만들고 있습니다.")

st.write("---")
st.subheader("📌 소개 요약")
st.markdown(f"""**이름:** {name}
**나이:** {age}
**전공:** {major}
**학번:** {year}
**학년:** {grade}
**취미:** {hobby}""")
st.write(about)
