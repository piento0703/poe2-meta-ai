# CODEX.md

## Repository Purpose

This repository is a long-term PoE2 AI theorycraft and build research project.

Codex should help evolve this repository into a fully autonomous build analysis system.

---

# Core Objectives

The system should eventually:

* parse skills/supports/passives/items
* understand mechanics semantically
* detect broken interactions
* estimate DPS/survivability
* simulate build progression
* generate leveling guides
* generate final build recommendations

---

# Important Constraints

## DO NOT rewrite everything

Preserve and extend existing systems.

Current systems already implemented:

* archetype classifier
* build generator
* build validity filter
* semantic parser
* interaction engine
* report generators

Extend incrementally.

---

## Keep Systems Modular

Preferred:

* reusable modules
* focused scripts
* composable pipelines

Avoid giant single-file systems.

---

## Internal Language Rules

Internal mechanics/tags:

* MUST remain English
* MUST stay canonical

Examples:

* projectile
* trigger
* returning_projectile
* gain_as_extra

User-facing reports:

* Prefer Korean

---

# Preferred Development Flow

When implementing major systems:

1. analyze existing structure
2. propose architecture
3. implement incrementally
4. add validation checks
5. generate markdown reports
6. avoid fake data

---

# High Priority Next Systems

## 1. DPS Approximation Engine

Estimate relative build power using:

* hit count
* projectile scaling
* trigger frequency
* crit scaling
* conversion scaling
* overlap mechanics

Approximation is acceptable.

Relative comparison is more important than exact numbers.

---

## 2. Survivability Engine

Estimate:

* EHP
* sustain
* recovery
* avoidance
* mitigation

---

## 3. Leveling Planner

Generate:

* level ranges
* skill transitions
* passive progression
* gear checkpoints

Example:

* LV1~12
* LV12~28
* LV28 trigger transition
* LV55 final build online

---

## 4. Passive Path Planner

Goal:

* automatically determine notable progression
* recommend efficient routes
* approximate shortest paths

---

## 5. Gear Evolution Engine

Recommend:

* early game
* mid game
* late game
* final BIS

including rare affix evolution.

---

# Important Mechanic Priorities

High importance mechanics:

* returning projectile
* shotgun
* chain overlap
* trigger loops
* gain-as-extra
* conversion stacking
* crit trigger engines

Codex should prioritize interaction analysis involving these mechanics.

---

# Reports

Generated reports should go under:

```text
reports/
```

Examples:

* interaction_report.md
* op_build_candidates.md
* leveling_guides.md
* final_build_guides.md

---

# Validation

Before ranking builds:

* validate legality
* validate support compatibility
* validate weapon restrictions
* validate trigger conditions

---

# Long-Term Vision

The final project should resemble:

"AI-powered autonomous PoE2 build researcher"
