# OCDS for the European Union

## Standard forms for public procurement

```eval_rst
.. toctree::
   :maxdepth: 2

   F01
   F02
   F03
```

## Common mappings

<div class="wy-table-responsive">
  <div class="wy-table-responsive"><table class="docutils">
    <thead>
      <tr>
        <th>XPath</th>
        <th>OCDS guidance</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td id="/@LG">
          <p><code>/@LG</code></p>
        </td>
        <td>
<p>Lowercase, and map to <code>language</code></p>
        </td>
      </tr>
      <tr>
        <td id="/@CATEGORY">
          <p><code>/@CATEGORY</code></p>
        </td>
        <td>
<p>Discard. TED translates at form-level. OCDS translates at field-level.</p>
        </td>
      </tr>
      <tr>
        <td id="/LEGAL_BASIS">
          <p><code>/LEGAL_BASIS</code></p>
        </td>
        <td>
<p>Map to <code>tender.legalBasis</code> <span class="badge badge-proposal">Proposal</span></p>
        </td>
      </tr>
  </tbody></table></div>
</div>

## Common operations

### Add a party

Add an `Organization` object to the `parties` array, and set its `.id`.