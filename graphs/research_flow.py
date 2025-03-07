from agents.research_agent import ResearchAgent
from agents.drafting_agent import DraftingAgent

def run_research_workflow(query, mistral_model_path):
    research_agent = ResearchAgent()
    drafting_agent = DraftingAgent(model_path=mistral_model_path)

    print(f"Searching for: {query}")
    research_data = research_agent.search(query)

    print("Drafting final response...")
    final_response = drafting_agent.draft_response(research_data)

    print("\nFinal Drafted Response:\n")
    print(final_response)
