#!/usr/bin/env python3

"""
CURR BEST
This script recursively processes directories containing nonempty ".lyx" files.
For each .lyx file it:
  1. Extracts the document body (text between "\begin_body" and "\end_body").
  2. Converts layout blocks so that each block starts with a newline.
     The mapping now is:
         Section* → "# "
         Subsection* → "## "
         Subsubsection* → "### "
         (Other layout names remain unprefixed.)
  3. Converts math insets:
       • If the inset’s content starts with "\begin{align*}" then it’s assumed a complete block and is wrapped with a single pair of "$$ ... $$" (on one line).
       • Else if the content contains a newline or is wrapped by "\[" and "\]", it is treated as block math.
         In that case, the inner content (with the delimiters removed) is wrapped in
             $$
             \begin{align*} ... inner ... \end{align*}
             $$
       • Otherwise, it is treated as inline math and wrapped with a single pair of "$ ... $" (with no extra newlines).
  4. Converts quote insets of the form:
         \begin_inset Quotes erd ... \end_inset
     If the inner content is empty, it is replaced by the fixed string " מ״מ " (with single spaces);
     otherwise, the inner text is output.
  5. (Bracket changes have been reverted – no substitution is applied to brackets.)
  6. Straight double-quotes (") are replaced with alternating Hebrew-style quotes.
  7. Extra newlines outside of protected math blocks are collapsed.
  8. No title header is inserted from the file name; headings come solely from layout blocks.
  9. Each .lyx file is output as its own Markdown file named "{basename}_.md".

Note: A newline is now inserted before each layout block.
"""

import os, re


# (1) Extract document body:
def extract_body(text):
    m = re.search(r'\\begin_body(.*?)\\end_body', text, re.DOTALL)
    return m.group(1) if m else text


# (2) Layout conversion:
# Map layout names to markdown headers.
# Per your request, Section* is the top-level heading.
layout_map = {
    "Section*": """\n
    # """,
    "Subsection*": """\n
    ## """,
    "Subsubsection*": """\n
    ### """
    # Other layouts (e.g. Title, Standard, Description) will be output as plain text.
}


def convert_layout_blocks(text):
    # Insert a newline before each layout block.
    def repl(match):
        layout = match.group(1).strip()
        content = match.group(2).strip()
        prefix = layout_map.get(layout, "")
        # Return with a newline before and after.
        return "\n" + prefix + content + "\n newline"
        # return f"<div classname='{layout}'>\n" + prefix + content + "\n newline</div>"

    pattern = re.compile(r'\\begin_layout\s+([^\n]+)\n(.*?)\\end_layout', re.DOTALL)
    return pattern.sub(repl, text)


# (3) Math inset conversion:
def convert_math_insets(text):
    """
    Convert math insets of the form:
         \begin_inset Formula <content>
         \end_inset
    If the content starts with "\begin{align*}" then assume it’s already a complete block.
    Else if the content contains a newline or is wrapped by "\[" and "\]", treat as block math:
         remove the delimiters (if any) and wrap with:
             $$
             \begin{align*} ... inner ... \end{align*}
             $$
    Otherwise, treat as inline math (wrapped with a single pair of $…$).
    """
    pattern = re.compile(r'\\begin_inset\s+Formula\s+(.*?)\\end_inset', re.DOTALL)

    def repl(match):
        content = match.group(1).strip()
        # (Bracket fixing is reverted, so we leave content unchanged.)
        # Check if it's already a full align* block.
        if content.startswith("\\begin{align*}"):
            return "\n$$ " + content.strip() + " $$"
        elif ("\n" in content) or (content.startswith("\\[") and content.endswith("\\]")):
            inner = content
            if inner.startswith("\\[") and inner.endswith("\\]"):
                inner = inner[2:-2].strip()
            return "\n$$ \\begin{align*} " + inner + " \\end{align*} $$\n"
        else:
            if content.startswith("$") and content.endswith("$"):
                inner = content[1:-1].strip()
            else:
                inner = content
            return "$" + inner + "$"

    return pattern.sub(repl, text)


# (4) Quote inset conversion:
def convert_quote_insets(text):
    """
    Convert quote insets of the form:
         \begin_inset Quotes erd
         (optional content with possible newlines)
         \end_inset
    The function strips all extra whitespace/newlines from the inner content
    and then wraps the resulting text in straight double quotes.
    """
    pattern = re.compile(r"\s\\begin_inset\s+Quotes\s+erd\s*(.*?)\\end_inset\s+", re.DOTALL)

    def repl(match):
        inner = match.group(1)
        # Collapse all whitespace (including newlines) to a single space, then strip.
        inner_clean = re.sub(r' \s+ ', '', inner).strip()
        return f'"'

    return pattern.sub(repl, text)

# (5) (Bracket fixes are now reverted: do nothing.)
def bracket_fix(text: str):
    bracket_mapping = {
        "{": "}",
        "}": "{",
        "]": "[",
        "[": "]",
        "(": ")",
        ")": "("
    }

    text_mode = True
    last_math = 0
    for (idx, char) in enumerate(text):
        if char == "$":
            # print(f"{idx} is $")
            if last_math == 0 or idx - last_math > 1:
                text_mode = not text_mode
            last_math = idx
        if bracket_mapping.get(char) and text_mode:
            if idx and text[idx - 1] != "t":
                # s = s[:index] + newstring + s[index + 1:]
                text = text[:idx] + bracket_mapping[char] + text[idx + 1:]
    return text



# (6) Hebrew quotes conversion:
def fix_hebrew_quotes(text):
    result = []
    open_quote = '״'
    close_quote = '“'
    use_open = True
    for ch in text:
        if ch == '"':
            result.append(open_quote if use_open else close_quote)
            use_open = not use_open
        else:
            result.append(ch)
    return "".join(result)


# (7) Whitespace cleanup:
def cleanup_whitespace(text):
    # Protect block math (delimited by $$ ... $$) with placeholders.
    blocks = {}

    def mark_block(match):
        placeholder = f"%%BLOCK{len(blocks)}%%"
        blocks[placeholder] = match.group(0).strip()
        return placeholder

    text = re.sub(r'\$\$\s*(.*?)\s*\$\$', mark_block, text, flags=re.DOTALL)
    # Collapse newlines to a single space.
    text = re.sub(r'\n+', " ", text)
    # Restore block math with newlines.
    for placeholder, block in blocks.items():
        text = text.replace(placeholder, "\n" + block + "\n")
    # Collapse multiple spaces.
    return re.sub(r'\s+', " ", text).strip()


# (8) Full conversion pipeline:
def lyx_to_markdown(lyx_text, filename):
    # Do not add file title from filename; rely solely on layout conversion.
    body = extract_body(lyx_text)
    body = convert_layout_blocks(body)
    body = convert_math_insets(body)
    body = convert_quote_insets(body)
    body = fix_hebrew_quotes(body)
    body = cleanup_whitespace(body)
    # We no longer apply any additional bracket fixes.
    return body


def insert_newlines_around_markers(text):
    # Insert a newline before any group of '#' that is not already preceded by a newline.
    text = re.sub(r'(?<!\n)(#+)', r'\n\1', text)
    # Insert a newline before any occurrence of "$$/" that isn't already preceded by a newline.
    text = re.sub(r'(?<!\n)(\$\$/)', r'\n\1', text)
    # Insert a newline after any occurrence of "$$" that is not immediately followed by a "/" character.
    text = re.sub(r'(\$\$)(?!/)', r'\1\n', text)
    text = text.replace("newline", "\n")
    text = bracket_fix(text)
    text = text.replace("\\numeric on ", "")
    text = text.replace(" \\numeric off", "")
    text = text.replace("\\series bold ", "**")
    text = text.replace(" \\series default", "**")
    return text

# (9) Process each .lyx file separately, writing {basename}_.md:
def process_directory(root_dir):
    for current_dir, dirs, files in os.walk(root_dir):
        lyx_files = [f for f in files if f.lower().endswith('t.lyx')]
        for filename in lyx_files:
            print(f"Processing {filename}")
            file_path = os.path.join(current_dir, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    lyx_content = f.read()
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue
            md_content = lyx_to_markdown(lyx_content, filename)
            if md_content:
                base = os.path.splitext(filename)[0]
                output_filename = base + "_.md"
                output_path = os.path.join(current_dir, output_filename)
                md_content = insert_newlines_around_markers(md_content)
                try:
                    with open(output_path, "w", encoding="utf-8") as outf:
                        outf.write(md_content)
                    print(f"Wrote {output_path}")
                except Exception as e:
                    print(f"Error writing {output_path}: {e}")


if __name__ == "__main__":
    process_directory(".")
