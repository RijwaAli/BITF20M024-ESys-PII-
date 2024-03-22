pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the GitHub repository
                git branch: 'main', url: 'https://github.com/RijwaAli/BITF20M024-ESys-PII-.git'
            }
        }
        
        stage('Build') {
            steps {
                // Build your project (replace 'mvn clean install' with your actual build command)
                bat 'clean 
            }
        }
        
        stage('Test') {
            steps {
                // Run your tests (replace 'mvn test' with your actual test command)
                bat 'test'
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
