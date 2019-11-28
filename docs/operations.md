# Common operations

To avoid repetition in the guidance, we refer and link to the following common operations.

## Create a release

1. Set [`id`](https://standard.open-contracting.org/latest/en/schema/identifiers/#release-id) to the notice number.
1. Set `initiationType` to 'tender'.
1. Set `ocid` as described below.

The notice's `ocid` will either be a new `ocid`, or the same `ocid` as the previous publication concerning this procedure. The notice's `ocid` will be a new `ocid` if one of the following is true:

* The notice is the first publication concerning the procedure.
* The previous publication is a Prior information notice or Periodic indicative notice that has multiple `/OBJECT_CONTRACT` (*Object*) elements.
* The notice is a Contract award notice for an award within a framework agreement or dynamic purchasing system.

If none is true, then set the notice's `ocid` to be the same as the previous publication's `ocid`. Otherwise, set the notice's [`ocid`](https://standard.open-contracting.org/latest/en/schema/identifiers/#contracting-process-identifier-ocid) by prepending your [OCID prefix](https://standard.open-contracting.org/latest/en/implementation/registration/) to a unique identifier of your choice (e.g. a [version 4 UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) or a suitable system-internal identifier).

If the notice is a Contract award notice for an award within a framework agreement or dynamic purchasing system, you must also add a `RelatedProcess` object to the `relatedProcesses` array, set its `.id` to '1', add 'framework' to its `.relationship` array, set its `.scheme` to 'ocds', and set its `.identifier` to the `ocid` of the procedure that set up the framework agreement or dynamic purchasing system.

## Reference a previous publication

If the *Previous publication concerning this procedure* is neither a Prior information notice nor a Periodic indicative notice (PIN), or if the PIN has a single `/OBJECT_CONTRACT` (*Object*) element, then discard `/PROCEDURE/NOTICE_NUMBER_OJ`. In this case, the *previous publication concerning this procedure* is the OCDS release with the same `ocid` as this release and with the nearest earlier `date` to this release.

Otherwise, if the *Previous publication concerning this procedure* is a Prior information notice or Periodic indicative notice that has multiple `/OBJECT_CONTRACT` (*Object*) elements, add a `RelatedProcess` object to the `relatedProcesses` array, set its `.id` to '1', add 'planning' to its `.relationship` array, set its `.scheme` to 'eu-oj' (or to a scheme of your choice if outside the EU), and map `/PROCEDURE/NOTICE_NUMBER_OJ` to `.identifier`.

## Add a party

Add an `Organization` object to the `parties` array, and set its `.id` (string). **A party's `.id` needs to be consistent across all notices.** It is recommended to implement a register of organization identifiers to assign consistent identifiers. For more information, [see the OCDS documentation](https://standard.open-contracting.org/latest/en/schema/identifiers/#organization-ids).

## Add a bids statistic

Add a `BidsStatistic` object to the `bids.statistics` array, and set its `.id` (string) sequentially across all notices of the same type for this procedure. (A first F03 notice for a given procedure uses `id`'s '1' through '9', a second F03 notice for the same procedure uses `id`'s '10' and up, etc.)

## Set time components

If a time component is missing from a date, use `T23:59:59Z` for end dates and `T00:00:00Z` for other dates.

## Get a translation

1. Download "Form labels R2.0.9 (zip)" from [TED schemas](https://publications.europa.eu/en/web/eu-vocabularies/tedschemas)

To translate a label from English to another language:

1. Find the row with the label in the "EN" column
1. Take the value in the desired column of the same row

To translate a label from another language to English:

1. Find the row with the label in the appropriate column
1. Take the value in the "EN" column of the same row
