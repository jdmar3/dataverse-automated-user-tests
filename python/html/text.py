text = {
    'document_title':'Validator for FDA Dataverse',
    'document_description':'This document shows the automated compliance of tests on the FDA dataverse to ensure CFR Part11 functionality operates.',

    # tests

    'r01_title': 'Dataverse must support authentication process where all users login via UNC Shibboleth using Two-factor authentication',
    'r01_p01': 'On the Dataverse landing page, click on the Log In link located at the upper right-hand corner. ',
    'r01_p02': 'Select https://sso.unc.edu/idp in the institution drop down list. ',
    'r01_p03': 'Click the Continue button.',
    'r01_p04': 'Follow the prompts for UNC SSO to enter login credentials.',

    'r02_title': 'Dataverse must allow the ability to define groups, define user roles, and assign user roles to groups',
    'r02_p01': 'Click on the Edit button located at the upper right-hand side of the dataverse landing page.',
    'r02_p02': 'In the drop-down list that appears, select the Permissions option.',
    'r02_p03': 'Click on the Roles section header to expand the section.',
    'r02_p04': 'Click on the Add New Role button.',
    'r02_p05': 'In the Edit Role dialogue box that appears, enter the Role Name, Identifier, and Description in the corresponding fields.',
    'r02_p06': 'In the Role Permissions section below, click on the boxes next to the actions that users/groups assigned the new role should be able to perform.',
    'r02_p07': 'Click on the Save Changes button.',
    # 'r02_p08': 'Click on the Edit button located at the upper right-hand side of the screen.',
    # 'r02_p09': 'In the drop-down box that appears, select the Permissions option.',
    # 'r02_p10': 'Click on the Roles section header to expand the section.',
    # 'r02_p11': 'Review the definitions for the available role types listed. If a desired role type is not listed, see III. Adding a new user/group role.',
    'r02_p08': 'Click on the Users/Groups section header to expand the section.',
    'r02_p09': 'Click on the Assign Roles to Users/Groups button.',
    'r02_p10': 'In the Assign Role dialogue box that appears, enter the user or group name in the Users/Groups field.',
    'r02_p11': 'Select the appropriate role for the user/group by clicking on the radio button next to the desired Role option.',
    'r02_p12': 'Click on the Save Changes button.',

    'r03_title': 'Dataverse must support study and dataset creation where the archivist must be able to create a new Sub-Dataverse',
    'r03_p01': 'Click on the Add Data button located at the right side of the dataverse landing page above the list of sub-dataverses and datasets.',
    'r03_p02': 'In the drop-down list that appears, select the New Dataverse option.',
    'r03_p03': 'On the New Dataverse page, complete the form provided by entering the appropriate information into the text fields or by selecting options from the given drop-down list for each of the corresponding fields.',
    'r03_p04': 'Click on the Create Dataverse button.',
    'r03_p05': 'On the new dataverse landing page, click on the Publish button to make the dataverse discoverable.',

    'r04_title': 'Dataverse must support study and dataset creation where the archivist must be able to edit Sub-Dataverse properties',
    'r04_p01': 'Click on the Edit button at the upper-right hand side of the dataverse landing page.',
    'r04_p02': 'In the drop-down list that appears, select the General Information option.',
    'r04_p03': 'Edit the dataverse properties by entering the appropriate information into the text fields or by selecting options from the given drop-down list for each of the corresponding fields.',
    'r04_p04': 'If the dataverse requires that datasets in the dataverse include metadata elements that are not included in the default metadata elements (i.e., metadata fields from Root), click on the pre-selected Use metadata fields from Root checkbox to deselect this option.',
    'r04_p05': 'Select from the options listed in the Metadata Fields section by clicking on the box(es) corresponding to the appropriate metadata type(s).',
    'r04_p06': 'If the dataverse requires browse/search facets beyond the default facets (i.e., browse/search facets from Root), click on the preselected Use browse/search facets from Root checkbox to deselect this option. ',
    'r04_p07': 'Click on the dropdown box below to select the metadata type that includes the metadata fields to be used for facets OR leave the All Metadata Fields option to allow selection of metadata fields from any available metadata type.',
    'r04_p08': 'In the list box, select the metadata field to be used as a browse/search facet.',
    'r04_p09': 'Click on the right arrow button --> to add the metadata field to the list of selected fields.  Repeat for each metadata field to be used as a browse/search facet for the dataverse.',
    'r04_p10': 'Click on the Save Changes button.',

    'r05_title': 'Dataverse must support study and dataset creation where the archivist must be able to create a new metadata template',
    'r05_p01': 'On the dataverse landing page, click on the Edit button and select the Dataset Templates option from the drop-down list.',
    'r05_p02': 'Click on the Create Dataset Template button.',
    'r05_p03': 'Enter a descriptive name in the Template Name field.',
    'r05_p04': 'In the Citation Metadata form, enter information that is standard across all datasets in the dataset into the applicable metadata fields.',
    'r05_p05': 'To provide instructions on how to complete a metadata field, click on the (None - click to add) link above the metadata text field.',
    'r05_p06': 'Enter the metadata field instructions in the Custom instructions field that appears, then click on the check button.',
    'r05_p07': 'Click on the Save + Add Terms button.',
    'r05_p08': 'In the Dataset Terms section, select the appropriate terms for the datasets in the dataverse by selecting from the License/Data Use Agreement drop-down list provided.',
    'r05_p09': 'Enter custom dataset terms, information about restricted files, and terms of access in the fields provided.',
    'r05_p10': 'Click on the Save Dataset Template button.',

    'r06_title': 'Dataverse must support study and dataset creation where the archivist must be able to edit a metadata template',
    'r06_p01': 'On the dataverse landing page, click on the Edit button and select the Dataset Templates option from the drop-down list.',
    'r06_p02': 'Click on the Edit Template button and select the Metadata option in the drop-down list that appears.',
    'r06_p03': 'In the Citation Metadata form, enter updated information that is standard across all datasets in the dataset into the applicable metadata fields.',
    'r06_p04': 'To add or update instructions on how to complete a metadata field, click on the (None - click to add) link above the text field for the metadata element.',
    'r06_p05': 'Enter the metadata field instructions in the Custom instructions field that appears, then click on the check button.',
    'r06_p06': 'Click on the Save Changes button.',
    'r06_p07': 'On the dataverse landing page, click on the Edit button and select the Dataset Templates option from the drop-down list.',
    'r06_p08': 'Click on the Edit Template button and select the Terms option in the drop-down list that appears.',
    'r06_p09': 'In the Terms form, enter updated information that is standard across all datasets in the dataset into the applicable terms fields.',
    'r06_p10': 'Click on the Save Changes button.', 

    'r09_title': 'Dataverse must support study and dataset creation where the archivist must be able to create a new dataset/study',
    'r09_p01': 'Click on the Add Data button located at the upper-right hand side of the dataverse landing page.',
    'r09_p02': 'In the drop-down list that appears, select the New Dataset option.',
    'r09_p03': 'In the dataset metadata page, select the Host Dataverse from the drop-down list provided.',
    'r09_p04': 'Click on the Terms tab on the dataset landing page.',
    'r09_p05': 'Click on the Edit Terms Requirements button.',
    'r09_p06': 'In the Dataset Terms section, select the appropriate terms by selecting from the License/Data Use Agreement drop-down list provided.',
    'r09_p07': 'Enter and/or update custom dataset terms, information about restricted files and terms of access in the fields provided.',
    'r09_p08': 'Click on the Save Changes button.',
    'r09_p09': 'Once the dataset record has been reviewed, click on the Publish Dataset button to the right-hand side of the dataset citation to finalize and create version 1 of the dataset.',

#TODO: I guessed on some of these reqs and I think they need to be moved. Anything that isn't data (e.g. dataset metadata, file metadata, terms) is probably req 12?
    # 'r10_title': 'Dataverse must support study and dataset creation where the archivist must be able to edit properties of dataset/study',
    # 'r10_p01': 'Click the checkbox next to the file(s) that require(s) editing.',
    # 'r10_p02': 'Click on the Edit Files button above the file list and select the Metadata option.',
    # 'r10_p03': 'Update the file name, file path, and description in the corresponding metadata fields for each file as needed.',
    # 'r10_p04': 'Click on the Save Changes button.',
    # 'r10_p05': 'Click on the Terms tab on the dataset landing page.',
    # 'r10_p06': 'Click on the Edit Terms Requirements button.',
    # 'r10_p07': 'In the Dataset Terms section, select the appropriate terms by selecting from the License/Data Use Agreement drop-down list provided.',
    # 'r10_p08': 'Enter and/or update custom dataset terms, information about restricted files and terms of access in the fields provided.',
    # 'r10_p09': 'Click on the Save Changes button.',

    'r11_title': 'Dataverse must support dataset/study management where the archivist must be able to create metadata',
    'r11_p01': 'Complete the metadata form in the Citation Metadata section of the page by entering the appropriate information into the text fields provided or by selecting options from the given drop-down list for each of the corresponding citation metadata fields.',
    'r11_p02': 'After creation, on the newly created dataset page, click on the Edit Dataset button located to the right-hand side of the dataset citation.  Select the Metadata option.',
    'r11_p03': 'In each section of the metadata form, add additional descriptive information about the dataset by entering the appropriate information into the text fields provided or by selecting options from the given drop-down list for each of the corresponding metadata fields.',
    'r11_p04': 'Click on the Save Changes button.',

    'r12_title': 'Dataverse must support dataset/study management where the archivist must be able to edit metadata',
    'r12_p01': 'Click on the Edit Dataset button located to the right-hand side of the dataset citation. Select the Metadata option.',
    'r12_p02': 'In each section of the metadata form, edit descriptive information about the dataset by entering the updated information into the text fields provided or by selecting alternative options from the given drop-down list for each of the corresponding metadata fields.',
    'r12_p03': 'Click on the Save Changes button.',
    'r12_p04': 'Click the checkbox next to the file(s) that require(s) editing.',
    'r12_p05': 'Click on the Edit Files button above the file list and select the Metadata option.',
    'r12_p06': 'Update the file name, file path, and description in the corresponding metadata fields for each file as needed.',
    'r12_p07': 'Click on the Save Changes button.',
    'r12_p08': 'Click on the Terms tab on the dataset landing page.',
    'r12_p09': 'Click on the Edit Terms Requirements button.',
    'r12_p10': 'In the Dataset Terms section, select the appropriate terms by selecting from the License/Data Use Agreement drop-down list provided.',
    'r12_p11': 'Enter and/or update custom dataset terms, information about restricted files and terms of access in the fields provided.',
    'r12_p12': 'Click on the Save Changes button.',

    'r13_title': 'Dataverse must support dataset/study management where the archivist must be able to ingest existing data files',
    'r13_p01': 'Upload dataset files in the Upload with HTTP via your browser section of the page by clicking on the Select Files to Add button.',
    'r13_p02': 'In the file explorer box that appears, navigate to and select each file to be included in the dataset.',
    #'r13_p03': 'Alternatively, drag and drop each dataset file into the Drag and drop files here box.  A list of uploaded files will appear with an MD5 and editable file-level metadata fields for each file.',

    'r14_title': 'Dataverse must support dataset/study management where the archivist must be able to review data set/study metadata',
    'r14_p01': 'Inspect the list of files and corresponding file-level metadata to ensure that the correct files were ingested.',
    'r14_p02': 'Inspect the metadata to ensure that the metadata is complete, accurate, and free of typos or grammatical errors.',
    'r14_p03': 'Confirm that that the Dataset Terms are appropriate for the dataset.', 

    'r15_title': 'Dataverse must support dataset/study editing and versioning where the archivist must be able to ingest new version of an existing file',
    'r15_p01': 'Click on the file name to navigate to the file landing page.',
    'r15_p02': 'Click on the Edit File button to the right of the file citation and select the Replace option.',
    'r15_p03': 'Upload the new version of the file in the Upload with HTTP via your browser section of the page by clicking on the Select Files to Add button.',
    'r15_p04': 'In the file explorer box that appears, navigate to and select each file to be included in the dataset.',
    # 'r15_p05': 'Alternatively, drag and drop each dataset file into the Drag and drop files here box.',
    'r15_p06': 'The new file will appear with an MD5 and editable file-level metadata fields. ',
    'r15_p07': 'Confirm that the MD5 matches the pre-dataverse ingest MD5.',
    'r15_p08': 'If necessary, update the file name, file path, and description in the corresponding metadata fields.',
    'r15_p09': 'Click on the Save Changes button.',

    'r16_title': 'Dataverse must support dataset/study editing and versioning where the archivist must be able to add a new file',
    'r16_p01': 'Click on the Upload Files button above the file list.',
    'r16_p02': 'Upload the new file in the Upload with HTTP via your browser section of the page by clicking on the Select Files to Add button.',
    'r16_p03': 'In the file explorer box that appears, navigate to and select the new file to be included in the dataset.',
    'r16_p04': 'Alternatively, drag and drop the new file into the Drag and drop files here box.  The new file uploaded files will appear with an MD5 and editable file-level metadata fields. ',
    'r16_p05': 'Confirm that the MD5 matches the pre-dataverse ingest MD5.',
    'r16_p06': 'If necessary, update the file name and define the file path in the corresponding metadata fields.',
    'r16_p07': 'Add a file description in the Description text field for the new file.',
    'r16_p08': 'Click on the Done button.',

    'r17_title': 'Dataverse must support dataset/study editing and versioning where the archivist must be able to add comments defining changes to dataset/study',
    'r17_p01': 'Add version change notes to the Notes metadata field.',

    'r18_title': 'Dataverse must support dataset/study publication where an archivist must be able to review materials for publication',
    'r18_p01': 'Inspect the list of files and corresponding file-level metadata to ensure that the correct files were ingested.',
    'r18_p02': 'Inspect the citation metadata to ensure that the metadata is complete, accurate, and free of typos or grammatical errors.',
    'r18_p03': 'Confirm that that the Dataset Terms are appropriate for the dataset.',

    'r20_title': 'Dataverse must support dataset/study publication where an archivist must be able compare the pre and post ingest checksum of the file',
    'r20_p01': 'Confirm that the MD5 matches the pre-dataverse ingest MD5 for each file.',
    'r20_p02': 'If necessary, update the file name and define the file path in the corresponding metadata fields for each uploaded file.',
    'r20_p03': 'Add a file description in the Description text field for each uploaded file.',
    'r20_p04': 'Click on the Save Dataset button.',

    'r21_title': 'Dataverse must support Dataset and study discovery where archivists and compliance officers are able to search metadata for individual studies',
    'r21_p01': 'Enter search terms in the search box on the dataverse landing page.',
    'r21_p02': 'Click on the magnifying glass button next to the search box.',
    'r21_p03': 'Select the relevant dataset from the search results that appear.',
    'r21_p04': 'Click on the Advanced Search link next to the search box.',
    'r21_p05': 'In the advanced search form, enter search terms into the corresponding metadata fields.',
    'r21_p06': 'Click on the Find button.',
    'r21_p07': 'Select the relevant dataset from the search results that appear.',

    'r22_title': 'Dataverse must support Dataset and study discovery where archivists and compliance officers are able to view metadata and data files',
    'r22_p01': 'Navigate to the relevant dataset record landing page',
    'r22_p02': 'Review the list of dataset files. To view additional file information, click on the file name to navigate to the file landing page.',
    'r22_p03': 'Review dataset citation and descriptive metadata by clicking on the Metadata tab.',
    'r22_p04': 'Review dataset terms by clicking on the Terms tab.',

    'r23_title': 'Dataverse must support Dataset and study discovery where archivists and compliance officers are able to view version history',
    'r23_p01': 'Navigate to the relevant dataset record landing page and click on the Versions tab',
    'r23_p02': 'To view version details, click on the View Details link for the relevant dataset version.',
    'r23_p03': 'To view differences among versions, click on the checkbox next to the versions to be compared, then click on the View Differences button.',

    'r24_title': 'Dataverse must support Dataset and study discovery where archivists and compliance officers are able to browse Dataverse',
    'r24_p01': 'Dataset records appear on the dataverse main page.  To browse beyond the 10 dataset records on the main landing page, click on a page number or Next > button located below the dataset list.',
    'r24_p02': 'If needed, add filters to the datasets listed.',
    'r24_p03': 'Select the relevant dataset.',

    #TODO: I think I want to test downloading the full zip as well. Maybe instead of download multiple?
    'r25_title': 'Dataverse must support exporting archived packages for audits where archivist and compliance officers must be able to export a dataset/study and audit trail in human readable form for delivery to auditor',
    'r25_p01': 'Navigate to the landing page of the relevant dataset record.',
    'r25_p02': 'To download an individual file, click on the access file icon next to the file information, and select the desired file format from the Download Options section of the drop-down list.',
    'r25_p03': 'To download multiple files, click on the checkbox next to each dataset file that requires downloading.',
    'r25_p04': 'Click on the Download button above the file list, then select the file format required from the available options in the drop-down list.',
    
}

