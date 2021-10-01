pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        sh '/usr/local/bin/python3 test.py'
      }
    }
  }
  stage('Example stage 2') {
     steps {
       echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
}
