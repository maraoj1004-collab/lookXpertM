import streamlit as st
import time
import pandas as pd
import urllib.parse

# ⭐ 반드시 첫 번째
st.set_page_config(page_title="LookXpertM", layout="wide")

# -------------------------------------------------
# LLM 더미 함수 (나중에 연결 가능)
# -------------------------------------------------
def ask_llm(weather, situation, tone, budget, prefer, user_name):
    return f"""
👤 사용자: {user_name}
✔ 날씨: {weather}
✔ 상황: {situation}
✔ 스타일 톤: {tone}
✔ 예산: {budget:,}원
✔ 선호 스타일: {prefer}

👉 추천 코디 예시:
- 상의: 니트 또는 셔츠
- 하의: 슬랙스 또는 데님
- 아우터: 상황에 맞는 코트/패딩
- 컬러: 톤에 맞춰 매칭
"""

# -------------------------------------------------
# 메인 타이틀
# -------------------------------------------------
st.title("👗 LookXpertM – Fashion Recommender")
st.caption("패션 추천 챗봇 Prototype")

# -------------------------------------------------
# Sidebar
# -------------------------------------------------
with st.sidebar:
    st.title("👤 사용자 프로필")
    user_name = st.text_input("닉네임", "패셔니스타")
    prefer = st.radio("선호 스타일", ["미니멀", "스트릿", "캐주얼", "비즈니스"])
    st.info(f"{user_name}님 취향 반영 중입니다 😊")

# -------------------------------------------------
# 세션 상태
# -------------------------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

# -------------------------------------------------
# 탭 구성
# -------------------------------------------------
tab1, tab2, tab3 = st.tabs(["👕 추천", "🕑 추천 기록", "⭐ 찜 목록"])

# -------------------------------------------------
# TAB 1 – 추천
# -------------------------------------------------
with tab1:

    col1, col2, col3 = st.columns(3)

    weather = col1.selectbox("☀️ 날씨", ["선택", "추움", "보통", "더움", "흐림", "장마"])
    situation = col2.selectbox("💼 상황", ["선택", "출근", "데이트", "캐주얼", "여행", "면접"])
    tone = col3.selectbox("🎨 톤", ["선택", "웜톤", "쿨톤", "뉴트럴"])

    budget = st.slider("💰 예산", 20000, 300000, 80000)

    if st.button("🎯 코디 추천 받기", use_container_width=True):
        if "선택" in [weather, situation, tone]:
            st.warning("모든 값을 선택해주세요!")
        else:
            with st.spinner("LookXpertM AI가 코디를 분석 중입니다..."):
                time.sleep(1)

            st.success("추천 생성 완료!")

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

# -------------------------------------------------
# TAB 2 – 추천 기록
# -------------------------------------------------
with tab2:
    st.subheader("📜 이전 추천 기록")
    if len(st.session_state.history) == 0:
        st.write("아직 추천 기록이 없어요 😄")
    else:
        st.table(pd.DataFrame(st.session_state.history, columns=["조건"]))

# -------------------------------------------------
# TAB 3 – 찜 목록
# -------------------------------------------------
with tab3:
    st.subheader("⭐ 찜한 아이템")
    st.write(st.session_state.favorites)

# -------------------------------------------------
# 겨울 패션 Q&A
# -------------------------------------------------
st.header("❄ 겨울 패션 Q&A")

q = st.selectbox(
    "질문을 선택하세요",
    [
        "요즘 인기 있는 겨울 아우터는?",
        "최근 패딩 트렌드 알려줘",
        "숏패딩 vs 롱패딩 뭐사야해?",
        "겨울 코트 소재 추천해줘"
    ]
)

if st.button("✨ 답변 보기"):
    if q == "요즘 인기 있는 겨울 아우터는?":
        st.write("✔ 숏패딩, 덤블 자켓, 하프 다운, 퍼 자켓이 특히 인기예요.")
    elif q == "최근 패딩 트렌드 알려줘":
        st.write("✔ 크롭 기장, 라이트 다운, 투웨이 지퍼가 트렌드입니다.")
    elif q == "숏패딩 vs 롱패딩 뭐사야해?":
        st.write("✔ 활동성=숏패딩 / 야외 체류 길면=롱패딩 추천!")
    elif q == "겨울 코트 소재 추천해줘":
        st.write("✔ 울 80% 이상, 캐시미어 블렌드, 메리노울 소재가 좋아요.")

# -------------------------------------------------
# 🔗 패션 트렌드 링크
# -------------------------------------------------
st.header("🧭 패션 트렌드 링크 추천")

if st.button("✔ 보그 & 엘르 링크 열기"):
    st.link_button("VOGUE KOREA 트렌드 기사", 
                   "https://www.vogue.co.kr/category/fashion/fashion-trend/")
    st.link_button("ELLE KOREA 패션 트렌드", 
                   "https://www.elle.co.kr/Fashion")

# -------------------------------------------------
# 무신사 검색 URL 자동 생성기
# -------------------------------------------------
st.header("🛍 무신사 검색 URL 자동 생성기")

keyword = st.text_input("키워드 입력 (예: 겨울패딩)", value="겨울패딩")
color = st.text_input("색상 입력 (예: BLACK)", value="BLACK")

encoded_keyword = urllib.parse.quote(keyword)

url = f"https://www.musinsa.com/search/goods?keyword={encoded_keyword}&keywordType=keyword&gf=F&color={color}"

st.write("🔗 자동 생성된 링크:")
st.link_button("무신사 검색 결과 열기", url)

st.code(url, language="text")

# -------------------------------------------------
# 전체 초기화
# -------------------------------------------------
if st.button("🧹 전체 초기화"):
    st.session_state.history = []
    st.session_state.favorites = []
    st.rerun()




