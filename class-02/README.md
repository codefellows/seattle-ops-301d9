# Class 02

## Class Outline

1. Warm-Up
1. Review
1. Lecture
1. Demo
1. Lab 

## Overview

The network mapping tool Nmap is an open source, command line utility commonly used in network discovery ("enumeration" in offensive terms), security auditing, and pentesting. Nmap can audit whether ports are open or closed on a target host.

Today you will perform a series of basic scanning operations using Nmap and learning more about network ports and protocols.

## How does this topic fit?

**Where we've been**:
Previously we studied network traffic analysis using Wireshark.

**What are we focusing on today**:
Today, we'll be using Nmap to scan for network ports.

**Where we're headed**:
In the next class we'll be exploring network segmentation.

## Network Scanning with NMAP

### Why
- Nmap helps in discovering devices and hosts on a network. This is crucial for network administrators to maintain an up-to-date inventory of all devices connected to the network. It aids in identifying unauthorized or rogue devices, as well as potential security vulnerabilities that might be present in the network.
- Nmap can be used to perform security assessments of networks, identifying open ports, services, and potential vulnerabilities. By understanding what services are running on network devices, administrators can take proactive steps to secure and patch vulnerable systems.
- Nmap can be used to test the effectiveness of firewalls and intrusion detection systems. By simulating various scan types and techniques, administrators can evaluate how well their network defenses are holding up against potential attackers.
- Nmap can assist in ongoing network monitoring by providing insights into the status of network devices, services, and ports. This helps administrators detect any changes or anomalies that might indicate a security breach or system malfunction.
- Ethical hackers and penetration testers often use Nmap to gather information about a target network before attempting to exploit vulnerabilities. This helps them understand potential attack vectors and plan their strategies accordingly.
- Understanding the services and ports that are active on devices can help network administrators optimize network traffic and resource allocation. Unnecessary or insecure services can be disabled or reconfigured for better performance and security.
- In the event of a security incident, Nmap can be used to quickly assess the extent of the compromise and identify affected systems. This information is crucial for timely and effective incident response.

### What
- Network Scanning: The process of systematically investigating a network to discover active hosts, open ports, and services running on those hosts.
- Port: A logical endpoint for communication on a network device. Ports are numbered and associated with specific protocols (e.g., port 80 for HTTP).
- Penetration Testing: A controlled and authorized attempt to exploit vulnerabilities in a system to identify security weaknesses. Also known as ethical hacking.
- Ethical Hacker: A person who uses hacking techniques to identify and fix security vulnerabilities, rather than exploiting them for malicious purposes.
- Port Scanning: The act of sending packets to a range of port numbers on a target system to determine which ports are open and potentially vulnerable.
- Banner Grabbing: Collecting information about a service by reading the banner or identification string it sends when a connection is established.
- Network Enumeration: The process of gathering information about hosts on a network, including their IP addresses, open ports, and services.
- TCP/IP: Transmission Control Protocol/Internet Protocol. A suite of networking protocols that defines how data is sent and received over the internet.
- UDP (User Datagram Protocol): A connectionless protocol that operates at the transport layer of the TCP/IP model. It's often used for tasks that require quick data transmission, such as real-time video streaming.
- ICMP (Internet Control Message Protocol): A network protocol used to send error messages and operational information about network conditions.
- Compliance: Adhering to industry-specific regulations and standards related to security and data protection.
- Asset Inventory: A record of all devices and resources (hardware, software, and data) within a network.
- Risk Assessment: The process of identifying and evaluating potential risks and vulnerabilities in a system or network.
- Network Segmentation: Dividing a network into smaller segments to improve security and manageability.

### How
- Prepare a network environment and stage Kali Linux
- Port scanning with Nmap
- Reporting Nmap findings
- Explore some protocol-related capabilities of Wireshark
- Run a `netstat` command to show all active ports

### Experimentation and Discovery Ideas
- What ports and protocols do I need to know to pass CompTIA Net+?
- What types of Transport Layer (Layer 4) protocols are there?
- What types of Network Layer (Layer 3) protocols are there? 

## Learning Objectives

### Students will be able to

#### Describe and Define

- Network Enumeration
- Nmap
- Service Fingerprinting
- Network ports
- Port scanning

#### Execute

- Perform port scans using Nmap.

## Helpful Resources

- [Wireshark Docs on the "Protocol Hierarchy" Window](https://www.wireshark.org/docs/wsug_html_chunked/ChStatHierarchy.html#:~:text=This%20is%20a%20tree%20of,be%20shown%20at%20the%20bottom.){:target="blank"}

## Notes

### Host-only vs NAT Network

The lab is going to ask you to prepare a suitable network environment by placing 2-3 different hosts together, either on the the same Host-only network with a pfSense router, or on the same NAT Network (without a pfSense router). Ideally, choose VMs with different OSs and/or different configurations (such as a Windows 10 host, an Ubuntu Server, and a pfSense router). These will be your targets today.

Let's weigh the pros and cons of a Host-only network vs a NAT Network to decide which path is best for your lab.

#### Option 1: Set Up Host-only Network and pfSense Router

- Pros:
  - Isolation: Host-only networks provide isolation from the external network, ensuring that your VMs can communicate with each other but not with external networks. This is useful for creating a controlled testing environment.
  - Advanced Routing and Firewall: By using pfSense, you can set up advanced routing and firewall rules, allowing you to control traffic between VMs and even simulate complex network scenarios.
  - Custom Configuration: You have more control over IP addressing, subnetting, and network configurations, which can be helpful for emulating specific network setups.

- Cons:
  - Complex Setup: Setting up pfSense as a virtual router requires more configuration and understanding of networking concepts. It might not be suitable for beginners.
  - Resource Overhead: Running an additional virtual machine (pfSense) consumes resources such as memory and CPU. This might impact the performance of your host system if it's not powerful enough.

1. Open VirtualBox and go to "File" > "Host Network Manager."
2. Create a new Host-only network if you haven't already.
3. Install and set up pfSense (if you choose this route) as a virtual machine using the ISO image from the pfSense website.

#### Option 2: Set Up NAT Network

- Pros:
  - Simplicity: NAT Networks are simpler to set up compared to a pfSense router. VirtualBox handles the NAT and DHCP configuration for you.
  - Easy Internet Access: VMs in a NAT Network can easily access the internet through the host machine's internet connection without additional configuration.
  - Limited Exposure: VMs are shielded from direct external access, which can be beneficial if you're concerned about security.

- Cons:
  - Limited Customization: You have less control over network configurations. The NAT Network setup is more suitable for basic scenarios where you want your VMs to access the internet.
  - Less Complex Testing: NAT Networks might not be suitable for testing complex networking scenarios that involve specific routing and firewall configurations.
  - Limited VM-to-VM Communication: VMs in a NAT Network can communicate with each other, but external connections cannot directly initiate communication with VMs.

1. If you're not using a pfSense router, you can set up a NAT Network in VirtualBox.
2. In VirtualBox, go to "File" > "Preferences" > "Network."
3. Create a new NAT Network.

#### Create VMs and Connect to Network

1. Create Virtual Machines for the Windows 10 host, Ubuntu Server, pfSense (if applicable), and Kali Linux.
2. When configuring network adapters for each VM, choose either the Host-only network or the NAT Network you created.
3. Configure IP addresses for each VM manually or through DHCP, depending on your network setup.