# Steps are taken to do the MCQ generator END to END and deployment of project

# Created a virtual env with python version 3.10 

1.first login to the AWS: https://aws.amazon.com/console/

2.Search about the EC2

3.you need to config the UBUNTU Machine

4.launch the instance

5.update the machine:

6.sudo apt update

7.sudo apt-get update

8.sudo apt upgrade -y

9.sudo apt install git curl unzip tar make sudo vim wget -y

10.git clone "Your-repository"

11.sudo apt install python3-pip

12.pip3 install -r requirements.txt

13.python3 -m streamlit run StreamlitAPP.py

14.if you want to add openai api key create .env file in your server using touch .env, do the vi .env 
15.press insert #copy your api key and paste it there #press and then :wq and hit enter

16.go with security and add the inbound rule add the port 8501 
17. Used your public IP address to access the application.