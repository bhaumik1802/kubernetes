Question 1

Create a namespace called ggckad-s0 in your cluster.
Run the following pods in this namespace.
A pod called pod-a with a single container running the kubegoldenguide/simple-http-server image
A pod called pod-b that has one container running the kubegoldenguide/alpine-spin:1.0.0 image, and one container running nginx:1.7.9
Write down the output of kubectl get pods for the ggckad-s0 namespace.

Question 2

All operations in this question should be performed in the ggckad-s2 namespace.
Create a ConfigMap called app-config that contains the following two entries:

'connection_string' set to 'localhost:4096'
'external_url' set to 'google.com'
Run a pod called question-two-pod with a single container running the kubegoldenguide/alpine-spin:1.0.0 image, and expose these configuration settings as environment variables inside the container.

Question 3

All operations in this question should be performed in the ggckad-s2 namespace. Create a pod that has two containers. Both containers should run the kubegoldenguide/alpine-spin:1.0.0 image. The first container should run as user ID 1000, and the second container with user ID 2000. Both containers should use file system group ID 3000.

Question 4

All operations in this question should be performed in the ggckad-s4 namespace. This question will require you to create a pod that runs the image kubegoldenguide/question-thirteen. This image is in the main Docker repository at hub.docker.com.

This image is a web server that has a health endpoint served at '/health'. The web server listens on port 8000. (It runs Python’s SimpleHTTPServer.) It returns a 200 status code response when the application is healthy. The application typically takes sixty seconds to start.

Create a pod called question-13-pod to run this application, making sure to define liveness and readiness probes that use this health endpoint.


Question 5

All operations in this question should be performed in the ggckad-s5 namespace. Create a file called question-5.yaml that declares a deployment in the ggckad-s5 namespace, with six replicas running the nginx:1.7.9 image.

Each pod should have the label app=revproxy. The deployment should have the label client=user. Configure the deployment so that when the deployment is updated, the existing pods are killed off before new pods are created to replace them.
