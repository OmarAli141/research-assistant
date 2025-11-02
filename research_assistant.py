from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import requests
from bs4 import BeautifulSoup
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

class ResearchAssistant:
    def __init__(self):
        """
        Initialize the research assistant with necessary components.
        """
        self.llm = ChatOllama(
            model="deepseek-r1:1.5b",
            temperature = 0.3,
            top_k = 40,
            top_p = 0.9,
            num_ctx = 2048,
        )
        print("Research assistant initialized")

    def search_web(self, query: str, num_results: int = 3) -> list:
        """
        Search the web for the given query using DuckDuckGo.
        Returns a list of URLs.
        """
        try:
            # Initialize the DuckDuckGo search API wrapper
            ddg_search = DuckDuckGoSearchAPIWrapper()

            # Perform search and limit the number of results to the specified number
            results = ddg_search.results(query, max_results=num_results) 

            # Extract the URLs
            urls = [r["link"] for r in results]
            print(f"Found {len(urls)} results: {urls}")
            return urls
        except Exception as e:
            print(f"Error searching the web: {e}")
            return []
        
    def scrape_text(self, url: str) -> str:
        """
        Scrape the text from the given URLs.
        Returns the text as a string.
        """
        try:
            response = requests.get(url)

            # check if the request was successful
            if response.status_code == 200:
                # Parse the content of the request
                soup = BeautifulSoup(response.text, "html.parser")
                # Extract all text from the webpage
                page_text = soup.get_text(separator=" ",strip=True)

                return page_text 
            else:
                return f"Failed to scrape the text from the URL: {url}" 

        except Exception as e:
            print(f"Error scraping the text from the URL: {e}")
            return ""

    def summarize_text(self, text_or_summaries, question: str = None) -> str:
        """
        Summarize the given text or list of summaries.
        Returns the summary as a string.
        """
        # Check if input is a list of summaries or a single text
        if isinstance(text_or_summaries, list):
            combined_summary = "\n\n".join(text_or_summaries)
        else:
            combined_summary = text_or_summaries
        
        prompt_template = """
        You are a research analyst.
        Based on the following summaries from multiple sources, write a comprehensive,
        factual, and well-structured report answering the question below.

        Question: {question}

        Summaries:
        {combined_summary}

        Write the final report in Markdown format (with sections, bullets, and sources if mentioned).
        """

        # Prepare the question text dynamically
        question_text = f"Question : {question}" if question else "No Specific Question Provided"

        # Build the prompt template
        prompt = ChatPromptTemplate.from_template(prompt_template)
        formatted_prompt = prompt.format(question=question_text, combined_summary=combined_summary)

        # Run through the LLM
        response = self.llm.invoke(formatted_prompt)

        return response.content.strip()

    def research_topic(self, question:str) -> str:
        """
        Research the given topic and answer the question.
        Returns the answer as a string.
        """
        urls = self.search_web(question)
        summaries = []
        for url in urls:
            text = self.scrape_text(url)
            summary = self.summarize_text(text,question)
            summaries.append(summary)

        final_report = self.summarize_text(summaries,question)
        return final_report

if __name__ == "__main__":
    print("=" * 60)
    print("🤖 Research Assistant - Interactive Mode")
    print("=" * 60)
    print("\nOptions:")
    print("1. Ask a research question")
    print("2. Exit")
    print("\n" + "-" * 60)
    
    assistant = ResearchAssistant()
    
    while True:
        try:
            choice = input("\nEnter your choice (1 or 2): ").strip()
            
            if choice == "1":
                print("\n" + "-" * 60)
                question = input("Enter your research question: ").strip()
                
                if not question:
                    print("❌ Please enter a valid question!")
                    continue
                
                print("\n🔍 Starting research...")
                print("⏳ This may take a moment...\n")
                
                try:
                    report = assistant.research_topic(question)
                    
                    print("\n" + "=" * 60)
                    print("📊 RESEARCH REPORT")
                    print("=" * 60)
                    print(report)
                    print("=" * 60)
                    
                except Exception as e:
                    print(f"\n❌ Error during research: {e}")
                    print("Make sure Ollama is running on localhost:11434")
                    
            elif choice == "2":
                print("\n👋 Thank you for using Research Assistant. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please enter 1 or 2.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")




