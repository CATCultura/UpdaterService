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
                sh 'sudo docker kill $(sudo docker ps -q -f ancestor=dataset-retrieval-service)'
                sh 'sudo docker rmi dataset-retrieval-service -f'
                sh 'sudo docker build -t dataset-retrieval-service .'
                sh 'sudo docker run -d -p 50001:5001 dataset-retrieval-service'
            }
        }

      //  stage('Notify') {
          //  steps {
           //    discordSend description: "Jenkins Pipeline Build", footer: "Results from a build", link: env.BUILD_URL, result: currentBuild.currentResult, title: JOB_NAME, webhookURL: "https://discord.com/api/webhooks/1029023402079572108/PSi21wQLj8EdmwAYw6DbyEsGuppRKibwV7r81QVq743lG5Z3_qZw2vNIr5jJ_sU_15RZ"
           // }
        //}

    }
}