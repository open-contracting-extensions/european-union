# OCDS for the European Union

This website describes how to express, in OCDS, the information in Tenders Electronic Daily (TED) notices.

## European context

### Legal

The primary legislation for public contracting in the European Union includes:

* [Directive 2014/24/EU](https://eur-lex.europa.eu/eli/dir/2014/24/oj) on public procurement
* [Directive 2014/23/EU](https://eur-lex.europa.eu/eli/dir/2014/23/oj) on the award of concession contracts
* [Directive 2014/25/EU](https://eur-lex.europa.eu/eli/dir/2014/25/oj) on procurement by entities operating in the water, energy, transport and postal services sectors
* [Regulation (EC) No 1370/2007](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02007R1370-20171224)

The secondary legislation includes the [Commission Implementing Regulation (EU) 2019/1780](https://eur-lex.europa.eu/eli/reg_impl/2019/1780/oj) (eForms), which establishes standard forms for the publication of procurement notices, and repeals the earlier [Commission Implementing Regulation (EU) 2015/1986](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015R1986).

This guidance does not cover:

* [Directive 2009/81/EC](https://eur-lex.europa.eu/eli/dir/2009/81/oj) on the coordination of procedures for the award of certain works contracts, supply contracts and service contracts by contracting authorities or entities in the fields of defence and security

### Technical

[PDF files](https://simap.ted.europa.eu/standard-forms-for-public-procurement) of the forms are provided by the European Commission, for reference only ([Prior information notice](https://simap.ted.europa.eu/documents/10184/99173/EN_F01.pdf), for example). However, the PDF files don't formally specify the form fields and their possible values (numbers, dates, codes, etc.). These are specified in the Tenders Electronic Daily (TED) [XML schemas](https://op.europa.eu/en/web/eu-vocabularies/e-procurement/tedschemas). Of particular interest is the Publication Schema, which is used to publish notices.

Reading the schema, however, is challenging, unless you're familiar with XML Schema and related tools. To make it easier to understand the structure of the notices, we generated [XML files](https://github.com/open-contracting/european-union-support/tree/main/output/samples) for the notices, which provide validation rules in comments, and retain XML Schema elements like `<choice>` only where necessary.

The European Commission also provides [template PDF files](https://publications.europa.eu/documents/3938058/5358176/Archive.zip/ce7ceb02-94b0-04e8-8b9f-7fb4acf1ccdb), in which label keys like `ca` stand for labels like 'Contracting authority', and provides an Excel file that maps the label keys to labels in official languages of the European Union.

This guidance is based on the TED publication XML schema R2.0.9 (S05, 2021-07-30). It does not cover XML schema R2.0.8, used for the standard forms related to Directive 2009/81/EC, which are:

* F16: Prior information notice for contracts in the field of defence and security
* F17: Contract notice for contracts in the field of defence and security
* F18: Contract award notice for contracts in the field of defence and security
* F19: Subcontract notice

## TED-to-OCDS mapping

This website takes the human-readable form labels from the standard form PDF files, pairs them with the machine-readable element names from the TED XML files, and provides guidance on how to express the information in OCDS.

In this way, a policy analyst can see the relationship to the standard forms established in the Implementing Regulation, and a software developer can see the relationship to the elements defined in the TED XML schema.

```{toctree}
:maxdepth: 2

forms/index
operations
```

### Reading this website

The guidance on each page above follows the same order as a standard form and is organized into the same sections. Within each section, there is a table with three columns. For example:

<table class="docutils">
  <colgroup>
    <col width="8%">
    <col width="50%">
    <col width="42%">
  </colgroup>
  <thead>
    <tr>
      <th>Index</th>
      <th>Label and XPath</th>
      <th>OCDS guidance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>II.1.1</td>
      <td id="/OBJECT_CONTRACT/TITLE">
        <p>Title<br><code>/OBJECT_CONTRACT/TITLE</code></p>
      </td>
      <td>
<p>Map to <code>tender.title</code></p>
      </td>
    </tr>
  </tbody>
</table>

* **Index** makes it easy to find the content at the same index in the form
* **Label and XPath** contains a paired form label and XML path
* **OCDS guidance** describes how to transform TED XML to OCDS JSON (in most cases, the transformation is reversible)

Most fields map simply and directly from TED XML to OCDS JSON. Badges are used to call attention to special cases:

* <span class="badge badge-warning">Attention</span> If there is a potential issue with the guidance, it is described briefly, and a link is provided to a GitHub issue to acknowledge or dismiss the potential issue.
* <span class="badge badge-issue">Issue</span> If there is a reported issue with the guidance, it is described briefly, and a link is provided to the GitHub issue.

When reading the guidance on this website, it may be useful to refer to the notice's [PDF file](https://simap.ted.europa.eu/standard-forms-for-public-procurement) (be sure to open the new, not old, form), to see whether the field is a check box, radio button, etc. and to its [XML file](https://github.com/open-contracting/european-union-support/tree/main/output/samples), to see the validation rules and other context.

### Understanding the concepts in the forms

In many cases, the form labels from the PDF files and the element names from the XML files are both short and ambiguous, and therefore difficult to interpret. In such cases, it is useful to refer to:

* the European Union's primary legislation ([above](#legal))
* the European Commission's [Public procurement standard forms guidance](https://ec.europa.eu/docsroom/documents/24191/attachments/1/translations/en/renditions/native)
* the description of corresponding business terms in [eForms' extended annex](https://ec.europa.eu/docsroom/documents/43488)
* any TED notices that use the field

## Technical reference

```{toctree}
:maxdepth: 2

reference/index
changelog
```

## We want your feedback!

To contribute, please first read this page, and then dive into the guidance. Feedback is discussed openly on GitHub. To browse all issues or to open another issue, visit [this website's GitHub issues](https://github.com/open-contracting-extensions/european-union/issues).
