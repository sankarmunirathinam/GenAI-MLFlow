pipeline {
    agent any
    environment {
        DOCKER_WORKDIR = "C:/ProgramData/Jenkins/.jenkins/workspace/MLFlow/"
    }
    stages {
        stage('Checkout SCM') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/sankarmunirathinam/GenAI-MLFlow.git']]])
            }
        }
        stage('Build') {
            steps {
                script {
                    // Convert Windows path to Unix-style path for Docker
                    def dockerWorkdir = "${DOCKER_WORKDIR}".replaceAll('\\\\', '/').replaceAll('C:', '/c')
                    withEnv(["DOCKER_WORKDIR=${dockerWorkdir}"]) {
                        bat "docker build -t mlflow-demo:latest ."
<<<<<<< HEAD
=======
                    }
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    // Convert Windows path to Unix-style path for Docker
                    def dockerWorkdir = "${DOCKER_WORKDIR}".replaceAll('\\\\', '/').replaceAll('C:', '/c')
                    withEnv(["DOCKER_WORKDIR=${dockerWorkdir}"]) {
                        docker.image('mlflow-demo:latest').inside {
                            bat "cmd.exe /c 'echo Hello from inside the container'"
                        }
>>>>>>> ba4cbfd5c9ac06894d35fd858565ed0e166f5a60
                    }
                }
            }
        }
        // stage('Run') {
        //     steps {
        //         script {
        //             // Convert Windows path to Unix-style path for Docker
        //             def dockerWorkdir = "${DOCKER_WORKDIR}".replaceAll('\\\\', '/').replaceAll('C:', '/c')
        //             withEnv(["DOCKER_WORKDIR=${dockerWorkdir}"]) {
        //                 docker.image('mlflow-demo:latest').inside {
        //                     bat "cmd.exe /c 'echo Hello from inside the container'"
        //                 }
        //             }
        //         }
        //     }
        // }
    }
}
