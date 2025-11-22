import asyncio
import os
from dotenv import load_dotenv
from pathlib import Path
from openai import AsyncOpenAI

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY가 .env 파일에 설정되지 않았습니다. 프로젝트 루트의 .env 파일을 확인하세요.")

openai_client = AsyncOpenAI(api_key=openai_api_key)

async def call_async_openai(prompt: str, model: str = "gpt-5-mini") -> str:
    response = await openai_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content

async def main():
    print("비동기 API 호출하기")
    prompt = "비동기 프로그래밍에 대해 두세 문장으로 설명해주세요."
    openai_response = await call_async_openai(prompt)
    print(f"OpenAI 응답: {openai_response}")

if __name__ == "__main__":
    asyncio.run(main())