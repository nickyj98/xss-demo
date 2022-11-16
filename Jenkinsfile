pipeline {
  agent any
  stages {
    stage('Checkout SCM') {
      steps {
        git branch: 'master', url: 'https://github.com/nickyj98/xss-demo.git'
      }
    }
	
	stage('pyflask init') {
			steps {
				sh 'apt-get install python3 -y'
				sh 'apt-get -y install python3-pip'
				sh 'pip3 install gunicorn flask'
			}
		}


    stage('OWASP DependencyCheck') {
      steps {
        dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'Default'
      }
    }
	
	stage('pyflask run') {
		steps {
			sh 'gunicorn -b 0.0.0.0:5000 wsgi:app'
		}	
	}
  }  
  post {
    success {
      dependencyCheckPublisher pattern: 'dependency-check-report.xml'
    }
  }
}