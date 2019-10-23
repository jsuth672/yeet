python manage.py test
 
sudo apt-get install curl software-properties-common
curl -sL https://deb.nodesource.com/setup_12.x | sudo bash -
sudo apt install -y nodejs
export SONAR_SCANNER_VERSION=4.0.0.1744
export SONAR_SCANNER_HOME=$HOME/.sonar/sonar-scanner-$SONAR_SCANNER_VERSION-linux
rm -rf $SONAR_SCANNER_HOME
mkdir -p $SONAR_SCANNER_HOME
curl -sSLo $HOME/.sonar/sonar-scanner.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-$SONAR_SCANNER_VERSION-linux.zip
unzip $HOME/.sonar/sonar-scanner.zip -d $HOME/.sonar/
rm $HOME/.sonar/sonar-scanner.zip
export PATH=$SONAR_SCANNER_HOME/bin:$PATH
export SONAR_SCANNER_OPTS="-server"
 
if [ "$TRAVIS_PULL_REQUEST" = "false" ]; then
  sonar-scanner \
  -Dsonar.projectKey=yeet \
  -Dsonar.organization=jsuth672 \
  -Dsonar.sources=. \
  -Dsonar.host.url=https://sonarcloud.io \
  -Dsonar.login=102ee2804abfe6395cf93c0adc2e60b84785e9fc \
  -Dsonar.python.coverage.reportPaths=nosecover.xml \
  -Dsonar.python.xunit.reportPaths=nosetests.xml
else
  echo "checking pull request..."
  sonar-scanner \
  -Dsonar.projectKey=yeet \
  -Dsonar.organization=jsuth672 \
  -Dsonar.sources=. \
  -Dsonar.host.url=https://sonarcloud.io \
  -Dsonar.login=102ee2804abfe6395cf93c0adc2e60b84785e9fc \
  -Dsonar.pullrequest.key=$TRAVIS_PULL_REQUEST \
  -Dsonar.pullrequest.branch=$TRAVIS_PULL_REQUEST_BRANCH \
  -Dsonar.pullrequest.base=master \
  -Dsonar.python.coverage.reportPaths=nosecover.xml \
  -Dsonar.python.xunit.reportPaths=nosetests.xml
fi
