docker run -itd ^
-v /d/Desktop/docker_src/package:/root/package ^
--privileged=true ^
--name misaka0 ^
--hostname misaka0 ^
--net misaka ^
--ip 192.168.60.10 ^
--add-host misaka0:192.168.60.10 ^
--add-host misaka1:192.168.60.11 ^
--add-host misaka2:192.168.60.12 ^
centos:centos7 /usr/sbin/init

docker run -itd ^
-v /d/Desktop/docker_src/package:/root/package ^
--privileged=true ^
--name misaka1 ^
--hostname misaka1 ^
--net misaka ^
--ip 192.168.60.11 ^
--add-host misaka0:192.168.60.10 ^
--add-host misaka1:192.168.60.11 ^
--add-host misaka2:192.168.60.12 ^
centos:centos7 /usr/sbin/init

docker run -itd ^
-v /d/Desktop/docker_src/package:/root/package ^
--privileged=true ^
--name misaka2 ^
--hostname misaka2 ^
--net misaka ^
--ip 192.168.60.12 ^
--add-host misaka0:192.168.60.10 ^
--add-host misaka1:192.168.60.11 ^
--add-host misaka2:192.168.60.12 ^
centos:centos7 /usr/sbin/init

start cmd /k docker exec -it misaka0 /bin/bash
start cmd /k docker exec -it misaka1 /bin/bash
start cmd /k docker exec -it misaka2 /bin/bash