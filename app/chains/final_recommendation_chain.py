from ..services import llm_service
from langchain_core.messages import HumanMessage, SystemMessage
from .rate_choice_chain import MealRating

def final_recommendation(MealRating) -> str:
    llm = llm_service.get_llm(temperature=0.3)
    prompt = f"Based on the following meal rating: {MealRating}, provide a final recommendation for the client to improve their meal choices aligned with their health goals."
    
    response = llm.invoke([
        SystemMessage(content="You are an expert nutritionist providing final recommendations based on meal evaluations."),
        HumanMessage(content=prompt)
    ])
    return response.content