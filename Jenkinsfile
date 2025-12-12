pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = '8d591293-37db-4f75-add3-5f07cd5f94c3'
        DOCKER_IMAGE = 'kailashsubramaniyan/emc-capstone-project'
        EC2_IP = '54.94.224.148' // Replace with your EC2 public IP
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

        stage('Deploy to EC2') {
            steps {
                withCredentials([sshUserPrivateKey(
                    credentialsId: 'EC2_APP_DEPLOY_SSH_KEY', 
                    keyFileVariable: 'SSH_KEY', 
                    usernameVariable: 'EC2_USER'
                )]) {
                    sh """
                        echo "Deploying Docker container on EC2..."
                        ssh -i \$SSH_KEY -o StrictHostKeyChecking=no \$EC2_USER@\$EC2_IP '
                            # Stop existing container if running
                            docker stop emc-capstone || true
                            docker rm emc-capstone || true

                            # Pull latest image from Docker Hub
                            docker pull $DOCKER_IMAGE:latest

                            # Run container
                            docker run -d --name emc-capstone -p 5000:5000 $DOCKER_IMAGE:latest
                        '
                    """
                }
            }
        }

    }

    post {
        always {
            echo "Build, Push & Deploy Completed."
        }
    }
}
