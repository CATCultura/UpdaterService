pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh 'python3 -m unittest test.test_DataCleaner'
            }
        }

        stage('Deploy') {
            steps {
                sh "echo a"
            }
        }

        stage('Notify') {
            steps {
                discordSend description: "Jenkins Pipeline Build", footer: "Results from a build", link: env.BUILD_URL, result: currentBuild.currentResult, title: JOB_NAME, webhookURL: "https://discord.com/api/webhooks/1029023402079572108/PSi21wQLj8EdmwAYw6DbyEsGuppRKibwV7r81QVq743lG5Z3_qZw2vNIr5jJ_sU_15RZ"
            }
        }

    }
}