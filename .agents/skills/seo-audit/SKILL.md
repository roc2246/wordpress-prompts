---
name: seo-audit
description: Audit a website or web project for technical SEO, on-page SEO, semantic HTML, accessibility-related SEO, performance, crawlability, and indexability issues. Use for static HTML, server-rendered sites, JavaScript applications, CMS and e-commerce sites, custom frameworks, source-code reviews, rendered-page reviews, live-site audits, and SEO reports.
metadata:
  author: riley-childs
  version: "1.0"
---

# SEO Audit

Produce an evidence-based, technology-neutral SEO audit for a single page or an entire website. Review the rendered experience when available, distinguish direct SEO defects from indirect accessibility or usability concerns, and avoid inferring runtime behavior from source code alone.

## Activation and inputs

Use this skill when the request asks to audit, review, diagnose, or improve SEO, search visibility, crawlability, indexability, metadata, structured data, or search-oriented HTML.

Accept any combination of:

- Source files, templates, build output, configuration, headers, and deployment artifacts.
- One or more URLs, rendered HTML, browser observations, crawl exports, server logs, status-code samples, or performance reports.
- Screenshots as supporting evidence only; they cannot establish source markup, HTTP behavior, or crawler access.
- A stated page scope, URL scope, device scope, locale scope, or business/search-intent context.

If scope is not stated, define the observed scope before auditing. Do not require a specific CMS, framework, language, hosting provider, analytics product, or SEO plugin.

## Evidence rules

1. Start by listing available evidence, requested scope, crawl/device/locale limits, and unavailable checks.
2. Separate `Confirmed` findings from `Potential` issues requiring verification.
3. Cite the exact URL, file, selector, element, response, report row, or repeated pattern supporting each finding.
4. Treat generated or client-side content as unknown until rendered output, runtime behavior, or an equivalent artifact has been inspected.
5. Do not claim that a page is absent, blocked, duplicated, fast, accessible, indexed, or canonicalized without evidence appropriate to that claim.
6. When evidence conflicts, record the conflict, prefer the more direct observation, and state what would resolve it.
7. Never promise rankings, traffic, indexing, or rich-result eligibility. Describe likely impact and uncertainty instead.

## Workflow

1. Establish scope and evidence. Identify whether the audit is single-page or site-wide, source-level or rendered/live, and which devices, locales, URLs, and authenticated states are represented.
2. Identify the delivery model only after inspecting evidence. Record relevant technology facts, but keep the recommendations portable.
3. Inspect crawlability and indexability: status codes, redirects and chains, robots directives, XML sitemaps, canonical URLs, duplicate URL variants, pagination, HTTPS/mixed content, and internal-link discovery.
4. Inspect rendered and source document structure: title, description, headings, main content, landmarks, links, images, forms, URLs, Open Graph/social metadata, and structured data.
5. Evaluate content quality and intent: topic alignment, usefulness, depth, duplication, thin or empty states, template repetition, and whether important content depends on rendering or interaction.
6. Evaluate mobile compatibility, JavaScript rendering risks, internationalization and `hreflang`, Core Web Vitals or available performance evidence, and resource behavior that could affect crawling or user experience.
7. Record positive practices as well as defects. Avoid turning valid variations into findings without a user, crawler, or maintainability consequence.
8. Classify every finding by severity, confidence, affected scope, and effort. Prioritize using likely SEO impact, confidence, implementation effort, and number of affected pages.
9. Recommend a technology-neutral solution first. Add implementation-specific examples only when the project technology has been positively identified.
10. Provide verification steps that can falsify the finding or confirm the fix, then order the work by dependencies and expected value.

Load `references/evidence-checklist.md` for the detailed inspection checklist. Load `references/report-template.md` when producing the full report or when consistent finding fields are needed.

## Severity and effort

Use one severity per finding:

- **Critical**: Broad or fundamental risk to crawling, indexability, security-related delivery, or the availability of important content; address urgently.
- **High**: Likely material loss of discoverability, relevance, or usable search experience across important pages.
- **Medium**: Meaningful issue affecting a subset of pages, signals, or users, or a risk whose impact depends on verification.
- **Low**: Limited impact, localized quality issue, or worthwhile cleanup after higher-value work.
- **Informational**: Context, positive practice, or observation without a required corrective action.

Use one effort estimate: `Quick fix`, `Moderate effort`, or `Significant effort`. Severity is not a substitute for confidence; a high-severity suspected issue may remain a potential issue until verified.

## Single page versus site audit

For a single page, inspect the complete document and its immediate discovery context, including representative inbound links, URL variants, response behavior, and relevant templates or components.

For a site audit, sample deliberately: key templates, page types, locales, device states, authenticated/public states, pagination states, error pages, and representative products or content. Report the sample and do not generalize to all pages unless the evidence supports a repeated pattern. When a crawl or inventory exists, quantify affected URLs and distinguish sampled findings from site-wide findings.

## Source versus rendered/live review

Source review can establish authored patterns, configuration, templates, and possible generated output. Rendered review can establish the effective DOM, visible content, client-side links, metadata after scripts run, and interaction-dependent content. Live review can additionally establish response behavior, redirects, headers, robots access, sitemap availability, and resource loading. State which layer supports each conclusion and label unobserved layers as verification gaps.

## Standard report

Return, in this order:

1. Executive summary.
2. Overall SEO health assessment with scope and limitations.
3. Confirmed findings.
4. Potential issues requiring verification.
5. Positive practices already present.
6. Prioritized recommendations.
7. Suggested implementation order.
8. Verification steps for every recommended change.

Every finding and recommendation should include category, severity, confidence level, evidence, affected page/file/element/pattern, why it matters, recommended solution, estimated effort, and verification method. Use tables for scanability, but explain non-obvious consequences in plain language.

## Guardrails

- Do not treat a preferred convention as a defect without a meaningful SEO, accessibility, usability, or maintainability reason.
- Do not infer canonicalization, indexing, redirects, status codes, sitemap contents, or rendered metadata from filenames or framework conventions.
- Do not invent keywords, alt text, search intent, business priorities, or page importance; mark the missing context and request it in verification steps.
- Do not recommend hiding content, misleading metadata, manipulative links, doorway pages, or other tactics intended to deceive users or crawlers.
- Keep accessibility and usability findings explicitly labeled as indirect SEO impact unless there is a direct search-related consequence.