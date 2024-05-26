pipeline {
  agent {
    docker {
      image 'python:3.11'
      args '-u root'
    }
  }

  triggers {
    cron('H/10 * * * *')
  }

  stages {
    stage('Clone repository') {
      steps {
        script {
          git credentialsId: '', url: 'https://github.com/svshan/Python_Traineeship.git', branch: 'main'
        }
      }
    }

    stage('Install requirements') {
      steps {
        script {
          sh 'pip install -r requirements.txt'
        }
      }
    }

    stage('Run tests') {
      steps {
        catchError {
          script {
            sh 'pytest *.py'
          }
        }
      }
    }
  }
}
