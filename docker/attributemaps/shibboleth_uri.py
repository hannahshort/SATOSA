EDUPERSON_OID = 'urn:oid:1.3.6.1.4.1.5923.1.1.1.'
NETSCAPE_LDAP = 'urn:oid:2.16.840.1.113730.3.1.'
NOREDUPERSON_OID = 'urn:oid:1.3.6.1.4.1.2428.90.1.'
PKCS_9 = 'urn:oid:1.2.840.113549.1.9.'
UCL_DIR_PILOT = 'urn:oid:0.9.2342.19200300.100.1.'
UMICH = 'urn:oid:1.3.6.1.4.1.250.1.57.'
X500ATTR = 'urn:oid:2.5.4.'

MAP = {
    "identifier": "urn:mace:shibboleth:1.0:attributeNamespace:uri",
    'fro': {
        EDUPERSON_OID+'1': 'eduPersonAffiliation',
        EDUPERSON_OID+'2': 'eduPersonNickname',
        EDUPERSON_OID+'3': 'eduPersonOrgDN',
        EDUPERSON_OID+'4': 'eduPersonOrgUnitDN',
        EDUPERSON_OID+'5': 'eduPersonPrimaryAffiliation',
        EDUPERSON_OID+'6': 'eduPersonPrincipalName',
        EDUPERSON_OID+'7': 'eduPersonEntitlement',
        EDUPERSON_OID+'8': 'eduPersonPrimaryOrgUnitDN',
        EDUPERSON_OID+'9': 'eduPersonScopedAffiliation',
        EDUPERSON_OID+'10': 'eduPersonTargetedID',
        EDUPERSON_OID+'11': 'eduPersonAssurance',
        EDUPERSON_OID+'12': 'eduPersonPrincipalNamePrior',
        EDUPERSON_OID+'13': 'eduPersonUniqueId',
        EDUPERSON_OID+'16': 'eduPersonOrcid',
        NETSCAPE_LDAP+'1': 'carLicense',
        NETSCAPE_LDAP+'2': 'departmentNumber',
        NETSCAPE_LDAP+'3': 'employeeNumber',
        NETSCAPE_LDAP+'4': 'employeeType',
        NETSCAPE_LDAP+'39': 'preferredLanguage',
        NETSCAPE_LDAP+'40': 'userSMIMECertificate',
        NETSCAPE_LDAP+'216': 'userPKCS12',
        NETSCAPE_LDAP+'241': 'displayName',
        NOREDUPERSON_OID+'1': 'norEduOrgUniqueNumber',
        NOREDUPERSON_OID+'2': 'norEduOrgUnitUniqueNumber',
        NOREDUPERSON_OID+'3': 'norEduPersonBirthDate',
        NOREDUPERSON_OID+'4': 'norEduPersonLIN',
        NOREDUPERSON_OID+'5': 'norEduPersonNIN',
        NOREDUPERSON_OID+'6': 'norEduOrgAcronym',
        NOREDUPERSON_OID+'7': 'norEduOrgUniqueIdentifier',
        NOREDUPERSON_OID+'8': 'norEduOrgUnitUniqueIdentifier',
        NOREDUPERSON_OID+'9': 'federationFeideSchemaVersion',
        PKCS_9+'1': 'email',
        UCL_DIR_PILOT+'3': 'mail',
        UCL_DIR_PILOT+'25': 'dc',
        UCL_DIR_PILOT+'37': 'associatedDomain',
        UCL_DIR_PILOT+'60': 'jpegPhoto',
        X500ATTR+'2': 'knowledgeInformation',
        X500ATTR+'4': 'sn',
        X500ATTR+'5': 'serialNumber',
        X500ATTR+'6': 'c',
        X500ATTR+'7': 'l',
        X500ATTR+'8': 'st',
        X500ATTR+'9': 'street',
        X500ATTR+'10': 'o',
        X500ATTR+'11': 'ou',
        X500ATTR+'12': 'title',
        X500ATTR+'14': 'searchGuide',
        X500ATTR+'15': 'businessCategory',
        X500ATTR+'16': 'postalAddress',
        X500ATTR+'17': 'postalCode',
        X500ATTR+'18': 'postOfficeBox',
        X500ATTR+'19': 'physicalDeliveryOfficeName',
        X500ATTR+'20': 'telephoneNumber',
        X500ATTR+'21': 'telexNumber',
        X500ATTR+'22': 'teletexTerminalIdentifier',
        X500ATTR+'23': 'facsimileTelephoneNumber',
        X500ATTR+'24': 'x121Address',
        X500ATTR+'25': 'internationaliSDNNumber',
        X500ATTR+'26': 'registeredAddress',
        X500ATTR+'27': 'destinationIndicator',
        X500ATTR+'28': 'preferredDeliveryMethod',
        X500ATTR+'29': 'presentationAddress',
        X500ATTR+'30': 'supportedApplicationContext',
        X500ATTR+'31': 'member',
        X500ATTR+'32': 'owner',
        X500ATTR+'33': 'roleOccupant',
        X500ATTR+'36': 'userCertificate',
        X500ATTR+'37': 'cACertificate',
        X500ATTR+'38': 'authorityRevocationList',
        X500ATTR+'39': 'certificateRevocationList',
        X500ATTR+'40': 'crossCertificatePair',
        X500ATTR+'42': 'givenName',
        X500ATTR+'43': 'initials',
        X500ATTR+'44': 'generationQualifier',
        X500ATTR+'45': 'x500UniqueIdentifier',
        X500ATTR+'46': 'dnQualifier',
        X500ATTR+'47': 'enhancedSearchGuide',
        X500ATTR+'48': 'protocolInformation',
        X500ATTR+'50': 'uniqueMember',
        X500ATTR+'51': 'houseIdentifier',
        X500ATTR+'52': 'supportedAlgorithms',
        X500ATTR+'53': 'deltaRevocationList',
        X500ATTR+'54': 'dmdName',
        X500ATTR+'65': 'pseudonym',
    },
    'to': {
        'associatedDomain': UCL_DIR_PILOT+'37',
        'authorityRevocationList': X500ATTR+'38',
        'businessCategory': X500ATTR+'15',
        'c': X500ATTR+'6',
        'cACertificate': X500ATTR+'37',
        'carLicense': NETSCAPE_LDAP+'1',
        'certificateRevocationList': X500ATTR+'39',
        'countryName': X500ATTR+'6',
        'crossCertificatePair': X500ATTR+'40',
        'dc': UCL_DIR_PILOT+'25',
        'deltaRevocationList': X500ATTR+'53',
        'departmentNumber': NETSCAPE_LDAP+'2',
        'destinationIndicator': X500ATTR+'27',
        'displayName': NETSCAPE_LDAP+'241',
        'dmdName': X500ATTR+'54',
        'dnQualifier': X500ATTR+'46',
        'domainComponent': UCL_DIR_PILOT+'25',
        'eduPersonAffiliation': EDUPERSON_OID+'1',
        'eduPersonEntitlement': EDUPERSON_OID+'7',
        'eduPersonNickname': EDUPERSON_OID+'2',
        'eduPersonOrgDN': EDUPERSON_OID+'3',
        'eduPersonOrgUnitDN': EDUPERSON_OID+'4',
        'eduPersonPrimaryAffiliation': EDUPERSON_OID+'5',
        'eduPersonPrimaryOrgUnitDN': EDUPERSON_OID+'8',
        'eduPersonPrincipalName': EDUPERSON_OID+'6',
        'eduPersonPrincipalNamePrior': EDUPERSON_OID+'12',
        'eduPersonScopedAffiliation': EDUPERSON_OID+'9',
        'eduPersonTargetedID': EDUPERSON_OID+'10',
        'eduPersonAssurance': EDUPERSON_OID+'11',
        'eduPersonUniqueId': EDUPERSON_OID+'13',
        'eduPersonOrcid': EDUPERSON_OID+'16',
        'email': PKCS_9+'1',
        'emailAddress': PKCS_9+'1',
        'employeeNumber': NETSCAPE_LDAP+'3',
        'employeeType': NETSCAPE_LDAP+'4',
        'enhancedSearchGuide': X500ATTR+'47',
        'facsimileTelephoneNumber': X500ATTR+'23',
        'fax': X500ATTR+'23',
        'federationFeideSchemaVersion': NOREDUPERSON_OID+'9',
        'generationQualifier': X500ATTR+'44',
        'givenName': X500ATTR+'42',
        'gn': X500ATTR+'42',
        'houseIdentifier': X500ATTR+'51',
        'initials': X500ATTR+'43',
        'internationaliSDNNumber': X500ATTR+'25',
        'jpegPhoto': UCL_DIR_PILOT+'60',
        'knowledgeInformation': X500ATTR+'2',
        'l': X500ATTR+'7',
        'localityName': X500ATTR+'7',
        'mail': UCL_DIR_PILOT+'3',
        'member': X500ATTR+'31',
        'norEduOrgAcronym': NOREDUPERSON_OID+'6',
        'norEduOrgUniqueIdentifier': NOREDUPERSON_OID+'7',
        'norEduOrgUniqueNumber': NOREDUPERSON_OID+'1',
        'norEduOrgUnitUniqueIdentifier': NOREDUPERSON_OID+'8',
        'norEduOrgUnitUniqueNumber': NOREDUPERSON_OID+'2',
        'norEduPersonBirthDate': NOREDUPERSON_OID+'3',
        'norEduPersonLIN': NOREDUPERSON_OID+'4',
        'norEduPersonNIN': NOREDUPERSON_OID+'5',
        'o': X500ATTR+'10',
        'organizationName': X500ATTR+'10',
        'organizationalUnitName': X500ATTR+'11',
        'ou': X500ATTR+'11',
        'owner': X500ATTR+'32',
        'physicalDeliveryOfficeName': X500ATTR+'19',
        'pkcs9email': PKCS_9+'1',
        'postOfficeBox': X500ATTR+'18',
        'postalAddress': X500ATTR+'16',
        'postalCode': X500ATTR+'17',
        'preferredDeliveryMethod': X500ATTR+'28',
        'preferredLanguage': NETSCAPE_LDAP+'39',
        'presentationAddress': X500ATTR+'29',
        'protocolInformation': X500ATTR+'48',
        'pseudonym': X500ATTR+'65',
        'registeredAddress': X500ATTR+'26',
        'rfc822Mailbox': UCL_DIR_PILOT+'3',
        'roleOccupant': X500ATTR+'33',
        'searchGuide': X500ATTR+'14',
        'serialNumber': X500ATTR+'5',
        'sn': X500ATTR+'4',
        'st': X500ATTR+'8',
        'stateOrProvinceName': X500ATTR+'8',
        'street': X500ATTR+'9',
        'streetAddress': X500ATTR+'9',
        'supportedAlgorithms': X500ATTR+'52',
        'supportedApplicationContext': X500ATTR+'30',
        'surname': X500ATTR+'4',
        'telephoneNumber': X500ATTR+'20',
        'teletexTerminalIdentifier': X500ATTR+'22',
        'telexNumber': X500ATTR+'21',
        'title': X500ATTR+'12',
        'uniqueMember': X500ATTR+'50',
        'userCertificate': X500ATTR+'36',
        'userPKCS12': NETSCAPE_LDAP+'216',
        'userSMIMECertificate': NETSCAPE_LDAP+'40',
        'x121Address': X500ATTR+'24',
        'x500UniqueIdentifier': X500ATTR+'45',
    }
}
