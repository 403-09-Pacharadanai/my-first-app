import time
import streamlit as st

st.title("🐒 Chest Nuts Monkey Gameplay 1978")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""
if "ans6_val" not in st.session_state:
    st.session_state.ans6_val = ""


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.ans3_val = ""  # เคลียร์ค่าช่องข้อ 3
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 4
    st.session_state.ans5_val = ""  # เคลียร์ค่าช่องข้อ 5
    st.session_state.ans6_val = ""  # เคลียร์ค่าช่องข้อ 6
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 ผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6):
    st.balloons()
    score = 0

    # แก้ไขการกำหนดตัวแปรให้ตรงข้อ
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()
    u_ans6 = ans6.strip().lower()

    # ตรวจข้อ 1
    if u_ans1 == "chest nut":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "expensive":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ตรวจข้อ 3
    if u_ans3 == "entrance":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    # ตรวจข้อ 4
    if u_ans4 == "ancient":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    # ตรวจข้อ 5
    if u_ans5 == "monkey":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")

    # ตรวจข้อ 6
    if u_ans6 == "nobility":
        st.success("✅ ข้อ 6: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 6: ยังไม่ถูกต้อง (คุณตอบ '{u_ans6}')")

    # สรุปผลคะแนน 6 ระดับ
    if score == 6:
        st.success("😜 คุณเป็นราชาลิงเกาลัด")
    elif score == 5:
        st.success("🧐 คุณเป็นราชณิกุลลิงเกาลัด")
    elif score == 4:
        st.info("😳 คุณเป็นสมาร์ทลิงเกาลัด")
    elif score == 3:
        st.info("😖 คุณเป็นลิงเกาลัดชั้นประถม")
    elif score == 2:
        st.warning("😭 คุณเป็นลิงเกาลัดกินขี้มูก")
    elif score == 1:
        st.warning("😱 คุณเป็นลิงเกาลัดจัณฑาล")
    else:
        st.error("👽 คุณคือผงลิงเกาลัด")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(60 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (แก้ไขค่า value ให้ตรงกับ session_state ของตัวเอง)
ans1 = st.text_input(
    "ข้อ 1: C___t n_t - เกาลัด. 🌰",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: E___ns__e - แพง. 🤑",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3: E_t___ce - ทางเข้า. 🚪",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: A____nt - โบราณ. 🏺",
    value=st.session_state.ans4_val,
)
ans5 = st.text_input(
    "ข้อ 5: M__k__ - ลิง. 🐒🙈🙉🙊",
    value=st.session_state.ans5_val,
)
ans6 = st.text_input(
    "ข้อ 6: N___li__ - ขุนนาง. 🤴🏰",
    value=st.session_state.ans6_val,
)

# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5
st.session_state.ans6_val = ans6

# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง Dialog ผลลัพธ์ (แก้ไขการส่งพารามิเตอร์ให้ครบทั้ง ans1 ถึง ans6)
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6)
