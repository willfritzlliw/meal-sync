from ..services import tools
from ..services import llm_service
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage, SystemMessage

class MealRating(BaseModel):
    score: int = Field(description="Rating score from 1 to 10")
    reasoning: str = Field(description="Explanation for the given score")
    health_impact: str = Field(description="Description of how the meal impacts health goals")
    recommendations: str = Field(description="Suggestions for improvement or alternatives")

def rate_choice(meal: str, criteria: str) -> MealRating:
    llm = llm_service.get_llm(temperature=0.3)
    structured_llm = llm.with_structured_output(MealRating)

    prompt = f"Given the following meal: {meal}, rate the meal based on the following health goal criteria: {criteria}."
    
    response = structured_llm.invoke([
        SystemMessage(content="You are an expert nutritionist evaluating meals."),
        HumanMessage(content=prompt)
    ])
    return response  # returns MealRating instance