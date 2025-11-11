import streamlit as st
import random

# 퀴즈 데이터 예시 (질문/보기/정답/해설)
QUIZ_DATA = [
    {
        "question": "볼링 한 게임은 총 몇 프레임으로 구성되어 있나요?",
        "choices": ["8프레임", "10프레임", "12프레임", "15프레임"],
        "answer": "10프레임",
        "explanation": "볼링 한 게임은 10개의 프레임으로 구성됩니다."
    },
    {
        "question": "볼링에서 첫 투구로 10개의 핀을 모두 쓰러뜨리는 것을 뭐라고 하나요?",
        "choices": ["스페어", "더블", "스트라이크", "터키"],
        "answer": "스트라이크",
        "explanation": "첫 투구로 10개 핀 전부 쓰러뜨리는 것을 스트라이크라고 합니다."
    },
    {
        "question": "볼링 투구 시 넘어서는 안 되는 선을 무엇이라 하나요?",
        "choices": ["파울 라인", "스윙 라인", "출발선", "베이스 라인"],
        "answer": "파울 라인",
        "explanation": "파울 라인을 넘어가면 그 투구는 무효가 됩니다."
    },
    {
        "question": "볼링에서 연속으로 두 번 스트라이크를 기록하는 것을 뭐라고 하나요?",
        "choices": ["더블", "트리플", "스페어", "터키"],
        "answer": "더블",
        "explanation": "연속 두 번 스트라이크를 더블이라고 합니다."
    },
    {
        "question": "볼링 핀 하나의 점수는 몇 점인가요?",
        "choices": ["1점", "2점", "5점", "10점"],
        "answer": "1점",
        "explanation": "핀이 하나 넘어질 때마다 1점씩 얻습니다."
    },
    {
        "question": "볼링에서 '거터'란 무엇을 의미하나요?",
        "choices": [
            "레인 주변의 도랑으로 볼이 빠지는 곳",
            "투구 대기하는 구역",
            "핀을 쓰러뜨리는 기술",
            "투구 시작 점"
        ],
        "answer": "레인 주변의 도랑으로 볼이 빠지는 곳",
        "explanation": "거터는 볼링 레인 양쪽의 홈으로, 공이 이곳에 빠지면 점수를 얻지 못합니다."
    },
    {
        "question": "볼링에서 연속 3번 스트라이크를 기록하는 것을 무엇이라 하나요?",
        "choices": ["더블", "터키", "트리플", "스페어"],
        "answer": "터키",
        "explanation": "연속 세 번 스트라이크를 '터키'라고 부릅니다."
    },
    {
        "question": "볼링에서 레인의 표준 길이는 얼마인가요?",
        "choices": ["약 15m", "약 18.3m", "약 20m", "약 23.7m"],
        "answer": "약 18.3m",
        "explanation": "볼링 레인의 표준 길이는 약 18.3m(60피트)입니다."
    },
    {
        "question": "볼링에서 볼링 핀의 높이는 대략 얼마나 될까요?",
        "choices": ["15cm", "25cm", "38cm", "50cm"],
        "answer": "38cm",
        "explanation": "볼링 핀의 공식 높이는 약 38cm입니다."
    },
    {
        "question": "볼링에서 게임 점수 계산 시 스트라이크를 치면 몇 점의 보너스를 받나요?",
        "choices": ["다음 1번 투구 점수", "다음 2번 투구 점수", "다음 3번 투구 점수", "0점"],
        "answer": "다음 2번 투구 점수",
        "explanation": "스트라이크를 치면 다음 2번 투구 점수를 보너스로 받습니다."
    }
]



# 5개 랜덤 선택
if "sampled_quiz" not in st.session_state:
    st.session_state.sampled_quiz = random.sample(QUIZ_DATA, 5)
    st.session_state.user_answers = [None] * 5
    st.session_state.submitted = False

st.title("볼링 상식 퀴즈!!")
st.text("")
st.markdown("**5문제 중 3문제 이상 맞추면 선물을 드려요~**")
st.markdown("**볼링 동호회 가입 해주실거죠??!!**")
st.markdown("가입 문의 :")
st.markdown("Service AI개발팀 김도형 A / OP기획팀 황혜림 M")
st.divider()
# 퀴즈 화면
# for idx, q in enumerate(st.session_state.sampled_quiz):
#     st.write(f"Q{idx + 1}. {q['question']}")
#     st.session_state.user_answers[idx] = st.radio(
#         f"보기 {idx+1}", q['choices'], index=None, key=f"quiz_{idx}")
# # 스타일 정의 (한 번만 하면 됨)
# st.markdown(
#     """
#     <style>
#     .question-box {
#         border: 2px solid #4CAF50;
#         border-radius: 10px;
#         padding: 15px;
#         margin-bottom: 15px;
#         background-color: #f9f9f9;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # 문제 별 출력
# for idx, q in enumerate(st.session_state.sampled_quiz):
#     st.markdown(f"<div class='question-box'>", unsafe_allow_html=True)  # 박스 시작
#     st.write(f"Q{idx + 1}. {q['question']}")                            # 문제
#     st.session_state.user_answers[idx] = st.radio(
#         f"보기 {idx+1}", q['choices'], index=None, key=f"quiz_{idx}")   # 선택지
#     st.markdown("</div>", unsafe_allow_html=True)                      # 박스 닫기

for idx, q in enumerate(st.session_state.sampled_quiz):
    st.markdown(f"**Q{idx + 1}. {q['question']}**")  # 문제번호와 질문을 굵게
    st.session_state.user_answers[idx] = st.radio(
        f"보기 {idx+1}", q['choices'], index=None, key=f"quiz_{idx}")
    st.divider()  # 각 문제 끝에 구분선 삽입



# 제출 버튼
if st.button("최종 제출"):
    st.session_state.submitted = True

# # 결과 및 해설 화면
# if st.session_state.submitted:
#     correct_count = 0
#     for idx, q in enumerate(st.session_state.sampled_quiz):
#         user_ans = st.session_state.user_answers[idx]
#         if user_ans == q["answer"]:
#             correct_count += 1
#             st.success(f"{idx+1}번 정답! ({user_ans})")
#         else:
#             st.error(f"{idx+1}번 오답! (선택: {user_ans}, 정답: {q['answer']})")
#         st.info(f"해설: {q['explanation']}")
#     st.write(f"총 {correct_count}개 맞춤!")
#     st.balloons()

# if st.session_state.submitted:
#     correct_count = 0
#     for idx, q in enumerate(st.session_state.sampled_quiz):
#         user_ans = st.session_state.user_answers[idx]
#         if user_ans == q["answer"]:
#             correct_count += 1

#     # 맞춘 개수 먼저 크게 보여주기
#     st.markdown(f"<h2>총 {correct_count}개 맞춤!</h2>", unsafe_allow_html=True)

#     # 맞춘 개수에 따른 축하 또는 격려 메시지
#     if correct_count >= 3:
#         st.text("축하합니다. 선물을 받아가세요!")
#     else:
#         st.text("아쉽네요. 참여 선물을 받아가세요~")

#     # 개별 문제별 정답/오답과 해설 출력
#     for idx, q in enumerate(st.session_state.sampled_quiz):
#         user_ans = st.session_state.user_answers[idx]
#         if user_ans == q["answer"]:
#             st.success(f"{idx+1}번 정답! ({user_ans})")
#         else:
#             st.error(f"{idx+1}번 오답! (선택: {user_ans}, 정답: {q['answer']})")
#         st.info(f"해설: {q['explanation']}")

#     st.balloons()


if st.session_state.submitted:
    correct_count = 0
    for idx, q in enumerate(st.session_state.sampled_quiz):
        user_ans = st.session_state.user_answers[idx]
        if user_ans == q["answer"]:
            correct_count += 1

    st.markdown(f"<h2>총 {correct_count}개 맞춤!</h2>", unsafe_allow_html=True)

    if correct_count >= 3:
        st.text("축하합니다. 선물을 받아가세요!")
    else:
        st.text("아쉽네요. 참여 선물을 받아가세요~")

    for idx, q in enumerate(st.session_state.sampled_quiz):
        user_ans = st.session_state.user_answers[idx]

        # 박스 스타일 HTML과 CSS
        box_html = f"""
        <div style='border:2px solid #4CAF50; border-radius:10px; padding:15px; margin-bottom:10px;'>
            <b>Q{idx+1}. {q['question']}</b><br>
            {'정답' if user_ans == q["answer"] else '오답'}: {user_ans} (정답: {q['answer']})<br>
            해설: {q['explanation']}
        </div>
        """
        st.markdown(box_html, unsafe_allow_html=True)

    st.balloons()


