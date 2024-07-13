pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    withEnv(["WORKSPACE_UNIX=$(cygpath -u \"${env.WORKSPACE}\")"]) {
                        bat """
                        docker build -t mlflow-demo:latest ${env.WORKSPACE_UNIX}
                        """
                    }
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    withEnv(["WORKSPACE_UNIX=$(cygpath -u \"${env.WORKSPACE}\")"]) {
                        bat """
                        docker inspect -f . mlflow-demo:latest
                        docker run -d -t -w ${env.WORKSPACE_UNIX} -v ${env.WORKSPACE_UNIX}:${env.WORKSPACE_UNIX} -v ${env.WORKSPACE_UNIX}@tmp:${env.WORKSPACE_UNIX}@tmp -e VAR1 -e VAR2 mlflow-demo:latest cmd.exe
                        """
                    }
                }
            }
        }
    }
}
