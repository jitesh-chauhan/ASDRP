pipeline {
    agent any
triggers {
        githubPush()
    }
    environment {
        IMAGE_NAME = "vardain/asdrp"
        IMAGE_TAG = "latest"
    }

    stages {

        // stage('Checkout') {
        //     steps {
        //         checkout scm
        //     }
        // }
        stage('Debug Workspace') {
    steps {
        sh 'pwd'
        sh 'ls -l'
    }
}

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Login and Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: '831b56e7-1506-4479-aca9-fc013e6d700b', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push ${IMAGE_NAME}:${IMAGE_TAG}
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Replace image in asdrp-deployment.yaml
                    sh "sed -i 's|image:.*|image: ${IMAGE_NAME}:${IMAGE_TAG}|' asdrp-deployment.yaml"

                    // Apply k8s manifests
                    sh "kubectl apply -f asdrp-deployment.yaml"
                    sh "kubectl apply -f asdrp-service.yaml"
                }
            }
        }
stage('Expose Service Port') {
            steps {
                script {
                    // Run port-forward in background using nohup
                    sh 'nohup kubectl port-forward service/asdrp-service 8000:8000 > port-forward.log 2>&1 &'
                }
            }
        }    
}
    post {
        always {
            sh "docker logout"
        }
   }
}
