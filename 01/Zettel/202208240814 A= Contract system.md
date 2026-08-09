**Attachment**:: [[64836A1B-BA57-4290-BA34-23B3BD1AE8BB_1_102_o.jpeg]]
**Date**:: 2022-08-24T08:14:00
**Action**::  
**Topics**:: 
**Type**:: [[Activity]]
**Remarks**:: 
**Person**:: 
**Link**:: 
**Thread**:: 

---
## Notes
![[64836A1B-BA57-4290-BA34-23B3BD1AE8BB_1_102_o.jpeg]]
1. get data from Input site
2. populate contract data to word
	- Site settings -> Site content type
		- create column - mainly text format except for number
	- Settings > Advanced Settings > Allow management of content types -> Yes
		- Documents > Settings > Add from existing site content types
		- now "Document", if click "New", will have "Contract summary"
	- import template to SharePoint
		- Documents > Settings > "Contract Summary"
			- Advanced settings -> Upload a new document template

if(empty(outputs('Get_item')?['body/Paymentterms']),'_',outputs('Get_item')?['body/Paymentterms'])


@{outputs('Get_item')?['body/Paymentterms']}

To do items:
- [ ] #task create group for team access - contract site, power automate [Flow from Input Site to Contract site]
- [ ] #task build up connection between contract site and content site
- [ ] #task communicate with team to use the new contract system


![[D63897AB-A8C1-490C-9685-D68C67E2FE16_1_102_o.jpeg]]