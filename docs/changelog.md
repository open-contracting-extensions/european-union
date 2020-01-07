# Changelog

## 2020-01-07

### Added

* Add missing mappings for T01, T02.

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

* [Create a release](../operations/#create-a-release): Use a new `ocid` for a Contract award notice for an award within a framework agreement or dynamic purchasing system.

## 2019-11-15

### Added

* F23, F25, T02: Add mapping to `Award.id`.
* Add missing mappings for F23, F25.

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
  * *Proportion*: Expand `minPercentage` and `maxPercentage` into `minimumPercentage` and `maximumPercentage` to match other field names.

## 2019-10-18

### Added

* F25: II.1.5 Method used for calculating the estimated value of the concession (`/OBJECT_CONTRACT/CALCULATION_METHOD`)

### Changed

* Add Additional Contact Points and Charges extensions to home page
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

## Fixed

* Fix [referencing a previous publication](../operations#reference-a-previous-release) to use `relatedProcesses[].relationship` as an array
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

* Add missing mappings for F12, F21.

### Changed

* Clarify the mappings for:
  * VI.3 Additional information (`/COMPLEMENTARY_INFO/INFO_ADD`)
  * F14 (`/CHANGES/CHANGE/NEW_VALUE/NOTHING`)

## Fixed

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
