echo "Real mac address": 
ethtool -P wlp4s0

echo "Changing mac adress..."
sudo ifconfig wlp4s0 down
sudo macchanger -r wlp4s0
sudo ifconfig wlp4s0 up

