# Meal Sync

## Overview

Meal Sync is an intelligent agent designed to help you stay on track with your health goals. It analyzes your meals and provides a score based on how well they align with your personalized health objectives. Simply describe your meal, and Meal Sync will tell you if it's in sync with your diet!

This project uses a combination of FastAPI for the web server and LangChain to create the agentic AI that powers the meal scoring.

## Features

*   **Personalized Health Goals:** Input and save your unique health goals.
*   **Meal Analysis:** Submit a descriptive text of your meal for analysis.
*   **Sync Score:** Receive a score indicating how well your meal aligns with your goals.
*   **Agentic AI:** Powered by LangChain to provide intelligent and contextual scoring.
*   **FastAPI Backend:** A robust and fast API to handle requests.

## Tech Stack

*   **Backend:** FastAPI
*   **AI/LLM Orchestration:** LangChain
*   **Configuration:** Pydantic, python-dotenv
*   **Web Server:** Uvicorn

## Getting Started

### Prerequisites

*   Python 3.9+
*   An OpenAI API key (or other LLM provider key)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd meal-sync
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your environment variables:**
    Create a `.env` file in the root of the project and add your API keys and other configuration:
    ```
    OPENAI_API_KEY="your-openai-api-key"
    ```

### Running the Application

To start the FastAPI server, run the following command from the root of the project:

```bash
python main.py
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

The following are the main API endpoints for Meal Sync:

*   `GET /`: A simple endpoint to check if the server is running.
*   `GET /hello`: An example endpoint from the API router.
