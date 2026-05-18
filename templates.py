# templates.py

import os

folders = [

    # Root App
    "app",

    # API
    "app/api",
    "app/api/routes",

    # Core
    "app/core",

    # Database
    "app/database",

    # Middleware
    "app/middleware",

    # Models
    "app/models",

    # Schemas
    "app/schemas",

    # Services
    "app/services",

    # RAG Services
    "app/services/rag",

    # LLM Services
    "app/services/llm",

    # Embedding Services
    "app/services/embeddings",

    # Agents
    "app/services/agents",

    # Streaming
    "app/services/streaming",

    # Utils
    "app/utils",

    # Websocket
    "app/websocket",

    # AI Models
    "ai_models",
    "ai_models/llm",
    "ai_models/llm/llama3",

    "ai_models/embeddings",
    "ai_models/embeddings/bge-small-en-v1.5",

    "ai_models/reranker",
    "ai_models/reranker/bge-reranker-base",

    # Data
    "data",
    "data/raw_documents",
    "data/processed_documents",
    "data/embeddings",
    "data/faiss_index",
    "data/chat_history",

    # Scripts
    "scripts",

    # Tests
    "tests",

    # Deployment
    "deployment",
]

files = [

    # Main Files
    ".env",
    "README.md",
    "requirements.txt",
    "run.py",

    # App Files
    "app/main.py",

    # API Files
    "app/api/api_router.py",

    "app/api/routes/auth_routes.py",
    "app/api/routes/chat_routes.py",
    "app/api/routes/upload_routes.py",
    "app/api/routes/admin_routes.py",
    "app/api/routes/analytics_routes.py",

    # Core Files
    "app/core/config.py",
    "app/core/security.py",
    "app/core/logger.py",
    "app/core/constants.py",
    "app/core/dependencies.py",

    # Database Files
    "app/database/mysql_db.py",
    "app/database/mongodb.py",
    "app/database/redis_cache.py",
    "app/database/faiss_db.py",

    # Middleware Files
    "app/middleware/auth_middleware.py",
    "app/middleware/logging_middleware.py",
    "app/middleware/rate_limit.py",

    # Model Files
    "app/models/user_model.py",
    "app/models/chat_model.py",
    "app/models/document_model.py",
    "app/models/feedback_model.py",

    # Schema Files
    "app/schemas/auth_schema.py",
    "app/schemas/chat_schema.py",
    "app/schemas/upload_schema.py",
    "app/schemas/response_schema.py",

    # RAG Service Files
    "app/services/rag/retriever.py",
    "app/services/rag/hybrid_search.py",
    "app/services/rag/reranker.py",
    "app/services/rag/query_rewriter.py",
    "app/services/rag/citation_generator.py",
    "app/services/rag/memory_manager.py",
    "app/services/rag/response_generator.py",
    "app/services/rag/rag_pipeline.py",

    # LLM Files
    "app/services/llm/huggingface_service.py",
    "app/services/llm/model_loader.py",
    "app/services/llm/prompt_templates.py",

    # Embedding Files
    "app/services/embeddings/embedding_model.py",
    "app/services/embeddings/embedding_generator.py",
    "app/services/embeddings/embedding_cache.py",

    # Agent Files
    "app/services/agents/retrieval_agent.py",
    "app/services/agents/reasoning_agent.py",
    "app/services/agents/validation_agent.py",
    "app/services/agents/routing_agent.py",
    "app/services/agents/agent_workflow.py",

    # Streaming Files
    "app/services/streaming/websocket_manager.py",
    "app/services/streaming/stream_response.py",

    # Utils Files
    "app/utils/pdf_loader.py",
    "app/utils/docx_loader.py",
    "app/utils/excel_loader.py",
    "app/utils/text_cleaner.py",
    "app/utils/chunking.py",
    "app/utils/tokenizer.py",
    "app/utils/helpers.py",

    # WebSocket File
    "app/websocket/chat_socket.py",

    # Scripts
    "scripts/ingest_documents.py",
    "scripts/generate_embeddings.py",
    "scripts/create_faiss_index.py",
    "scripts/backup_database.py",

    # Tests
    "tests/test_rag.py",
    "tests/test_api.py",
    "tests/test_embeddings.py",
    "tests/test_agents.py",

    # Deployment
    "deployment/Dockerfile",
    "deployment/docker-compose.yml",
    "deployment/nginx.conf",
]


def create_project_structure():

    print("\nCreating Project Structure...\n")

    # Create Folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created Folder: {folder}")

    # Create Files
    for file in files:

        with open(file, "w") as f:
            pass

        print(f"Created File: {file}")

    print("\nProject Structure Created Successfully!")


if __name__ == "__main__":
    create_project_structure()