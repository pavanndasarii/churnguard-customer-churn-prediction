# SwiftBasket – AI-Powered Customer Support Assistant

## Overview

SwiftBasket is a fictional quick-commerce company created for this demonstration project.

This project is a policy-based customer support assistant that retrieves relevant information from a collection of eight sample policy documents using semantic search.

It uses ChromaDB for document retrieval, LangGraph for workflow orchestration, and FastAPI to expose a REST API.

## Features

- Semantic search over customer support policy documents
- ChromaDB vector database
- LangGraph retrieval workflow
- FastAPI REST API
- Structured JSON responses with source document IDs
- Docker containerization

## Technology Stack

- Python
- ChromaDB
- LangGraph
- FastAPI
- Pydantic
- Docker

## Project Structure

support_assistant/
- docs/                  # Eight sample policy documents
- chroma_db/             # Persistent ChromaDB database
- main.py                # FastAPI application
- requirements.txt       # Python dependencies
- Dockerfile             # Docker configuration
- README.md

## Workflow

1. Eight sample SwiftBasket policy documents are stored in the docs folder.
2. Documents are indexed in ChromaDB using its embedding functionality.
3. A customer submits a question through the FastAPI endpoint.
4. LangGraph executes the policy retrieval workflow.
5. ChromaDB retrieves the most relevant policy document.
6. The API returns the retrieved policy text and its source document ID.

Note: This implementation performs semantic retrieval and returns the retrieved policy text. It does not use an external LLM to generate responses.

## API Usage

Endpoint:

POST /ask

Request:

{
  "query": "How long does delivery take?"
}

Response:

{
  "answer": "Retrieved delivery policy text...",
  "sources": ["doc_01"]
}

## Run Locally

Install dependencies:

pip install -r requirements.txt

Start the API:

uvicorn main:app --reload

API documentation:

http://localhost:7860/docs

## Run with Docker

Build the image:

docker build -t swiftbasket-support .

Run the container:

docker run -d --name swiftbasket-api -p 7860:7860 swiftbasket-support

The API will be available at:

http://localhost:7860

## Project Scope

This is an educational demonstration using fictional company policies and sample data. It is not affiliated with any real quick-commerce company.
