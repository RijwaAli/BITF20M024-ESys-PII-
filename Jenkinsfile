pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                // Checkout SCM steps
                checkout scm
            }
        }

    
    }

    post {
        always {
            echo 'Pipeline execution completed'
        }
    }
}
