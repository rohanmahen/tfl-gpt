from journey import journey
from location import location


from langchain import PromptTemplate
from langchain.tools import BaseTool, Tool
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.agents import initialize_agent
from langchain.chains import LLMChain

import dotenv

dotenv.load_dotenv()


# Create a class to represent the TFL Tool
desc = (
    "A tool to find the fastest journey between two locations in London, England. "
    "Use this tool when you have specified an origin and a destination as parameters. "
    "To use the tool, you must provide the following parameters: ['origin', 'destination']."
    "Only use this tool in the most recent message if the two locations specified are in London, England."
)


class TFLTool(BaseTool):
    name = "TFL Tool"
    description = desc

    def _run(self, origin: str, destination: str) -> str:
        # get lat and lng from origin and destination in natural language
        origin_position = location(origin)
        destination_position = location(destination)

        # get journey information from origin to destination
        return journey(origin_position, destination_position)


# BUGGY FIX
from langchain.agents.conversational_chat.base import ConversationalChatAgent

ConversationalChatAgent._validate_tools = lambda *_, **__: ...

# Initialise LLM

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo", temperature=0  # text-davinci-003 is not a chat model!
)

memory = ConversationBufferWindowMemory(
    memory_key="chat_history",
    window=1,
    return_messages=True,
)


prompt = PromptTemplate(input_variables=["query"], template="{query}")

llm_chain = LLMChain(llm=llm, prompt=prompt)

llm_tool = Tool(
    name="Language Model",
    func=llm_chain.run,
    description="Useful for when you need to answer questions about anything.",
)

tools = [
    TFLTool(),
    llm_tool,
]

# initialise agent
agent = initialize_agent(
    llm=llm,
    memory=memory,
    agent="chat-conversational-react-description",
    tools=tools,
    verbose=True,
    max_iterations=3,
    early_stopping_method="generate",
)


# Test it out
while True:
    query = input("What journey are you planning?: ")
    if query == "exit":
        break
    res = agent(query)
    print(res["output"])
    print("\n")
