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

    stage('Copy history') {
    steps {
    script {
    sh 'cp -r allure-report/history allure-results/history'
  }
  }
  }

    stage('Reports') {
    steps {
    allure([
  includeProperties: false,
  jdk: '',
  properties: [ ],
  reportBuildPolicy: 'ALWAYS',
  results: [ [ path: '${env.WORKSPACE}/allure-results' ] ]
  ])
  }
  }
  }
  }