#10:bf:48:65:3b:b2
ifconfig eth0 down
ifconfig eth0 hw ether 00:11:43:E3:C8:11
ifconfig eth0 up
ifconfig eth0 |grep HWaddr
