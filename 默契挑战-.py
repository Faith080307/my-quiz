# coding = utf-8
import streamlit as st

# 1. 初始化题目和答案数据
questions = [
    {"q": "春天1 or 夏天2 or 秋天3 or 冬天4", "options": ["春天", "夏天", "秋天", "冬天"], "a": "秋天"},
    {"q": "早起看日出1 or 熬夜就看星星2", "options": ["早起看日出", "熬夜看星星"], "a": "熬夜看星星"},
    {"q": "吃薯条：致死量番茄酱1 or 一包即可2", "options": ["致死量番茄酱", "一包即可"], "a": "致死量番茄酱"},
    {"q": "黑巧1 or 牛奶巧2", "options": ["黑巧", "牛奶巧"], "a": "牛奶巧"},
    {"q": "最喜欢的水果是", "options": ["黄桃", "芒果","哈密瓜"], "a": "黄桃"},
    {"q": "考过最低分数的科目", "options": ["物理", "数学","生物"], "a": "物理"},
    {"q": "喜欢长发1 or 短发2", "options": ["长发", "短发","都可以"], "a": "都可以"},
    {"q": "冷色调1 or 暖色调2", "options": ["冷色调", "暖色调"], "a": "暖色调"},
    {"q": "单曲循环1 or 随机播放2", "options": ["单曲循环", "随机播放","都可以"], "a": "都可以"},
    {"q": "火车靠窗看风景1 or 飞机靠窗看云层2", "options": ["火车靠窗看风景", "飞机靠窗看云层"], "a": "飞机靠窗看云层"}
]

# 2. 初始化游戏状态
if "level" not in st.session_state:
    st.session_state.level = 0
if "count" not in st.session_state:
    st.session_state.count = 0.0
if "show_next_btn" not in st.session_state:
    st.session_state.show_next_btn = False
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.title("🌟 默契挑战 🌟")
st.markdown("---")

# 3. 游戏结束后的结算页面
if st.session_state.game_over:
    score = st.session_state.count
    score_text = f"{score * 100:.0f}%"

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
        st.session_state.show_next_btn = False
        st.rerun()

else:
    # 4. 正常答题逻辑
    current_q = questions[st.session_state.level]
    st.subheader(f"第 {st.session_state.level + 1} / {len(questions)} 题")

    # 使用单选按钮，index=None 保证默认不选中
    user_choice = st.radio(
        current_q["q"],
        current_q["options"],
        key=f"radio_{st.session_state.level}",
        index=None
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        # 只有没提交过答案时，才显示“提交”按钮
        if not st.session_state.show_next_btn:
            submit_btn = st.button("📤 提交答案", use_container_width=True, type="primary")
            if submit_btn:
                if user_choice is None:
                    st.warning("⚠️ 请先选择一个选项再提交哦！")
                else:
                    # 核心逻辑：暗中计分，不显示对错
                    if user_choice == current_q["a"]:
                        st.session_state.count += 0.1

                    # 标记已提交，准备进入下一题
                    st.session_state.show_next_btn = True
                    st.rerun()

    with col2:
        # 只有提交过答案后，才显示“下一题”按钮
        if st.session_state.show_next_btn:
            next_btn = st.button("➡️ 下一题", use_container_width=True, type="secondary")
            if next_btn:
                st.session_state.level += 1
                st.session_state.show_next_btn = False

                # 检查是否全部答完
                if st.session_state.level >= len(questions):
                    st.session_state.game_over = True

                st.rerun()