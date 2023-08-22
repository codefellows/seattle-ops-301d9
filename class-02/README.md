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
