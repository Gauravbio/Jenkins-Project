pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/your-username/your-flask-app.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                sh './$VENV_DIR/bin/pip install --upgrade pip'
                sh './$VENV_DIR/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './$VENV_DIR/bin/python -m unittest discover tests'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'nohup ./$VENV_DIR/bin/python app.py &'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
        }
    }
}
