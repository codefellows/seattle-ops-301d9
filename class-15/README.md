# Class 15

## Class Outline

1. Ops 301 Review & Exam Prep 
1. [Ops 401 Preview](https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/){:target="blank"}
1. 301 Final Project Overview
1. Ops 401 Entrance Exam 

## Overview

Today we'll review Ops 301, preview Ops 401, then assemble project teams. Final exam will be unlocked.

## How does this topic fit?

**Where we've been**:
In the previous class we explored Group Policy and how we can use it to enforce Windows system configurations at scale across an organization.

**What are we focusing on today**:
Today, we will be preparing to take the 401 Entrance Exam and for Final Projects.

**Where we're headed**:
In Cybersecurity 401, we will focus on Governance, Risk, and Compliance; Data Security; Security Operations; Cloud Security; Threat Modeling and Analysis; Threat Hunting; Web Application Security; and Penetration Testing.

## 401 Entrance Exam Study Guide

### Networking

- What is the OSI (Open Systems Interconnection) model, and how does it categorize networking functions into seven layers?
- Explain the difference between a switch, a router and a hub in a network, and when each device is typically used.
- What is an IP address, and how does it facilitate communication between devices on a network?
- Describe the purpose of subnetting in IP addressing and how it helps with efficient address allocation.
- What is DNS (Domain Name System), and how does it translate human-readable domain names into IP addresses?
- Discuss the primary differences between TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) and when to use each.
- Explain the role of NAT (Network Address Translation) in conserving IP addresses and enhancing network security.
- What is DHCP (Dynamic Host Configuration Protocol), and how does it simplify the process of IP address assignment in networks?
- How does ARP (Address Resolution Protocol) work, and why is it important in local network communication?
- What are common methods for securing a wireless network, and why is encryption crucial for wireless security?

### OSI Model

- What is the OSI model, and why was it developed in the field of networking?
- Describe the seven layers of the OSI model, from Layer 1 (Physical) to Layer 7 (Application), and provide an example of a function or protocol associated with each layer.
- Explain the concept of encapsulation in the context of the OSI model and how data is encapsulated as it passes through each layer.
- What is the primary purpose of the Physical Layer, and what are some common devices and media associated with this layer?
- How does the Data Link Layer address devices on the same network segment, and what are MAC addresses used for?
- Describe the role of the Network Layer in routing data between different networks, including the use of IP addresses.
- What is the function of the Transport Layer, and how do TCP and UDP differ in their approach to data transmission?
- How does the Session Layer establish, maintain, and terminate communication sessions between applications?
- Explain the responsibilities of the Presentation Layer, including data translation, encryption, and compression.
- What is the Application Layer, and how does it provide a user interface to access network services and applications?

### Network Traffic Analysis with Wireshark

- What is Wireshark, and why is it a valuable tool for network traffic analysis?
- How can you capture network traffic using Wireshark, and what are some important considerations when starting a capture?
- Explain the difference between display filters and capture filters in Wireshark. When would you use each type?
- What types of information can you gather from the packet details displayed in Wireshark during a traffic capture?
- How can Wireshark assist in diagnosing network performance issues such as latency or packet loss?
- What is a "packet capture file" in Wireshark, and why is it useful for offline analysis?
- Describe some of the common network protocols that Wireshark can analyze and decode.
- What is the purpose of color-coding in Wireshark's packet list? How can it help in traffic analysis?
- Explain the benefits of using Wireshark's Follow TCP Stream feature when analyzing network traffic.
- How does Wireshark help identify potential security threats or suspicious network activity during traffic analysis?

### Configuring and Monitoring Ports and Protocols

- What is the significance of ports in networking, and how are they identified?
- Explain the difference between TCP and UDP protocols, and provide examples of when each is typically used.
- How can you check the open ports on a computer or network device using command-line tools?
- Describe the process of port forwarding and when it might be necessary in a network configuration.
- What is a well-known port, and can you provide examples of services associated with well-known ports?
- How can you use a firewall to control and monitor incoming and outgoing traffic on specific ports?
- What are the potential security risks associated with open ports, and how can they be mitigated?
- Explain the concept of port scanning, and discuss its role in network security assessments.
- How does network monitoring software help in tracking the usage and status of ports and protocols?
- What is the role of Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS) in monitoring and protecting against suspicious port activity?

### Basic Scanning Operations with Nmap

- What is Nmap, and why is it a popular tool for network scanning and discovery?
- Describe the difference between an active scan and a passive scan in Nmap.
- What are the primary scanning techniques used in Nmap (e.g., SYN scan, UDP scan), and when should you use each one?
- Explain how Nmap can be used to identify open ports on a remote host.
- What is the purpose of OS fingerprinting in Nmap, and how does it work?
- How can you specify a target range of IP addresses in an Nmap scan?
- Describe the use of timing options (e.g., -T1, -T4) in Nmap scans and their impact on scan speed and accuracy.
- What is the Nmap Scripting Engine (NSE), and how can it be used to extend Nmap's functionality?
- How can you save the results of an Nmap scan to a file for further analysis?
- Explain the concept of banner grabbing in Nmap and its relevance in network reconnaissance.

### IP Addresses

- What is an IP address, and why is it important in computer networking?
- Explain the difference between IPv4 and IPv6, including their address formats and purposes.
- How is an IP address structured, and what distinguishes the network portion from the host portion?
- Describe the purpose of a subnet mask and how it is used to determine the network and host portions of an IP address.
- What is the significance of the default gateway (or router) in an IP network, and how is it related to IP addressing?
- Explain the concept of private IP addresses and their role in internal network communication.
- How do you classify an IP address as belonging to one of the following classes: Class A, Class B, or Class C?
- Discuss the role of DHCP (Dynamic Host Configuration Protocol) in automatic IP address assignment.
- What is CIDR (Classless Inter-Domain Routing), and how does it affect IP addressing and subnetting?
- How can you determine the broadcast address and the number of host addresses available in a given subnet based on the subnet mask?

### Network Segmentation and Subnetting

- What is network segmentation, and why is it important in network design and security?
- Explain the concept of subnetting and how it helps in optimizing IP address allocation.
- What is the purpose of a subnet mask, and how is it used to divide an IP address into a network and host portion?
- Describe the advantages of using Variable Length Subnet Masks (VLSM) in subnetting.
- How can you calculate the number of available host addresses in a subnet based on its subnet mask?
- What is the default subnet mask for IPv4 Class A, Class B, and Class C networks?
- Explain the role of a gateway or router in connecting subnets within a network.
- Discuss the benefits of using VLANs (Virtual LANs) as a form of network segmentation.
- How does network segmentation enhance security and isolate network traffic?
- Describe a scenario where you would use supernetting and how it differs from subnetting.

### Routing

- What is routing in networking, and why is it necessary for data transmission between different networks?
- Explain the key functions of a router in a network.
- What is the primary role of a routing table, and how does it influence the routing process?
- Describe the difference between static routing and dynamic routing protocols.
- How does a router determine the best path for forwarding data packets to their destination network?
- What is a default route, and when might it be used in routing configurations?
- Discuss the purpose of routing metrics and how they impact routing decisions.
- Explain the concepts of interior routing protocols (IGP) and exterior routing protocols (EGP), and provide examples of each.
- How does the Border Gateway Protocol (BGP) differ from other routing protocols, and what is its significance in the Internet's routing infrastructure?
- Describe the process of route summarization (also known as route aggregation) and its benefits in routing optimization.

### VPN Tunneling

- What is a VPN (Virtual Private Network), and what is the primary purpose of VPN tunneling?
- Explain the difference between site-to-site VPNs and remote access VPNs.
- How does VPN tunneling ensure the confidentiality and integrity of data transmitted over the internet?
- Describe the role of encryption protocols like IPSec and SSL/TLS in VPN tunneling.
- What is tunnel mode and transport mode in IPSec, and when would you use each?
- How can you configure and establish a VPN tunnel between two remote locations?
- Discuss the concept of split tunneling in VPNs and its advantages and disadvantages.
- What is a VPN client and how does it interact with a VPN server during tunnel establishment?
- Explain the use of VPN protocols such as PPTP, L2TP, and OpenVPN, and their relative strengths and weaknesses.
- How can VPN tunneling be used to ensure secure remote access to a corporate network for remote workers?

### Web Server Deployment and Configuration

- What is a web server, and why is it a critical component of web application deployment?
- Explain the difference between a web server and an application server in the context of web applications.
- What is the role of a reverse proxy server, and how does it enhance web server performance and security?
- Describe the steps involved in deploying a web server using NGINX.
- How can you configure virtual hosts (server blocks) in NGINX, and why is this important for hosting multiple websites on a single server?
- Discuss common security measures and best practices for securing a web server against common vulnerabilities like SQL injection and XSS.
- What is HTTP/HTTPS redirection, and how can it be configured in NGINX?
- Explain the purpose of server-side caching in web server configurations and how it improves web application performance.
- How can you deploy and configure SSL/TLS certificates for secure communication on a web server?
- What is the role of a load balancer in web server deployments, and how does it help distribute incoming traffic efficiently?

### RADIUS Authentication and Integration

- What is RADIUS (Remote Authentication Dial-In User Service), and what are its primary functions in network security?
- Explain the difference between authentication, authorization, and accounting in RADIUS.
- How does RADIUS authentication enhance security in wireless networks, VPNs, and remote access solutions?
- What are the key components of a RADIUS infrastructure, including RADIUS client, RADIUS server, and RADIUS proxy?
- Describe the RADIUS authentication process, including the steps involved when a user attempts to access a network resource.
- How can RADIUS be integrated with OpenVPN for user authentication, and what are the benefits of this integration?
- What is the role of RADIUS attributes in controlling user access to network resources?
- Explain the concept of RADIUS server redundancy and load balancing for high availability.
- How does RADIUS support different authentication methods, such as PAP, CHAP, and EAP?
- Discuss the security considerations and best practices for implementing RADIUS authentication in a network environment.

### Traffic Mirroring and Analysis

- What is traffic mirroring, and why is it an important aspect of network monitoring and analysis?
- Explain the difference between in-line traffic monitoring and out-of-band traffic monitoring.
- How can port mirroring (SPAN) be configured on network switches, and what is its purpose?
- Describe the role of network taps in traffic mirroring and monitoring.
- What are the primary goals of traffic analysis, and how can it assist in network troubleshooting and security?
- How can you use packet analysis tools like Wireshark to capture and analyze network traffic?
- What is the significance of flow-based traffic analysis, and how is it different from packet-based analysis?
- Discuss the advantages and disadvantages of using NetFlow, sFlow, or IPFIX for traffic monitoring.
- How can traffic analysis tools help identify network anomalies, bottlenecks, and potential security threats?
- What is the relationship between traffic mirroring and intrusion detection systems (IDS) or intrusion prevention systems (IPS) in network security?

### AWS VPC and Cloud Infrastructure

- What is AWS VPC, and why is it an essential component of cloud infrastructure on Amazon Web Services?
- Describe the key components of an AWS VPC, including subnets, route tables, and security groups.
- How can you configure network ACLs (Access Control Lists) to control traffic in and out of subnets within an AWS VPC?
- Explain the purpose of AWS Elastic Load Balancers (ELBs) and how they enhance the availability and scalability of applications within a VPC.
- What is AWS Direct Connect, and how does it provide dedicated network connectivity to AWS services from on-premises data centers?
- Discuss the benefits of using VPC peering and Transit Gateway in complex network architectures.
- How can you implement Network Address Translation (NAT) within an AWS VPC, and why might you need it?
- Describe the process of establishing secure communication between an AWS VPC and an on-premises network.
- What are the best practices for securing an AWS VPC, including considerations for security groups, NACLs, and VPN connections?
- How does AWS VPC help organizations achieve network isolation, improved performance, and cost efficiency in their cloud infrastructure deployments?

### Windows Server and Active Directory

- What is Windows Server, and how does it differ from a regular Windows desktop operating system?
- Describe the role of Active Directory (AD) in a Windows Server environment and its significance in network management.
- How can you add the DNS (Domain Name System), AD (Active Directory), and DC (Domain Controller) roles to a Windows Server?
- Explain the purpose of a Domain Controller (DC) and its responsibilities in an Active Directory domain.
- What are the primary components of an Active Directory forest, domain, and organizational unit (OU)?
- Discuss the advantages of using Group Policy Objects (GPOs) in a Windows Server environment for centralized management.
- How can you set up and configure Active Directory Certificate Services (AD CS) for secure certificate management?
- What is the Active Directory Administrative Center (ADAC), and how does it simplify Active Directory management tasks?
- Describe the process of creating and managing user accounts and groups in Active Directory.
- How can you delegate administrative tasks in Active Directory using Role-Based Access Control (RBAC), and why is this important in large organizations?

### Group Policy and ADAC (Active Directory Administrative Center)

- What is Group Policy in Windows Server, and how does it help in managing and configuring Windows-based computers in a network?
- Explain the hierarchy of Group Policy Objects (GPOs) in Active Directory, including Local, Site, Domain, and Organizational Unit (OU) GPOs.
- How can you create and link a Group Policy Object to an organizational unit in Active Directory?
- What are Group Policy settings, and how do they differ from Group Policy Preferences?
- Describe the process of creating and applying a security filter to a Group Policy Object.
- How does Group Policy Inheritance work in Active Directory, and what role does the Local Group Policy play in this process?
- What is loopback processing in Group Policy, and when might it be useful?
- Explain the purpose of the Active Directory Administrative Center (ADAC) and how it simplifies administrative tasks in Active Directory.
- How can you use ADAC to create and manage user accounts, groups, and organizational units in Active Directory?
- Discuss the benefits of using fine-grained password policies in Active Directory, and explain how to configure them using ADAC.
