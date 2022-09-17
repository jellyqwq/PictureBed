yum -y update
yum install -y net-tools
cp ~/package/jdk-8u161-linux-x64.tar.gz ~/
tar -xzf ~/jdk-8u161-linux-x64.tar.gz -C ~/
mv ~/jdk1.8.0_161 ~/java
rm -rf ~/jdk-8u161-linux-x64.tar.gz
echo 'export PATH=$PATH:~/java/bin'>>~/.bashrc
echo 'export JAVA_HOME=~/java'>>~/.bashrc
source ~/.bashrc
jps
cp ~/package/apache-zookeeper-3.5.10-bin.tar.gz ~/
tar -xzf ~/apache-zookeeper-3.5.10-bin.tar.gz -C ~/
mv ~/apache-zookeeper-3.5.10-bin ~/zookeeper
rm -rf ~/apache-zookeeper-3.5.10-bin.tar.gz
cp ~/zookeeper/conf/zoo_sample.cfg ~/zookeeper/conf/zoo.cfg
mkdir ~/zookeeper/data
touch ~/zookeeper/data/myid
echo $HOSTNAME | echo ${HOSTNAME/misaka/}>>~/zookeeper/data/myid
sed -i "s#dataDir=.*#dataDir=~/zookeeper/data#g" ~/zookeeper/conf/zoo.cfg
echo 'server.0=192.168.60.10:2888:3888'>>~/zookeeper/conf/zoo.cfg
echo 'server.1=192.168.60.11:2888:3888'>>~/zookeeper/conf/zoo.cfg
echo 'server.2=192.168.60.12:2888:3888'>>~/zookeeper/conf/zoo.cfg
echo 'export PATH=$PATH:~/zookeeper/bin'>>~/.bashrc
source ~/.bashrc
