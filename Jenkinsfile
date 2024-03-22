pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                // Checkout SCM steps
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Use Maven tool configured in Jenkins
                withMaven(maven: 'MAVEN_HOME') {
                    // Run Maven commands
                    bat "mvn clean"
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed'
        }
    }
}
