# Exercise

To execute this automation code, install the dependencies in requirements.txt
~~~
 pip install -r requirements.txt
~~~

To install allure in windows, it's needed to install scoop, see: https://scoop.sh/

After setup the environnment, to run the tests:
~~~
behave -f allure -o allure-result ./features/login.feature
~~~


To generate the automation test report with allure (JAVA_HOME should be set in OS variables)

~~~
allure serve allure-result
~~~


