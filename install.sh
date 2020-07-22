echo -e "[ \e[32m + \e[0m ] Instalando Aplicaciones"
echo ""
sudo apt install python3 -y&&
sudo apt install python3-pip -y &&
sudo apt install nmap -y &&
sudo apt install hydra -y &&
sudo apt install tor -y &&
sudo apt install curl -y &&
sudo apt install nikto nmap -y &&
echo ""
echo -e "\e[32m OK \e[0m"

echo ""
echo -e "[ \e[32m + \e[0m ]Instalando Dependencias"
sudo pip3 install -r requirements.txt 
