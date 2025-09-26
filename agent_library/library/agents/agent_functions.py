from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor
from .agent_models import BookRecommendations
from .tools import search_tool, image_search_tool

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

book_parser = PydanticOutputParser(pydantic_object=BookRecommendations)

chat_prompt = ChatPromptTemplate.from_messages(
    [(
        'system',
        '''
        You are a book recommendation agent. You will be provided with a genre.
        Provide a list of 6 book recommendations.
        Make sure all links you provide are valid and working.
        Wrap the output in the specified format and provide no extra text\n{format_instructions}
        '''
    ),
    (
        'placeholder', '{chat_history}'
    ),
    (
        'human', '{query}'
    ),
    (
        'placeholder','{agent_scratchpad}'
    )]
).partial(format_instructions=book_parser.get_format_instructions())

tools = [search_tool]

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=chat_prompt
)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose=True
)

# Function to get book recommendations based on a genre query
def get_llm_recommendation(query: str) -> dict:

    raw_response = agent_executor.invoke({'query': query})

    try:
        structured_response = book_parser.parse(raw_response['output']).model_dump()
        return structured_response
    except Exception as e:
        print("Error parsing response:", e)

# Function for summary
def stream_summary(title: str):
    prompt = PromptTemplate.from_template(
        "Provide a concise summary for the book titled '{title}'."
    )

    chain = prompt | llm

    for chunk in chain.stream({'title': title}):
        yield chunk.content if hasattr(chunk, "content") else str(chunk)
        
#print(get_llm_recommendation("science fiction"))