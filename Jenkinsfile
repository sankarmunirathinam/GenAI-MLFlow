pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    docker.build('mlflow-demo:latest')
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    docker.image('mlflow-demo:latest').inside {
                        sh 'python mlflow_demo.py'
                    }
                }
            }
        }
    }
}
