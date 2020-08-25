pipeline {
  environment {
    registry = "docker_hub_account/repository_name"
  }
  agent {
    kubernetes {
      yamlFile 'test.yaml'
    }
  }
  stages {
    stage('build docker image') {
      steps {
        container('test') {
          sh 'echo "build number is ${BUILD_NUMBER}"'
          sh 'docker image build -t simplestory:5000/djangotest:${BUILD_NUMBER} ./django'
          sh 'docker image push simplestory:5000/djangotest:${BUILD_NUMBER}'
        }
      }
    }
    stage('deploy django pod') {
      steps {
        container('jnlp') {
          script {
            try {
              sh 'kubectl delete pod django-test -n ss-take1'
            }
            catch(all) {
              sh 'echo error in delete pod, nothing to worry'
            }
          }
          sh 'kubectl run django-test -n ss-take1 -l=app=django-test --image=simplestory:5000/djangotest:${BUILD_NUMBER} --port=8000'
          sh 'echo done'
        }
      }
    }
  }
}
