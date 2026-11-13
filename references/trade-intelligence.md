# Trade-code and shipment intelligence

Use this branch only when the offer is a physical good and cross-border trade evidence could improve market selection or company discovery. Skip it for services, software, individual-user research, local-only targets, and physical goods where trade data adds no useful signal.

## Purpose and boundaries

HS, HSN, HTS, CN, and national tariff codes classify goods; they do not identify a qualified customer by themselves. Use codes to:

- translate a product description into searchable commodity families;
- compare import or export demand by country, period, value, quantity, and port when available;
- discover candidate importers, exporters, distributors, or suppliers through accessible shipment sources;
- cross-check whether a company has handled a relevant product.

Never treat a code match, shipment row, or country total as proof of current demand, decision-making authority, company size, or a usable contact route. Verify the company and present offer fit independently.

## Inputs

Accept a known code when provided, but never require one. When no code is supplied:

1. Start from the user's exact product description and intended end use.
2. Identify classification details that can change the heading or subheading: material and composition percentages, physical form, filament or staple form where relevant, construction or manufacturing method, weight or dimensions, finish, packaging, and whether the product is complete, unfinished, or a component.
3. Research candidate HS4 and HS6 families from authoritative descriptions.
4. Determine the destination or reporting jurisdiction before selecting a national 8- or 10-digit code.
5. Ask only for unresolved characteristics that would change the search materially.

Record every inferred code as `candidate`, with jurisdiction, code level, description, source URL, checked date, confidence, and unresolved characteristics. Mark `verified for research` only after its description matches the supplied product and a current authoritative source. Final customs classification remains the responsibility of the exporter/importer and qualified customs adviser.

## Source order

### 1. Classification

Prefer current customs or trade-authority sources for the relevant jurisdiction. For India:

- [ICEGATE I4C import tariff enquiry](https://www.icegate.gov.in/Webappl/index_imp.jsp) accepts tariff heads and product descriptions and exposes current tariff and compliance information.
- [Indian Trade Portal](https://indiantradeportal.in/) supports ITC-HS or product-description search and trade-policy information.
- [DGFT HS code mapping PDF](https://content.dgft.gov.in/Website/HS_Code_Mappin.pdf) is a broad product-to-code mapping reference. It is useful for candidate discovery, but is static and must not replace live validation.

Use the linked DGFT PDF rather than embedding a stale copy. Codes, descriptions, units, and national extensions can change.

### 2. Aggregate market evidence

- India TradeStat provides official aggregate [export](https://tradestat.commerce.gov.in/eidb/commodity_wise_export) and [import](https://tradestat.commerce.gov.in/meidb/commoditywise_import) reports by commodity, country, region, period, value, and related views.
- [Trade Connect](https://www.trade.gov.in/) provides product and country guidance, trade events, and Indian exporter discovery features.
- Use equivalent official statistics from destination countries or UN/ITC sources when India data does not answer the market question.

Official Indian DGCIS dissemination is aggregate. Its [data dissemination policy](https://dgciskol.gov.in/Writereaddata/Downloads/Data_dissemination_policy1.pdf) says normal releases do not publish transaction-, invoice-, IEC-, importer-, exporter-, firm-, or vendor-level data. Do not promise named companies from TradeStat.

### 3. Company discovery

When the brief needs named companies, search accessible sources that expose company or shipment identity:

- public bills of lading or customs/shipment databases;
- trade-promotion and exporter directories;
- port, tender, procurement, and buyer directories;
- shipment-data products searchable by code, product, importer, exporter, origin, destination, or date;
- company sites, catalogues, filings, fair records, and public social pages.

Coverage, fields, freshness, country availability, and paywalls vary by provider. Use a paid or logged-in source only when already available and authorized. Record whether evidence is a full record, preview, snippet, or vendor claim. Never describe a preview as complete shipment coverage.

### 4. Company verification

For each discovered company:

1. Resolve legal name, aliases, domain, country, and business type.
2. Confirm product relevance on company-owned or attributable sources.
3. Note trade direction, product description, code, shipment date, and source when available.
4. Distinguish buyer/importer, consignee, notify party, freight forwarder, broker, distributor, and exporter. These roles are not interchangeable.
5. Find a sourced public business contact route.
6. Apply normal organization gates before outreach.

## Search construction

Use multiple code levels and product language:

- HS4 for broad market sizing and code uncertainty;
- HS6 for internationally comparable product families;
- national 8- or 10-digit codes for jurisdiction-specific trade queries;
- exact product descriptions, commercial synonyms, material terms, and end-use terms alongside codes.

Build queries from combinations such as:

- code + importer + destination country;
- code + buyer/distributor/wholesaler + city or market;
- product description + customs/shipment/import records;
- known exporter + destination buyer;
- candidate company + product/code + import/export.

Do not search only one exact code. Importers may declare adjacent codes, use broader descriptions, route goods through trading companies, or change classification over time.

## Evidence and output

Keep trade evidence in the ledger, not repeated across contact columns:

- candidate or verified research code;
- code level and jurisdiction;
- official description and source;
- import/export direction, origin, destination, and period;
- aggregate value/quantity and source when used for market ranking;
- company role, shipment/product description, date, and evidence URL when used for discovery;
- missing classification details and confidence;
- independent company-fit and contact evidence.

User-facing contact output should add trade fields only when useful: `trade signal`, `product/code`, `last observed date`, and `trade source`. Do not dump every code or shipment row into the main contact sheet.

## Decision rules

- Known user code: verify current description and jurisdiction before using it.
- Unknown code: infer candidate families; do not block discovery when exact classification is unnecessary.
- Multiple plausible codes: search each defensible family, compare yield, and keep uncertainty visible.
- Old or reallocated code: map to current code where authoritative evidence exists; retain old code only for historical searches.
- Aggregate data only: use it to prioritize markets, never to name buyers.
- Company-level record: use it for discovery, then verify current fit and route independently.
- No reliable code: continue with product-description and sector-source research; report the gap.
