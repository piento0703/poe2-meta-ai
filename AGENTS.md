# AGENTS.md

## Project Goal

This repository builds a PoE2 Autonomous Build Research Engine.

The final goal is:

* automatically detect overpowered builds
* understand skill/item/passive interactions
* estimate DPS and survivability
* generate leveling progression
* generate passive progression
* recommend gear evolution
* generate final build guides

This is NOT a simple tag matching project.

The core objective is:

"Understand why a build becomes broken."

---

## Current Pipeline

Current implemented systems:

* passive parser
* skill parser
* support parser
* unique parser
* archetype classifier
* build generator
* build validity filter
* semantic mechanic parser
* rare affix parser
* interaction engine
* OP candidate extractor

---

## Future Major Systems

High priority:

1. DPS approximation engine
2. survivability engine
3. leveling planner
4. passive path planner
5. ascendancy resolver
6. gear progression planner
7. interaction simulation engine

---

## Important Design Rules

### Canonical Internal Format

Internal tags/mechanics MUST remain English.

Examples:

* projectile
* trigger
* chain
* returning_projectile
* gain_as_extra

Do NOT localize internal logic identifiers.

---

### Korean Output

User-facing outputs should be Korean whenever possible.

Examples:

* reports
* summaries
* build explanations

---

### No Fake Data

Never invent actual game data.

If real data is missing:

* create sample files
* clearly mark TODO sections

---

### Modular Design

Prefer:

* small focused scripts
* reusable modules
* composable systems

Avoid giant monolithic scripts.

---

### Explain WHY

Do not only rank builds.

Explain WHY a build is strong.

Especially:

* returning projectile
* shotgun
* chain overlap
* trigger loops
* gain-as-extra scaling
* conversion stacking
* crit trigger engines

---

## Final Vision

The final system should behave like:

"AI-powered Path of Building researcher for PoE2"
