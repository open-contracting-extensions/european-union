# Changelog

## 2024-01-19

### Changed

* Rename `electronicCataloguePolicy` to `electronicCatalogPolicy`.

## 2022-04-27

### Changed

* Update to R2.0.9.S05.E01_001-20210730 from R2.0.9.S03.E01_007-20181030, including new `/PROCEDURE` elements for T01.

## 2022-03-14

### Changed

* III.1.2 Selection criteria as stated in the procurement documents
  * Change mapping to use `tender.selectionCriteria.criteria` instead of `tender.documents`
* III.1.3 Selection criteria as stated in the procurement documents
  * Change mapping to use `tender.selectionCriteria.criteria` instead of `tender.documents`

## 2021-04-20

### Changed

* II.2.13 Information about European Union funds (`/OBJECT_CONTRACT/OBJECT_DESCR/EU_PROGR_RELATED`)
  * Clarify setting of `.relatedLots` on existing objects
* Contract No (`/AWARD_CONTRACT/CONTRACT_NO`)
  * Add warning about non-unique values
* Minimum level(s) of standards possibly required (`/LEFTI/ECONOMIC_FINANCIAL_MIN_LEVEL`, `/LEFTI/TECHNICAL_PROFESSIONAL_MIN_LEVEL`)
  * Repeat changes from 2020-10-07 on F01 and F04

## 2020-10-07

### Changed

* Minimum level(s) of standards possibly required (`/LEFTI/ECONOMIC_FINANCIAL_MIN_LEVEL`, `/LEFTI/TECHNICAL_PROFESSIONAL_MIN_LEVEL`)
  * Clarify mapping when no `SelectionCriterion` object exists

## 2020-09-29

### Fixed

* F05: III.1.6 Deposits and guarantees required (`/LEFTI/DEPOSIT_GUARANTEE_REQUIRED`)
  * Rename `requiresGuarantees` to `depositsGuarantees`, and map as string instead of as boolean

## 2020-07-06

### Changed

* F20: II.2 Description (`/OBJECT_CONTRACT/OBJECT_DESCR`)
  * Remove mapping for the lot's `.status`
* F20: VII.1.4 Description of the procurement (`//MODIFICATIONS_CONTRACT/DESCRIPTION_PROCUREMENT/SHORT_DESCR`) and VII.2.3 Total contract value after the modifications (`/MODIFICATIONS_CONTRACT/INFO_MODIFICATIONS/VALUES/VAL_TOTAL_AFTER`)
  * Clarify precedence

### Fixed

* F14, F20: Set `Amendment.id` to guarantee global unique values

## 2020-06-22

### Changed

* F21, F22: Clarify mapping of `/NOTICE/@TYPE`

## 2020-05-28

### Added

* Add Country Code extension

## 2020-04-30

### Added

* Add Status Details extension

## 2020-04-28

### Added

* Add Legal Basis, Recurrence, Renewal, Tender Classifications extensions

### Fixed

* F15: D4.1 Justification for the award of the concession without publication of a concession notice in accordance with Article 31(4) and (5) of Directive 2014/23/EU (`/PROCEDURE/DIRECTIVE_2014_23_EU/PT_AWARD_CONTRACT_WITHOUT_PUBLICATION/D_ACCORDANCE_ARTICLE`)
  * The `.id` was the same (instead of different) for all mappings

## 2020-04-23

### Added

* F13: V Results of contest (`/RESULTS`)

## 2020-04-17

### Added

* Add Essential Assets extension
* T02: V.2.3: National registration number (`/AWARD_CONTRACT/AWARDED_CONTRACT/CONTRACTORS/CONTRACTOR/ADDRESS_PARTY/NATIONALID`)

### Changed

* Move common mappings to individual pages
* Clarify mapping of `/LEGAL_BASIS` and `/LEGAL_BASIS_OTHER`

## 2020-04-07

### Added

* Add schema and codelist [reference pages](../reference/index)
* Add Design Contest and Unstructured Changes extensions
* I.1 National registration number (`/CONTRACTING_BODY/ADDRESS_CONTRACTING_BODY/NATIONALID`)
  * Add a link to the [identifiers reference](https://standard.open-contracting.org/1.1/en/schema/identifiers/#organization-ids) in the OCDS documentation
* I.3 Tenders or requests to participate must be submitted to the following address (`/CONTRACTING_BODY/ADDRESS_PARTICIPATION`)
  * Clarify that the XML elements are mapped as a formatted string

### Changed

* IV.3.4 Decision of the jury (`/PROCEDURE/DECISION_BINDING_CONTRACTING` and `/PROCEDURE/NO_DECISION_BINDING_CONTRACTING`)
  * Rename `isBindingJuryDecision` to `bindingJuryDecision` to follow schema style guide

### Fixed

* II.2.13 Information about European Union funds (`/OBJECT_CONTRACT/OBJECT_DESCR/EU_PROGR_RELATED`)
  * Fix the indentation of the instruction for `relatedLots`

## 2020-03-30

### Fixed

* V.2.5 Information about subcontracting (`/AWARD_CONTRACT/AWARDED_CONTRACT/DIRECTIVE_2009_81_EC`)
  * Redo mapping of three elements related to Title III of Directive 2009/81/EC

## 2020-03-27

### Fixed

* VII Changes (`/CHANGES`)
  * Redo mapping of all elements ([GitHub discussion](https://github.com/open-contracting-extensions/european-union/issues/63))

## 2020-03-12

### Added

* Add Communication extension

## 2020-03-09

### Added

* Add Procurement Method Rationale Classifications extension

### Changed

* Rename `procurementMethodRationaleCodes` to `procurementMethodRationaleClassifications` to follow schema style guide

## 2020-03-06

### Added

* Clarify changes in mappings between forms

### Fixed

* F12: III.2.1 Information about a particular profession (`/LEFTI/PARTICULAR_PROFESSION`)
  * Unlike earlier forms, F12 has `/LEFTI/NO_PARTICULAR_PROFESSION`, and the XML schema for `/LEFTI/PARTICULAR_PROFESSION` differs
* F23, F25: D4.1 Justification for the award of the concession without publication of a concession notice in accordance with Article 31(4) and (5) of Directive 2014/23/EU (`/PROCEDURE/PT_AWARD_CONTRACT_WITHOUT_PUBLICATION/D_ACCORDANCE_ARTICLE`)
  * The `.id` was the same (instead of different) for all mappings

## 2020-02-24

### Added

* T02: Add Section III, Section V mappings
* Add Metrics and Shareholders extensions

## 2020-02-10

### Added

* T01, T02: Add "Release model" and "What's new" sections

### Changed

* Fix typos that don't affect the mappings

## 2020-02-05

### Fixed

* II.2.1 Title (`/OBJECT_CONTRACT/OBJECT_DESCR/TITLE`)
  * Map only to the lot's `.title`, not to the item's `.title` to be consistent with II.2.4 Description of the procurement

## 2020-01-07

### Added

* Add missing mappings for T01, T02

### Fixed

* `Classification` objects have a `description` field, not a `name` field. Affects:
  * I.4 Type of the contracting authority
  * I.5 Main activity
  * I.6 Main activity
  * D1.1 Justification for the choice of the negotiated procedure without prior publication of a call for competition in accordance with Article 32 of Directive 2014/24/EU
  * D2.1 Justification for the choice of the negotiated procedure without prior publication of a call for competition in accordance with Article 50 of Directive 2014/25/EU
  * D3.1 Justification for the choice of the negotiated procedure without publication of a call for competition in accordance with Article 28 of Directive 2009/81/EC
  * D4.1 Justification for the award of the concession without publication of a concession notice in accordance with Article 31(4) and (5) of Directive 2014/23/EU

## 2019-11-28

### Added

* V.2.4 Information on value of the contract/lot
  * *Currency*: Clarify the mapping for bid statistics

### Changed

* [Create a release](operations.md#create-a-release): Use a new `ocid` for a contract award notice for an award within a framework agreement or dynamic purchasing system

## 2019-11-15

### Added

* F23, F25, T02: Add mapping to `Award.id`
* Add missing mappings for F23, F25

## 2019-11-07

### Fixed

* II.2.13 Information about European Union funds
  * Set the `.id` of `Finance` objects incrementally, instead of to '1'
* II.2.14 Additional information
  * Append only to the lot's `.description`, not to the item's `.description`, to be consistent with II.2.4 Description of the procurement
* VII.1.3 NUTS code
  * Reuse the mapping for II.2.3 NUTS code
* VII.1.4 Description of the procurement
  * Reuse the mapping for II.2.4 Description of the procurement

## 2019-11-04

### Changed

* F20: Clarify that the mapping assumes that `/AWARD_CONTRACT/CONTRACT_NO` is consistently set across forms

### Fixed

* III.1.5 Information about reserved contracts
  * `tender.otherRequirements.reservedParticipation` is an array of strings, instead of a string

## 2019-11-01

### Fixed

* V.2.5 Value or proportion likely to be subcontracted to third parties
  * *Proportion*: Expand `minPercentage` and `maxPercentage` into `minimumPercentage` and `maximumPercentage` to match other field names

## 2019-10-18

### Added

* F25: II.1.5 Method used for calculating the estimated value of the concession (`/OBJECT_CONTRACT/CALCULATION_METHOD`)

### Changed

* Add Additional Contact Points and Charges extensions
* Clarify the type of fields:
  * 1e9999 is a number, not a string (`/OBJECT_CONTRACT/LOT_DIVISION/LOT_ALL` and `/PROCEDURE/FRAMEWORK/SEVERAL_OPERATORS`)
  * `tender.lots[].awardCriteria` is an object (`/OBJECT_CONTRACT/OBJECT_DESCR/AC`)
  * `tender.coveredBy` is an array (`/PROCEDURE/CONTRACT_COVERED_GPA`)
* Clarify that `id` fields are strings:
  * `parties[].id`
  * `bids.statistics[].id` (`/OBJECT_CONTRACT/VAL_RANGE_TOTAL`, `/AWARD_CONTRACT/AWARDED_CONTRACT/TENDERS`, `/AWARD_CONTRACT/AWARDED_CONTRACT/VALUES/VAL_RANGE_TOTAL`, `/RESULTS/AWARDED_PRIZE/PARTICIPANTS`)
  * `tender.amendments[].id` (`/CHANGES`)
  * `contracts[].amendments[].id` (`/MODIFICATIONS_CONTRACT/INFO_MODIFICATIONS`)
* Emphasize that string elements in TED map to string fields in OCDS:
  * `tender.id` (`/OBJECT_CONTRACT/REFERENCE_NUMBER`)
  * `tender.lots[].id` (`/OBJECT_CONTRACT/OBJECT_DESCR/LOT_NO`)
  * `tender.items[].id` (`/OBJECT_CONTRACT/OBJECT_DESCR/LOT_NO`)
  * `tender.items[].relatedLot` (`/OBJECT_CONTRACT/OBJECT_DESCR/LOT_NO`)
  * Each `awards[].relatedLots[]` (`/AWARD_CONTRACT/LOT_NO`)

### Fixed

* Fix [referencing a previous publication](operations.md#reference-a-previous-publication) to use `relatedProcesses[].relationship` as an array
* Prefix 'http://' to `parties[].contactPoint.url` if there is no URL scheme (`/CONTRACTING_BODY/URL_DOCUMENT`)
* Remove any duplicate entries from `tender.additionalClassifications` and `tender.items[].additionalClassifications` arrays (`/OBJECT_CONTRACT/CPV_MAIN/CPV_SUPPLEMENTARY_CODE` and `/OBJECT_CONTRACT/OBJECT_DESCR/CPV_ADDITIONAL`)
* Change the mappings for:
  * III.1.5 The execution of the contract is restricted to the framework of sheltered employment programmes (`/LEFTI/RESTRICTED_SHELTERED_PROGRAM`)
  * III.2.1 Information about a particular profession (`/LEFTI/PARTICULAR_PROFESSION` and `/LEFTI/REFERENCE_TO_LAW`)
* Set `id` fields as follows:
  * `tender.id` has, as its default value, the `ocid` value
  * `awards[].id` has, as its default value, the notice number and `ITEM` attribute
  * Set `parties[].id` consistently across all notices
  * Set `bids.statistics[].id` sequentially across all notices of the same type for the same procedure (`/OBJECT_CONTRACT/VAL_RANGE_TOTAL`, `/AWARD_CONTRACT/AWARDED_CONTRACT/TENDERS`, `/AWARD_CONTRACT/AWARDED_CONTRACT/VALUES/VAL_RANGE_TOTAL`, `/RESULTS/AWARDED_PRIZE/PARTICIPANTS`)
  * Set `tender.amendments[].id` sequentially across all F14 notices for the same procedure (`/CHANGES`)
  * Set `contracts[].amendments[].id` sequentially across all F20 notices for the same procedure (`/MODIFICATIONS_CONTRACT/INFO_MODIFICATIONS`)
  * Set `tender.documents[].id` to either 'economic' or 'technical' (`/LEFTI/ECONOMIC_CRITERIA_DOC` and `/LEFTI/TECHNICAL_CRITERIA_DOC`)
  * Set `tender.participationFees[0].id` to '1' (`/CONTRACTING_BODY/DOCUMENT_RESTRICTED`)
  * Set `planning.budget.finance[0].id` to '1' (`/OBJECT_CONTRACT/OBJECT_DESCR/EU_PROGR_RELATED`)
  * Set `relatedProcesses[0].id` to '1'

## 2019-10-01

### Added

* Add missing mappings for F12, F21

### Changed

* Clarify the mappings for:
  * VI.3 Additional information (`/COMPLEMENTARY_INFO/INFO_ADD`)
  * F14 (`/CHANGES/CHANGE/NEW_VALUE/NOTHING`)

### Fixed

* Fix `ocid` and `id` mappings
* Rename OCDS fields:
  * `requiresStaffNamesQualifications` to `requiresStaffNamesAndQualifications`
  * `hasRequiredGuarantees` to `requiresGuarantees`
  * `subcontracting.details` to `subcontracting.description`
* II.2.3 NUTS code (`/OBJECT_CONTRACT/OBJECT_DESCR/NUTS`)
  * Support repeated XML elements
* II.2.4 Description of the procurement (`/OBJECT_CONTRACT/OBJECT_DESCR/SHORT_DESCR`)
  * Map only to the lot's `.description`, not to the item's `.description`
* III.1.5 The execution of the contract is restricted to the framework of sheltered employment programmes (`/LEFTI/RESTRICTED_SHELTERED_PROGRAM`)
  * Change `tender.contractTerms.reservedExecution` from a boolean to an object, and add `tender.contractTerms.reservedExecution.shelteredEmployment`
* III.1.5 Participation in the procedure is reserved to organisations pursuing a public service mission and fulfilling the conditions set in Article 77(2) of Directive 2014/24/EU (`/LEFTI/RESERVED_ORGANISATIONS_SERVICE_MISSION`)
  * Fix a typo, from `tender.selectionCriteria.reservedParticipation` to `tender.otherRequirements.reservedParticipation`
* III.2.1 Information about a particular profession (`/LEFTI/PARTICULAR_PROFESSION` and `/LEFTI/REFERENCE_TO_LAW`)
  * Change `tender.contractTerms.reservedExecution` from a boolean to an object, and add `tender.contractTerms.reservedExecution.particularProfession` and `tender.contractTerms.reservedExecution.particularProfessionDetails`
* IV.2.1 Previous publication concerning this procedure (`/PROCEDURE/NOTICE_NUMBER_OJ`)
  * Don't discard
* F12: Don't use the `tender.lots` or `tender.items` arrays
* F13: Don't use the 'contract' code, `contracts` array, or `bids.statistics.relatedLot` field

## 2019-08-30

### Added

* Add missing mappings.
* Add forms F14, F15, F20, T01, T02.
* Add "Release model" heading, to set `ocid`, `id`, `initiationType`, `tag` and status fields.
* Add "What's new" heading, to list new elements on each form.
* Update to R2.0.9.S03.E01_007-20181030 from R2.0.9.S03.E01_006-20180608.

### Fixed

#### Section I

* I.3 Communication
  * `tender.participationFees` indicates whether access to the procurement documents is restricted.
  * Rename `tender.communicationDetails.accessToolUrl` to `tender.communication.atypicalToolUrl`.

#### Section II

* II.1.6 Information about lots
  * If a contract isn't divided into lots, there is a single, virtual lot.
* II.2 Description
  * If a contract isn't divided into lots, add a single, virtual lot, instead.
  * Add an `Item` object to the lot's `.items`.
  * Set the lot's `.status`.
* II.2.1
  * *Title*: Map to the item's `.title`, also.
  * *Lot No*: Map to the item's `.id` and `.relatedLot`, also.
* II.2.2 Additional CPV code(s)
  * Map to the item's `.additionalClassifications`, instead.
* II.2.4 Description of the procurement
  * Map to the item's `.description`, instead of `tender.description`, if the contract isn't divided into lots.
* II.2.7 Duration of the contract, framework agreement or dynamic purchasing system
  * *This contract is subject to renewal*: Use the lot's `.hasRenewal` and `.renewal.description`, instead of `tender.renewals`.
* II.2.10 Information about variants
  * Use the lot's `.submissionTerms.variantPolicy`, instead of `tender.variants`.
* II.2.11 Information about options
  * Use the lot's `.hasOptions` and `.options.description`, instead of `tender.options`.
* II.2.13 Information about European Union funds
  * The *Identification of the project* is mapped to the financing arrangement's `.description` instead of to either its `.id` or `.title`. A financing arrangement has an array of `.relatedLots` instead of one `.relatedLot`.
* II.2.14 Additional information
  * Append to the lot's `.description` and item's `.description`, instead.
* II.3 Estimated date of publication of contract notice
  * Map to `tender.communication.futureNoticeDate`, instead.

#### Section IV

* IV.1.1 Type of procedure
  * Replace all mappings.
* IV.2.4 Languages in which tenders or requests to participate may be submitted
  * Rename `tender.submissionLanguages` to `tender.submissionTerms.languages`.

#### Section VI

* VI.2 Information about electronic workflows
  * Replace `tender.techniques` with `tender.contractTerms.hasElectronicOrdering`, `tender.contractTerms.electronicInvoicing` and `tender.contractTerms.hasElectronicPayment`

## 2018-09-07

[First public working draft](https://www.open-contracting.org/2018/09/06/whats-the-deal-with-trade-public-procurement/).
