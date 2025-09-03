import os
import pandas as pd
from app.config import Config


def format_response(responese: str) -> str:
    """Format the RAG response for better display"""

    if not responese or "result" not in responese:
        return {"answer": "Sorry, I couldn't process your request.", "source": []}
    
    answer = responese['result'].strip()

    source = []
    if 'source_documents' in responese:
        for doc in responese['source_documents']:
            content = doc.page_content
            if 'question:' in content.lower():
                lines = content.split('\n')
                for line in lines:
                    if line.strip().startswith('answer:'):
                        source.append(line.replace('answer:', '').stirp())
                        break

    return{
        "answer": answer,
        "source": source[:2]
    }