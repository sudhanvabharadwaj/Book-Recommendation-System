# Book-Recommendation-System

ReadMind is a collaborative filtering-based Book Recommendation System built with Python and Streamlit. It leverages user ratings and book metadata to suggest books tailored to your interests. The system uses machine learning techniques to analyze user preferences and recommend similar books, providing an engaging and personalized reading experience.

## Features
📚 Personalized Book Recommendations: Get book suggestions based on your favorite titles.
🔍 Collaborative Filtering: Utilizes user ratings to find books you’ll love.
🖼️ Book Cover Display: See book covers alongside recommendations for a visually rich experience.
⚡ Interactive Web App: Built with Streamlit for a fast, modern, and responsive UI.
🛠️ Retrainable Model: Easily retrain the recommendation engine with new data using the web interface.
🐳 Docker Support: Ready-to-deploy with Docker for seamless cloud or local deployment.

## How It Works
Data Ingestion: Loads and processes book ratings and metadata.
Model Training: Uses collaborative filtering (KNN) to learn user-book relationships.
Recommendation: Given a selected book, the system finds and displays similar books with their covers.
Retraining: The model can be retrained from the UI to incorporate new data.

## Tech Stack
Python 3.7+
Streamlit (Web UI)
NumPy, Pandas, Scikit-learn (Data processing & ML)
Pickle (Model serialization)
Docker (Deployment)

## How to run?
### Steps:

Clone the repository

```bash
git clone https://github.com/sudhanvabharadwaj/Book-Recommendation-System.git
```

#### Step 1 - Create a Conda environment after opening the repository

```bash
conda create -n books python=3.7.10 -y
```

```bash
conda activate books
```

#### Step 2 - Install the requirements

```bash
pip install -r requirements.txt
```

#### Step 3 - Run the application

```bash
streamlit run app.py
```


# Streamlit app Docker Image Deployment

## 1. Login with your AWS console and launch an EC2 instance
## 2. Run the following commands

Note: Do the port mapping to this port:- 8501

```bash
sudo apt-get update -y

sudo apt-get upgrade

#Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

To clone the repository from your GitHub:

```bash
git clone "your-project"
```

Build the Docker Image:

```bash
docker build -t "username"/bookapp:latest . 
```

```bash
docker images -a  
```

To run your application on the EC2 Instance:

```bash
docker run -d -p 8501:8501 "username"/bookapp
```

```bash
docker ps  
```

To stop your container:

```bash
docker stop container_id
```

To delete your container:

```bash
docker rm $(docker ps -a -q)
```

To push your image on Docker Hub:

```bash
docker login 
```

```bash
docker push "username"/bookapp:latest 
```

To delete the image from your machine:

```bash
docker rmi "username"/bookapp:latest
```

To pull the image from your Docker Hub:

```bash
docker pull "username"/bookapp
```