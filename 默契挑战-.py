# coding = utf-8
import streamlit as st

# 1. 初始化题目和答案
questions = [
    {"q": "春天1 or 夏天2 or 秋天3 or 冬天4", "options": ["春天", "夏天", "秋天", "冬天"], "a": "秋天"},
    {"q": "早起看日出1 or 熬夜就看星星2", "options": ["早起看日出", "熬夜看星星"], "a": "熬夜看星星"},
    {"q": "吃薯条：致死量番茄酱1 or 一包即可2", "options": ["致死量番茄酱", "一包即可"], "a": "致死量番茄酱"},
    {"q": "黑巧1 or 牛奶巧2", "options": ["黑巧", "牛奶巧"], "a": "牛奶巧"},
    {"q": "最喜欢的水果是", "options": ["黄桃", "其他水果"], "a": "黄桃"},
    {"q": "考过最低分数的科目", "options": ["物理", "其他科目"], "a": "物理"},
    {"q": "喜欢长发1 or 短发2", "options": ["长发", "短发"], "a": "短发"},  # 假设你原本想写2，这里我帮你改成了短发
    {"q": "冷色调1 or 暖色调2", "options": ["冷色调", "暖色调"], "a": "暖色调"},
    {"q": "单曲循环1 or 随机播放2", "options": ["单曲循环", "随机播放"], "a": "随机播放"},  # 假设你原本想写2，这里我帮你改成了随机播放
    {"q": "火车靠窗看风景1 or 飞机靠窗看云层2", "options": ["火车靠窗看风景", "飞机靠窗看云层"], "a": "飞机靠窗看云层"}
]

# 2. 初始化游戏状态
if "level" not in st.session_state:
    st.session_state.level = 0
if "count" not in st.session_state:
    st.session_state.count = 0.0
if "show next_btn" not in st.session_state:
    st.session_state.show next_btn = False
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.title("🌟 默契挑战 🌟")
st.markdown("---")

# 3. 游戏结束后的结算页面
if st.session_state.game_over:
    score = st.session_state.count
    score_text = f"{score * 10:.0f}%"
    # 按钮逻辑：先提交，后下一题
    col1, col2 = st.columns([1, 1])

    with col1:
        # 只有没提交过答案时，才显示“提交”按钮
        if not st.session_state.show_next_btn:
            submit_btn = st.button("📤 提交答案", use_container_width=True, type="primary")
            if submit_btn:
                if selected_option is None:
                    st.warning("⚠️ 请先选择一个选项再提交哦！")
                else:
                    check_answer()
                    st.rerun()
# 根据分数给出不同的评价
    if score == 0.0:
        feedback = f"你与我的契合程度为：{score_text} 💢 来细数你的罪恶吧！"
    elif score < 0.6:
        feedback = f"你与我的契合程度为：{score_text} 有共鸣但不多~"
    elif score == 0.6:
        feedback = f"你与我的契合程度为：{score_text} 你对我的认识刚刚及格~"
    elif score == 0.7:
        feedback = f"你与我的契合程度为：{score_text} 与你交流肯定很愉快~"
    elif score == 0.8:
        feedback = f"你与我的契合程度为：{score_text} 剩下的20%是我们畅聊的话题~"
    elif score == 0.9:
        feedback = f"你与我的契合程度为：{score_text} 不用多说，一个眼神就懂~"
    else:  # 1.0
        feedback = f"你与我的契合程度为：{score_text} 🌟 UNBELIEVABLE 🌟 世另我！"

    st.success(feedback)
    if st.button("🔄 再玩一次"):
        st.session_state.level = 0
        st.session_state.count = 0.0
        st.session_state.game_over = False
        st.rerun()
else:
    # 4. 正常答题逻辑
    current_q = questions[st.session_state.level]
    st.subheader(f"第 {st.session_state.level + 1} 题")


    if st.session_state.level >= len(questions):
        st.session_state.game_over = True

        st.rerun()