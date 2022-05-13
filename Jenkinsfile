pipeline {
    agent any

    tools {
        maven "MAVEN"
    }

    stages {
        stage('Build') {
            steps {
            bat "mvn clean package -DskipTests"
            }
        }
        stage('Archive') {
            steps {
            archiveArtifacts artifacts: 'target/*.jar', followSymlinks: false
            }

        }
           
        
    }
}