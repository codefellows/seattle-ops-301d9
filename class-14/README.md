# Class 14

## Class Outline

1. Diversity, Equity, Inclusion and Belonging Open Discussion
1. Review
1. Lecture
1. Demo
1. Lab 

## Overview

Systems administrations can use OUs (Organizational Units) and GPOs (Group Policy Objects) to apply computer configurations to specific departments or teams in the organization. Group policy can be used to protect user data by applying folder redirection to the Windows user files.

## How does this topic fit?

**Where we've been**:
Previously we focused on Active Directory as a means of authenticating users on the domain.

**What are we focusing on today**:
Today we'll be exploring Group Policy and how we can use it to enforce Windows system configurations at scale across the organization.

**Where we're headed**:
Next class we will be preparing to take the 401 Entrance Exam and for Final Projects.

## Group Policy

### Why
- Group Policy enables administrators to centralize the management of various settings, configurations, and security policies for multiple users and computers in an organization. This centralization simplifies the administrative tasks and reduces the need for manual configuration on each individual machine.
- Group Policy ensures consistency in system configurations and security settings across the network. This consistency is critical for maintaining a standardized and secure IT environment, reducing the risk of configuration errors and security vulnerabilities.
- Group Policy helps enhance network security by allowing administrators to enforce security policies, such as password complexity requirements, account lockout policies, firewall settings, and more. It helps protect against unauthorized access and data breaches.
- Many organizations must adhere to industry-specific regulations and compliance standards (e.g., HIPAA, GDPR, PCI DSS). Group Policy can help enforce the necessary security and privacy settings to meet these requirements.
- Group Policy reduces the time and effort required for system administration tasks. Instead of manually configuring each computer, administrators can apply changes and updates to multiple machines simultaneously, saving both time and labor costs.
- Group Policy can be applied to remote computers, making it a valuable tool for managing and configuring machines that are not physically present in the same location as the administrator.
- Group Policy can be used to deploy software applications, updates, and patches to computers in the network, ensuring that all machines have the required software and security updates.
- Group Policy is highly configurable and flexible, allowing administrators to create custom policies that meet the specific needs of their organization.

### What
- Group Policy (GP): The feature in Microsoft Windows that allows administrators to define and enforce policies and settings for users and computers within a network environment.
- Active Directory (AD): A directory service provided by Microsoft that stores and organizes information about network resources, including users, groups, and computers.
- Group Policy Object (GPO): A container for Group Policy settings that can be applied to users, computers, or groups in an Active Directory domain.
- Domain: A logical grouping of network resources, users, and computers in an Active Directory environment.
- Organizational Unit (OU): A container within Active Directory that allows administrators to organize and manage users, groups, and computers.
- Policy Setting: A specific configuration or rule defined within a Group Policy Object, affecting system behavior or security.
- Group Policy Editor: A Windows tool (Group Policy Management Console or gpedit.msc) used to create, edit, and manage Group Policy settings.
- Security Policy: A set of rules and configurations that define security settings, including password policies, account lockout policies, and user rights assignments.
- Group Policy Inheritance: The process by which GPOs are applied to objects in a hierarchical manner, allowing settings from multiple GPOs to accumulate.
- Enforcement: The process of ensuring that Group Policy settings are applied and cannot be overridden by lower-level policies.
- Group Policy Filtering: The process of applying GPOs selectively to specific users, groups, or computers based on criteria such as WMI filters or security filtering.
- Loopback Processing: A feature that allows Group Policy to be applied to users based on the location of the computer, not just the user.
- WMI Filter: A filter used to determine whether a GPO should be applied to a computer based on the computer's attributes.
- Scope of Management (SOM): The scope within Active Directory where a Group Policy Object is linked, determining which objects are affected by the GPO.
- Group Policy Template: A predefined set of settings for common configurations, which can be imported and applied to a GPO.
- Resultant Set of Policy (RSoP): A tool for analyzing and troubleshooting the effective Group Policy settings on a computer.
- Group Policy Preferences (GPP): An extension of Group Policy that allows administrators to configure settings such as mapped drives, printers, and registry keys.
- Group Policy Central Store: A centralized location for storing administrative templates used by Group Policy.
- Backup and Restore (GPO): The process of backing up and restoring Group Policy Objects.
- Group Policy Update: The process of refreshing Group Policy settings on a computer, typically done at regular intervals or manually triggered.

### How
Group Policy works through a series of processes to ensure that the configured policies are applied consistently across the network. Here's an explanation of how Group Policy works:
- **Creation and Configuration of Group Policy Objects (GPOs)**:
  - **Step 1:** Administrators create Group Policy Objects (GPOs) using the Group Policy Management Console (GPMC) or the Local Group Policy Editor (gpedit.msc) on individual machines.
  - **Step 2:** Within a GPO, administrators configure settings, policies, and preferences. These settings can include security policies, software installation, registry settings, and more.
  - **Step 3:** Administrators can link GPOs to specific Active Directory containers, such as domains, organizational units (OUs), or sites. This determines where the GPO will apply within the AD hierarchy.
  - **Step 4:** Administrators can also use filters like WMI filters and security filtering to further refine which users, groups, or computers the GPO will affect.
- **Client-Side Processing**:
  - **Step 5:** Windows clients (computers and users) within the AD domain periodically check for Group Policy updates. This typically happens every 90 minutes, with a randomized offset to prevent network congestion.
  - **Step 6:** When a client starts up or logs in, it initiates a Group Policy update. Additionally, an administrator can manually trigger a Group Policy update using the `gpupdate` command.
- **Location of Group Policy Objects**:
  - **Step 7:** The client identifies its location in the AD hierarchy. It determines the site, domain, and OU it belongs to.
  - **Step 8:** The client retrieves a list of GPOs linked to its location in the AD hierarchy. This list includes GPOs linked to the site, domain, and OUs that apply to the client.
- **Applying Group Policy Settings**:
  - **Step 9:** The client processes the list of GPOs in the order specified (local, site, domain, OU). It checks each GPO for security filtering and WMI filtering criteria to determine if it should be applied.
  - **Step 10:** If a GPO is applicable, the client retrieves the GPO settings and configurations from the network. This includes security settings, registry changes, and more.
  - **Step 11:** The client applies the settings from each GPO in the specified order. Settings from higher-level GPOs are typically overridden by settings in lower-level GPOs, but exceptions exist, such as when settings are configured with the "Enforced" option.
  - **Step 12:** The client updates its local Group Policy settings database with the applied GPO settings.
- **Resultant Set of Policy (RSoP)**:
  - **Step 13:** The client calculates the Resultant Set of Policy (RSoP) based on the applied GPO settings. The RSoP provides a comprehensive view of the effective policy settings for that client.
- **Execution of Group Policy Scripts and Software Installation**:
  - **Step 14:** If GPOs include login or startup scripts, the client executes these scripts. Login scripts can be batch files or PowerShell scripts that perform specific tasks during login.
  - **Step 15:** If GPOs are configured for software installation, the client installs or updates software packages defined in the GPO.
- **Policy Refresh and Maintenance**:
  - **Step 16:** After initial processing and during regular intervals, clients continue to periodically check for Group Policy updates. This ensures that GPO settings remain up to date and that changes made by administrators are applied.
- **Logging and Reporting**:
  - **Step 17:** Windows Event Logs on client computers and domain controllers record Group Policy processing events and errors. These logs are valuable for troubleshooting and auditing.
- **End User or Computer Interaction**:
  - **Step 18:** Finally, the user or computer interacts with the system based on the applied policies and configurations. These policies can affect a wide range of behaviors, including security, desktop appearance, software availability, and more.

### Experimentation and Discovery Ideas
- Imagine you're tasked with improving the efficiency of a large organization's IT infrastructure. How might you experiment with Group Policy to achieve this goal, and what potential challenges or obstacles do you foresee in implementing these experiments?
- Consider the principle of "security by design." How can Group Policy be leveraged to create a more secure network environment, and what experimental approaches could be taken to continuously enhance security through policy settings?
- In the context of Group Policy, what role does user experience play, and how might you experiment with policies to balance security and user productivity? Can you think of any real-world examples where organizations have struggled to strike this balance effectively?
- Group Policy allows for the deployment of software and updates. How could you experiment with this feature to optimize software distribution in an organization, reduce downtime, or minimize network traffic?
- Imagine you are managing a network in a rapidly evolving industry. How might you use Group Policy to quickly adapt to new technological advancements or security threats? What experiments could you conduct to ensure your network remains agile and responsive?
- What are the ethical considerations when using Group Policy to monitor and control user activities within an organization? How might you experiment with policy settings to strike a balance between monitoring for security purposes and respecting individual privacy?
- Think about the future of Group Policy. How might emerging technologies like cloud computing, IoT, and AI impact the way we use Group Policy for network management? What experiments could you conduct to explore these potential advancements?
- Consider the concept of "failure as a learning opportunity." Can you think of a scenario where a network experienced issues due to misconfigured Group Policies, and what lessons could be learned from such an incident? How might you experiment with policy deployment and testing to minimize such failures?

## Learning Objectives

### Students will be able to

#### Describe and Define

- OU
- GPO
- Group Policy Editor
- Group Policy management (GPMC or AGPM)

#### Execute
- Students should be able to create a domain user account within Active Directory.
- Students should understand the purpose of OUs in Active Directory.
- They should be able to create an OU and associate it with a specific group of users or computers.
- Students should be able to create a new GPO using the Group Policy Management Console (GPMC).
- They should understand how to configure settings and policies within a GPO.
- Students should be capable of setting up a file share on a Windows Server.
- Ideally, they should also be able to apply basic security settings to the file share to limit access to the intended user(s).
- Students should understand how to link a GPO to an Organizational Unit.
- They should know how to associate a GPO with a specific domain user account.
- Students should be able to test the effectiveness of the Group Policy by performing actions on the client machine (e.g., saving a picture) and verifying the expected results on the Windows Server (e.g., the appearance of the saved picture in the shared folder).
- They should understand the concepts of Group Policy application, including the need for user logins or manual policy updates using `gpupdate`.

## Helpful Resources

- [Professor Messer - Group Policy](https://www.professormesser.com/security-plus/sy0-401/group-policy/){:target="blank"}
- [Group Policy Planning and Deployment Guide](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754948(v=ws.10)){:target="blank"}
- [Back to Basics: Groups vs Organizational Units in Active Directory](http://techgenix.com/back-basics-groups-vs-organizational-units-active-directory/){:target="blank"}
- [Microsoft Learn - Group Policy](https://learn.microsoft.com/en-us/search/?terms=Group%20Policy){:target="blank"}
- [Microsoft Certification - Azure Administrator Associate](https://learn.microsoft.com/en-us/certifications/azure-administrator/){:target="blank"}
  - While not specifically focused on Group Policy, this certification covers a wide range of Azure and Windows administration topics, including Group Policy management in Azure Active Directory.

## Notes
