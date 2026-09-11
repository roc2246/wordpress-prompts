# Images and Media

- Review `alt` on every `img`: descriptive for meaningful content, empty for decorative content, and flagged when purpose is unknowable.
- Recommend `figure`/`figcaption` for a captioned or independently referenced media unit.
- Preserve media behavior while checking `picture`, `srcset`, `sizes`, and responsive source selection where present.
- Consider `loading="lazy"` for below-the-fold noncritical images, not automatically for prominent content.
- Retain or add stable `width` and `height` when intrinsic dimensions are known and they prevent layout shift.
- Check captions, transcripts, controls, and accessible names for audio/video when the surrounding context requires them.
- Do not invent dimensions, alt text, captions, or loading policy without evidence from context.
