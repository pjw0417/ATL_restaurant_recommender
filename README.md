# RAGaurant: A RAG-Powered LLM for Personalized Restaurant Recommendation in Atlanta

## Abstract
In this work, I present RAGaurant, a retrieval-augmented generation (RAG) system that leverages the LLaMA 3 language model for personalized restaurant recommendation in Atlanta. My approach combines structured restaurant metadata (e.g., category, star ratings, review counts) with unstructured user google reviews to produce high-quality, context-aware suggestions in natural language. 
I first preprocess and normalize a real-world dataset of Atlanta restaurants, incorporating review sentiment and popularity metrics. This information is embedded and indexed using FAISS to support retrieval, which is integrated with LLaMA 3 via prompt engineering to form a conversational recommender. The system interprets user queries—such as preferences for cuisine type, rating thresholds, minimum review counts or distance from user—and dynamically generates top restaurant picks along with rationale. 
By uniting semantic search with generative capabilities, RAGaurant demonstrates the potential of modern LLMs in location-aware recommendation tasks. The experimental results demonstrate that retrieval-augmented prompting enables more personalized and context-aware restaurant suggestions than baseline keyword-based techniques.


## Data Sources
https://www.kaggle.com/datasets/grohith/atlanta-restaurant-reviews?select=dataset_Google-Maps-Reviews-Scraper_2023-10-07_22-26-46-127.xlsx


## Approach
Utilize open source Llama 3 and implement RAG and prompt engineering 

## References
[1] Hai-Dang Kieu, Minh Duc Nguyen, Thanh-Son Nguyen, and Dung D. Le. Keyword-driven retrieval-augmented large language models for cold-start user recommendations. arXiv preprint arXiv:2405.19612, 2024. 

[2] Ali Rostami. An integrated framework for contextual personalized LLM-based food recommendation. arXiv preprint arXiv:2504.20092, 2025.

[3] Ali Rostami, Ramesh Jain, and Amir M. Rahmani. Food recommendation as language processing (F-RLP): A personalized and contextual paradigm. arXiv preprint arXiv:2402.07477, 2024. 

[4] Vahid Azizi and Fatemeh Koochaki. LlamaRec-LKG-RAG: A single-pass, learnable knowledge graph-RAG framework for LLM-based ranking. arXiv preprint arXiv:2506.07449, 2025. 

[5] Sadhana D. End-to-end RAG based restaurant recommendation system with LLM, Elasticsearch, LlamaIndex. Medium, January 2025. https://medium.com/@sadhansd02/end-to-end-rag-based-restaurant-recommendation-system-with-llm-elasticsearch-llamaindex-2a73ad1d3aed. 

[6] Nouamane El Gueddari. Building a RAG-based restaurant recommendation system with LLMs and LangChain — Part 1. Medium, November 2024. https://medium.com/@ElGueddari/building-a-rag-based-restaurant-recommendation-system-with-llms-and-langchain-part-1-1e88e860f874. 
