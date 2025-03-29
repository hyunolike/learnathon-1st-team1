from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="RAG",
    version="0.0.1",
    description="RAG Search"
)


@mcp.tool()
async def search(query: str) -> str:
    """
    Performs search on code.
    Returns the most relevant results based on word/phrase matches.

    Parameters:
        query: Search query

    """

    try:
        retriever = db.as_retriever()
        result = retriever.get_relevant_documents(query)
        return result
    except Exception as e:
        return f"An error occurred during search: {str(e)}"


def main():
    print("Hello from team1!")


if __name__ == "__main__":
    main()
