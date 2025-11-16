from ..services import llm_service
from langchain_core.messages import HumanMessage, SystemMessage

def optimize_criteria(current_criteria: str) -> str:
    llm = llm_service.get_llm(temperature=0.4)
    prompt = f"Current health goal criteria from unlicensed client: {current_criteria}\nOptimize the health goal criteria based on expert analysis. Help the inexperience client develop a clear and concise criteria."
    
    response = llm.invoke([
        SystemMessage(content="You are an expert nutritionist helping to refine health goal criteria based on your expertise and industry best practices. return only a sentence. a criteria string (this is being used programmatically)."),
        HumanMessage(content=prompt)
    ])
    return response.content