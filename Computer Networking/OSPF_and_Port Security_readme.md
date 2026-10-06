Username: Admin
Password: cisco
Privileged Exec Password: ChumBucket12

This is a simple network lab setup that features three office locations.

Each office is equipped with a router connected to its own internal LAN.
Every LAN includes a switch and several end devices, such as PCs, printers, and servers.

PCs receive their IP addresses via DHCP from the DHCP-Serv1 server, except for the Management PC, which is statically configured. The Management PC is the only device authorized to SSH into the routers.

All end devices can communicate with each other across the network. This is made possible through OSPF, which is used by the routers to dynamically advertise routes.

To enhance security and performance:

PortFast and BPDU Guard are enabled on all switch ports connected to end devices.

Port Security is also configured:

In the Boston and Cheyenne offices, violation mode is set to restrict.

In the Destin office, violation mode is set to shutdown.