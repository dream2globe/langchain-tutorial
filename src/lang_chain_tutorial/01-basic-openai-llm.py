import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
os.environ["OPENAI_API_KEY"]


# Hello World
def hello_world_llm():
    llm = ChatOpenAI(
        temperature=0.1,  # 창의성 (0.0 ~ 2.0)
        model_name="gpt-4o",  # 모델명
    )
    question = "대한민국의 수도는 어디인가요?"
    response = llm.invoke(question)
    print(f"{response}")
    print(f"{response.content}")
    print(f"{response.response_metadata}")


# LogProb 활성화
def llm_with_logprob():
    llm_with_logprob = ChatOpenAI(
        temperature=0.1,  # 창의성 (0.0 ~ 2.0)
        max_tokens=2048,  # 최대 토큰수
        model_name="gpt-3.5-turbo",  # 모델명
    ).bind(logprobs=True)

    question = "대한민국의 수도는 어디인가요?"
    response = llm_with_logprob.invoke(question)
    print(f"{response.response_metadata}")


# 스트리밍 출력
def streaming():
    llm = ChatOpenAI(
        temperature=0.1,  # 창의성 (0.0 ~ 2.0)
        model_name="gpt-4o",  # 모델명
    )
    answer = llm.stream("대한민국의 아름다운 관광지 10곳과 주소를 알려주세요!")
    for token in answer:
        print(token.content, end="", flush=True)

# 멀티모달
def multi_model():
    
# System, User 프롬프트 수정
def user_defined_prompt():