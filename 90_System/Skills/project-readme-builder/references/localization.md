# Localization

Support README generation in mainstream languages, including Chinese, English, Japanese, Korean, Spanish, French, German, Portuguese, Turkish, Russian, and others requested by the user.

## Language Selection

- User-specified language wins.
- If existing docs are mostly Chinese and no public audience is stated, use Chinese by default.
- If the repo is intended for GitHub/public reuse and no language is specified, use English as primary and offer localized companion files when useful.
- Preserve technical identifiers, commands, file paths, package names, and API names in their original spelling.

## Output Modes

### Single Language

Use only `README.md`.

### Single File Multi-Language

Use one `README.md` with language anchors near the top.

Example:

```markdown
Languages: [English](#english) | [中文](#中文) | [日本語](#日本語) | [한국어](#한국어)
```

Use this only for small projects because long multilingual files become noisy.

### Multi-File Localization

Use language-specific files:

```text
README.md
README.zh-CN.md
README.ja.md
README.ko.md
```

For projects with multiple localized READMEs or long showcase docs, use a dedicated README directory:

```text
README.md
READMEs/README.zh-CN.md
READMEs/README.zh-TW.md
READMEs/README.ja.md
READMEs/README.ko.md
READMEs/README.es.md
```

Keep the root `README.md` as the GitHub landing page and link to the localized files. Do not scatter localized README files in the repo root.

In every file, add language switch links:

```markdown
Languages: [English](README.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md)
```

For public projects with many translations, keep the language rail compact and near the top:

```markdown
[English](README.md) | [简体中文](READMEs/README.zh-CN.md) | [繁體中文](READMEs/README.zh-TW.md) | [日本語](READMEs/README.ja.md) | [한국어](READMEs/README.ko.md) | [Español](READMEs/README.es.md)
```

If localized READMEs live in a `READMEs/` folder, verify paths from the primary README and from each localized file.

Example from root `README.md`:

```markdown
Languages: [English](README.md) | [简体中文](READMEs/README.zh-CN.md) | [日本語](READMEs/README.ja.md) | [한국어](READMEs/README.ko.md)
```

Example from `READMEs/README.zh-CN.md`:

```markdown
Languages: [English](../README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md)
```

## Translation Quality

- Translate product explanation naturally, not word-for-word.
- Keep command examples identical across languages unless platform conventions differ.
- Keep internal links synchronized across language files.
- Avoid culture-specific idioms in technical instructions.
- If a project name has an official untranslated name, keep it unchanged.
