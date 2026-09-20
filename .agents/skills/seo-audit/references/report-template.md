# SEO Audit Report Template

Use this structure for a complete audit. Replace bracketed text and remove sections that are genuinely not applicable.

## 1. Executive summary

- Scope reviewed: [pages, URL set, templates, devices, locales, and evidence layers]
- Main strengths: [brief list]
- Highest-impact confirmed risks: [brief list]
- Main uncertainty or missing evidence: [brief list]
- Recommended first action: [one concrete next step]

## 2. Overall SEO health assessment

State a concise assessment grounded in the scope. Do not use a numeric score unless the scoring method, evidence coverage, and limitations are defined. Explain whether the assessment is page-specific, sample-based, or site-wide.

## 3. Confirmed findings

| ID | Category | Severity | Confidence | Affected scope | Evidence | Effort |
| --- | --- | --- | --- | --- | --- | --- |
| SEO-001 | [technical/on-page/semantic/performance/etc.] | [Critical/High/Medium/Low/Informational] | [High/Medium/Low] | [URL/file/element/pattern] | [direct observation] | [Quick fix/Moderate effort/Significant effort] |

For each ID, explain:

- Why it matters.
- Technology-neutral recommended solution.
- Technology-specific implementation notes only when the technology is confirmed.
- How to verify the fix and what result would disconfirm the finding.

## 4. Potential issues requiring verification

Use the same fields as confirmed findings, but state the missing evidence and the exact check needed before implementation. Do not present these as defects.

## 5. Positive practices already present

List observed strengths with evidence and scope. Avoid implying that a positive practice guarantees rankings or complete compliance.

## 6. Prioritized recommendations

| Priority | Finding IDs | Action | Impact rationale | Confidence | Affected pages | Effort | Dependency |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [SEO-001] | [action] | [why now] | [level] | [count/scope] | [estimate] | [none or ID] |

Prioritize using likely impact, confidence, effort, and affected-page count. Explicitly note when a lower-severity quick fix should precede a higher-severity change because it is a dependency or an easy verification win.

## 7. Suggested implementation order

1. Resolve access, delivery, status-code, redirect, and indexability blockers.
2. Establish canonical URL, sitemap, internal discovery, and rendering correctness.
3. Fix template-level metadata, document structure, content access, and repeated issues.
4. Address mobile, performance, structured data, and internationalization issues according to evidence and scope.
5. Re-crawl, re-render, and monitor representative pages after deployment.

Adjust this order when dependencies or business priorities require it, and explain the change.

## 8. Verification plan

For every recommendation specify:

- Test input and representative URLs.
- Layer tested: source, rendered DOM, live response, crawl, performance, or manual review.
- Expected result.
- Regression checks for important variants, devices, locales, and error states.
- Recheck timing for changes whose external processing is not immediate.