# eccenca Documentation Style Guide

Editorial rules for the eccenca Corporate Memory documentation.
Transcribed from the Confluence page *eccenca Documentation Style Guide* (draft, revision 10, 2026-08-31).

Cite these rules by number in review findings and commit messages, e.g. "field values as lists (3.4)".
When the Confluence page changes, update this file — it is the version the skills work against.

## 1. Text formatting

### 1.1 Bold text

Use **bold** for the exact names of UI elements that users need to locate or interact with:
buttons, menu items, navigation items, tabs, sections, field labels, selectable options.

- Click **Create new**.
- Open **Projects** under **BUILD**.
- Enter a value in the **Label** field.

Preserve the exact spelling and capitalization used in the product interface.
Do not use bold for general emphasis.

### 1.2 Do not use capitalization for emphasis

Do not use uppercase letters to emphasize words or phrases.
Use capitalization only when required by standard English, product names, technical values, or the exact spelling of a UI element.
Prefer regular text over typographic emphasis whenever possible.

### 1.3 Plain text

Use regular, unformatted text for explanations, introductions, and transitional phrases:
"In this example we use:", "For this example, enter the following values:", "The remaining fields can remain at their default values."
Do not use italics for these phrases unless emphasis is explicitly required.

### 1.4 User input and values

Use `backticks` for text that users enter, paste, select, or provide as a value:
form field values, names and labels created by the user, URIs and URLs used as values, identifiers,
property paths, file names and file paths, commands, code fragments, configuration values.

- Label: `JSON Services`
- Graph URI: `http://ld.company.org/prod-instances/`
- Value path: `ProductManager`
- Upload the `services.json` file.

Do not use backticks for general technical concepts.

## 2. UI references

### 2.1 Use exact UI terminology

Always use the exact names, spelling, and capitalization shown in the current eccenca user interface.
Do not rename, shorten, or paraphrase UI labels.
If the product displays **Create new**, do not write "Create New" or "New project".

### 2.2 Distinguish UI elements from values

Use **bold** for the UI element and `backticks` for the value entered into it:
"Enter `JSON Services` in the **Label** field and click **Create**."

### 2.3 Use interaction terms consistently

- **Click** for buttons, icons, links, and other clickable controls.
- **Select** for options, tabs, entries, or values from a list.
- **Enter** for text typed into a field.
- **Upload** for files.
- **Open** for existing projects, pages, dialogs, or items.

Do not switch between "click", "press", "pick", and "choose" for the same type of interaction.

### 2.4 Document non-obvious interactions

Explicitly describe interactions that users need to complete but may not be obvious from the interface:
"After entering the Graph URI, select the **Custom entry** suggestion to confirm the value."
Do not assume that entering a value is sufficient if another action is required to apply or confirm it.

### 2.5 Avoid product-centered phrasing

Focus on the task or action rather than on what the product enables, allows, or offers.

- Prefer: "Select an available graph in the **Graph** field." / "Click **Download** to download the vocabulary."
- Avoid: "The Graph field allows the selection of an available graph." / "The system offers the option to download a vocabulary."

Do not attribute human characteristics or intentions to the product or user interface.

## 3. Procedures

### 3.1 Use direct instructions

Start steps with verbs: Click, Select, Enter, Open, Upload, Navigate to.

- Prefer: "Click **Create new**."
- Avoid: "You can click **Create new**." / "The user should click **Create new**."

### 3.2 Avoid direct address and first person

Do not address the reader with "you", "your", "yours".
For procedural instructions, use the imperative and start with the required action.

- Prefer: "Enter `JSON Services` in the **Label** field."
- Avoid: "You need to enter `JSON Services` in the **Label** field."

For explanatory text, refer to the product, feature, field, or object rather than the reader.

- Prefer: "All other fields can remain at their default values." / "The project is created."
- Avoid: "You can leave all other fields at their default values." / "Your project is created."

Do not replace "you" with "the user" unless different user roles must be distinguished.
Prefer active and concise constructions; use passive voice only when the actor is irrelevant or it produces the clearest sentence.
Do not use first-person pronouns (I, we, our, us).

### 3.3 Use one action per step where possible

Keep procedural steps short and focused.
Separate actions into individual steps when an action changes the screen, opens a dialog, or starts a new part of the workflow.
Do not combine several unrelated actions into one long step.

### 3.4 Present multiple field values as a list

When users enter values into several fields, present the fields and values as a list:

    Enter the following values:

    - **Name:** `Create Service Triples`
    - **Description:** `Lifts the Service file into the Knowledge Graph`
    - **Source Dataset:** `JSON Services`

### 3.5 Mention optional fields explicitly

Clearly indicate when a field or setting is optional:
"**Description (optional):** `Lifts the Service file into the Knowledge Graph`"

### 3.6 Use present tense

- Prefer: "The dialog opens." / "The dataset appears in the project."
- Avoid: "The dialog will open." / "The dataset will appear in the project."

### 3.7 Keep instructions concise and sentences short

Remove filler words.

- Prefer: "Click **Create**." / "Select **JSON**."
- Avoid: "Now simply click on the **Create** button." / "Next, you will need to select **JSON** from the available options."

Express one main idea per sentence.
As a guideline, keep sentences to roughly 25 words or fewer, and split long sentences when this improves readability.

### 3.8 Do not over-document obvious interactions

Describe only what is needed to complete the task.
"Click **Create**." is usually sufficient.
Do not describe the position, color, or shape of a standard button unless that helps locate it.

### 3.9 Avoid unnecessary politeness

Do not use "please", "thank you", or similar conversational phrases in procedural documentation.

### 3.10 Focus on the task

Describe the action required rather than what the interface allows.

- Prefer: "Select a graph."
- Avoid: "The dialog allows a graph to be selected."

### 3.11 Use lists consistently

- Numbered list when the order of the steps matters, bulleted list when it does not.
- Introduce a list with a complete sentence, ending in a colon when the list follows directly.
- Keep list items grammatically parallel: complete sentences for all items, or fragments for all items.
- Periods when all items are complete sentences; no end punctuation when all items are fragments.
- Capitalize the first word of each item unless a technical term requires lowercase.
- Keep lists to roughly nine items or fewer; split long lists or use a table.

## 4. Language and technical content

### 4.1 Keep terminology consistent

Use the same term for the same concept throughout the documentation.
Do not alternate between synonyms unless they refer to different concepts.
Prefer the terminology used by the eccenca product itself.

> Repository clarification, not part of the Confluence page: do not settle which term the product uses by
> counting occurrences in `docs/`.
> See "Do not infer terminology from majority usage" in `repo-conventions.md`.

### 4.2 Use the full product name on first mention

Use **eccenca Corporate Memory** on the first mention in prose text on each page; use **Corporate Memory** afterwards.
Do not use "CMEM" in prose text — keep `CMEM` only in code, IRIs, JSON keys, parameters, and other literal technical values.
Do not use articles as part of product names.

> Repository clarification, not part of the Confluence page: `cmemc` is exempt from this rule and is never
> expanded, being a product name of its own rather than an abbreviation.
> See "The cmemc exemption" in `repo-conventions.md`.

### 4.3 Use US English

organization (not organisation), visualization (not visualisation), catalog (not catalogue).

### 4.4 Preserve exact technical values

Write technical values exactly as users need to enter or recognize them: capitalization, punctuation,
namespaces, URIs, paths, identifiers, file extensions — for example `rdfs:label`, `services.json`,
`http://ld.company.org/prod-instances/`.

When referring to a file extension as a term, include the leading period and use lowercase:
".csv file", not "CSV file" or "csv file".

### 4.5 Preserve exact file names

Write file names exactly as they appear, including capitalization and extension: "Upload the `services.json` file."
Do not replace an exact file name with a generic description when users need to identify a specific file.

### 4.6 Use clear, sentence-case headings

Use sentence case for headings at every level: "Create a new dataset".
When referring to a UI element, preserve the capitalization used in the product: **Create new**.
Make headings descriptive enough to indicate the content that follows, and keep them concise.
Do not use an ampersand (&) in headings unless it is part of an exact UI or API term.
Write the first sentence after a heading so that it can be understood independently of the heading.

### 4.7 Use notes and warnings intentionally

Use notes for useful additional information that is not required to complete the procedure.
Use warnings when ignoring the information may cause data loss, unexpected changes, or other significant consequences.
Do not use notes or warnings simply to emphasize normal instructions.

### 4.8 Write one sentence per line in Markdown

Write each sentence on a separate line in the Markdown source.
Line breaks within a paragraph do not affect the rendered output but make changes easier to review in Git.
Do not insert manual line breaks within a sentence to control source line length.

### 4.9 Avoid contractions

Prefer "does not", "cannot", "it is" over "doesn't", "can't", "it's".
Note that "cannot" is the correction target, not a contraction — it is deliberately allowed.

### 4.10 Use abbreviations consistently

Use an abbreviation only when it improves readability and its meaning is clear.
Spell out an uncommon term on first occurrence with the abbreviation in parentheses: "graphical user interface (GUI)".
After the first occurrence, use the abbreviation consistently.
Do not spell out commonly understood technical abbreviations.
Avoid abbreviations in headings unless commonly known.
Form plurals with a lowercase s: APIs.

## 5. Images and icons

### 5.1 Use current product icons

Always use the icon that matches the current eccenca product interface.
Do not assume that icons on existing pages are still current.

The eccenca icons live in `overrides/.icons/eccenca/` (the style guide states `overrides/icons/eccenca`; the
directory is dot-prefixed on disk).
When adding or updating an icon: verify that it matches the current product UI, use the icon from that directory,
replace outdated icons when encountered, and do not use similar-looking or generic icons as substitutes.

### 5.2 Keep screenshots up to date

Screenshots must reflect the current user interface.
When updating a page, check whether existing screenshots still match UI labels, icons, navigation, dialogs,
field names, and layout.
Replace screenshots if an outdated product state could confuse users.

### 5.3 Use appropriate data in screenshots

Screenshots must not contain personal data of real persons, data from customer projects, or other confidential
or sensitive information.
Use clearly fictional example data, and review all visible data before adding a screenshot.

### 5.4 Show only relevant information

A screenshot supports the instruction immediately before or after it.
Focus on the relevant part of the interface and avoid large areas that do not contribute to the instruction.
Do not use screenshots as a substitute for written instructions.

### 5.5 Use descriptive image file names

Use lowercase words separated by hyphens, no spaces.
Keep names concise but descriptive enough to identify the product area, feature, or view.

### 5.6 Use descriptive captions

- Prefer: "Create new JSON dataset dialog", "Transformation configuration"
- Avoid: "Screenshot 1", "See below", "The following image"

### 5.7 Ensure that screenshots are readable

Screenshots must be large and clear enough for all relevant UI elements and text to be readable at normal viewing size.
Crop to the relevant area.
Highlight a specific area only when this helps identify the element referenced in the text.

## 6. Review and quality assurance

Documentation changes are reviewed by a second person before publication.
The review verifies spelling and grammar, correct product names and terminology, clarity and comprehensibility,
compliance with this style guide, correct formatting and layout, and consistency with the current product interface.
