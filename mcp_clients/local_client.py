import asyncio
from fastmcp import Client, FastMCP
from dotenv import load_dotenv

PATH_LOCAL_MCP_SERVER = load_dotenv()

# Mcp client
client = Client(PATH_LOCAL_MCP_SERVER)

async def main():
    async with client:
        # Basic server interaction
        await client.ping()
        
        # List available operations
        tools = await client.list_tools()
        print(f"TOOLS: {tools}\n")
        
        resources = await client.list_resources()
        print(f"RESOURCES: {resources}\n")

        prompts = await client.list_prompts()
        print(f"PROMPTS: {prompts}\n")
        
        # Execute operations
        print("Calling  an mcp tool: Adding 1 + 1")
        result = await client.call_tool("add", {"a": 1, "b": 1})
        print(result)

asyncio.run(main())
