pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                // Clean the workspace
                bat 'mvn clean'
                
                // Compile and test the project
                bat 'mvn test'
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
