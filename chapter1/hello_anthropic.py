import anthropic
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

conversation = []

conversation.append({"role": "user", "content": "안녕 나는 시현이야."})

response = client.messages.create(
    model = "claude-3-5-haiku-latest",
    max_tokens=1000,
    messages=conversation
)

assistant_message = response.content[0].text
print(assistant_message)
conversation.append({"role": "assistant", "content": assistant_message})

conversation.append({"role": "user", "content": "내 이름이 뭐라고?"})

response = client.messages.create(
    model="claude-3-5-haiku-latest",
    max_tokens=1000,
    messages=conversation
)

print(response.content[0].text)