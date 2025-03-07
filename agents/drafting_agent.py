from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import LlamaCpp

class DraftingAgent:
    def __init__(self, model_path):
        self.llm = LlamaCpp(model_path=model_path)

    def draft_response(self, research_data):
        # Limit the research data to fit within the context window
        max_tokens = 300  # Further reduce the token limit
        trimmed_data = research_data[:max_tokens]

        prompt = ChatPromptTemplate.from_template(
            "Summarize the following research data concisely:\n{research_data}"
        )
        chain = prompt | self.llm
        return chain.invoke({"research_data": trimmed_data})
