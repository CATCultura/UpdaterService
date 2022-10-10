pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh 'python -m unittest test.test_DataCleaner.py'
            }
        }

        stage('Deploy') {

        }

    }
}