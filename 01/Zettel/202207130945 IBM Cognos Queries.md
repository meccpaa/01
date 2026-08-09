**Attachment**:: 
**Date**:: 2022-07-13T09:45:00
**Action**::  
**Topics**:: 
**Type**:: [[Coding]]
**Remarks**:: 
**Person**:: 
**Link**:: 

---
## Notes

#### [[Partner query]]
```SQL
if([Interco Co] = 'BNB' or [Interco Co] = 'AIP' or [Interco Co] = 'BBI' or [Interco Co] = 'BNE' or [Account] = '144802' or [Account] = '146032' or [Account] = '146222'  or [Account] = '146223'   or [Account] = '515814' or [Account] = '515585' or [Account] = '515586' or [Account] = '516564' or [Je Desc] contains 'BO&E (CY87)' or [Je Desc] contains '(IPS)' or [Je Desc] contains 'CX71' or [Je Desc] contains 'CR44' or [Je Desc] contains 'from 102' or [Je Desc] contains 'Being recharge of corporate function staff cost') then ('I/C: PCCW Media Limited')

else (if([Interco Co] = 'BHE' or [Interco Co] = 'BHP' or [Interco Co] = 'BIV' or [Interco Co] = 'BHC' or [Interco Co] = 'BHP' or 
[Account] = '146024' or [Account] = '146021' or [Account] = '146023' or [Account] = '146020'
 or [Account] = '146021' or [Je Name] contains 'TSSF5RHG') then ('I/C: HONG KONG TELECOMMUNICATIONS (HKT) LIMITED')

else (if([Interco Co] = 'BHU' or [Account] = '146058') then ('I/C: ESMARTHEALTH LIMITED')

else (if([Interco Co] = 'BAF' or [Account] = '146006') then ('I/C: HKT SERVICES LIMITED')

else (if([Interco Co] = 'AJG' or [Account] = '143654') then ('I/C: POWER LOGISTICS LIMITED')

else (if([Interco Co] = 'AHI' or [Account] = '146043') then ('I/C: HK TELEVISION ENTERTAINMENT COMPANY LTD')

else (if([Interco Co] = 'AHM' or [Account] = '147100') then ('I/C: PCCW HKT')

else (if( [Interco Co] = 'BER' or [Account] = '146099' ) then ('I/C: HKT PAYMENT LIMITED')

else (if([Interco Co] = 'BET' or [Account] = '146131') then ('I/C: THE CLUB TRAVEL SERVICES LIMITED')

else (if([Interco Co] = 'BER' or [Account] = '146099') then ('I/C: HKT PAYMENT LTD')

else (if( [Interco Co] = 'BED' or [Account] = '146098') then ('I/C: CLUB HKT LIMITED')

else (if([Interco Co] = 'AOF' or [Interco Co] = 'AWB' or [Interco Co] = 'BMM' or [Interco Co] = 'BWJ' or [Interco Co] = 'BWC' or
[Account] = '143619' or [Account] = '146201' or [Account] = '146204' or [Account] = '146119' or [Account] = '143871') then ('I/C: CSL MOBILE LIMITED')

else (if([Interco Co] = 'AEB' or [Interco Co] = 'ALW' or [Account] = '147278' or [Account] = '143525') then ('I/C: PCCW GLOBAL LIMITED')

else (if( [Interco Co] = 'BDB' or [Interco Co] = 'BDC' or [Interco Co] = 'BDD' or [Interco Co] = 'BDE' or [Interco Co] = 'BDA' or [Account] = '144852' or [Account] = '144853' or [Account] = '144854' or [Account] = '144855') then ('OTT I/C: SBD')

else (if([Interco Co] = 'AJE' or [Account] = '143691') then ('I/C: PCCW TELESERVICES HOLDING COMPANY LTD (BVI)')

else (if([Interco Co] = 'BSL' or [Interco Co] = 'ABA' or [Account] = '143697' or [Account] = '143510') then ('I/C: Solutions')

else (if([Interco Co] = 'AWE' or [Account] = '143872') then ('I/C: PCCW DIGITAL SOLUTIONS LIMITED')

else (if([Interco Co] = 'BST' or [Account] = '144840' or [Je Name] contains 'BASCORPLQ06') then ('I/C: PH Solutions')

else (if([Interco Co] = 'BSG' or [Account] = '144849') then ('I/C: SG Solutions')

else (if([Interco Co] = 'BAT' or [Interco Co] = 'ADM' or [Account] = '146046' or [Account] = '143839') then ('I/C: PC MUSIC HOLDINGS LIMITED')

else (if([Interco Co] = 'BBC' or [Account] = '144843') then ('OTT I/C: OTT HK')

else (if([Interco Co] = 'BVK' or [Account] = '144847') then ('OTT I/C: MOOV')

else (if([Interco Co] = 'AHY' or [Account] = '143617') then ('I/C: PCCW Productions Limited')

else (if([Interco Co] = 'APP' or [Account] = '147004') then ('I/C: PCCW')

else (if([Interco Co] = 'APA' or [Account] = '147006' or [Je Name] contains 'HCOANT') then ('I/C: PCCW Services Limited')

else (if([Interco Co] = 'AHN' or [Account] = '143608') then ('I/C: PCCW INTERACTIVE MEDIA HOLDINGS LIMITED')

else (if([Interco Co] = 'BBU' or [Account] = '144839') then ('OTT I/C: VUCLIP CONSOLIDATION')

else (if([Interco Co] = 'BLO' or [Account] = '146081') then ('I/C: GATEWAY COMMUNICATIONS PTY LTD (SOUTH AFRICA)')

else (if([Interco Co] = 'BBO' or [Account] = '144836') then ('OTT I/C: PCCW OTT (CAYMAN ISLANDS) HOLDINGS LIMITED')

else (if([Interco Co] = 'AEH' or [Account] = '143607') then ('I/C: PCCW GLOBAL, INC.')

else (if([Interco Co] = 'AIJ' or [Account] = '147378') then ('I/C: VDC POWERBASE HONG KONG DATA CENTERS LIMITED')

else (if([Interco Co] = 'BAJ' or [Account] = '146009') then ('I/C: PCCW MEDIA HOLDINGS LIMITED')

else (if([Interco Co] = 'AUP' or [Account] = '147071') then ('I/C: PCCW NETWORK SERVICES LTD')

else (if([Interco Co] = 'BBP' or [Account] = '146015') then ('I/C: NOW PRODUCTIONS LIMITED')

else (if([Interco Co] = 'BDF' or [Account] = '144861') then ('OTT I/C: PCCW OTT SERVICES LIMITED')

else (if([Interco Co] = 'BBR' or [Account] = '144841') then ('OTT I/C: VIU INTERNATIONAL LIMITED')

else (if([Interco Co] = 'BBD' or [Account] = '144844') then ('OTT I/C: PCCW OTT (Singapore) Pte. Ltd')

else (if([Interco Co] = 'BBE' or [Account] = '144845') then ('OTT I/C: PCCW OTT (THAILAND) COMPANY LIMITED')

else (if([Interco Co] = 'BDP' or [Account] = '144865') then ('OTT I/C: PCCW OTT (PHILIPPINES), INC.')

else (if (upper([Je Desc]) contains 'GOOGLE') then ('GOOGLE ASIA PACIFIC PTE LTD') 
else (if (upper([Je Desc]) contains 'APPLE') then ('Apple') 
else (if (upper([Je Desc]) contains 'ADYEN') then ('Adyen')
else (if (upper([Je Desc]) contains 'SPOTX') then ('SpotX')
else (if (upper([Je Desc]) contains 'INMOBI') then ('inmobi')
else (if (upper([Je Desc]) contains 'PUBMATIC') then ('Pubmatic')
else (if (upper([Je Desc]) contains 'XANDR') then ('Xandr')
else (if (upper([Je Desc]) contains 'UDOMAIN') then ('Udomain')
else (if (upper([Je Desc]) contains 'AWS' or upper([Je Desc]) contains 'AMAZON') then ('AMAZON WEB SERVICES INC')
else (if (upper([Je Desc]) contains 'FB') then ('FACEBOOK IRELAND LIMITED')
else (if (upper([Je Desc]) contains 'FACEBOOK') then ('FACEBOOK IRELAND LIMITED')
else (if (upper([Je Desc]) contains 'ZEBRA') then ('ZEBRA STRATEGIC OUTSOURCE SOLUTION LIMITED')
else (if (upper([Je Desc]) contains 'MASTERLINK') then ('Masterlink')
else (if (upper([Je Desc]) contains 'AKAMAI') then ('Akamai')
else (if (upper([Je Desc]) contains 'RUBICON') then ('Rubicon') 
else (if (upper([Je Desc]) contains 'ADCOLONY') then ('Adcolony') 
else (if (upper([Je Desc]) contains 'OPENX') then ('OpenX') 
else (if (upper([Je Desc]) contains 'CLEVERTAP') then ('CleverTap') 
else (if (upper([Je Desc]) contains 'APP ANNIE') then ('App Annie') 
else (if (upper([Je Desc]) contains 'ASIAPAY' or upper([Je Desc]) contains 'MOOV ECOMM' or upper([Je Desc]) contains 'EMOTO' or upper([Je Desc]) contains 'MOOV MOTO' or upper([Je Desc]) contains '(MOTO)') then ('Asiapay') 

else (if ([Je Source A] = 'IBS') then ('Control - CAB Billing') 

else (if ([Account] = '718690' and [Je Source A] = 'Spreadsheet') then (substr(substr([Je Desc], 10, 100),1,position('-',substr([Je Desc], 10, 100))-1))

else ('zzz-Other')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
```
	
#### [[Location query]]
```SQL
if([Ccc] = 'CNQ1' or [Ccc] = 'CVB8' or [Ccc] = 'CVC3' or [Ccc] = 'CVC4' or [Ccc] = 'CVC5' or [Ccc] = 'CVC8' or [Ccc] = 'CXA0') then ('HK') 

else (if([Ccc] = 'CNR3' or [Ccc] = 'CVD0' or [Ccc] = 'CVD2' or [Ccc] = 'CVC0') then ('SG')

else (if([Ccc] = 'CNR5' or [Ccc] = 'CVD1' or [Ccc] = 'CVE0' or [Ccc] = 'CVE1' or [Ccc] = 'CVC1' or [Ccc] = 'CXL5') then ('TH')

else (if([Ccc] = 'CNR8' or [Ccc] = 'CVD3' or [Ccc] = 'CVD6' or [Ccc] = 'CVT9') then ('PH')

else (if([Ccc] = 'CNQ5' or [Ccc] = 'CVD4' or [Ccc] = 'CVD7') then ('OS')

else (if([Ccc] = 'CVB7') then ('VO')

else (if([Ccc] = 'CNU8' or [Ccc] = 'CVC9' or [Ccc] = 'CNU9' or [Ccc] = 'CXL6' or [Ccc] = 'CXL8' or [Ccc] = 'CXM0' or [Ccc] = 'CXM1') then ('VC')

else (if([Ccc] = 'CW92' or [Ccc] = 'CNR6' or [Ccc] = 'CNR1' or [Ccc] = 'CHS9' or [Ccc] = 'CVK0' or [Ccc] = 'CVK1' or [Ccc] = 'CVK3') then ('MOOV')

else (if([Ccc] = 'CW64') then ('Media.com')

else (if([Ccc] = 'CV15' or [Ccc] = 'CHS7' or [Ccc] = 'CW57' or [Ccc] = 'CW90') then ('Otr')

else (if([Ccc] = 'CEW2') then ('now.com')

else (if([Ccc] = 'CVB9') then ('Mgt Off')

else (if([Ccc] = 'CVT0') then ('OTT Services')

else (if([Ccc] starts with 'CUL' or [Ccc] = 'CUM7' or [Ccc] = 'CUM4' or [Ccc] = 'CUM9') then ('Vlogger')

else (if([Ccc] = 'CVR0' or [Ccc] = 'CVS2') then ('Viu Intl')

else ('Other')))))))))))))))
```

#### [[Ac type query]]
```SQL
if ([Account] starts with '553') then ('ITAD')

else (if ([Account] starts with '67' or [Account] starts with '68' or [Account] starts with '7160' or [Account] starts with '7162' or [Account] = '782200') then ('ITAD')

else (if ([Account] starts with '731') then ('ITAD')
else (if ([Account] starts with '81') then ('ITAD')
else (if ([Account] starts with '83') then ('ITAD')
else (if ([Account] starts with '85') then ('ITAD')

else(if([Account] starts with '5') then ('Revenue') 
else(if([Account] starts with '0' or [Account] starts with '1') then ('Asset') 
else(if([Account] starts with '2' or [Account] starts with '3') then ('Liability') 
else(if([Account] starts with '31' or [Account] starts with '32'or [Account] starts with '33') then ('Equity') 
else(if([Account] starts with '9') then ('HC') 


else (if ([Account] = '615351') then ('COS')

else (if ([Account] = '615350' or [Account] = '615354' or [Account] = '615362' or [Account] = '616403' or [Account] = '616402' or [Account] = '785350' or [Account] = '786390') then ('COS')

else (if ([Account] = '786656' or [Account] = '616027') then ('COS')

else (if ([Account] = '615356') then ('COS')

else (if ([Account] = '616439' or [Account] = '717154') then ('COS')

else (if ([Account] = '616466' or [Account] = '616467') then ('COS')

else (if ([Account] = '616550' or [Account] = '616551') then ('COS')

else (if ([Account] = '616404' or [Account] = '616450' or [Account] = '616451' or [Account] = '616459' or [Account] = '616498' or [Account] = '717157' or [Account] = '785360' or [Account] = '615424' or [Account] = '615422') then ('COS')

else (if([Account] = '616452') then ('COS')

else (if([Account] = '616454') then ('COS')

else (if ([Account] = '783043' or [Account] = '783045' or [Account] = '615353') then ('COS')

else (if ([Account] = '615352') then ('COS')

else (if ([Account] = '616460' or [Account] = '611848' or [Account] = '717174') then ('COS')

else (if ([Account] = '615469' or [Account] = '615470' or [Account] = '615460' or [Account] = '615461' or [Account] = '615463' or [Account] = '615468' or [Account] = '717175') then ('COS')

else (if ([Account] = '717173' or [Account] = '786657' or [Account] = '615462') then ('COS')

else (if ([Account] = '717172' or [Account] = '615466' or [Account] = '786658') then ('COS')

else (if ([Account] = '615464' or [Account] = '615465' or [Account] = '615467' or [Account] = '611858' or [Account] = '645385' or [Account] = '615212' or [Account] = '786463' or [Account] = '717140') then ('COS')

else (if ([Account] = '616406' or [Account] = '786490' or [Account] = '786493' or [Account] = '786391' or [Account] = '615430') then ('COS')

else (if ([Account] starts with '702' or [Account] = '786511') then ('Opex')

else (if ([Account] = '718690') then ('Opex')

else (if ([Account] = '717601') then ('Opex')

else (if ([Account] = '660000' or [Account] = '661101' or [Account] = '661102' or [Account] = '661104' or [Account] = '661105' or [Account] = '784110' or [Account] = '784130' or [Account] = '663000' or [Account] = '663120' or [Account] = '663420' or [Account] = '784192' or [Account] = '784330' or [Account] = '784370' or [Account] = '785210' or [Account] = '784112' or [Account] = '784140') then ('Opex')

else (if ([Account] starts with '6' or [Account] starts with '7') then ('Opex')


else ('Expense'))))))))))))))))))))))))))))))))))

```
#### [[OTT Product query]]
```SQL
if([Ccc] = 'CNQ1' or [Ccc] = 'CVB8' or [Ccc] = 'CVC3' or [Ccc] = 'CVC4' or [Ccc] = 'CVC5' or [Ccc] = 'CVC8' or [Ccc] = 'CXA0') then ('Viu') 

else (if([Ccc] = 'CNR3' or [Ccc] = 'CVD0' or [Ccc] = 'CVD2' or [Ccc] = 'CVC0') then ('Viu')

else (if([Ccc] = 'CNR5' or [Ccc] = 'CVD1' or [Ccc] = 'CVE0' or [Ccc] = 'CVE1' or [Ccc] = 'CVC1' or [Ccc] = 'CXL5') then ('Viu')

else (if([Ccc] = 'CNR8' or [Ccc] = 'CVD3' or [Ccc] = 'CVD6' or [Ccc] = 'CVT9') then ('Viu')

else (if([Ccc] = 'CNQ5' or [Ccc] = 'CVD4' or [Ccc] = 'CVD7' or [Ccc] = 'CVC9' or [Ccc] = 'CVB7' or [Ccc] = 'CNU8' or [Ccc] = 'CNU9' or [Ccc] = 'CXL6' or [Ccc] = 'CXL8' or [Ccc] = 'CXM0' or [Ccc] = 'CXM1') then ('Viu')

else (if([Ccc] = 'CW92' or [Ccc] = 'CNR6' or [Ccc] = 'CNR1' or [Ccc] = 'CHS9' or [Ccc] = 'CVK0' or [Ccc] = 'CVK1' or [Ccc] = 'CVK3') then ('MOOV')

else (if([Ccc] = 'CW64') then ('Otr')

else (if([Ccc] = 'CV15' or [Ccc] = 'CHS7' or [Ccc] = 'CW57' or [Ccc] = 'CW90') then ('Otr')
else (if([Ccc] = 'CEW2') then ('Otr')

else (if([Ccc] starts with 'CUL' or [Ccc] = 'CUM7' or [Ccc] = 'CUM4' or [Ccc] = 'CUM9') then ('Vlogger')

else ('Other'))))))))))
```
#### [[Team query]]
```SQL
if([Ccc] = 'CW92' or [Ccc] = 'CNR6' or [Ccc] = 'CNR1' or [Ccc] = 'CHS9' or [Ccc] = 'CVK0' or [Ccc] = 'CVK1' or [Ccc] = 'CVK3') then ('MOOV')

else (if([Ccc] = 'CEW2') then ('now.com')

else (if([Ccc] = 'CW64') then ('Game or media.com')

else (if([Ccc] starts with 'CUL') then ('Vlogger')

else (if(upper([Partner]) contains 'ZEBRA' and (upper([Je Desc]) contains 'IVAN' or upper([Je Desc]) contains 'IY' or upper([Je Desc]) contains 'TP' or upper([Je Desc]) contains 'PRODUCT TEAM')) then ('Product') 

else (if(upper([Partner]) contains 'ZEBRA' and (upper([Je Desc]) contains 'DL' or upper([Je Desc]) contains 'MKT')) then ('Marketing')

else (if(upper([Partner]) contains 'ZEBRA' and (upper([Je Desc]) contains 'MEG' or upper([Je Desc]) contains 'ML' or upper([Je Desc]) contains 'MARIANNE')) then ('Content')

else (if([Account] = '718690' or [Account] = '616406' or upper([Partner]) contains 'MASTERLINK') then ('Product')

else ('Other'))))))))
```
#### [[Ac Group query]]
```SQL
if ([Account] = '515123' or [Account] = '515555' or [Account] = '515580' or [Account] = '515581' or [Account] = '515582' or [Account] = '515817' or [Account] = '515819' or [Account] = '515822' or [Account] = '518170') then ('Subscription Revenue') 

else (if ([Account] = '515823' or [Account] = '515826' or [Account] = '588773' or [Account] = '588775' or [Account] = '588776' or [Account] = '588777' or [Account] = '588811' or [Account] = '515824' or [Account] = '515821') then ('Subscription Revenue')

else (if([Account] = '515820' or [Account] = '515825' or [Account] = '588771') then ('Subscription Revenue')

else (if([Account] = '515129' or [Account] = '515552' or [Account] = '588814') then ('Subscription Revenue')

else (if([Account] = '515126' or [Account] = '588780') then ('Subscription Revenue')

else (if([Account] = '515585' or [Account] = '515586' or [Account] = '515814' or [Account] = '516564' or [Account] = '588812' or [Account] = '588813') then ('Subscription Revenue')

else (if ([Account] = '515553' or [Account] = '515554' or [Account] = '515557' or [Account] = '515561' or [Account] = '515564' or [Account] = '515565' or [Account] = '515566' or [Account] = '515568' or [Account] = '515569' or [Account] = '515587' or [Account] = '515588') then ('Subscription Revenue')

else (if ([Account] = '515550' or [Account] = '515811' or [Account] = '515812' or [Account] = '515813' or [Account] = '515815') then ('Subscription Revenue')

else (if ([Account] = '518073') then ('Subscription Revenue')

else (if ([Account] = '515570' or [Account] = '588766' or [Account] = '518171') then ('Advertising Revenue')

else (if ([Account] = '516220' or [Account] = '516221' or [Account] = '516223' or [Account] = '516227' or [Account] = '516228' or [Account] = '516229') then ('Advertising Revenue')

else (if ([Account] = '518101' or [Account] = '586492') then ('Advertising Revenue')

else (if ([Account] = '515818' or [Account] = '588774' or [Account] = '586493' or [Account] = '518173' or [Account] = '518174') then ('Content license revenue')

else (if ([Account] = '515583' or [Account] = '588772' or [Account] = '516222' or [Account] = '538606') then ('Other revenue')

else (if ([Account] = '515562' or [Account] = '516225' or [Account] = '588781') then ('Other revenue')

else (if ([Account] = '516224' or [Account] = '516226' or [Account] = '516230' or [Account] = '516231' or [Account] = '516232') then ('Other revenue')

else (if ([Account] = '515558') then ('Other revenue')

else (if ([Account] = '615351') then ('Content Lic (MOOV)')

else (if ([Account] = '615350' or [Account] = '615354' or [Account] = '615362' or [Account] = '616403' or [Account] = '616402' or [Account] = '785350' or [Account] = '786390') then ('Content Lic (media)')

else (if ([Account] = '786656' or [Account] = '616027') then ('Content Lic (now.com)')

else (if ([Account] = '615356') then ('Content Lic (game)')

else (if ([Account] = '616439' or [Account] = '717154') then ('Content Lic (others)')

else (if ([Account] = '616466' or [Account] = '616467') then ('Content License Costs (for IA)')

else (if ([Account] = '616550' or [Account] = '616551') then ('Content Costs Capitalization')

else (if ([Account] = '616404' or [Account] = '616450' or [Account] = '616451' or [Account] = '616459' or [Account] = '616498' or [Account] = '717157' or [Account] = '785360' or [Account] = '615424' or [Account] = '615422') then ('Content Production Costs')

else (if([Account] = '616452') then ('Dubbing & Subtitling')

else (if([Account] = '616454') then ('Contractor')

else (if ([Account] = '783043' or [Account] = '783045' or [Account] = '615353') then ('Sale costs to Telco')

else (if ([Account] = '615352') then ('External payment gateways')

else (if ([Account] = '616460' or [Account] = '611848' or [Account] = '717174') then ('Sale commission')

else (if ([Account] = '615469' or [Account] = '615470' or [Account] = '615460' or [Account] = '615461' or [Account] = '615463' or [Account] = '615468' or [Account] = '717175') then ('Advertising Production Costs')

else (if ([Account] = '717173' or [Account] = '786657' or [Account] = '615462') then ('Event, Festival and Partnership - COS')

else (if ([Account] = '717172' or [Account] = '615466' or [Account] = '786658') then ('Goodies')

else (if ([Account] = '615464' or [Account] = '615465' or [Account] = '615467' or [Account] = '611858' or [Account] = '645385' or [Account] = '615212' or [Account] = '786463' or [Account] = '717140') then ('Other COS')

else (if ([Account] = '616406' or [Account] = '786490' or [Account] = '786493' or [Account] = '786391' or [Account] = '615430') then ('Network costs - COS')

else (if ([Account] starts with '63' or [Account] starts with '791' or [Account] = '786580' or [Account] = '786680' or [Account] = '718939') then ('Staff costs')

else (if ([Account] starts with '64' or [Account] = '782110') then ('R&M')

else (if ([Account] starts with '707' or [Account] starts with '708' or [Account] = '718837') then ('Professional fees')

else (if ([Account] starts with '709' or [Account] = '784360'  or [Account] = '784361') then ('TnE')

else (if ([Account] starts with '702' or [Account] = '716500' or [Account] = '786511') then ('PnP')

else (if ([Account] = '718690') then ('Tools')

else (if ([Account] = '717601') then ('Publishing Fee')

else (if ([Account] starts with '66' or [Account] = '784110' or [Account] = '784130' or [Account] = '784192' or [Account] = '784330' or [Account] = '784370' or [Account] = '785210' or [Account] = '784112' or [Account] = '784140') then ('Rental')

else (if ([Account] starts with '553') then ('Other Income / Loss')

else (if ([Account] starts with '67' or [Account] starts with '68' or [Account] starts with '7160' or [Account] starts with '7162' or [Account] = '782200') then ('D&A')

else (if ([Account] starts with '731') then ('G/L on Disp.')

else (if ([Account] starts with '81') then ('Interest Inc / Exp')

else (if ([Account] starts with '83') then ('Tax')

else (if ([Account] starts with '85') then ('MI')

else (if ([Account] = '050211') then ('Content acquisition')
else (if ([Account] = '050213') then ('In-house production content')
else (if ([Account] starts with '14') then ('Interco account')

else ('Other'))))))))))))))))))))))))))))))))))))))))))))))))))))

```
#### [[Ac subgroup query]]
```SQL
if ([Account] = '515123' or [Account] = '515555' or [Account] = '515580' or [Account] = '515581' or [Account] = '515582' or [Account] = '515817' or [Account] = '515819' or [Account] = '515822' or [Account] = '518170') then ('PC + IAP') 

else (if ([Account] = '515823' or [Account] = '515826' or [Account] = '588773' or [Account] = '588775' or [Account] = '588776' or [Account] = '588777' or [Account] = '588811' or [Account] = '515824' or [Account] = '515821') then ('mobile bundle')

else (if([Account] = '515820' or [Account] = '515825' or [Account] = '588771') then ('Top Up Card')

else (if([Account] = '515129' or [Account] = '515552' or [Account] = '588814') then ('PCD')

else (if([Account] = '515126' or [Account] = '588780') then ('Subscription - Eye')

else (if([Account] = '515585' or [Account] = '515586' or [Account] = '515814' or [Account] = '516564' or [Account] = '588812' or [Account] = '588813') then ('Subscription - TV')

else (if ([Account] = '515553' or [Account] = '515554' or [Account] = '515557' or [Account] = '515561' or [Account] = '515564' or [Account] = '515565' or [Account] = '515566' or [Account] = '515568' or [Account] = '515569' or [Account] = '515587' or [Account] = '515588') then ('media.now')

else (if ([Account] = '515550' or [Account] = '515811' or [Account] = '515812' or [Account] = '515813' or [Account] = '515815') then ('now.com Sports subscription')

else (if ([Account] = '518073') then ('now.com Finance subscription')

else (if ([Account] = '515570' or [Account] = '588766' or [Account] = '518171') then ('OTT Advertising')

else (if ([Account] = '516220' or [Account] = '516221' or [Account] = '516223' or [Account] = '516227' or [Account] = '516228' or [Account] = '516229') then ('Advertising production revenue')

else (if ([Account] = '518101' or [Account] = '586492') then ('now.com Advertising')

else (if ([Account] = '515818' or [Account] = '588774' or [Account] = '586493' or [Account] = '518173' or [Account] = '518174') then ('Content license revenue')

else (if ([Account] = '515583' or [Account] = '588772' or [Account] = '516222' or [Account] = '538606') then ('Event, Festival and Partnership')

else (if ([Account] = '515562' or [Account] = '516225' or [Account] = '588781') then ('Transaction')

else (if ([Account] = '516224' or [Account] = '516226' or [Account] = '516230' or [Account] = '516231' or [Account] = '516232') then ('Vlogger revenue')

else (if ([Account] = '515558') then ('Game')

else (if ([Account] = '615351') then ('Content Lic (MOOV)')

else (if ([Account] = '615350' or [Account] = '615354' or [Account] = '615362' or [Account] = '616403' or [Account] = '616402' or [Account] = '785350' or [Account] = '786390') then ('Content Lic (media)')

else (if ([Account] = '786656' or [Account] = '616027') then ('Content Lic (now.com)')

else (if ([Account] = '615356') then ('Content Lic (game)')

else (if ([Account] = '616439' or [Account] = '717154') then ('Content Lic (others)')

else (if ([Account] = '616466' or [Account] = '616467') then ('Content License Costs (for IA)')

else (if ([Account] = '616550' or [Account] = '616551') then ('Content Costs Capitalization')

else (if ([Account] = '616404' or [Account] = '616450' or [Account] = '616451' or [Account] = '616459' or [Account] = '616498' or [Account] = '717157' or [Account] = '785360' or [Account] = '615424' or [Account] = '615422') then ('Content Production Costs')

else (if([Account] = '616452') then ('Dubbing & Subtitling')

else (if([Account] = '616454') then ('Contractor')

else (if ([Account] = '783043' or [Account] = '783045' or [Account] = '615353') then ('Sale costs to Telco')

else (if ([Account] = '615352') then ('External payment gateways')

else (if ([Account] = '616460' or [Account] = '611848' or [Account] = '717174') then ('Sale commission')

else (if ([Account] = '615469' or [Account] = '615470' or [Account] = '615460' or [Account] = '615461' or [Account] = '615463' or [Account] = '615468' or [Account] = '717175') then ('Advertising Production Costs')

else (if ([Account] = '717173' or [Account] = '786657' or [Account] = '615462') then ('Event, Festival and Partnership - COS')

else (if ([Account] = '717172' or [Account] = '615466' or [Account] = '786658') then ('Goodies')

else (if ([Account] = '615464' or [Account] = '615465' or [Account] = '615467' or [Account] = '611858' or [Account] = '645385' or [Account] = '615212' or [Account] = '786463' or [Account] = '717140') then ('Other COS')

else (if ([Account] = '616406' or [Account] = '786490' or [Account] = '786493' or [Account] = '786391' or [Account] = '615430') then ('Network costs - COS')

else (if ([Account] = '702112' or [Account] = '702119' or [Account] = '702211' or [Account] = '702113') then ('Customer acquisition')
else (if ([Account] = '702220' or [Account] = '702212' or [Account] = '702113' or [Account] = '702114' or [Account] = '702277') then ('Branding and content marketing')
else (if ([Account] starts with '702' or [Account] = '786511') then ('Other P&P')

else (if ([Account] = '718690') then ('Tools')

else (if ([Account] = '717601') then ('Publishing Fee')

else (if ([Account] = '660000' or [Account] = '661101' or [Account] = '661102' or [Account] = '661104' or [Account] = '661105' or [Account] = '784110' or [Account] = '784130' or [Account] = '663000' or [Account] = '663120' or [Account] = '663420' or [Account] = '784192' or [Account] = '784330' or [Account] = '784370' or [Account] = '785210' or [Account] = '784112' or [Account] = '784140') then ('Rental')

else (if ([Account] = '050211') then ('Content acquisition')
else (if ([Account] = '050213') then ('In-house production content')
else (if ([Account] starts with '14') then ('Interco account')

else ('Other'))))))))))))))))))))))))))))))))))))))))))))

```

#### [[Tx type query]]
```SQL
if([Je Desc] contains 'TB Posting') then ('TB Posting')
else (if([Je Desc] contains 'echarge from OTT HK' or [Je Desc] contains 'recharge to Vuclip') then('Recharge')
else (if([Je Name] contains 'FMB_C') then('DM JE') 
else (if([Je Name] contains 'FMB_') then ('JE - TV Fin')
else (if([Je Source A] = 'Assets') then('Assets')
else (if([Je Source A] = 'BANK_REC') then('HKT receipt')
else (if([Je Source A] = 'Cost Management') then('GSP')
else (if([Je Source A] = 'Human Resources') then('HR')
else (if([Je Source A] = 'IBS') then('Billing B2B')
else (if([Je Source A] = 'IMS' or [Je Source A] = 'MOB') then('Billing B2C')
else (if([Je Source A] = 'Payables') then('RFP')
else (if([Je Source A] = 'Purchasing') then('GSP')
else (if([Je Source A] = 'INTERCO') then('Interco')

else (if([Je Category A] = 'IC_DRAGON') then('Netvigator (BHC, BHE)')
else (if([Je Category A] = 'IC_CAL') then('Solutions')
else (if([Je Category A] = 'IC_CPE') then('Commercial & consumer (BHE)')

else ('Other'))))))))))))))))
```

### within a join group
#### [[Branch code query]]
```SQL
if([Ccc] = 'CVB7') then('PVSO')

else(if([Ccc] = 'CNR5' or [Ccc] = 'CVC1' or [Ccc] = 'CVD1' or [Ccc] = 'CVE0' or [Ccc] = 'CVE1')  then ('PDMT')

else(if([Ccc] = 'CNR3' or [Ccc] = 'CVC0' or [Ccc] = 'CVD0' or [Ccc] = 'CVD2') then('PDMS')

else(if([Ccc] = 'CNR8' or [Ccc] = 'CVD3' or [Ccc] = 'CVD6' or [Ccc] = 'CVT9') then('PDMP')

else(if([Ccc] = 'CNQ5' or [Ccc] = 'CVD4' or [Ccc] = 'CVD7' or [Ccc] = 'CVX0' or [Ccc] = 'CVX1' or [Ccc] = 'CVX2' or [Ccc] = 'CVX3') then('PDMO')

else(if([Ccc] = 'CNQ1' or [Ccc] = 'CVB8' or [Ccc] = 'CVC3') then('PPWT')

else(if([Ccc] = 'CVY0') then('PPWI')

else(if([Ccc] = 'CHS7') then('PPWP')

else(if([Ccc] = 'CV15' or [Ccc] = 'CW57' or [Ccc] = 'CW90' or [Ccc] = 'CEW2' or [Ccc] = 'CVC2' or [Ccc] = 'CW64') then('PPWG')

else(if([Ccc] = 'CVJ0' or [Ccc] = 'CVJ1' or [Ccc] = 'CVK0' or [Ccc] = 'CVL0' or [Ccc] = 'CVL1' or [Ccc] = 'CW92' or [Ccc] = 'CHS9' or [Ccc] = 'CNQ0' or [Ccc] = 'CNR1' or [Ccc] = 'CNR6') then('PPWY')

else(if([Ccc] starts with 'CUL' or [Ccc] = 'CUM0' or  [Ccc] = 'CUM4' or  [Ccc] = 'CUM7' or  [Ccc] = 'CUM9') then('PCSI')

else(if([Ccc] = 'CVA0' or [Ccc] = 'CVA1' or [Ccc] = 'CVA2' or [Ccc] = 'CVA3' or [Ccc] = 'CVB9' or [Ccc] = 'CVC8' or [Ccc] = 'CVR0' or [Ccc] = 'CVR1' or [Ccc] = 'CVR2'  or [Ccc] = 'CVR3' or [Ccc] = 'CVR4' or [Ccc] = 'CVS0' or [Ccc] = 'CVS2') then('PAIB')

else(if([Ccc] = 'CVC9' or [Ccc] = 'CJN9' or [Ccc] = 'X504' or [Ccc] = 'X505' or [Ccc] = 'X506' or [Ccc] = 'X507' or [Ccc] = 'CNU8' or [Ccc] = 'CNU9') then('PPWK')

else(if([Ccc] = 'CJN7' or [Ccc] = 'CVC4' or [Ccc] = 'CVD5' or [Ccc] = 'CVE2' or [Ccc] = 'CVK1' or [Ccc] = 'CVT0') then('PCWT')

else(if([Ccc] = 'CJN8' or [Ccc] = 'CVC5' or [Ccc] = 'CVC6' or [Ccc] = 'CVC7' or [Ccc] = 'CVE5' or [Ccc] = 'CVK2' or [Ccc] = 'CVS1') then('POTC')

else(if([Ccc] = 'CXK3' or [Ccc] = 'CXA0' or [Ccc] = 'CXA1' or [Ccc] = 'CXK4' or [Ccc] = 'CXK5' or [Ccc] = 'CXL4' or [Ccc] = 'CXL5' or [Ccc] = 'CJN6' or [Ccc] = 'CXK3' or [Ccc] = 'CXL6' or [Ccc] = 'CXL7' or [Ccc] = 'CXL8' or [Ccc] = 'CXL9' or [Ccc] = 'CXM0' or [Ccc] = 'CXM1' or [Ccc] = 'CUL3' or [Ccc] = 'CUL5' or [Ccc] = 'CUL9' or [Ccc] = 'CUM3' or [Ccc] = 'CUM8') then('POTT')

else([Query1].[Branch Code]))))))))))))))))
```
