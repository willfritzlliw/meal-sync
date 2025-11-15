from fastapi import FastAPI
from .api import endpoints
from .config import settings
from .chains import summarize_chain

app = FastAPI()

app.include_router(endpoints.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/summarize")
async def root():
    text = summarize_chain.summarize_text(""" 
A hamburger, often known as a burger, consists of fillings—usually a patty of ground meat, typically beef—placed inside a sliced bun, sesame seed bun, or bread roll. The patties are often served with lettuce, tomato, onion, pickles, bacon, or chilis. The filling of the burger can be topped with condiments such as ketchup, mustard, mayonnaise, relish or a "special sauce", often a variation of Thousand Island dressing. A burger with the patty topped with cheese is called a cheeseburger.[1] Under some definitions, a hamburger is considered a sandwich.

Hamburgers are typically associated with fast-food restaurants and diners but are also sold at other restaurants, including high-end establishments. There are many international and regional variations of hamburgers. Some of the largest multinational fast-food chains feature burgers as one of their core products: McDonald's Big Mac and Burger King's Whopper have become global icons of American culture
""")
    return {"message": text}
