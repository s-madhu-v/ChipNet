# Run this as "source" and from the home folder of the user "madhu"
# Setting up xrdp
sudo apt update
sudo apt install xfce4 xfce4-goodies -y
sudo apt install xrdp -y
echo "xfce4-session" | tee .xsession
sudo systemctl restart xrdp
# Allowing rdp connections
sudo ufw allow 3389
# Add user to docker group
sudo usermod -aG docker madhu # assuming username is 'madhu'
# For Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i ./google-chrome-stable_current_amd64.deb
# Installing Python 3.9
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.9 -y
sudo apt-get install python3.9-venv -y
sudo apt-get install python3.9-tk -y
# Setting up Github Desktop
sudo apt-get update
sudo apt-get install gdebi-core -y
sudo wget https://github.com/shiftkey/desktop/releases/download/release-3.1.1-linux1/GitHubDesktop-linux-3.1.1-linux1.deb
sudo gdebi GitHubDesktop-linux-3.1.1-linux1.deb
