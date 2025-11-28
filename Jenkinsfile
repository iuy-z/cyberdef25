pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'irum90'
        DOCKERHUB_REPO = 'cyberdef25'
        IMAGE_TAG      = 'latest'
        IMAGE_NAME     = "${DOCKERHUB_USER}/${DOCKERHUB_REPO}:${IMAGE_TAG}"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker image ${IMAGE_NAME}..."
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Login to Docker Hub') {
            steps {
                // Using Jenkins credentials with ID 'dockerhub_creds'
                echo "Logging in to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: 'dockerhub_creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing Docker image to Docker Hub..."
                sh "docker push ${IMAGE_NAME}"
            }
        }

        stage('Run Container with Docker Compose') {
            steps {
                echo "Running container using docker-compose..."
                sh '''
                    docker-compose down || true
                    docker-compose up --build -d
                '''
            }
        }
    }

    post {
        always {
            echo "Jenkins pipeline finished successfully."
        }
    }
}
