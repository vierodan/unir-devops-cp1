pipeline {
   agent any
   stages {
      stage('Mock Build') {
         steps {
            echo 'Eyyy this is Python is not necessary to compile anything'
            echo WORKSPACE
            bat 'dir'
         }
      }
      stage('Unit Tests'){
         steps{
            bat ...
               SET PYTHONPATH=%WORKSPACE%
               pytest test\\unit
            ...
         }
      }
   }
}