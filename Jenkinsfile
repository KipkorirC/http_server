pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: '1001', url: 'https://github.com/KipkorirC/http_server.git',  branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker-compose build'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // You can add tests here if needed
                    // For example, you might want to run a container and test it
                    sh 'docker-compose up -d'
                    sleep(5) // Wait for the server to start
                    // Test the server response
                    def response = sh(script: 'curl -s http://localhost:8081', returnStdout: true).trim()
                    if (response != 'Hello, World!') {
                        error "Unexpected response from server: ${response}"
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Deploy your application (e.g., push to a production server)
                    // This could involve pushing the image to a registry or deploying to a server
                    echo 'Deploying application...'
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
