# Common operations

To avoid repetition in the guidance, we refer and link to the following common operations.

## Create a release

1. If this is the first publication concerning the procedure, or if the previous publication is either a Prior information notice or a Periodic indicative notice that is for prior information only, set [`ocid`](http://standard.open-contracting.org/latest/en/schema/identifiers/#contracting-process-identifier-ocid) by prepending your [OCID prefix](http://standard.open-contracting.org/latest/en/implementation/registration/) to a unique identifier of your choice (e.g. a [version 4 UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier)). Otherwise, this notice's `ocid` should be the same as the previous publication's `ocid`.
1. Set [`id`](http://standard.open-contracting.org/latest/en/schema/identifiers/#release-id) to the notice number.
1. Set `initiationType` to 'tender'.

## Reference a previous publication

If the *Previous publication concerning this procedure* is neither a Prior information notice nor a Periodic indicative notice (PIN), or if the PIN is **not** for prior information only, then discard `/PROCEDURE/NOTICE_NUMBER_OJ`. In this case, the *previous publication concerning this procedure* is the OCDS release with the same `ocid` as this release and with the nearest earlier `date` to this release.

Otherwise, if the *Previous publication concerning this procedure* is either a Prior information notice or a Periodic indicative notice that is for prior information only, add a `RelatedProcess` object to the `relatedProcesses` array, set its `.id`, set its `.relationship` to 'planning', set its `.scheme` to 'eu-oj' (or to a scheme of your choice if outside the EU), and map `/PROCEDURE/NOTICE_NUMBER_OJ` to `.identifier`.

## Add a party

Add an `Organization` object to the `parties` array, and set its `.id`. A party's `.id` needs to be consistent across all forms.

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
