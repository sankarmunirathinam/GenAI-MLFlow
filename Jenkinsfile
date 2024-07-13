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
                    // Convert Windows path to Unix path using sh command
                    def workspaceUnix = bat(script: 'cygpath -u "${WORKSPACE}"', returnStdout: true).trim()
                    withEnv(["WORKSPACE_UNIX=${workspaceUnix}"]) {
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
                    // Use the converted path for Docker run command
                    def workspaceUnix = bat(script: 'cygpath -u "${WORKSPACE}"', returnStdout: true).trim()
                    withEnv(["WORKSPACE_UNIX=${workspaceUnix}"]) {
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
