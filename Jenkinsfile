pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the GitHub repository
                git 'https://github.com/RijwaAli/BITF20M024-ESys-PII-.git'
            }
        }
        
        stage('Build') {
            steps {
                // Build your project (replace 'mvn clean install' with your actual build command)
                sh 'mvn clean install'
            }
        }
        
        stage('Test') {
            steps {
                // Run your tests (replace 'mvn test' with your actual test command)
                sh 'mvn test'
            }
        }
        
        stage('Deploy') {
            steps {
                // Deploy your application (replace this with your actual deployment steps)
                sh 'echo "Deploying the application"'
            }
        }
    }
    
    post {
        always {
            // Clean up or perform any other necessary actions after the pipeline execution
            echo 'Pipeline execution completed'
        }
        
        success {
            // Actions to perform when the pipeline succeeds
            echo 'Pipeline succeeded!'
        }
        
        failure {
            // Actions to perform when the pipeline fails
            echo 'Pipeline failed!'
        }
    }
}
