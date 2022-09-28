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
                    sh 'ls'
                }
            }
            stage('Verify The Steps') {
                steps{
                    sh 'cat Jenkinsfile'
                }
            }
            
            stage('Build Docker Image') {
                steps{
                    sh "docker build -t fastapi:v1 ."
                }
            }
            stage('Run Docker Image And Expose API'){
                steps {
                sh "docker run --name fastapiapp23 fastapi:v1"
                }
            }
            stage("Testing Application"){
                steps {
                    sh 'curl http://localhost:8080/'



               }
            }
        }
}
