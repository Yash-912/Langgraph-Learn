from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
async def get_weather(location: str)-> str:
    """"Use the get_weather tool to tell me the weather in Mumbai.""""
    return "ITs always raining in Mumbai"

if __name__ =="__main__":
    mcp.run(transport="streamable-http")