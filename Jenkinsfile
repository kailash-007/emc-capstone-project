pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = '8d591293-37db-4f75-add3-5f07cd5f94c3'
        DOCKER_IMAGE = 'kailashsubramaniyan/emc-capstone-project'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    echo "Building Docker image..."
                    docker build -t $DOCKER_IMAGE:latest .
                '''
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                        credentialsId: DOCKER_HUB_CREDENTIALS,
                        usernameVariable: 'USERNAME',
                        passwordVariable: 'PASSWORD'
                )]) {
                    sh '''
                        echo "Logging in to Docker Hub..."
                        echo "$PASSWORD" | docker login -u "$USERNAME" --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                    echo "Pushing Docker image..."
                    docker push $DOCKER_IMAGE:latest
                '''
            }
        }
    }

    post {
        always {
            echo "Build & Push Completed."
        }
    }
}
