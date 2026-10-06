This network demonstrates IP DHCP Snooping.

DHCP Snooping is enabled on Access-SW1, with only interface G0/1 marked as trusted. Option 82 is disabled on both Access-SW1 and Core-SW1.

PC0 and PC1 successfully obtain IPs from the 192.168.10.0/24 DHCP pool on Router0.

Rogue-R1 has its own DHCP pool, but since it's connected via an untrusted port, clients do not receive IPs from it (disconnecting Core-SW1 from Router0 will demonstrate this).

The laptop in Rogue LAN confirms Rogue-R1’s DHCP functionality, but Access-SW1's DHCP Snooping blocks Rogue DHCP offers to the main LAN.