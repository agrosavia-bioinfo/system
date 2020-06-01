# bluetooth
# If the system requires no Bluetooth devices, disable this service
#chkconfig bluetooth off
service bluetooth stop

# avahi-daemon
# The Avahi daemon implements the DNS Service Discovery and Multicast
# DNS protocols, which provide service and host discovery on a network.
# It allows a system to automatically identify resources on the network,
# such as printers or web servers.
#chkconfig avahi-daemon off
service avahi-daemon stop
 
# cups
# Do you need the ability to print from this machine or to allow others
# to print to it? If not:
#chkconfig cups off
service cupsd stop
service cups-browsed stop

# Others
service modem-manager stop
