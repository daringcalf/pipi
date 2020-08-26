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
    stage('build sweb image') {
      steps {
        container('test') {
          sh 'echo "build number is ${BUILD_NUMBER}"'
          // sh 'docker image build -t simplestory:5000/djangotest:${BUILD_NUMBER} ./django'
          // sh 'docker image push simplestory:5000/djangotest:${BUILD_NUMBER}'
          sh 'docker image build -t simplestory:5000/sweb:${BUILD_NUMBER} ./django'
          sh 'docker image push simplestory:5000/sweb:${BUILD_NUMBER}'
        }
      }
    }
    stage('roll sweb pods') {
      steps {
        container('jnlp') {
          // script {
          //   try {
          //     // sh 'kubectl delete pod django-test -n ss-take1'
          //     // sh 'kubectl delete pod sweb -n simplestory'
          //   }
          //   catch(all) {
          //     sh 'echo error in delete pod, nothing to worry'
          //   }
          // }
          // sh 'kubectl run django-test -n ss-take1 -l=app=django-test --image=simplestory:5000/djangotest:${BUILD_NUMBER} --port=8000'
          sh 'echo "rolling deploy sweb ..."'
          sh 'kubectl set image deployment sweb sweb=simplestory:5000/sweb:${BUILD_NUMBER} -n simplestory'
          sh 'echo "sweb is using ${BUILD_NUMBER} now, remember to edit the yaml"'
        }
      }
    }
    stage('restart nginx container') {
      steps {
        container('jnlp') {
          environment {
            POD = """${sh(
                    returnStdout: true,
                    script: 'kubectl get pod | grep nginx | awk \'{print $1}\''
                  )}""" 
          }
          sh 'kubectl exec -it ${POD} -c nginx -- /bin/sh -c "kill 1"'
          sh 'echo container nginx restarted'
        }
      }
    }
  }
}
