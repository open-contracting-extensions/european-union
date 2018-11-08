```eval_rst
:orphan:
```

# Common operations

To avoid repetition in the guidance, we refer and link to the following common operations.

## Create a release

1. Set [`ocid`](http://standard.open-contracting.org/latest/en/schema/identifiers/#contracting-process-identifier-ocid) by prepending your [OCID prefix](http://standard.open-contracting.org/latest/en/implementation/registration/) to `/OBJECT_CONTRACT/REFERENCE_NUMBER` (*Reference number*) if it is available, or to another internal identifier if not.
    * If this notice is preceded by a Contract notice or Design contest notice (CN), this notice's `ocid` should correspond to the CN's `ocid`.
    * If this notice is preceded by a Prior information notice or Periodic indicative notice (PIN), this notice's `ocid` should correspond to one of the PIN's `ocid`’s.
1. Set [`id`](http://standard.open-contracting.org/latest/en/schema/identifiers/#release-id) by appending `/COMPLEMENTARY_INFO/DATE_DISPATCH_NOTICE` (*Date of dispatch of this notice*) to `/OBJECT_CONTRACT/REFERENCE_NUMBER` (*Reference number*) if it is available, or to another internal identifier if not.
1. Set `initiationType` to 'tender'.

## Add a party

Add an `Organization` object to the `parties` array, and set its `.id`.

## Set time components

If a time component is missing from a date, use `T23:59:59Z` for end dates and `T00:00:00Z` for other dates.
