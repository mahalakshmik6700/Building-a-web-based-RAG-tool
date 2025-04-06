# Building-a-web-based-RAG-tool
# Web-Based RAG Tool for Product Catalog QA

This project is a *Retrieval-Augmented Generation (RAG)* tool that allows users to ask questions about a product catalog. It fetches the catalog from a GitHub repository, encodes it using sentence embeddings, indexes it with FAISS, and serves semantic answers via a FastAPI backend and React-based frontend.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Tech Stack](#tech-stack)
- [Setup Guide](#setup-guide)
- [GitHub Integration](#github-integration)
- [Docker Setup](#docker-setup)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Extending the Tool](#extending-the-tool)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Overview

This tool is built for teams who want to provide AI-powered search and Q&A over their product catalog, using semantic similarity rather than just keyword search.

Imagine asking:

> "Which products are suitable for outdoor use?"  
> "What are the specs of our latest wireless router?"

And instantly getting a precise answer extracted from your structured catalog.

---

## Key Features

- *Live GitHub Data*: Loads product data directly from your GitHub repository.
- *Semantic Embeddings*: Uses sentence-transformers for accurate text understanding.
- *FAISS Vector Search*: Fast and scalable similarity search engine.
- *Modular FastAPI Backend*: Clean and production-ready.
- *Modern React Frontend*: Simple and intuitive UI.
- *Dockerized*: Full support for containerized development and deployment.
- *Open Source Friendly*: Easy to extend and self-host.

---

## System Architecture
