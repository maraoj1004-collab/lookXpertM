import streamlit as st

st.set_page_config(page_title="LookXpert", layout="wide")

st.title("👗 LookXpert")
st.subheader("패션 추천 챗봇 UI Prototype")

st.write("아직 AI 모델은 연결되지 않았어요.")
st.write("지금은 UI 구조를 먼저 잡는 단계입니다.")

if st.button("오늘의 코디 추천"):
    st.success("니트 + 슬랙스 + 로퍼 조합을 추천해요 ✨")
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    weather = st.selectbox("날씨", ["선택", "추움", "보통", "더움"])

with col2:
    situation = st.selectbox("상황", ["선택", "출근", "데이트", "캐주얼", "여행"])

with col3:
    tone = st.selectbox("톤", ["선택", "웜톤", "쿨톤", "뉴트럴"])

st.divider()
st.subheader("👕 추천 코디")

if st.button("추천 받기"):
    st.markdown("""
    ### 오늘의 추천 ✨
    - **상의**: 니트
    - **하의**: 슬랙스
    - **신발**: 로퍼
    - **포인트**: 미니멀한 컬러 매치
    """)
st.info("⚙️ 현재는 UI 프로토타입 단계이며, 추후 LLM 기반 추천 로직이 연결될 예정입니다.")
st.divider()
st.subheader("👕 추천 코디")

if st.button("오늘의 코디 추천", key="top_reco"):
    st.success("니트 + 슬랙스 + 로퍼 조합을 추천해요 ✨")

...

if st.button("추천 받기", key="detail_reco"):
    st.markdown("""
    ### 오늘의 추천 ✨
    - **상의**: 니트
    - **하의**: 슬랙스
    - **신발**: 로퍼
    - **포인트**: 미니멀한 컬러 매치
    """)

