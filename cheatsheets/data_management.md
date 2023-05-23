# Data Management
* 11 Data Management Areas
	* Data Governance
	* Data Architecture
	* Data Modeling and Design
	* Data Storage and Operations
	* Data Security
	* Data Integration and Interoperability
	* Document and Content Management
	* Reference and Master Data
	* Data Warehousing and Business Intelligence
	* Metadata
	* Data Quality
## Data Governance
* Data Governance Definition
* Data Domains <https://en.wikipedia.org/wiki/Data_domain>
* Data Governance Roles:
	* CDO <https://en.wikipedia.org/wiki/Chief_data_officer>
	* Data Steward <https://en.wikipedia.org/wiki/Data_steward>
	* Business Steward
	* Technical Steward
* Data Dictionary <https://en.wikipedia.org/wiki/Data_dictionary>
## GDPR
* <https://gdpr-info.eu/>
* <https://gdpr.eu/>
* General Data Protection Regulation, 11 chapters and 99 articles, implemented on 25th may 2018, is a regulation in EU law on data protection and privacy of all individuals citizens of the EU and the EEA, aswel at the export of personal data outside of the EU and EEA.
* Scope
* Consent (art. 7)
	* conditions...
* Pseudonymisation vs Tokenization (reversability and availability).
* Data at rest
* Data in transit
* Data in use
* 5 techniques:
	* Data Masking
	* Data Scrambling (can be reversed)
	* Data Encryption
	* Tokenization
	* Data Blurring
* Right of access (art. 15)
* Right to rectification (art. 16)
* Right to erasure (art. 17) (vs right to be forgotten)
* Right to restriction of processing (art. 18)
* Right to data portability (art. 20)
* Right to object (art. 21)
* Data protection by design and by default (art. 25)
* DPO (Data Protection Officer)
* Right to be informed
* Data Breaches
* Right to breach notification
* Sanctions
* Cases of inforcement (Google,...)

## Data Quality
* 6 Dimensions of Data Quality (CUVACT)
    * Completeness (NOT NULL + non-incomplete data) (e.g. missing or incomplete critical data)
    * Uniqueness (UNIQUE / PK) (e.g. two times the same persons name.)
    * Validity (correct data format) (DATA TYPE + CHECK) (e.g. phone number of the correct format.)
    * Accuracy (The data represents the real world.) (e.g. John is John and not Jon.)
    * Consistency (The data is the same from table to table.) (FK)
    * Timeliness (availability of the data / fast access)
