import streamlit as st
import time

# ⭐ 반드시 첫 번째 Streamlit 명령
st.set_page_config(page_title="LookXpertM", layout="wide")

# -----------------------------
# 헤더
# -----------------------------
st.title("👗 LookXpertM")
st.caption("패션 추천 챗봇 – Prototype")

# -----------------------------
# Sidebar – 사용자 정보
# -----------------------------
with st.sidebar:
    st.title("👤 사용자 프로필")
    user_name = st.text_input("닉네임", "패셔니스타")
    prefer = st.radio("선호 스타일", ["미니멀", "스트릿", "캐주얼", "비즈니스"])
    st.info(f"{user_name}님 취향 반영 중입니다 😊")

# 세션 초기화
if "history" not in st.session_state:
    st.session_state.history = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

# -----------------------------
# 탭 구성
# -----------------------------
tab1, tab2, tab3 = st.tabs(["👕 추천", "🕑 추천 기록", "⭐ 찜 목록"])

# -----------------------------
# TAB 1 – 추천
# -----------------------------
with tab1:

    col1, col2, col3 = st.columns(3)

    with col1:
        weather = st.selectbox("☀️ 날씨", ["선택", "추움", "보통", "더움", "흐림", "장마"])

    with col2:
        situation = st.selectbox("💼 상황", ["선택", "출근", "데이트", "캐주얼", "여행", "면접"])

    with col3:
        tone = st.selectbox("🎨 톤", ["선택", "웜톤", "쿨톤", "뉴트럴"])

    budget = st.slider("💰 예산", 20000, 300000, 80000)

    if st.button("추천 받기", use_container_width=True):
        if "선택" in [weather, situation, tone]:
            st.warning("모든 값을 선택해주세요!")
        else:
            with st.spinner("LookXpertM AI가 코디를 분석 중입니다..."):
                time.sleep(1.2)

            st.success("분석 완료!")

            rec = f"{weather}/{situation}/{tone}/{budget}"
            st.session_state.history.append(rec)

            img_col, text_col = st.columns([1, 2])

            with img_col:
                st.image("https://via.placeholder.com/300x400.png?text=Recommended+Look")

            with text_col:
                st.markdown("### 🏷️ 옥스포드 셔츠 + 슬림 슬랙스")
                st.write(f"- 상황: **{situation}**")
                st.write(f"- 톤: **{tone}**")
                st.write(f"- 예산: **{budget:,}원 이하**")

                if st.button("⭐ 찜하기"):
                    st.session_state.favorites.append("옥스포드 셔츠 + 슬림 슬랙스")
                    st.success("찜 목록에 추가되었습니다!")

# -----------------------------
# TAB 2 – 추천 기록
# -----------------------------
with tab2:
    st.subheader("📜 이전 추천 기록")
    st.write(st.session_state.history)

# -----------------------------
# TAB 3 – 찜 목록
# -----------------------------
with tab3:
    st.subheader("⭐ 찜한 아이템")
    st.write(st.session_state.favorites)

st.subheader("👚 추천 이미지 갤러리")

image_urls = [
    "https://via.placeholder.com/300x400.png?text=Dress",
    "https://via.placeholder.com/300x400.png?text=Jacket",
    "https://via.placeholder.com/300x400.png?text=Casual",
]

st.image(image_urls, width=250, caption=["원피스", "자켓", "캐주얼"])


st.markdown("""
### ⭐ 추천 코디
- 🧥 상의: 옥스포드 셔츠
- 👖 하의: 슬림 슬랙스
- 👟 신발: 화이트 스니커즈
""")

for i, item in enumerate(st.session_state.favorites):
    col1, col2 = st.columns([4,1])
    col1.write(item)
    if col2.button("삭제", key=f"del_{i}"):
        st.session_state.favorites.pop(i)
import pandas as pd
df = pd.DataFrame(st.session_state.history, columns=["조건"])
st.table(df)


if st.button("🎯 전체 초기화"):
    st.session_state.history = []
    st.session_state.favorites = []
    st.experimental_rerun()


st.info(f"{user_name}님 스타일에 맞춰 추천했어요 ✨")


progress = st.progress(0)
for p in range(100):
    time.sleep(0.01)
    progress.progress(p+1)


