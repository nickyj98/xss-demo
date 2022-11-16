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
				sh 'apt-get install lsof -y '
				sh' if lsof -Pi :5000 -sTCP:LISTEN ; then (kill -9 $(lsof -t -i:5000)) ; else echo \"not running\" ; fi'
				sh' rm /var/jenkins_home/workspace/TestDeploy/database.db &'
			}
		}

	stage('pytest init') {
			steps {
				sh 'pip3 install selenium'
				sh 'pip3 install webdriver-manager'
				sh 'pip3 install pytest'
				sh 'pip3 install pytest-html' 
            }
		}

    stage('OWASP DependencyCheck') {
      steps {
        dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'Default'
      }
    }
	
	stage('pyflask run') {
		steps {
			sh 'JENKINS_NODE_COOKIE=dontKillMe nohup gunicorn -b 0.0.0.0:5000 wsgi:app &'
		}	
	}
	stage('run pytests') {
            steps {
            	sleep time: 5
				sh 'pytest ./pytest/pyGUItests.py --html=./pytest/report.html --self-contained-html || exit 0'
        }
    }
  }  
  post {
    success {
      dependencyCheckPublisher pattern: 'dependency-check-report.xml'
    }
  }
}