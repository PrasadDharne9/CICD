pipeline {
    agent any

    stages {
        stage('Data Extraction') {
            steps {
                sh 'python code/data_extraction/extract_data.py'
            }
        }
        
        stage('Model Training') {
            steps {
                sh 'python code/model_training/train_model.py'
            }
        }
        
        stage('Forecast Deployment') {
            steps {
                sh 'python code/forecast_deployment/deploy_forecasts.py'
            }
        }
    }
    
    post {
        always {
            // Archive artifacts for later access
            archiveArtifacts artifacts: ['forecasts/*.csv', 'models/*.pkl'], allowEmptyArchive: true
        }
    }
}