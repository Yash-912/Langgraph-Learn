from langchain_mcp_adapters.client import MultiServerMCPClient
# from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathServer.py"],
                "transport": "stdio"
            },
            "weather":{
                "url": "http://127.0.0.1:8000/mcp",
                "transport": "streamable_http"
            }
        }
    
    ) 
    import os 
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tool = await client.get_tools()
    model = ChatGroq(model="llama-3.3-70b-versatile")
    agent = create_agent(
        model, tool
    )
    
    math_response = await agent.ainvoke(
        {"messages": [{"role":"user","content":"What is 3 multiplied by 15?"}]}
    )
    print("Ans ", math_response["messages"][-1].content)
    
    

    tools = await client.get_tools()
    
    
    
    response = await agent.ainvoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What's the weather in Mumbai?"
            }
        ]
    }
    )

    print(response["messages"][-1].content)

asyncio.run(main())