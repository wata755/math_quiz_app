import streamlit as st
import random

# ページタイトル
st.title("数学問題アプリ")

# セッションステート初期化
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'score' not in st.session_state:
    st.session_state.score = 0

# ジャンル選択
genre = st.sidebar.selectbox("出題ジャンルを選んでください", ("3元一次方程式", "たすき掛け因数分解"))

# 3元一次方程式の問題作成
def generate_linear_equation():
    a, b, c, d, e, f, g, h, i, j, k, l = [random.randint(1, 9) for _ in range(12)]
    question = f"{a}x + {b}y + {c}z = {d},  {e}x + {f}y + {g}z = {h},  {i}x + {j}y + {k}z = {l}"
    answer = "仮"  # 今回は解かないので仮
    return question, answer

# たすき掛け因数分解の問題作成
def generate_factorization():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    d = random.randint(1, 9)
    question = f"{a * c}x² + {(a * d) + (b * c)}x + {b * d}"
    answer = f"({a}x+{b})({c}x+{d})"  # 答えも作る
    return question, answer

# 出題数
num_questions = 25

# 問題リスト初期化
questions = []
answers = []

# 問題生成
for i in range(num_questions):
    if genre == "3元一次方程式":
        q, a = generate_linear_equation()
    elif genre == "たすき掛け因数分解":
        q, a = generate_factorization()
    questions.append(q)
    answers.append(a)

# 問題表示
st.subheader(f"{genre}の問題")
for i in range(num_questions):
    st.write(f"問題{i+1}: {questions[i]}")
    st.text_input(f"答え{i+1}", key=f"answer_{i}")

# 採点ボタン
if st.button("採点する"):
    score = 0
    st.write("採点結果：")
    for i in range(num_questions):
        user_answer = st.session_state[f"answer_{i}"]
        correct_answer = answers[i]
        if genre == "3元一次方程式":
            st.write(f"問題{i+1}: あなたの答え「{user_answer}」 → 正解: {correct_answer}（採点対象外）")
        else:
            if user_answer.replace(" ", "") == correct_answer:
                st.write(f"問題{i+1}: 正解！")
                score += 4  # 1問4点
            else:
                st.write(f"問題{i+1}: 不正解。正解は {correct_answer}")
    if genre == "たすき掛け因数分解":
        st.write(f"合計得点: {score}点（{num_questions * 4}点満点）")

