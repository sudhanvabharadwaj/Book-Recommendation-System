# Book-Recommendation-System

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