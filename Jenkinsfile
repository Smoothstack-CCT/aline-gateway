pipeline {
    environment {
        registry = "laxwalrus/capstone-gateway"
        registryCredential = "laxwalrus"\
        dockerImage = ""
    }
    agent any

    tools {
        maven "MAVEN"
    }

    stages {
        stage("Build MVN") {
            steps {
                bat "mvn -Dmaven.test.failure.ignore=true clean package"
            }
        }


        stage("Build Docker"){
            steps{
                script {
                    dockerImage = docker.Build registry + ":$BUILD_NUMBER"
                }

            }            
        }

        stage("Deploy Docker"){
            steps{
                script{
                    docker.withRegistry("",registryCredential){
                        dockerImage.push()
                    }
                }
            }
        }

        stage("Cleaning"){
            steps{
                bat "docker rmi $registry:$BUILD_NUMBER"
            }
        }
        
        stage('Archive') {
            steps {
            archiveArtifacts artifacts: 'target/*.jar', followSymlinks: false
            }

        }
    }
}