# SEO Evidence Checklist

Use only the sections applicable to the workspace evidence and scope. Inspect source files, local configuration, content, assets, generated output, and supplied offline reports only. Record `observed`, `not observed`, `not applicable`, or `not verified`; absence of evidence is not evidence of absence.

## Delivery, crawlability, and indexability

- URL variants: HTTP/HTTPS, host variants, trailing slash, case, parameters, fragments, subpaths, and duplicate entry points.
- HTTP status-code handling visible in source/configuration, or status codes documented in supplied local reports.
- Redirect destinations, redirect count, loops, temporary/permanent intent, and chains visible in source/configuration or supplied reports.
- `robots.txt` location, syntax, user-agent coverage, disallow/allow scope, sitemap references, and conflicts with page-level directives.
- XML sitemap availability, valid URLs, canonical alignment, status codes, last-modified accuracy, segmentation, and discoverability.
- Page-level robots directives, response headers, canonical URL, and conflicts between them.
- Internal links to important pages, crawlable hrefs, link depth, orphan candidates, navigation states, and pagination paths.
- Duplicate URL patterns, faceted/filter states, session or tracking parameters, and near-duplicate templates.
- HTTPS configuration, insecure resources, HTTP redirects, and canonical protocol/host handling visible in source/configuration or supplied reports.

## Document, metadata, and content

- Unique, descriptive page title and meta description where applicable; alignment with actual page content.
- One clear primary topic and useful main content; heading hierarchy that reflects document structure rather than visual size.
- `main`, navigation, header, footer, complementary content, and other landmarks where they accurately describe the page.
- Search intent, content usefulness, depth appropriate to the task, duplicate/thin/empty states, and template boilerplate.
- Stable, readable URL structure; unnecessary parameters, opaque identifiers, and misleading paths.
- Descriptive internal anchor text and links that are present without requiring unsupported interaction.
- Image filenames, intrinsic dimensions, loading behavior, and meaningful alternative text; distinguish decorative images.
- Open Graph and other social metadata where sharing is in scope; do not confuse social previews with ranking signals.
- Forms, labels, validation, and client-side-only states where they affect access to content or task completion.

## Rendering, mobile, and performance

- Content, links, metadata, structured data, and navigation emitted in local source/generated HTML versus dependent on JavaScript; use supplied rendered HTML only as an artifact.
- Rendering failures, hydration/route transitions, blocked resources, infinite scroll, lazy content, and interaction-only discovery.
- Mobile viewport configuration, responsive layout code, and locally observable responsive patterns; treat tap targets, overflow, shifts, and desktop parity as potential risks unless supplied evidence confirms them.
- Available Core Web Vitals or lab/field performance evidence; identify metric, device, sample, date, and URL scope.
- Large or blocking resources, third-party dependencies, caching, compression, image sizing, and layout stability when evidence exists.

## Structured data and internationalization

- Structured-data syntax, parseability, required properties for the claimed type, visible-content alignment, duplicates, and validation evidence.
- Do not infer rich-result eligibility from markup alone; record unsupported properties, policy or feature uncertainty, and validation status.
- Locale and regional URL model, language declarations, translated content, self-referencing and reciprocal `hreflang`, default handling, and canonical alignment.
- Locale redirects, currency/availability variation, and whether important variants are discoverable and indexable.

## Evidence quality

For each check, preserve the smallest useful proof: workspace-relative file and code location, supplied URL/response record, source excerpt, local rendered selector, crawl row, screenshot description, performance record, or repeated count. Note artifact timestamp and conditions when supplied evidence may vary. Do not obtain new evidence from the network.