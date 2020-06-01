cd /etc/systemd
sudo rm logind.conf
sudo ln -s  logind-enable-lid-closed.conf logind.conf
sudo restart systemd-logind
