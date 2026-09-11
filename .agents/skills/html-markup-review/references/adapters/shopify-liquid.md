# Shopify and Liquid Adapter

Use for Shopify Liquid and similar tag-based templates. Apply core rules to the resulting HTML.

- Preserve Liquid expressions, filters, loops, conditionals, schema references, and section/block settings.
- Treat Liquid tags embedded in attributes or children as template syntax; inspect the static structure around them.
- Do not replace dynamic URLs, translations, product data, or theme hooks with literals.
- Check repeated product/navigation markup at the template level without assuming the runtime data shape.
