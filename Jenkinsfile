pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                // Checkout SCM steps
                checkout scm
            }
        }
        
        
        stage('Test') {
            steps {
                // Add your test steps here
                echo 'Running tests...'
                // You can add more steps such as running test commands, executing test scripts, etc.
                
            }
        }
        
        
    }

    post {
        always {
            echo 'Pipeline execution completed'
        }
    }
}
