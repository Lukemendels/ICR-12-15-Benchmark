// Stored text never determines element names, attributes or executable behavior.
function textNode(document, tag, value, className) {
  const element = document.createElement(tag);
  element.textContent = String(value ?? 'Not recorded');
  if (className) element.className = className;
  return element;
}
function safeSourceURL(value) {
  if (typeof value !== 'string') return null;
  try {
    const url = new URL(value);
    return ['http:', 'https:'].includes(url.protocol) && !url.username && !url.password ? url.href : null;
  } catch { return null; }
}
function sourceLink(document, source) {
  const url = safeSourceURL(source.url);
  if (!url) return textNode(document, 'span', source.id + ' — no permitted public URL');
  const link = textNode(document, 'a', source.id + ' · Open published source');
  link.href = url; link.target = '_blank'; link.rel = 'noopener noreferrer';
  return link;
}
