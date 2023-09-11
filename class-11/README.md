# Class 11

## Class Outline

1. Warm-Up
1. Review
1. Lecture
1. Demo
1. Lab 

## Overview

Microsoft Windows Server is an OS that facilitates the hosting of critical authoritative Windows services on the network, including Active Directory, DNS, DHCP, and Domain Controller roles. Microsoft's Evaluation Center allows for the use of Windows Server for 180 days free with full functionality. When deployed in tandem with Windows 10 Pro endpoints, once can establish a domained LAN with little more than VirtualBox and some relevant Microsoft documentation.

## How does this topic fit?

**Where we've been**:
In the previous class we performed cloud computing with AWS.

**What are we focusing on today**:
Today we'll be introduced to servers, what they are and why they're high value assets.

**Where we're headed**:
n the next class, we'll be exploring DNS server administration and practice deploying key server roles AD DS, DC, etc.

## Windows Server

### Why
- ITIL (Information Technology Infrastructure Library) streamlines IT service management processes, while Agile enables adaptive project management, increasing efficiency.
- Both frameworks emphasize delivering services and products that meet or exceed customer expectations.
- ITIL reduces operational costs through optimized processes, while Agile's iterative approach can lead to faster delivery and cost savings.
- Windows Server 2019 offers centralized tools for efficient server management, enhancing control and monitoring capabilities.
- It includes advanced security features like Windows Defender ATP, enhancing protection against modern threats.
- Windows Server 2019 seamlessly integrates with Azure, simplifying hybrid cloud management and workload migration.
- RAID (Redundant Array of Independent Disks) provides data redundancy, ensuring data accessibility even when disk drives fail, minimizing data loss and downtime.
- Certain RAID configurations enhance data access speed by distributing data across multiple drives.
- RAID configurations can be expanded to accommodate growing storage needs without data loss.
- RAID helps maintain data integrity by detecting and correcting errors, and it complements backup strategies for enhanced data protection.

### What
- Service Management: The practice of designing, delivering, managing, and improving IT services to meet business needs.
- Incident Management: The process of managing and resolving incidents to restore normal service operations as quickly as possible.
- Problem Management: The process of identifying and addressing the root causes of recurring incidents or problems within IT services.
- Change Management: The process of controlling and managing changes to IT services, minimizing the risk of service disruptions.
- Service Request Management: The process of handling service requests from users or customers, such as access requests or software installations.
- Service Level Agreement (SLA): A formal agreement that defines the level of service a customer can expect and the responsibilities of the service provider.
- Key Performance Indicator (KPI): Metrics used to evaluate the performance and effectiveness of IT services and processes.
- Scrum: A specific Agile framework that emphasizes iterative development, with fixed-length time frames called sprints.
- Kanban: An Agile method that focuses on visualizing and managing work in progress to optimize workflow and efficiency.
- User Story: A user-centric description of a software feature or functionality, often written in a specific format (As a [user], I want [feature] so that [benefit].).
- Sprint: A fixed time frame (usually 2-4 weeks) in Scrum for completing a set of user stories or tasks.
- Product Owner: A role in Agile responsible for defining and prioritizing the product backlog and ensuring the development team builds the right features.
- Scrum Master: A role in Scrum responsible for facilitating the Scrum process and removing impediments to the team's progress.
- Continuous Integration (CI): The practice of automatically integrating code changes into a shared repository and running tests to ensure code quality.
- Active Directory (AD): A directory service developed by Microsoft for managing and organizing resources in a Windows network environment.
- Cluster Sets: A feature in Windows Server 209 that enables the creation of large-scale clusters for high availability and failover capabilities.
- Windows Admin Center: A web-based management tool for Windows Server that provides a centralized interface for server administration.
- RAID 0 (Striping): A RAID level that stripes data across multiple disks for improved performance but offers no redundancy.
- RAID 1 (Mirroring): A RAID level that duplicates data on two drives for fault tolerance and redundancy.
- RAID 5 (Parity): A RAID level that uses parity information to provide data redundancy with efficient use of storage.
- RAID 6 (Double Parity): Similar to RAID 5 but with double parity for increased fault tolerance.
- Hot-Swapping: The ability to replace a failed drive in a RAID array without shutting down the system.
- Data Integrity: Ensuring the accuracy and reliability of data through error detection and correction mechanisms.
- Storage Performance: The speed and efficiency at which data can be read from or written to storage devices.

### How
**How does ITIL work?**
  - Service Strategy: ITIL aligns IT services with business objectives, defines service levels, and ensures financial planning and demand management.
  - Service Design: ITIL focuses on designing services, technology architecture, and processes, including capacity, availability, and IT service continuity management.
  - Transition to Service: ITIL guides the transition of services from development to production, including change management, configuration management, and release and deployment management.
  - Service Operation: ITIL provides daily operational guidance for incident management, problem management, request fulfillment, event management, and access management.
  - Continual Service Improvement (CSI): ITIL fosters a culture of continuous improvement through measurement, analysis, identifying areas for enhancement, implementing improvements, and gathering feedback.
**How does Agile Methodology work?**
  - User-Centric Approach: Prioritizing user needs through user stories and frequent feedback.
  - Iterative Development: Breaking projects into small, manageable iterations (sprints) for incremental progress.
  - Cross-Functional Teams: Collaborating across roles to deliver working increments of the product.
  - Continuous Testing: Regularly testing and refining to improve product quality.
  - Adaptability: Quickly responding to changing requirements and customer feedback to deliver value.
**How does RAID work?**
  - Data Redundancy: Storing data redundantly across multiple drives to ensure availability and fault tolerance.
  - Data Striping: Distributing data across multiple drives for improved read/write performance.
  - Parity Calculation: Using parity information for error detection and correction, enhancing data integrity.
  - Fault Tolerance: Allowing the system to continue operation even if one or more drives fail.
  - Scalability: Enabling storage capacity expansion without data loss by adding additional drives to the array.

### Experimentation and Discovery Ideas
- What are the key business benefits of implementing ITIL practices in an organization, and how might these benefits be measured or quantified?
- Can you think of a real-world scenario where a lack of standardized IT service management processes could lead to negative consequences for a business or its customers?
- How might the adoption of ITIL principles impact the role of IT professionals within an organization, and what skills or changes in mindset might be required to embrace this framework?
- In your opinion, what are the most significant advantages of Agile methodologies like Scrum or Kanban when compared to more traditional project management approaches?
- How does Agile encourage teams to adapt to changing customer requirements during a project, and can you provide an example of a situation where this adaptability could be beneficial?
- Agile places a strong emphasis on collaboration and self-organizing teams. How might fostering a culture of collaboration improve overall team performance and innovation?
- What are the key considerations when deciding whether to migrate to Windows Server 2019 or continue using an older version of Windows Server in an organization?
- How does Windows Server 2019 facilitate hybrid cloud integration, and can you envision a specific use case where this integration would be advantageous for a business?
- What security challenges might organizations face in the context of Windows Server 2019, and how does this version address those challenges compared to its predecessors?
- When selecting a RAID configuration, how should an organization balance the trade-offs between data redundancy, storage capacity, and performance? Can you provide a real-world scenario to illustrate this?
- In what situations would you recommend RAID 1 (mirroring) over RAID 5 (parity), or vice versa, considering both data protection and storage efficiency?
- Can you think of a scenario where the hot-swapping feature of RAID configurations could significantly impact business continuity and system uptime?

## Learning Objectives

### Students will be able to

#### Describe and Define

- ITIL Framework
- Agile Methodology
- Windows Server 2019
- Enhanced Security Configuration
- Workgroup
- Domain
- Client-server architecture
- Types of servers
- RAID configuration types

#### Execute

- Given a budget, select and recommend a physical server
- Install Windows Server 2019
- Set Windows Server to a static IP address
- Configure IE security settings
- Create a network topology diagram

## Helpful Resources

- For a more comprehensive introduction to Agile, take LinkedIn's [Agile Foundations Online Class](https://www.linkedin.com/learning/agile-foundations){:target="blank"}.

## Notes
