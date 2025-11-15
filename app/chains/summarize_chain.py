from ..services import tools
from ..services import llm_service
from langchain_core.messages import HumanMessage, SystemMessage

def summarize_text(text: str) -> str:
    llm = llm_service.get_llm(temperature=0.5)
    prompt = f"Summarize the following text:\n\n{text}"
    response = llm.invoke([
        SystemMessage(content="You are a nutritionist with expertise in helping people achieve a health goal specific to their unique goal, right now you are summarizing a recipe for future use in meal planning"),
        HumanMessage(content=prompt)
    ])
    return response.content