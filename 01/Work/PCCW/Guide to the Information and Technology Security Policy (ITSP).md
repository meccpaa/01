---
Type:
Created: 2026-08-27 11:40
---
15 distinct domains
Applied to all group entities, personnel and 3rd parties (e.g. vendors and partners who access our information assets)
- information owner
- information assets
- CIA triad: confidentiality (no unauthorized disclosure), integrity (accurate data), availability (systems up)

### Section 1: Information Security Policies
- Policy management - living document, reviewed annually or when critical changes occur
- Compliance is Mandatory
### Section 2: Organization of Information Security
- Segregation of Duties - critical functions are divided among different people
- Security in Project Management
### Section 3: Human Resource Security
covers the entire employee lifecycle
- prior to employment
- during employment
- termination or change of role

#### Key responsibilities for maintaining a secure environment
- follow policies and procedures
- protect sensitive information
- report security concerns - askit@pccw.com, ITSecurity@pccfw.com

### Section 4: Asset Management - Know It, Classify It, Protect It
Know it: Inventory of Assets, incl. data, hardware, software, and 
-  entrusted to PCCW/HKT
- rented or leased by PCCW / HKT
- used by service providers to deliver services to PCCW / HKT

#### Understanding, Owning, and Using Company Resources
- Definition of assets
- Ownership and accountability
- Acceptable use

- End-of-Life Systems - risk on outdated OS, library, or application server; must be replaced or decommissioned timely
- Ownership of Assets - with designated information owner, 
- Acceptable Use of Assets - 

#### Device and Data Handling
1. Secure devices - unauthorized access and physical theft; password-protected and encrypted
2. mitigate USB/Media Risks
3. Approved storage usage

#### Media Handling
1. Management of removable media
2. disposal of media
3. physical media transfer

#### Information classification
- strictly confidential
- confidential
- internal
- public domain

#### Labelling of information
- information classification
- output labelling
- classification review

### Section 5: Access Control

only the right people access the right data at the right time.
core principles: least privilege, need to know, segregation of duties
golden rules for all staff: 
- no shared accounts, 
- no external devices on the internal network

#### Access Control Best Practices
- robust authentication
- unique user identification
- least privilege principle (need to know basis)

#### Common Access Dangers
- Password Sharing
- Unlocked Devices
- Unsafe Remote Access

#### Business requirements of access control
remote access (VPN): all remote access to the Group internal network requires MFA. There is no exception

#### User Access Management
- user access provisioning - approval process
- management of privileged access
- physical media transfer

#### System and Application Access Control
Enforce mandatory password management system
1. password complexity - 8 character, with uppercase, lowercase and numbers
2. enforce password history
3. enforce password expiration
4. account lockout


### Section 6: Cryptography - Encrypting Our Most Sensitive Data

the use of encryption to protect data
when: mandatory for strictly confidential and confidential information
key management

### Section 7: Physical & Environmental Security
clear desk clear screen policy
unattended equipment
secure areas
equipment sitting and protection

### Section 8: Operations Security - Keeping Our Services Secure Available
focuses on the secure day-to-day running of our production systems
- documented procedures
- change management - goal: prevent unplanned changes from causing outages
	- every change must have an impact analysis, approval, implementation plan, and rollback plan
- capacity management

#### Protection from Malware and Backup
#### Mobile devices and Teleworking
#### Secure system practices
- approved software only
- updates and patches awareness

#### Secure Communication Methods
- use approved tools
- avoid unsecured networks
- verify sender identity

#### Data Protection
- data masking
- data leakage prevention

### Section 9: Communications Security - Securing Data in Motion
- Network segregation
- Information transfer
- Web filtering

### Section 10: System Acquisition, Development and Maintenance - Security by Design
- Security by design
- Secure coding: input validation, secure error handling, code scanning and review
- Access to source code: 
	- all source code must be stored in secure, centralised source code management system, 
	- using unauthorized repositories (e.g. personal GitHub accounts) for company code is strictly prohibited

#### Test Data
production data, esp strictly confidential and confidential information, shall not be used in non-production environments (development, testing, UAT)

### Section 11: Third Party Relationships
- Policy for 3rd parties
- Security in agreements
- Your responsibility

#### Third-party risks
- vendor risks
- share minimum data
- watch for supplier fraud

### Section 12: Information Security Incident Management
responsibilities, reporting, severity classification, learning from incidents (after every incident, a post-mortem and root cause analysis are performed to prevent recurring. all remedial actions are tracked)

### Section 13: Information Security Aspects of Business Continuity Management
ensure our critical services can survive a major disaster.
- planning: 
- verification
- redundancy

