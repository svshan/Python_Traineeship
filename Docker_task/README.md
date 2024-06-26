### Task reference:
Virtualisation, containerisation (QAT-3766)

### Install Selenoid:
1. Download and install Configuration manager (app used to automatically configure Aerokube products):
wget https://github.com/aerokube/cm/releases/download/1.8.8/cm_darwin_amd64
2. Change the permissions:
chmod +x cm_darwin_amd64 
3. Run file from current directory:
./cm_darwin_amd64
4. Start Selenoid:
./cm selenoid start --vnc
5. Start Selenoid UI:
./cm_darwin_amd64 selenoid-ui start
6. See the IP address where Selenoid UI is running:
ifconfig
7.  Display the logs for a Docker container:
docker logs selenoid/ docker logs selenoid-ui
8. Display the detailed information about a Docker container:
docker inspect selenoid