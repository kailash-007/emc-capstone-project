pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    echo "Creating Python virtual environment..."
                    python3 -m venv venv

                    echo "Activating venv..."
                    . venv/bin/activate

                    echo "Upgrading pip..."
                    pip install --upgrade pip

                    echo "Installing dependencies..."
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    else
                        echo "No requirements.txt found, skipping"
                    fi
                '''
            }
        }

        stage('Run Application Test') {
            steps {
                sh '''
                    echo "Running Python App..."

                    . venv/bin/activate
                    python3 main.py || true

                    echo "Python test run complete."
                '''
            }
        }
    }

    post {
        always {
            echo "Build Finished."
        }
    }
}
