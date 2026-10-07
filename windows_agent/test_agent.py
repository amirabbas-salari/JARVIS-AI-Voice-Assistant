import os

from dotenv import load_dotenv

from windows_use import Agent
from windows_use.providers import ChatOpenRouter


load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError(
        "OPENROUTER_API_KEY is not set"
    )


MODEL = "nvidia/nemotron-3-ultra-550b-a55b:free"


llm = ChatOpenRouter(
    model=MODEL,
    api_key=api_key,
)


agent = Agent(
    llm=llm,
    mode="normal",
    max_steps=15,
    use_accessibility=True,
    use_vision=False,
)


print("=" * 60)
print("Windows-Use Test")
print("=" * 60)

task = "Open Google Chrome and search for NVIDIA"

print(f"\nTask: {task}\n")

result = agent.invoke(task)

print("\n" + "=" * 60)
print("RESULT")
print("=" * 60)

if result:
    print(result.content)

    if result.error:
        print("\nERROR:")
        print(result.error)
else:
    print("Agent returned no result.")