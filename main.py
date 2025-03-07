from config import CONFIG
from graphs.research_flow import run_research_workflow
import os

if __name__ == "__main__":
    query = input("Enter your search query: ")

    os.environ['TAVILY_API_KEY'] = "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"

    run_research_workflow(
        query=query,
        mistral_model_path="D:\\deep_research_ai\\models\\mistral-7b-instruct-v0.2.Q4_0.gguf"
    )
