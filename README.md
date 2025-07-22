# Atlanta Restaurant Recommender

## Abstract
In this work, I present RAGaurant, a retrieval-augmented generation (RAG) system that leverages the LLaMA 3 language model for personalized restaurant recommendation in Atlanta. My approach combines structured restaurant metadata (e.g., category, star ratings, review counts) with unstructured user google reviews to produce high-quality, context-aware suggestions in natural language. I first preprocess and normalize a real-world dataset of Atlanta restaurants, incorporating review sentiment and popularity metrics. This information is embedded and indexed using FAISS to support retrieval, which is integrated with LLaMA 3 via prompt engineering to form a conversational recommender. The system interprets user queries—such as preferences for cuisine type, rating thresholds, minimum review counts or distance from user—and dynamically generates top restaurant picks along with rationale. By uniting semantic search with generative capabilities, RAGaurant demonstrates the potential of modern LLMs in location-aware recommendation tasks. The experimental results demonstrate that retrieval-augmented prompting enables more personalized and context-aware restaurant suggestions than baseline keyword-based techniques.


## Data Sources
https://www.kaggle.com/datasets/grohith/atlanta-restaurant-reviews?select=dataset_Google-Maps-Reviews-Scraper_2023-10-07_22-26-46-127.xlsx


## Approach
Utilize open source Llama 3 and implement RAG and prompt engineering 

## References
