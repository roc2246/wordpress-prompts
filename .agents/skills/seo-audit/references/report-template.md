# SEO Audit Report Template

Use this structure for a complete audit. Replace bracketed text and remove sections that are genuinely not applicable.

## 1. Executive summary

- Scope reviewed: [workspace root, recursive folder scope, file classes, and local artifacts]
- Main strengths: [brief list]
- Highest-impact confirmed risks: [brief list]
- Main uncertainty or missing evidence: [brief list]
- Recommended first action: [one concrete next step]

## 2. Project and evidence reviewed

- Technology identified from source: [technology and evidence, or unknown]
- Files and directories reviewed: [inventory summary]
- Local reports/artifacts reviewed: [list or none]
- Explicit exclusions: [dependencies, generated output, unrelated files, or none]
- Evidence limitations: [runtime behavior, deployment, live-site checks, or other gaps]

## 3. Confirmed SEO issues

| ID | Category | Severity | Confidence | Affected scope | Evidence | Effort |
| --- | --- | --- | --- | --- | --- | --- |
| SEO-001 | [technical/on-page/semantic/performance/etc.] | [Critical/High/Medium/Low/Informational] | [High/Medium/Low] | [workspace file and code location/pattern] | [direct source evidence] | [Quick fix/Moderate effort/Significant effort] |

For each ID, explain:

- Why it matters.
- Technology-neutral recommended solution.
- Technology-specific implementation notes only when the technology is confirmed.
- Offline verification method and what result would disconfirm the finding.

## 4. Potential risks

Use the same fields as confirmed findings, but state the missing source or runtime evidence. Do not present these as confirmed defects.

## 5. Items requiring live-site verification

List checks that cannot be performed from the workspace, such as deployed status codes, redirects, response headers, current robots/sitemap delivery, indexing state, external rendering, or current field performance. Do not perform these checks.

## 6. Positive SEO practices already present

List observed strengths with workspace evidence and scope. Avoid implying that a positive practice guarantees rankings or complete compliance.

## 7. Prioritized recommendations

| Priority | Finding IDs | Action | Impact rationale | Confidence | Affected pages | Effort | Dependency |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [SEO-001] | [action] | [why now] | [level] | [count/scope] | [estimate] | [none or ID] |

Prioritize using likely impact, confidence, effort, and affected-page count. Explicitly note when a lower-severity quick fix should precede a higher-severity change because it is a dependency or an easy verification win.

## 8. Suggested implementation order

1. Resolve confirmed source-level metadata, document structure, routing, and discoverability issues.
2. Fix repeated template/component and configuration patterns affecting multiple page types.
3. Address content, structured data, mobile, performance, internationalization, and accessibility-related issues supported by workspace evidence.
4. Separately plan deployment and live-site verification for runtime-only risks.

Adjust this order when dependencies or business priorities require it, and explain the change.

## Verification details

For every recommendation specify:

- Test input and representative files or local artifacts.
- Layer tested: source, local generated output, supplied rendered artifact, supplied report, or manual review.
- Expected result.
- Regression checks for important templates, routes, locales, devices, and error states where represented locally.
- Separate live-site verification required after deployment, without attempting it during this audit.