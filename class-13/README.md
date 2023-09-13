# Class 13

## Class Outline

1. Warm-Up
1. Review
1. Lecture
1. Demo
1. Lab 

## Overview

ADAC (Active Directory Administrative Center) facilitates the convenient administration of user profiles from any Windows endpoint that can achieve connectivity with the DC. This application acts as a user identity control panel capable of many tasks ranging from user creation to simple password changes.

## How does this topic fit?

**Where we've been**:
In the previous class we explored DNS server administration and practice deploying key server roles AD DS, DC, etc.

**What are we focusing on today**:
Today we will focus on Active Directory as a means of authenticating users on the domain.

**Where we're headed**:
In the next class we will be exploring Group Policy and how we can use it to enforce Windows system configurations at scale across the organization.

## Active Directory

### Why
- Active Directory provides a centralized repository for managing user accounts, groups, and computer objects within a network. This centralization simplifies user provisioning, deprovisioning, and authentication processes, making it easier for administrators to manage large numbers of users.
- AD enables Single Sign-On (SSO), allowing users to log in once with their credentials and access various resources (e.g., files, applications, email) without needing to re-enter their username and password for each resource. This improves user experience and security.
- Active Directory allows administrators to define access control policies and permissions for resources such as files, folders, and printers. This ensures that only authorized users or groups can access specific resources, enhancing security and data protection.
- AD includes Group Policy, which enables administrators to define and enforce security and configuration settings across all connected Windows machines in a network. This ensures consistent security and compliance across the organization.
- Active Directory can scale to accommodate large enterprise networks with thousands of users and devices. It also supports redundancy and failover mechanisms to ensure high availability of directory services.
- AD provides a structured and hierarchical directory schema that helps organize and manage network resources efficiently. This schema can be customized to fit the organization's specific needs.
- Active Directory offers security features like Kerberos authentication, encryption, and auditing capabilities. It logs events and activities, making it easier to track and investigate security incidents.
- AD seamlessly integrates with other Microsoft products and services, such as Microsoft Exchange for email, SharePoint for collaboration, and Azure AD for cloud-based identity management. This integration simplifies the deployment and management of Microsoft-based technologies.
- AD allows users to reset their passwords or unlock their accounts without involving IT support, reducing the administrative burden on helpdesk teams.
- Administrators can use scripting languages (e.g., PowerShell) to automate various tasks related to user management, group management, and system configuration, making IT operations more efficient.

### What
- Active Directory (AD): The centralized directory service in Microsoft Windows environments for managing and organizing resources, including user accounts, groups, computers, and more.
- Domain: A logical grouping of network objects (e.g., users, computers) within an Active Directory forest. Domains are used to manage security policies and administer resources.
- Forest: A collection of one or more Active Directory domains that share a common schema, configuration, and global catalog. Forests provide a boundary for security and administrative purposes.
- User Account: A record in Active Directory that represents an individual user and contains information such as username, password, group memberships, and access permissions.
- Group: A collection of user accounts and computer accounts that simplifies the assignment of permissions and access rights. There are different types of groups, including security groups and distribution groups.
- Organizational Unit (OU): A container within a domain used to organize and manage objects in a hierarchical manner. OUs help in applying Group Policies and delegating administrative tasks.
- Group Policy: A feature that allows administrators to define and enforce security and configuration settings for users and computers within an Active Directory environment.
- Single Sign-On (SSO): A mechanism that allows users to log in once and gain access to multiple resources and applications without needing to re-enter their credentials.
- LDAP (Lightweight Directory Access Protocol): A protocol used to communicate with and query directory services like Active Directory. It provides a standardized way to access directory data.
- Kerberos: A network authentication protocol used by Active Directory to provide secure authentication for users and services.
- Trust Relationship: A logical link established between domains or forests to allow users in one domain or forest to access resources in another while maintaining security boundaries.
- Replication: The process of synchronizing directory data between domain controllers in different locations to ensure consistency and fault tolerance.
- Schema: The blueprint or template that defines the structure and attributes of objects stored in Active Directory. It's critical for the consistency and integrity of directory data.
- Global Catalog: A distributed data repository that contains a subset of Active Directory information from all domains in a forest, making it possible to search for objects across the entire forest.
- Security Descriptor: An object's security settings that define who can access and modify it, including permissions and access control lists (ACLs).
- Forest Functional Level: A setting that determines the features and capabilities available in an Active Directory forest, based on the version of Windows Server being used.
- Domain Controller: A server running Windows Server and Active Directory services responsible for managing authentication and directory-related functions within a domain.
- Azure Active Directory (Azure AD): Microsoft's cloud-based identity and access management service, which can be integrated with on-premises Active Directory for hybrid identity solutions.

### How
Active Directory (AD) is a complex system, however, here is a simplified step-by-step overview of the core processes that take place within Active Directory:
- **Installation and Configuration**:
  - Active Directory is installed on one or more Windows Server machines, which become Domain Controllers (DCs).
  - During installation, the first DC in the domain creates the initial AD database and the directory service (ntds.dit) and is known as the Primary Domain Controller (PDC) Emulator.
  - The administrator configures the domain's structure, including the forest, domains, organizational units (OUs), and DNS settings.
- **Object Creation and Management**:
  - Objects such as user accounts, computer accounts, groups, and organizational units are created and managed within Active Directory.
  - Each object has attributes that store information about it, like a user's username, password hash, group memberships, and more.
- **Replication**:
  - AD data is stored on multiple Domain Controllers across the network.
  - Replication ensures that changes made on one DC are synchronized to other DCs within the same domain to maintain consistency.
  - AD uses multi-master replication, meaning any DC can accept updates, but conflicts are resolved automatically.
- **Authentication**:
  - When a user logs in to a computer, the computer sends an authentication request to the nearest DC.
  - The DC validates the user's credentials (username and password) using the Kerberos authentication protocol.
  - If authentication is successful, the DC generates a security token for the user, which contains information about their group memberships and access rights.
- **Authorization and Access Control**:
  - The DC, after authenticating the user, checks the user's group memberships and applies security policies defined in Group Policy Objects (GPOs).
  - The DC then authorizes the user's access to resources based on their group memberships and permissions set on those resources.
- **DNS Resolution**:
  - DNS is critical for Active Directory's operation.
  - AD relies on DNS to locate domain controllers and other AD-related services.
  - Each domain controller registers DNS records that allow clients to find and authenticate to them.
- **Global Catalog**:
  - For cross-domain searches, clients query the Global Catalog (GC) server.
  - The GC contains a partial replica of all objects from all domains within the forest.
  - It provides a quick way to locate objects across the entire forest.
- **Trust Relationships**:
  - Trust relationships can be established between domains or forests to allow users and resources to interact seamlessly across boundaries.
  - Trusts define how authentication and authorization work between domains or forests.
- **Group Policy Application**:
  - Group Policy Objects (GPOs) are applied to user and computer objects based on their location in the AD hierarchy.
  - GPOs control various settings and configurations for users and computers.
- **Backup and Restore**:
  - AD data is critical, and regular backups are essential.
  - Windows Server provides tools for backing up and restoring AD data in case of failures or data corruption.

### Experimentation and Discovery Ideas
- What led to the development of Active Directory, and what problems was it designed to solve in Windows-based network environments?
- How might network management and security differ in an environment without Active Directory?
- What are the potential benefits and drawbacks of centralizing user and resource management, as Active Directory does?
- Can you think of scenarios where decentralization might be a better approach?
- What are the risks or vulnerabilities associated with relying heavily on a single identity management system like Active Directory?
- In an era of hybrid IT environments and cloud services, how does Active Directory adapt, and what challenges does it face?
- What are the considerations when integrating Active Directory with cloud-based identity management, like Azure Active Directory?
- How crucial is DNS in the functioning of Active Directory? What happens if DNS is not configured correctly in an AD environment?
- Can you envision alternative methods of naming and locating resources in a network?
- What impact does Single Sign-On (SSO) have on user productivity and security in an organization?
- Are there scenarios where SSO might not be the best approach, and what alternative authentication methods can you think of?
- How do Group Policy Objects (GPOs) contribute to the management and control of user and computer settings in Active Directory?
- Can you envision a scenario where managing settings without GPOs would be more efficient or practical?
- Considering emerging technologies like blockchain and zero-trust security, how might identity and access management evolve in the future?

## Learning Objectives

### Students will be able to

#### Describe and Define

- ADAC/ADUC
- RSAT
- RBAC
- ABAC

#### Execute
- Students should be able to join Windows endpoints to a domain.
- They should understand how to authenticate as a domain administrator.
- Students should be able to install Remote Server Administration Tools (RSAT) on a Windows 10 endpoint.
- They should know how to configure ADAC to authenticate into the Windows Server, allowing them to manage Active Directory resources.
- Students should be able to create user accounts in Active Directory Administrative Center (ADAC) by providing the required profile information, such as name, job title, department, and organization.
- They should understand how to organize these user accounts into Organizational Units (OUs) based on department.
- Students should be able to verify that the user profiles they created can successfully log in to the Windows 10 endpoint, demonstrating the functionality of Active Directory in managing user access.

## Helpful Resources

- [Professor Messer - Active Directory](https://www.professormesser.com/free-a-plus-training/220-1102/220-1102-video/active-directory-220-1102/){:target="blank"}
- [Microsoft Documentation - Active Directory Administrative Center](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/active-directory-administrative-center){:target="blank"}
- [Microsoft Learn - Active Directory](https://learn.microsoft.com/en-us/search/?terms=active%20directory){:target="blank"}
- [LinkedIn Learning - Active Directory](https://www.linkedin.com/learning/search?keywords=Active%20Directory){:target="blank"}

## Notes
