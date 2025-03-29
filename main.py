from langchain.retrievers.ensemble import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="RAG",
    version="0.0.1",
    description="RAG Search"
)


@mcp.tool()
async def search(query: str, top_k: int = 5) -> str:
    """
    Performs hybrid search (keyword + semantic) on code.
    Combines exact keyword matching and semantic similarity to deliver optimal results.
    The most versatile search option for general questions or when unsure which search type is best.

    Parameters:
        query: Search query
        top_k: Number of results to return
    """

    try:
        bm25_retriever = BM25Retriever.from_documents(split_docs, top_k)
        dense_retriever = db.as_retriever(search_kwargs={"k": top_k})
        retriever = EnsembleRetriever(
            retrievers=[bm25_retriever, dense_retriever],
            weights=[0.5, 0.5]
        )
        result = retriever.get_relevant_documents(query)
        return result
    except Exception as e:
        return f"An error occurred during search: {str(e)}"


def main():
    print("Hello from team1!")


if __name__ == "__main__":
    main()
