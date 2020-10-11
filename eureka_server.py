#!/usr/bin/python3
import os

path = 'eureka-server'

def mvn_C(): #mvn packge build function
   
   try:
       os.chdir('eureka-server')
   except:
       pass
   os.system("mvn package -Dspring.profiles.active=docker")

def doc_I(): #Docker image build function

   try:
       os.chdir('eureka-server')
   except:
       pass 

#in the bellow line you have to replace the docker hub user name of yours. (<Docker_User>/eureka-server) 
   os.system("docker build -f Dockerfile -t agkanon/eureka-server:latest .")
   os.system("docker push agkanon/eureka-server:latest")
   os.system("docker rmi agkanon/eureka-server:latest")
   os.system("docker pull agkanon/eureka-server:latest")
   os.system("docker run --network devops-net --name eureka-server -p 8761:8761 -d agkanon/eureka-server:latest")
   os.system("echo Welcome to Spring eureka UI on http://localhost:8761")

if not os.path.exists(path):
   os.system("git clone https://github.com/a2z-ice/eureka-server.git")
   mvn_C()
   doc_I()
   
else:
   os.system("git pull")
   mvn_C()
   doc_I() 
