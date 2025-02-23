pipeline {
    agent { 
        node {
            label 'jenkins-worker-1'
            }
      }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip3.12 install -r requires
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                echo "doing testing stuff.."
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo "Deliver.."
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
