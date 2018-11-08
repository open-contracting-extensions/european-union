# Changelog

## 2018-11-XX

### New mappings

* II.2.3 Place of performance
* II.1.7 Total value of the procurement
* VI.3 Additional information
* V Award of contract (except for V.2.4 and V.2.5)

### Updated mappings

* I.3 A `ParticipationFee` is used to indicate whether access to the procurement documents is restricted.
* II.2 If the contract is divided into lots, one `Item` is added per lot; otherwise, one `Item` is added in total. The item is used for the object of procurement's title (II.2.1), additional CPV codes (II.2.2), place of performance (II.2.3), description (II.2.4), and additional information (II.2.14).
* II.2.13 The *Identification of the project* is mapped to the financing arrangement's `.description` instead of to either its `.id` or `.title`. A financing arrangement has an array of `.relatedLots` instead of one `.relatedLot`.

### Other changes

* Add guidance on setting `ocid`, `id`, `initiationType`, `tag` and status fields.

## 2018-09-07

[First public working draft](https://www.open-contracting.org/2018/09/06/whats-the-deal-with-trade-public-procurement/).
