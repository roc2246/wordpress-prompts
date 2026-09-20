---
name: seo-audit
description: Perform a source-code-only SEO audit of the current workspace, including templates, configuration, content, assets, and local reports. Use for static HTML, server-rendered sites, JavaScript applications, CMS and e-commerce sites, custom frameworks, and technology-neutral SEO reports.
metadata:
  author: riley-childs
  version: "1.0"
---

# SEO Audit

Produce an evidence-based, technology-neutral SEO audit of the current workspace. Review source code, templates, configuration, content, assets, and locally available reports without modifying files. Distinguish confirmed source-code issues from potential runtime risks and live-site verification requirements.

## Activation and inputs

Use this skill when the request asks to audit, review, diagnose, or improve SEO, search visibility, crawlability, indexability, metadata, structured data, or search-oriented source code in the current workspace.

Accept any combination of:

- All files and directories available in the current workspace, including source files, templates, build output, configuration, headers, deployment artifacts, content, assets, and local reports.
- A theme or project folder named in the prompt. Treat it as a recursive scope: inventory all nested files and directories before selecting files for detailed review.
- Supplied offline evidence stored in or provided with the workspace, such as rendered HTML, crawl exports, Lighthouse reports, Search Console exports, server logs, status-code samples, performance reports, or screenshots.
- A stated page scope, URL scope, device scope, locale scope, or business/search-intent context.

If scope is not stated, define the observed scope before auditing. Do not require a specific CMS, framework, language, hosting provider, analytics product, or SEO plugin.

This is a source-code-only audit. Inspect only the current workspace and supplied local/offline evidence. Do not use browser tools, open or inspect a live website, require internet or network access, crawl a deployed website, invoke `/tests` or unrelated slash commands, generate tests, or modify files unless the user explicitly requests implementation. Do not refuse the audit because browser access is unavailable.

## Evidence rules

1. Start by listing available evidence, requested scope, crawl/device/locale limits, and unavailable checks.
2. Separate `Confirmed` findings from `Potential` issues requiring verification.
3. Cite the exact workspace-relative file and code location, report row, selector, element, or repeated pattern supporting each finding whenever possible.
4. Treat generated or client-side content as unknown until its source, local generated output, or supplied rendered artifact has been inspected.
5. Do not claim that a page is absent, blocked, duplicated, fast, accessible, indexed, or canonicalized without workspace or supplied evidence appropriate to that claim.
6. When evidence conflicts, record the conflict, prefer the more direct observation, and state what would resolve it.
7. Never promise rankings, traffic, indexing, or rich-result eligibility. Describe likely impact and uncertainty instead.

## Workflow

1. Establish the workspace scope and available evidence. Record the workspace root, supplied folder scope, local reports, and important unavailable runtime evidence.
2. Recursively inventory the current workspace before detailed review. Record nested paths, file types, templates/components, styles, scripts, assets, configuration, routes, content, reports, generated output, dependencies, and relevant patterns. Do not stop at the root or assume a fixed directory layout.
3. Identify the actual technology only from workspace evidence. Record framework, CMS, language, templating, build, routing, or deployment facts only when supported by files; keep recommendations technology-neutral until then.
4. Locate files responsible for document structure, metadata, routing, content rendering, configuration, headers, redirects, asset loading, and SEO integrations. Search systematically for all applicable implementations before concluding that functionality is absent.
5. Audit source-code coverage: titles, descriptions, canonical links, robots directives, robots.txt, XML sitemaps, headings, semantic HTML, links/navigation, URL generation, image alternatives/dimensions/loading, structured data, Open Graph/social metadata, language and `hreflang`, viewport, pagination, redirects/status handling visible in code, duplicate-content risks, JavaScript dependencies, performance patterns, and accessibility issues affecting discoverability or usability.
6. Evaluate supplied local reports and rendered artifacts as evidence, clearly labeling them as reports/artifacts rather than independently verified runtime behavior.
7. Record positive practices as well as defects. Avoid turning valid variations into findings without a user, crawler, accessibility, usability, or maintainability consequence.
8. Classify every finding as a confirmed source-code issue, potential runtime risk, or live-site verification required. Add severity, confidence, affected scope, and effort.
9. Recommend a technology-neutral solution first. Add technology-specific implementation guidance only after the project technology is positively identified.
10. Provide offline verification steps that can falsify the finding or confirm the source change, and list live-site checks separately without attempting them.

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

For a single page, inspect all workspace files that can generate or affect it, including layouts, partials, components, routing, content, configuration, assets, and relevant local reports.

For a supplied theme folder, recursively cover the complete folder tree. Trace findings from nested templates/components through their callers or shared layouts where possible, identify repeated patterns and affected page types, and distinguish authored source from generated output. Report the inventory boundary, excluded paths, reviewed files, and unverified runtime behavior.

For a workspace-wide audit, review all relevant files recursively and report exclusions. Use local reports or generated artifacts to quantify affected URLs when available, but do not generalize beyond the evidence.

## Source versus rendered/live review

Source review can establish authored patterns, configuration, templates, and possible generated output. Supplied rendered HTML or reports can establish only what those artifacts record. State which layer supports each conclusion and label unobserved runtime layers as verification gaps.

Treat live response status, redirect behavior, current robots and sitemap availability, deployed headers, indexing state, external rendering, and current field performance as requiring live-site verification. List these as follow-up checks only; never perform them in this skill.

## Standard report

Return, in this order:

1. Executive summary.
2. Project and evidence reviewed.
3. Confirmed SEO issues.
4. Potential risks.
5. Items requiring live-site verification.
6. Positive SEO practices already present.
7. Prioritized recommendations.
8. Suggested implementation order.

Every finding and recommendation should include category, severity, confidence level, evidence, affected page/file/element/pattern, why it matters, recommended solution, estimated effort, and verification method. Use tables for scanability, but explain non-obvious consequences in plain language.

## Guardrails

- Do not treat a preferred convention as a defect without a meaningful SEO, accessibility, usability, or maintainability reason.
- Do not infer canonicalization, indexing, redirects, status codes, sitemap contents, or rendered metadata from filenames or framework conventions.
- Do not invent keywords, alt text, search intent, business priorities, or page importance; mark the missing context and request it in verification steps.
- Do not recommend hiding content, misleading metadata, manipulative links, doorway pages, or other tactics intended to deceive users or crawlers.
- Keep accessibility and usability findings explicitly labeled as indirect SEO impact unless there is a direct search-related consequence.
- Do not modify workspace files, invoke `/tests`, run unrelated slash commands, or generate tests unless the user explicitly requests implementation or tests.
- Do not use browser tools, network access, live URLs, or deployed-site crawling for this audit.