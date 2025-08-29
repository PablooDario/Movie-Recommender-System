# Personality-Based Movie Recommender System  

## Overview  
This project develops a movie recommendation system that integrates **user personality traits** into the recommendation process. Traditional recommender systems rely mainly on user interactions (ratings, clicks, watch history). However, **psychological research** shows that personality strongly influences individual preferences, including movie choices.  

By incorporating the **Big Five Personality Traits** *(Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism)*, this system aims to deliver more **personalized and accurate recommendations** than conventional methods.  

The project follows a complete **end-to-end ML pipeline**, including:  
1. **Data acquisition and integration**  
2. **Data cleaning and preprocessing**  
3. **Feature engineering**  
4. **Model development** (multiple approaches)  
5. **API and backend services**  
6. **Web frontend for user interaction**  
7. **Containerization and orchestration**  
8. **Deployment to the cloud**  
9. **Monitoring and logging**  
10. **Security and authentication**  

---

## Data Sources  
- **Primary dataset:** [MovieLens 32M](https://grouplens.org/datasets/movielens/32m/) (user ratings and interactions).  
- **Metadata enrichment:** TMDb API (movie title, release date, runtime, genres, cast, crew, etc.).  

A comprehensive **data cleaning and preprocessing pipeline** ensures reliable input for training and evaluating the recommendation models.  

---

## Recommendation Models  
The system integrates four different approaches:  

1. **Content-Based Filtering** – recommends movies similar to those the user liked, based on metadata.  
2. **Collaborative Filtering** – leverages user–user and item–item similarity to recommend movies.  
3. **Personality-Based Model** – aligns users’ Big Five profiles with genre preferences to infer recommendations.  
4. **Hybrid Model** – combines all methods to maximize performance and personalization.  

---

## Web Application  
The system includes a web platform for **user interaction**, providing:  
- Secure **user registration and login**.  
- **Personalized movie recommendations**.  
- Detailed **movie metadata browsing** (title, runtime, genres, cast, crew, etc.).  
- Ability to **rate movies** (1–5 scale).  
- **Watchlist management** for saving favorite movies.  
- **Search functionality** with direct rating options.  

---

## Containerization & Infrastructure  
The project is fully containerized with **Docker** for scalability and reproducibility.  

- **Docker Compose** orchestrates services, including:  
  - Backend API (**FastAPI**)  
  - Frontend (**Next.js**)  
  - Database (**PostgreSQL**)  
  - **MLflow** (model tracking and versioning)  
  - **MinIO** (S3-compatible object storage for datasets and models)  

This setup ensures portability and straightforward deployment across local and cloud environments.  

---

## Security  
Security measures include:  
- **Password hashing**   
- **Authentication:** JWT 
- **Transport security:** HTTPS with Nginx 
- **Role-based access control** (user/admin privileges)  

---

## Deployment Strategies  
- **Local development:** via Docker Compose (services: FastAPI, PostgreSQL, MLflow, MinIO)  
- **Cloud deployment options:**  
  - **Heroku** for a minimal MVP  
  - **ngrok** for local tunneling and testing  
  - Planned extensions to **AWS**  

---

## Monitoring & Logging  
- **Model monitoring:** MLflow (performance metrics, model drift detection)  
- **API monitoring:** Prometheus + Grafana  
- **Error tracking:** Sentry  

---

## Project Structure  

```plaintext
movie-recommender/
│
├── backend/          # FastAPI backend (API, auth, recommendation logic)
├── frontend/         # Next.js frontend (UI components and pages)
├── ml/               # ML models, training scripts, experiments
├── infra/            # Docker and deployment configurations
├── data/             # Raw and processed datasets (DVC-tracked)
├── docker-compose.yml
├── README.md
└── requirements.txt
```

### Roadmap
- Dataset integration (MovieLens + TMDb) ✅
- Data cleaning & preprocessing ✅
- Content-based model ✅
- Collaborative filtering model
- Personality-based model
- Hybrid model
- Backend API (FastAPI)
- Frontend (Next.js)
- Containerization with Docker
- Deployment to cloud (AWS/Heroku)
- Monitoring & logging setup