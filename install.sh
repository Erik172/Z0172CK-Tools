echo "Solucionando Problemas"
sudo rm geckodriver
sudo rm /usr/local/share/geckodriver
sudo rm /usr/local/bin/geckodriver
sudo rm /usr/bin/geckodriver

echo -e "[ \e[32m + \e[0m ] Instalando Aplicaciones"
echo ""
sudo apt install python3 -y&&
sudo apt install python3-pip -y &&
sudo apt install nmap -y &&
sudo apt install hydra -y &&
sudo apt install tor -y &&
sudo apt install curl -y &&
sudo apt install nikto nmap -y &&
sudo apt install maven default-jdk default-jre openjdk-8-jdk openjdk-8-jre -y &&
sudo apt install zlib1g-dev libncurses5-dev lib32z1 lib32ncurses6 -y &&
sudo apt install screen -y &&
echo ""
echo -e "\e[32m OK \e[0m"

echo ""
echo -e "[ \e[32m + \e[0m ]Instalando Dependencias"
sudo pip3 install -r requirements.txt  



