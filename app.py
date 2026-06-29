pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/sivanathrj260304-ux/vv.git'
            }
        }

        stage('Run Application') {
            steps {
                timeout(time: 10, unit: 'SECONDS') {
                    bat 'python app.py'
                }
            }
        }
    }

    post {
        success {
            echo 'Application started successfully!'
        }
        aborted {
            echo 'Application was stopped after 10 seconds.'
        }
    }
}
