| Abbreviation | Full Form | What it is (simple definition) |
|---|---|---|
| HTTP | HyperText Transfer Protocol | The protocol browsers use to request web pages from servers. |
| HTTPS | HTTP Secure | Encrypted version of HTTP using SSL/TLS for security. |
| DNS | Domain Name System | Translates domain names (google.com) into IP addresses. |
| IP | Internet Protocol | The main protocol for addressing and routing packets across networks. |
| IPv4 | Internet Protocol version 4 | Uses 32‑bit addresses (e.g., 192.168.1.1); nearly exhausted. |
| IPv6 | Internet Protocol version 6 | Uses 128‑bit addresses; solves IPv4 shortage and adds features. |
| TCP | Transmission Control Protocol | Reliable, connection‑oriented protocol; guarantees delivery and order. |
| UDP | User Datagram Protocol | Faster, no‑guarantee protocol; used for streaming, VoIP, games. |
| MAC | Media Access Control | A unique hardware address burned into every network interface. |
| LAN | Local Area Network | A small network, e.g., in an office or home. |
| WAN | Wide Area Network | A network that spans large geographic areas (the internet is a WAN). |
| NAT | Network Address Translation | Lets multiple devices share one public IP address. |
| ARP | Address Resolution Protocol | Finds a device's MAC address from its IP address on the same network. |
| ICMP | Internet Control Message Protocol | Used for diagnostic tools like ping and error reporting. |
| DHCP | Dynamic Host Configuration Protocol | Automatically assigns IP addresses to devices on a network. |
| OSI | Open Systems Interconnection | A 7‑layer conceptual model for networking (Physical to Application). |


### What happens when you enter a URL in a browser and hit enter?
Once DNS translates url to IP address, the browser establishes a TCP connection and sends a HTTP GET
request to the server, then the server processes that request and sends back a HTTP response which usually contains
the html file for the page.


### Can you explain the OSI model and how it differs from the TCP/IP model?
The OSI model (Open Systems Interconnection model) is a framework that divides network communication
into seven distinct layers, each responsible for specific functions, facilitating interoperability
between different systems. These layers are:
- Physical: hardware, cables, electronic signals
- Data Link: handles local connection between two devices on a network (MAC addresses, switches)
- Network: IP addresses, finding the right destination
- Transport: TCP/UDP, transporting data
- Session: manages connection between two applications
- Presentation: translates the message
- Application: the interface to display data

**TCP/IP:**
- The TCP/IP (Transmission Control Protocol/Internet Protocol) model is the more
practical model the internet is built on.
- It's a suite of communication protocols used to interconnect network devices on the internet.
- It enables reliable data transfer and routing of packets between devices,
forming the foundation of internet communication.
- There's 4 layers:
    - Network Interface, Internet, Transport, Application

The main difference is OSI's stricter separation of presentation and session functions,
which TCP/IP doesn't define as separate layers.


### What is the difference between TCP and UDP?
TCP is a connection-oriented (3-way handshake) protocol that ensures accurate and ordered data delivery but it's slower.
It uses ACKs but UDP doesn't.
UDP is a fast and connectionless transport protocol that doesn't guarantee data delivery.
It's better when speed is more important than accuracy.


### What is the difference between HTTP and HTTPS?
The main difference is security. HTTP sends all data as plain text, which is vulnerable to eavesdropping and tampering.
HTTPS wraps that data in encryption using SSL/TLS, creating a secure,
verified tunnel between your browser and the server.


### What is a subnet and why is it used?
A subnet is a smaller, logical division of a larger network.
We use subnet masks to split an IP address into a 'network' part and a 'host' part.
You'd do this to manage traffic flow, boost security by isolating departments, and conserve IP addresses.


### What is the difference between a router and a switch?
Switches connect devices inside a single network, like your laptop, phone, and printer at home,
using MAC addresses (Layer 2). Routers connect different networks together,
like your home network to the internet, using IP addresses (Layer 3).
Your router at home gives you a private IP from a switch and a public IP from the router.


### What is NAT and why is it used?
NAT (Network Address Translation) allows multiple devices on a private network
(using private IPs) to share a single public IP address to access the internet.
This was a crucial solution to the IPv4 address shortage and provides a basic
layer of security by hiding the internal network structure.


### What is a VLAN?
A VLAN (Virtual LAN) is a way to create logically separate networks on the same physical switch.
This improves security by isolating sensitive traffic, reduces bandwidth consumption,
and allows for more flexible network management.

