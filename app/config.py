import os

class Config:
    # Model settings
    MODEL_NAME = "microsoft/phi-3-mini-4k-instruct"
    EMBEDDING_MODEL = "all-MiniLM-L6-v2"

    # Paths
    DATA_PATH = os.path.join("data", "bank_customer_service_faq.csv")
    CHORMA_DB_PATH = "chroma_db"

    # LLM settings
    MAX_NEW_TOKENS = 300
    TEMPERATURE = 0.7

    # Text splitting setting
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 0

    # Flask settings
    FLASK_HOST = "0.0.0.0"
    FLASK_PORT = 5000
    FLASK_DEBUG = False