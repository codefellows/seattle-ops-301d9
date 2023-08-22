# Class 01

## Class Outline

1. Welcome and Introduction
1. Discussion: Implicit Bias
1. Course Overview of Ops 301
1. Lecture
1. Demo
1. Lab 

## Overview

The Kali Linux distribution includes a plethora of offensive security software tools that you will find useful in this course. Wielded by pentesters, ethical hackers, forensics investigators, and enthusiasts, Kali Linux is the popular go-to weapon for performing all manner of cyber attacks. Today you will use one of its most infamous tools, Wireshark.

Wireshark is capable of network traffic analysis, and is generally regarded as a computer forensics tool for its ability to "zoom in" and scrutinize network traffic at the lowest level.

## How does this topic fit?

**Where we've been**:
In Ops 201 we learned about remote IT services, virtualization, AWS deployment, troubleshooting, Windows 10 deployment, network setup, pfSense firewall, scripting, and GitHub.

**What are we focusing on today**:
Today we'll learn about network infrastructure. The main topic of today is network traffic analysis using Wireshark.

**Where we're headed**:
Next class will focus on performing a series of basic scanning operations using Nmap and learning more about network ports and protocols.

## Network Traffic Analysis with Wireshark

### Why
- Network traffic analysis allows you to monitor and inspect the data flowing through your network. By analyzing network packets, you can identify unauthorized or malicious activities such as hacking attempts, malware infections, data breaches, and other security threats. This approach helps in detecting and responding to security incidents in real time, minimizing potential damage.
- When a security incident occurs, network traffic analysis can provide valuable insights into the nature and scope of the attack. It helps in understanding the attacker's tactics, techniques, and procedures, which in turn aids in conducting effective incident response and post-incident forensics. This information is crucial for preventing future attacks.
- Network traffic analysis is not only about security. It also plays a role in optimizing network performance. By examining network packets, you can identify bottlenecks, latency issues, packet loss, and other performance-related problems. This data helps network administrators fine-tune network configurations, ensuring smooth and efficient data flow.
- Many organizations have specific network usage policies and compliance requirements that must be adhered to. Network traffic analysis can help ensure that these policies are being followed and that data is being transmitted securely. It provides a way to monitor and enforce rules related to data access, data transfer, and network usage.
- Network traffic analysis enables the identification of unusual or anomalous behavior within the network. This could include sudden spikes in traffic, unusual communication patterns, or unexpected data transfers. Anomaly detection helps in early identification of potential security threats or system failures.
- When network issues arise, analyzing network traffic can help pinpoint the source of the problem. Whether it's a misconfiguration, a faulty device, or a communication breakdown, network traffic analysis provides insights that aid in effective troubleshooting and resolution.
- Understanding how users interact with the network can provide insights into their behavior and needs. Network traffic analysis can help identify patterns of user activity, which can be useful for optimizing network resources, enhancing user experience, and detecting unauthorized behavior.
- By continuously monitoring and analyzing network traffic, organizations can assess potential risks and vulnerabilities within their networks. This information allows them to prioritize security measures and implement appropriate safeguards to mitigate risks effectively.

### What
- Network Traffic Analysis: The process of capturing, inspecting, and analyzing data packets flowing across a computer network to gain insights into network behavior, security threats, and performance issues.
- Packet: A unit of data transmitted over a network. It includes both the data payload and control information, such as source and destination addresses.
- Protocol: A set of rules that govern how data is exchanged between devices on a network. Common protocols include TCP (Transmission Control Protocol), UDP (User Datagram Protocol), HTTP (Hypertext Transfer Protocol), and more.
- Intrusion Detection System (IDS): A security technology that monitors network traffic for suspicious or unauthorized activities and generates alerts when potential intrusions or attacks are detected.
- Intrusion Prevention System (IPS): Similar to an IDS, an IPS not only detects suspicious activities but also takes active measures to prevent unauthorized access or attacks.
- Encryption: The process of converting data into a secure, unreadable format to protect it from unauthorized access. Encryption ensures that only authorized parties can decipher the data.
- Anomaly Detection: The identification of deviations from normal behavior in network traffic or system activity. Anomaly detection helps in identifying potential security threats or performance issues.
- Incident Response: The process of managing and mitigating the aftermath of a security incident or data breach. It involves investigating the incident, containing its impact, and restoring normal operations.
- Payload: The actual data being transmitted within a packet, excluding any control or header information.
- Zero-Day Vulnerability: A software vulnerability that is exploited by attackers before the software vendor releases a patch or fix. It's called "zero-day" because there are zero days of protection after the vulnerability becomes known.

### How
- Using Wireshark on Kali Linux, create a PCAP file consisting of an HTTP GET request to the CERN website.
- In Wireshark, filter your view to only HTTP traffic from Kali to this site.
- Perform an analysis of both the TCP and HTTP traffic.
- Export the capture as a PCAP file.

### Experimentation and Discovery Ideas
- What does a packet header consists of?
- What happens during the TCP Handshake?
- What is an HTTP request?
- What is an HTTP response?
- What kind of information can be found in an HTTP header?
- What is so special about the CERN website?

## Learning Objectives

### Students will be able to

#### Describe and Define

- OSI model
- Kali Linux
- Wireshark
- PCAP
- Packet

#### Execute

- Capture network traffic using Wireshark
- Analyze network traffic and identify protocols of packets
- Analyze a packet and identify its components
- Export network traffic as a PCAP file

## Helpful Resources

- [Wireshark](https://www.wireshark.org/){:target="blank"}
- [Wireshark Cheat Sheet](https://www.comparitech.com/net-admin/wireshark-cheat-sheet/){:target="blank"}
- [Kali Linux](https://www.kali.org/downloads/){:target="blank"}

## Notes

