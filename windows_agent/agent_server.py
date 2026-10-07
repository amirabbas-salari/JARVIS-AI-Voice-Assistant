import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from windows_use import Agent
from windows_use.providers import ChatOpenRouter


load_dotenv()


# ============================================================
# Configuration
# ============================================================

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "nvidia/nemotron-3-ultra-550b-a55b:free"


if not OPENROUTER_API_KEY:
    raise RuntimeError(
        "OPENROUTER_API_KEY is not set in .env"
    )


# ============================================================
# LLM
# ============================================================

llm = ChatOpenRouter(
    model=MODEL,
    api_key=OPENROUTER_API_KEY,
)


# ============================================================
# Windows Agent
# ============================================================

agent = Agent(
    llm=llm,
    mode="normal",
    max_steps=15,
    use_accessibility=True,
    use_vision=False,
    log_to_console=True,
)


# ============================================================
# FastAPI
# ============================================================

app = FastAPI(
    title="JARVIS Windows Agent",
    version="1.0.0",
)


# ============================================================
# Request / Response Models
# ============================================================

class TaskRequest(BaseModel):
    task: str


class TaskResponse(BaseModel):
    success: bool
    result: str | None = None
    error: str | None = None


# ============================================================
# Health Check
# ============================================================

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "jarvis-windows-agent",
    }


# ============================================================
# Execute Windows Task
# ============================================================

@app.post("/execute", response_model=TaskResponse)
def execute_task(request: TaskRequest):

    task = request.task.strip()

    if not task:
        return TaskResponse(
            success=False,
            error="Task cannot be empty.",
        )

    print("\n" + "=" * 60)
    print("WINDOWS AGENT REQUEST")
    print("=" * 60)
    print(f"Task: {task}")
    print("=" * 60)

    try:

        result = agent.invoke(task)

        if result is None:
            return TaskResponse(
                success=False,
                error="Agent returned no result.",
            )

        if result.error:
            return TaskResponse(
                success=False,
                result=result.content,
                error=result.error,
            )

        return TaskResponse(
            success=True,
            result=result.content,
        )

    except Exception as e:

        print("\n[ERROR]")
        print(str(e))

        return TaskResponse(
            success=False,
            error=str(e),
        )