import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="용액의 성질 계산기", page_icon="🧪")

st.title("🧪 용액의 성질 계산기")
st.write("염기성 용액과 산성 용액의 양을 입력해 혼합 용액의 성질을 확인하세요.")

water_feature = ["산성", "중성", "염기성"]


# 계산 함수 (값을 매개변수로 받아 결과를 반환하도록 수정)
def water_calculation(base, acid):
    volume = acid - base

    if volume > 0:
        result = water_feature[0]
    elif volume == 0:
        result = water_feature[1]
    else:
        result = water_feature[2]

    total_volume = base + acid
    return result, total_volume


# 1. 사용자 입력 (min_value를 지정해 0 이하 입력 방지)
base = st.number_input("(1) 염기성 용액 양 (ml)", min_value=0.0, value=10.0, step=1.0)
acid = st.number_input("(2) 산성 용액 양 (ml)", min_value=0.0, value=10.0, step=1.0)

# 2. 계산 버튼 및 결과 출력
if st.button("결과 계산하기", use_container_width=True):
    if base <= 0 or acid <= 0:
        st.warning("⚠️ 두 용액의 양 모두 0보다 큰 양수로 입력해 주세요.")
    else:
        result, total_volume = water_calculation(base, acid)

        st.divider()
        st.subheader("📊 계산 결과")
        st.success(f"**용액의 성질:** {result}")
        st.info(f"**총 부피:** {total_volume:.1f} ml")
