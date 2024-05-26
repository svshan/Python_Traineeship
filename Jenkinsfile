pipeline {
  agent any

  environment {
    WORKSPACE = "${env.WORKSPACE}"
  }

  triggers {
    cron('H/10 * * * *')
  }

  stages {
    stage('Clone repository') {
      steps {
        script {
          git credentialsId: '', url: 'https://github.com/svshan/Python_Traineeship.git' , branch: 'main'
        }
      }
    }

    stage('Install requirements') {
      steps {
        script {
            sh 'python3 -m venv venv'
            sh '. venv/bin/activate && pip install -r requirements.txt'
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