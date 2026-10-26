# coding = utf-8
import streamlit as st

# 1. 初始化题目和答案
questions = [
    {"q": "我的生日是", "a": "0307"},
    {"q": "我上的大学是", "a": "华南师范大学"},
    {"q": "我的专业是", "a": "软件工程"}
]

max_tries = 3

# 2. 初始化游戏状态（保存在 session 中，防止网页刷新就重置）
if "level" not in st.session_state:
    st.session_state.level = 0
if "tries" not in st.session_state:
    st.session_state.tries = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.title("🎓 专属问答小游戏")
st.markdown("---")

# 3. 判断游戏是否结束
if st.session_state.game_over:
    st.error("💔 你已被毕业！游戏结束。")
    if st.button("🔄 重新开始"):
        st.session_state.level = 0
        st.session_state.tries = 0
        st.session_state.game_over = False
        st.rerun()
elif st.session_state.level >= len(questions):
    st.success("🎉 恭喜你！全部通关！你太了解我啦！")
    if st.button("🔄 再玩一次"):
        st.session_state.level = 0
        st.session_state.tries = 0
        st.session_state.game_over = False
        st.rerun()
else:
    # 4. 正常答题逻辑
    current_q = questions[st.session_state.level]
    st.subheader(f"第 {st.session_state.level + 1} 关")

    answer = st.text_input(current_q["q"], key=f"input_{st.session_state.level}_{st.session_state.tries}")

    if answer:
        if answer == current_q["a"]:
            st.success("✅ 回答正确！\n")
            st.session_state.level += 1
            st.session_state.tries = 0
            st.rerun()  # 自动跳到下一题
        else:
            st.session_state.tries += 1
            leave = max_tries - st.session_state.tries
            if leave > 0:
                st.error(f"❌ 回答错误，你还有 {leave} 次机会")
                st.rerun()
            else:
                st.session_state.game_over = True
                st.rerun()