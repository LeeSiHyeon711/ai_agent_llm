from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
import os

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = "OPEN_API_KEY"

llm = init_chat_model("gpt-5-mini", model_provider="openai")

class MovieReview(BaseModel):
    """영화 리뷰 스키마 정의"""
    title: str = Field(description="영화 제목")
    rating: float = Field(description="10점 만점 평정 (예: 7.5)")
    review: str = Field(description="한글 리뷰 (3~4분장)")

structured_llm = llm.with_structured_output(MovieReview)
result: MovieReview = structured_llm.invoke(
    "영화 '기생충'에 대한 리뷰를 작성해주세요."
)

print(result.title)
print(result.rating)
print(result.review)