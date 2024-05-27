pipeline {
  agent any

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

    stage('Setup Python Environment') {
      steps {
        script {
          sh 'python3 -m venv venv'
          sh './venv/bin/pip install --upgrade pip'
          sh './venv/bin/pip install -r requirements.txt'
        }
      }
    }

    stage('Run tests') {
      steps {
        catchError {
          script {
            sh './venv/bin/pytest *.py'
          }
        }
      }
    }
  }
}
