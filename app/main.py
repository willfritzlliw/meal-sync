from fastapi import FastAPI
from .api import endpoints
from .config import settings
from .chains import summarize_chain, optimize_criteria_chain, rate_choice_chain, final_recommendation_chain
from pydantic import BaseModel, Field

app = FastAPI()

app.include_router(endpoints.router)

class HealthGoalRequest(BaseModel):
    goal: str = Field(description="General health goal")
    meal: str = Field(description="Description of the meal to be evaluated")

class MealRatingResponse(BaseModel):
    summarized_meal: str = Field(description="Summarized version of the meal")
    optimized_goal: str = Field(description="Optimized health goal criteria")
    rating: str = Field(description="Rating of the meal based on the health goal")

@app.post("/", response_model=MealRatingResponse)
async def rate_meal(request: HealthGoalRequest):
    """Evaluate a meal against a health goal with AI-powered analysis."""
    # Step 1: Summarize the meal
    summarized_meal = summarize_chain.summarize_text(request.meal)
    
    # Step 2: Optimize the health goal criteria
    optimized_goal = optimize_criteria_chain.optimize_criteria(request.goal)
    
    # Step 3: Rate the summarized meal based on optimized criteria
    mealRating = rate_choice_chain.rate_choice(summarized_meal, optimized_goal)
    rating = final_recommendation_chain.final_recommendation(mealRating)
    return MealRatingResponse(
        summarized_meal=summarized_meal,
        optimized_goal=optimized_goal,
        rating=rating
    )
