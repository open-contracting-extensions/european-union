# Common mappings

All XML notices contain the following elements, which have no form labels:

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
