# Bank-Customer-Service-RAG
# 🏦 Banking Customer Service Assistant  
*An AI-Powered Retrieval-Augmented Generation System for Financial Institutions*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![LangChain](https://img.shields.io/badge/LangChain-0.1.16-orange)](https://python.langchain.com)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-purple)](https://huggingface.co)

---

## 🚀 Overview

The **Banking Customer Service Assistant** is an enterprise-grade AI solution that leverages Retrieval-Augmented Generation (RAG) technology to provide accurate, context-aware responses to banking customer inquiries. Built with modern AI frameworks, this system combines the power of large language models with domain-specific knowledge to deliver reliable customer support.

This solution addresses key challenges in financial services:
- **24/7 customer support** with consistent quality
- **Reduced operational costs** through automation
- **Improved response accuracy** with verified knowledge sources
- **Seamless integration** with existing banking infrastructure

---

## 🌟 Key Features

### ✅ Intelligent Q&A System
- Context-aware responses using Retrieval-Augmented Generation
- Confidence-based answer validation
- Source attribution for transparency

### 🖥️ User Experience
- Responsive web interface for customer interactions
- Pre-configured example questions for quick onboarding
- Real-time system status monitoring
- Mobile-friendly design

### ⚙️ Technical Architecture
- **Modular design** for easy maintenance and scaling
- **API-first approach** for integration with existing systems
- **Configuration management** for environment-specific settings
- **Error handling** and logging for production reliability

### 🔐 Banking-Specific Capabilities
- Domain-specific knowledge base for financial services
- Compliance-ready response patterns
- Secure architecture with no persistent data storage
- Support for common banking scenarios (account management, card services, transactions, security)

---

## 🛠️ Technology Stack

| Component | Technology |
|---------|------------|
| **Framework** | LangChain, Flask |
| **LLM** | Microsoft Phi-3 Mini 4K Instruct |
| **Embeddings** | all-MiniLM-L6-v2 |
| **Vector Database** | Chroma |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Deployment** | Docker |

---

## 📦 Installation & Setup  

### Prerequisites
- Python 3.9 or higher
- 8GB+ RAM recommended
- 10GB+ free disk space for model downloads
- Internet connection for initial setup

### Quick Start
```bash
# Clone the repository
git clone https://github.com/Eidos110/banking-customer-service.git
cd banking-customer-service

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the application
python run.py

