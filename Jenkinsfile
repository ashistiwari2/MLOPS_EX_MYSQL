pipeline {
    agent any
        stages {



           stage('Clone Source Repository') {
                /* Cloning the repository for web application */
                steps {
                    checkout scm
                }
            }
        stage('Verify The Clone') {
                steps{
                    bat 'dir'
                }
            }
            stage('Verify The Steps') {
                steps{
                    bat 'type Jenkinsfile'
                }
            }
            
            stage('Build Docker Image') {
                steps{
                    bat "docker build -t fastapi:v1 ."
                }
            }
            stage('Run Docker Image And Expose API'){
                steps {
                bat "docker run -d -p 8087:8008 --name fastapiapp fastapi:v1"
                }
            }
            stage("Testing Application"){
                steps {
                   echo "Run it at localhost:8007"



               }
            }
        }
}
