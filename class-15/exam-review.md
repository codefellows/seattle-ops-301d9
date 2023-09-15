# Exam Review

- What is Cloudflare?
  - Cloudflare is a well-known and widely used web security and performance solution. Cloudflare is known for mitigating DDoS attacks, providing a content delivery network (CDN), and offering various security features.

- What is a CAPTCHA challenge and how does it relate to layer 7 of the OSI model?
  - Completely Automated Public Turing test to tell Computers and Humans Apart, is a security mechanism designed to distinguish between humans and automated bots on the internet.
    - It presents users with a task or puzzle that is easy for humans to solve but difficult for computers to complete accurately.
  - Layer 7 is responsible for the applications and protocols that users interact with, such as web browsers, email clients, and file transfer protocols.
    - It deals with the content, formatting, and encryption of data.
    - Layer 7 (Application Layer) is the highest layer in the model and is closest to the end-user.
  - CAPTCHA challenges operate at the Application Layer of the OSI model. They are implemented as part of the website itself.
  - By placing the CAPTCHA challenge at layer 7, website administrators can effectively protect their applications from automated attacks and malicious activities.
    - This is because layer 7 security measures allow for a more granular understanding of user behavior, enabling the detection of suspicious or abnormal patterns that may indicate bot activity.

- Describe a captive portal referencing FreeRADIUS integrated with AD.
  - FreeRADIUS is an open-source server that provides centralized authentication, authorization, and accounting services (AAA).
  - A captive portal is a web page that users must access before getting network/internet access. Integrating FreeRADIUS with AD allows the captive portal to use AD's user authentication and management capabilities.

- According to Microsoft, what is the Private Memory Limit?
  - The maximum amount of memory that an application pool in IIS (Internet Information Services) can consume.
  - It is a configuration setting that helps allocate dedicated memory for applications within the pool.
  - By setting a specific limit, administrators can control memory usage, prevent excessive consumption, and maintain stability and performance.

- What does this nmap command do?

  `nmap -p1-1000 10.0.2.8`

    - It scans a range of ports 1 to 1000, inclusively, to generate a report of open ports on the IP address 10.0.2.8.

- What is happening when RAID "rebuilds an array"?
  - Redundant Array of Independent Disks (RAID) is a method of combining multiple physical drives into a single unit to enhance performance, fault tolerance, and data redundancy.
  - Replacing a malfunctioning drive with a new drive and allowing the system to rebuild the array is a standard recovery practice in RAID configurations.
  - After a drive failure, when a new drive is added to the array, the RAID software initiates a process called "rebuilding."
    - During this process, data from the remaining drives is copied to the new drive to restore redundancy and integrity.
    - Rebuilding the array ensures that all data is evenly distributed across the drives, maintaining the RAID configuration's integrity.

- What is Windows Defender used for?
  - Windows Defender is a built-in security feature provided by Microsoft for Windows operating systems.
  - It serves as an antivirus and anti-malware solution, offering protection against various types of threats that can compromise the security and stability of a Windows system.

- For each of these services, tell me what port it runs on, what it is, it's purpose:
  - Telnet
    - Port 23
    - Telecommunication Network
    - Telnet provides command-line interface for remote access and management of systems.
  - SSH
    - Port 22
    - Secure Shell
    - SSH enables secure remote access to systems.
  - DNS
    - Port 53
    - Domain Name System
    - DNS translates domain names into IP addresses.
  - SMTP
    - Port 25
    - Simple Mail Transfer Protocol
    - SMTP is used for sending and routing email messages between mail servers.
  - HTTP
    - Port 80
    - Hypertext Transfer Protocol
    - HTTP is the foundation of web browsing.
  - HTTPS
    - Port 443
    - Hypertext Transfer Protocol Secure
    - HTTPS is secure web browsing using encryption.
  - RDP
    - Port 3389
    - Remote Desktop Protocol
    - RDP allows remote desktop access to Windows systems.
  - Ping
    - Ping operates using the Internet Control Message Protocol (ICMP) and does not use a specific port for communication.

- Subnet classes:

  - What constitutes Class A addresses?
    - Range: 1.0.0.0 through 127.255.255.255
    - Subnet Mask: 255.0.0.0
    - Address Allocation: Class A subnets were designed for large networks, allowing for a large number of hosts per network but fewer networks overall.
    - Network ID: First octet (8 bits) is the network ID, while the remaining three octets are used for host addresses. 
    - Host ID: Last three octets (24 bits)
    - Number of Valid Host Addresses: 16,777,214 (2^24 - 2)
    - NOTE the exception: 127.0.0.0/8 – loopback addresses

  - What constitutes Class B addresses?
    - Range: 128.0.0.0 through 191.255.255.255
    - Subnet Mask: 255.255.0.0
    - Address Allocation: Class B subnets were intended for medium-sized networks, balancing the number of networks and hosts per network.
    - Network ID: First two octets (16 bits) represent the network ID, while the last two octets are used for host addresses.
    - Host ID: Last two octets (16 bits)
    - Number of Valid Host Addresses: 65,534 (2^16 - 2)

  - What constitutes Class C addresses:
    - Range: 192.0.0.0 through 223.255.255.255
    - Subnet Mask: 255.255.255.0
    - Address Allocation: Class C subnets were designed for small networks, allowing for a large number of networks but fewer hosts per network.
    - Network ID: First three octets (24 bits) are used for the network ID, while the last octet represents host addresses.
    - Host ID: Last octet (8 bits)
    - Number of Valid Host Addresses: 254 (2^8 - 2)
  
  > Tip: When calculating the number of valid host addresses, we subtract 2 from the total to account for the reserved addresses, the network address (where all bits in the host ID are set to 0) and the broadcast address (where all bits in the host ID are set to 1).

- OSI Model
  - mnemonic: 
    - 7 --> 1: All People Seem To Need Data Processing
    - 1 --> 7: Please Do Not Touch Steve's Pet Alligator
    - 1 --> 7: Please Do Not Throw Sausage Pizza Away
    - 7 --> 1: A Penguin Said To Not Drink Pepsi
        - Ask your chatbot for one relevant to your background... prompt: `Create a mnemonic that makes a sentence for the 7 layer OSI model that's relevant to someone with a background in flower sales.`

  - Physical Layer
    - Layer 1
    - Handles the physical transmission of data over the network, defining specifications for cables, connectors, and other physical aspects.
  - Data Link Layer
    - Layer 2
    - Provides error-free transmission of data frames between directly connected nodes and manages access to the physical medium.
  - Network Layer
    - Layer 3
    - Manages logical addressing, routing, and packet forwarding to enable communication between different networks.
  - Transport Layer
    - Layer 4
    - Ensures reliable and efficient data transfer between end systems, handling segmentation, sequencing, and flow control.
  - Session Layer
    - Layer 5
    - Establishes, manages, and terminates sessions between applications, allowing them to exchange data.
  - Presentation Layer
    - Layer 6
    - Translates, encrypts, and compresses data to ensure compatibility and security during transmission.
  - Application Layer
    - Layer 7
    - Provides high-level protocols for user interactions, such as email, web browsing, file transfer, and remote access.

- What does the `chmod` command do?
  - The chmod command in Unix-like operating systems is used to change the permissions of files and directories.
  - It allows you to modify the access permissions that determine who can read, write, and execute the file or directory.
  - The permissions can be set for three categories of users: the owner of the file, the group associated with the file, and other users.
  - By adjusting the permissions with chmod, you can control access to files and directories, ensuring the security and proper management of your system.
  - ex: `chmod 755 filename`
    - Grants read, write, and execute permissions to the owner, and read and execute permissions to the group and others.

- What is a DNS server configuration file responsible for?
  - It contains information specifying the settings and parameters that defines how the DNS server functions.

- What does it mean to "defragment a database " in Active Directory?
  - Its the process of optimizing the storage and arrangement of data within the Active Directory database files.
  - Over time, as data is added, modified, and deleted within the Active Directory database, it can become fragmented.
    - Fragmentation occurs when the database files contain empty or unused space scattered across various locations, resulting in suboptimal performance and efficiency.
  - Defragmentation can improve the efficiency of maintenance tasks, such as backup and restore operations.
    - A defragmented database reduces the time required for these tasks and minimizes the chances of errors or inconsistencies.

- When configuring a static route in pfSense, explain the difference between the "Destination Network" and the "Gateway".
  - "Destination Network" refers to the network or subnet that you want to reach via a specific route. It represents the network address and subnet mask of the destination network.
  - The "Gateway" refers to the IP address of the next-hop router or gateway device that will be used to reach the destination network. It acts as the intermediary or exit point for traffic heading to the destination network.

- Type of Networks:

  - **LAN**
    - Local Area Network
    - Covers a small geographical area, such as an office, home, or campus. It enables devices within the network to communicate and share resources.

  - **WAN**
    - Wide Area Network
    - Spans a large geographical area, often connecting multiple LANs together. It can cover a city, country, or even span globally. The internet is an example of a WAN

  - **MAN**
    - Metropolitan Area Network
    - Spans a city or metropolitan area. It provides high-speed connectivity and can interconnect multiple LANs.

  - **VPN**
    - Virtual Private Network
    - A secure network that allows users to access a private network over a public network (usually the internet). It enables secure remote access and private communication between users and the network.
    - Ex: a remote worker accessing their company's internal network securely over the internet using a VPN connection.

  - **SAN**
    - Storage Area Network
    - A specialized network that provides high-speed access to shared storage resources. It is commonly used in data centers to connect servers and storage devices.

  - **CAN**
    - Campus Area Network
    - Connects multiple LANs within a university campus, corporate campus, or educational institution.

  - **PAN**
    - Personal Area Network
    - Connects personal devices, such as smartphones, laptops, and wearable devices, within a small personal space.
    - Ex: bluetooth connectivity between a smartphone and a smartwatch, allowing them to exchange data and communicate.

- Difference between internet, intranet and extranet:

  - Internet
    - Network resources available to the general public at large via ISP
    - Open Access Model
      - A network model where resources and information are freely accessible to anyone without restrictions or limitations.
  
  - Intranet
    - Network resources available only to internal employees
    - Closed Access Model
      - A network model where access to resources and information is restricted or limited to a select group of authorized users or entities.

  - Extranet
    - Controlled private network resources only made available by hosting company to its partners, vendors/suppliers, or set of customers.
    - Controlled Access Model
      - A network model where access to resources and information is carefully regulated and managed, typically requiring authentication and authorization mechanisms to ensure only authorized users can access the network.

- What are some possible authentication-related security concerns?
  - Identity duplication
    - Identity duplication refers to the existence of multiple user accounts or identities for the same individual within a system or network, which can cause confusion, administrative challenges, and security risks.
  - Weak or compromised passwords
    - Compromised passwords due to data breaches or phishing attacks can result in unauthorized access to user accounts.
  - Credential theft
    - Attackers may employ various techniques, such as keyloggers, phishing, or malware, to steal user credentials, gaining unauthorized access to systems or sensitive information.
  - Insider threats
    - Employees or individuals with authorized access may misuse their privileges, intentionally or unintentionally.
  - Privilege creep
    - Refers to the gradual accumulation of excessive privileges or access rights granted to a user over time, often due to changes in job roles or responsibilities, leading to potential security risks and unauthorized access.
  - Access control misconfigurations
    - Incorrectly configured access controls, such as granting excessive privileges or not revoking access when needed, can result in unauthorized users gaining access to sensitive data or resources.
  - Social engineering attacks
    - Social engineering techniques, such as phishing or impersonation, can trick users into divulging their credentials or granting access to unauthorized individuals, compromising security.
  - Credential theft
    - Attackers may employ various techniques, such as keyloggers, phishing, or malware, to steal user credentials, gaining unauthorized access to systems or sensitive information.
  - Lack of multifactor authentication (MFA)
    - Relying solely on passwords for authentication increases the risk of unauthorized access. Implementing MFA, which combines multiple factors such as passwords, biometrics, or security tokens, adds an extra layer of security.
  - Third-party vulnerabilities
    - Outsourcing services or relying on third-party applications introduces the risk of security vulnerabilities in their systems, potentially leading to unauthorized access or data breaches.
  - Bring Your Own Device (BYOD) risks
    - Allowing employees to use their personal devices for work purposes can increase the risk of unauthorized access if these devices are not properly secured or managed.

- When configuring a VPN tunnel, what does the "Local Router IP" and the "Remote Router IP" refer to?
  - Local router IP
    - The local router IP refers to the IP address assigned to the router on the local network or device initiating the VPN connection.
    - It is the IP address that identifies the router within the local network.
  - Remote router IP
    - The remote router IP refers to the IP address assigned to the router on the remote network or device with which the VPN connection is being established.
    - It is the IP address that identifies the router within the remote network.

- What is the difference between a hub and a switch?
  - Collision domain
    - A hub operates in a shared collision domain, while a switch creates separate collision domains for each connected device.
      - In a hub, all connected devices share the same bandwidth and network traffic is broadcasted to all devices.
      - A switch forwards packets only to the intended recipient, reducing collisions and improving network efficiency.
  - Traffic handling
    - A hub broadcasts incoming traffic to all connected devices, regardless of the destination.
      - This means that every device on the hub receives all network traffic, resulting in more collisions and potentially slower performance.
    - A switch analyzes the destination MAC addresses of incoming packets and selectively forwards them only to the appropriate device, reducing unnecessary network congestion.
  - Bandwidth
    - Since a hub operates in a shared collision domain, the available bandwidth is divided among all connected devices.
      - As more devices communicate simultaneously, the available bandwidth decreases, leading to slower network speeds.
    - A switch, with its separate collision domains, provides dedicated bandwidth for each connected device, ensuring higher overall network performance.
  - Security
    - A hub provides no inherent security features.
      - Any device connected to a hub can intercept and analyze all network traffic, making it vulnerable to passive sniffing attacks.
    - A switch isolates network traffic between devices, enhancing security by preventing unauthorized access to network packets intended for other devices.

- What does it mean for a hard drive to be "hot-swappable"?
  - The drive can be safely removed and replaced while the system is still running, without requiring a system restart or interrupting the operation.

- Describe and define these common network and web security attacks:

  - Man-in-the-Middle (MitM), also known as "on-path", Attack
    - An attacker intercepts communication between two parties, making them believe they are directly communicating with each other.
    - The attacker can eavesdrop on the conversation, modify or inject data, or impersonate one or both parties.

  - Phishing
    - Involve tricking individuals into revealing sensitive information, such as usernames, passwords, or credit card details, by impersonating a trusted entity through fraudulent emails, websites, or messages.

  - DNS Spoofing
    - A malicious technique where an attacker manipulates the DNS (Domain Name System) resolution process to redirect users to a fake website that looks legitimate but is under the attacker's control.
    - This allows them to perform various malicious activities, such as phishing, stealing sensitive information, distributing malware, or conducting man-in-the-middle attacks.

  - DNS Tunneling
    - A technique that allows the encapsulation of non-DNS traffic within DNS packets to bypass network security controls.
    - The attacker abuses the DNS protocol's ability to carry arbitrary data by encoding the non-DNS traffic within DNS queries and responses.
    - DNS tunneling is often employed as an evasion technique to bypass firewalls, intrusion detection systems, or content filtering mechanisms that may be monitoring or blocking specific types of traffic.

  - Denial-of-Service (DoS) Attack
    - Aims to disrupt or deny access to a network, system, or service by overwhelming it with a flood of traffic or resource exhaustion, rendering it unable to function properly.

  - Distributed Denial-of-Service (DDoS, pronounced: "dee-doss", rhymes with "free-floss") Attack
    - Similar to a DoS attack, a DDoS attack involves multiple compromised systems (a botnet) flooding the target with a massive volume of traffic, making it even more difficult to mitigate.

  - SQL Injection
    - An attacker exploits vulnerabilities in a web application's input fields to insert malicious SQL code.
    - This allows the attacker to manipulate the application's database to gain unauthorized access to, extract, or destroy sensitive information.

  - Cross-Site Scripting (XSS)
    - Involves injecting malicious scripts into web pages viewed by users.
    - When the script executes in the user's browser, it can steal sensitive information, perform actions on behalf of the user, or deface the website.

  - Cross-Site Request Forgery (CSRF)
    - Trick users into unknowingly performing unwanted actions on a website where they are authenticated.
    - By exploiting the user's trust in the website, the attacker can carry out actions such as changing account settings or making unauthorized transactions.
  
  - Malware Attacks
    - Malicious software that is designed to damage, disrupt, or gain unauthorized access to systems.
    - Common types include viruses, worms, trojans, ransomware, and spyware.