pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t volleyball-site .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop volleyball-container || true
                docker rm volleyball-container || true

                docker run -d \
                --name volleyball-container \
                -p 5001:5001 \
                volleyball-site
                '''
            }
        }

    }
}
