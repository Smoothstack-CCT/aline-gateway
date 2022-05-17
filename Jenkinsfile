pipeline {
    enviroment {
        registry = "laxwalrus/capstone-gateway"
        registryCredential = "laxwalrus"\
        dockerImage = ""
    }
    agent any

    tools {
        maven "MAVEN"
    }

    stages {
        stage('Build') {
            steps {
            bat "mvn -Dmaven.test.failure.ignore=true clean package"
            }

            steps{
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }

            }
        }

        stage("Deploy"){
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