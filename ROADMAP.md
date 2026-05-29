# ROADMAP.md

# PoE2 Autonomous Build Research Engine

---

# Current Status

Implemented systems:

## Core Data Layer

* passive parser
* skill parser
* support parser
* unique parser
* localization maps

---

## Build Systems

* archetype classifier
* build generator
* build validity filter
* build report generator
* top build summary generator

---

## Mechanic Systems

* mechanic semantic parser
* rare affix parser
* interaction engine
* OP candidate extractor

---

# Current Architecture

```text id="s1q6sn"
Skills
+ Supports
+ Passives
+ Uniques
+ Rare Affixes
→ Mechanic Analysis
→ Interaction Analysis
→ Build Ranking
→ Reports
```

---

# Next Major Milestones

# Milestone 1 — DPS Approximation Engine

Status:
NOT IMPLEMENTED

Goal:

Estimate relative DPS using:

* hit count
* projectile count
* chain
* overlap
* trigger frequency
* crit scaling
* conversion scaling
* gain-as-extra scaling

Target Output:

```text id="0r5d2v"
estimated_dps_score
single_target_score
mapping_score
```

Priority:
VERY HIGH

---

# Milestone 2 — Survivability Engine

Status:
NOT IMPLEMENTED

Goal:

Estimate survivability using:

* life
* ES
* mitigation
* avoidance
* sustain
* recovery

Target Output:

```text id="fv01e7"
ehp_score
recovery_score
survivability_score
```

Priority:
VERY HIGH

---

# Milestone 3 — Leveling Planner

Status:
NOT IMPLEMENTED

Goal:

Generate leveling progression automatically.

Examples:

```text id="p6i1tr"
LV1~12
LV12~28
LV28 transition
LV55 final setup
```

Should include:

* leveling skills
* transition timing
* temporary setups
* required uniques
* required rare affixes

Priority:
HIGH

---

# Milestone 4 — Passive Path Planner

Status:
NOT IMPLEMENTED

Goal:

Automatically generate passive progression.

Should include:

* notable ordering
* efficient routing
* transition timing
* keystone timing

Priority:
HIGH

---

# Milestone 5 — Gear Evolution Planner

Status:
NOT IMPLEMENTED

Goal:

Generate:

* early game gear
* mid game gear
* late game gear
* final BIS

Should support:

* unique swaps
* rare affix upgrades
* crafting priorities

Priority:
HIGH

---

# Milestone 6 — Ascendancy Resolver

Status:
NOT IMPLEMENTED

Goal:

Automatically determine best ascendancy.

Should consider:

* trigger builds
* crit builds
* projectile builds
* ailment builds
* minion builds

Priority:
MEDIUM

---

# Milestone 7 — Legality Validation Engine

Status:
PARTIAL

Goal:

Validate:

* support compatibility
* weapon restrictions
* trigger legality
* conversion legality
* scaling legality

Priority:
VERY HIGH

---

# Milestone 8 — Meta Simulation Engine

Status:
NOT IMPLEMENTED

Goal:

Predict:

* broken builds after patches
* interaction abuse
* scaling explosions
* newly enabled archetypes

Priority:
MEDIUM

---

# Long-Term Goal

Final target:

```text id="t1bz2x"
AI-powered autonomous PoE2 build researcher
```

Comparable to:

```text id="y6bd1h"
Path of Building
+
theorycraft simulator
+
meta prediction engine
```

---

# Immediate Priority

Current recommended implementation order:

1. DPS approximation engine
2. legality validation engine
3. survivability engine
4. leveling planner
5. passive path planner
6. gear evolution planner
