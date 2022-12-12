pipeline {
    agent any

    stages {

        stage('Analysis') {
            steps {
                sh '/home/alumne/sonar-scanner-4.7.0.2747-linux/bin/sonar-scanner -Dsonar.projectKey=dataset-service -Dsonar.sources=. -Dsonar.host.url=http://10.4.41.41:9000 -Dsonar.login=sqp_aacc9e519af128ac5e8b592d316ffeda5e440450'
            }

        }


        stage('Test') {
            steps {
                sh 'python3 -m unittest test.test_DataCleaner'
            }
        }

        stage('Deploy') {
        when {branch 'dev-service'}
            steps {
                sh 'sudo docker kill $(sudo docker ps -q -f ancestor=dataset-retrieval-service)'
                sh 'sudo docker rmi dataset-retrieval-service -f'
                sh 'sudo docker build -t dataset-retrieval-service .'
                sh 'sudo docker run -d -p 5001:5001 -v dataset-json-repo:/py-service/data dataset-retrieval-service'
            }
        }

       stage('Notify') {
           steps {
              discordSend description: "Jenkins Pipeline Build", footer: "Results from a build", link: env.BUILD_URL, result: currentBuild.currentResult, title: JOB_NAME, webhookURL: "https://discord.com/api/webhooks/1029023402079572108/PSi21wQLj8EdmwAYw6DbyEsGuppRKibwV7r81QVq743lG5Z3_qZw2vNIr5jJ_sU_15RZ"
           }
        }

    }
}