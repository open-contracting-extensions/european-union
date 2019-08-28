# Changelog

## 2019-XX-XX

### Added

* Add all missing mappings.
* Add forms F14, F15, F20, T01, T02.
* Add "Release model" heading, to set `ocid`, `id`, `initiationType`, `tag` and status fields.
* Add "What's new" heading, to list new elements on each form.
* Update to R2.0.9.S03.E01_007-20181030 from R2.0.9.S03.E01_006-20180608.

### Changed

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
  * Map to the item's `.description`, instead.
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
