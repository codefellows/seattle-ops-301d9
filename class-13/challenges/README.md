# Ops Challenge: Powershell AD Automation

## Overview

Powershell can be a powerful tool in administering Active Directory (AD) users and computers. PowerShell AD Automation refers to the use of PowerShell scripting to automate tasks and operations related to Active Directory. Today you'll write a Powershell script to add a new user to AD.

## `New-ADUser` in Powershell

The `New-ADUser` cmdlet in PowerShell is part of the Active Directory module and is used to create a new user account in an Active Directory domain. Active Directory is a directory service developed by Microsoft that manages and organizes network resources, including user accounts, groups, computers, and more. The `New-ADUser` cmdlet allows administrators to automate the process of creating user accounts.

Here's a basic syntax and explanation of some common parameters for the `New-ADUser` cmdlet:

```powershell
New-ADUser -Name <UserName> -SamAccountName <SamAccountName> -UserPrincipalName <UPN> -GivenName <FirstName> -Surname <LastName> -DisplayName <DisplayName> -Path <OUPath> -AccountPassword (ConvertTo-SecureString -AsPlainText "<Password>" -Force) -Enabled $true
```

- `-Name`: Specifies the display name of the user.
- `-SamAccountName`: Specifies the SAM (Security Accounts Manager) account name, which is a unique identifier for the user.
- `-UserPrincipalName`: Specifies the User Principal Name (UPN) for the user. The UPN is in the format of user@domain.com and is used for user authentication.
- `-GivenName`: Specifies the first name of the user.
- `-Surname`: Specifies the last name of the user.
- `-DisplayName`: Specifies the name that is displayed in the Active Directory Users and Computers console.
- `-Path`: Specifies the Organizational Unit (OU) where the user account will be created.
- `-AccountPassword`: Sets the user's password. You should use the `ConvertTo-SecureString` cmdlet to convert a plain text password into a secure string.
- `-Enabled`: Sets whether the user account is enabled (`$true`) or disabled (`$false`).

Here's an example of how you might use the `New-ADUser` cmdlet to create a new user account:

```powershell
New-ADUser -Name "John Cokos" -SamAccountName "jCokos" -UserPrincipalName "jCokos@contoso.com" -GivenName "John" -Surname "Cokos" -DisplayName "John Cokos" -Path "OU=Users,DC=contoso,DC=com" -AccountPassword (ConvertTo-SecureString -AsPlainText "P@ssw0rd" -Force) -Enabled $true
```

In this example, a new user account named "John Cokos" is created with the specified attributes and placed in the "Users" Organizational Unit of the "contoso.com" domain. The account is enabled, and the password is set to "P@ssw0rd" (which should be replaced with a strong password).

Please note that using the `New-ADUser` cmdlet requires administrative privileges in Active Directory, and you should exercise caution and follow your organization's security policies when creating user accounts programmatically.

## Resources

- You will need a Windows Server with AD DS installed and the server promoted to Domain Controller.
- [Microsoft Documentation: New-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2019-ps)

## Demonstration

Refer to [DEMO.md](DEMO.md)
