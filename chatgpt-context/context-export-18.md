# CHATGPT CONTEXT EXPORT — V1 NESTED ARTIFACTS (CONTINUED)



---

## FILE `roman-claude-context/memory/work.md`

```text
# Professional and career context

## AО «Завод «Сельмаш», Киров

Historical working context:

- Position: deputy head of production-dispatch department (зам. начальника ПДО).
- Start date previously stated: **07.02.2026**.
- Salary context: **72,000 RUB** base; combinations with part-time percentages of 20/25/33% were discussed.
- Managed warehouse/production-support operations with roughly **31 loaders** and **11 storekeepers** in the discussed snapshot.
- Warehouse service windows previously discussed:
  - workwear: Mon/Tue/Wed/Fri 08:00–14:00;
  - central tool warehouse (ЦИС): Mon/Wed/Fri 08:00–14:00.
- Warehouse consolidation topics included №10/№18 and №3/№19.
- ERP context: migration from 1C УПП to 1C ERP; OPZS had been introduced; resource specifications were missing.

## GK «Профстрой», Киров

Historical snapshot:

- Role: director of procurement management.
- Period previously stated: **01.07.2026–07.08.2026**.
- Group context: precast concrete plant, transport fleet ~80 vehicles, quarry in Sovetsky district, industrial construction in Murashi, civil construction of 9 apartment buildings.
- Procurement organization included ОСЗ and ООП teams.
- Recurring problems: no resource specifications, requests without planning, PТО bottleneck, retrospective procurement, payment discipline and blocked accounts.
- Procurement thresholds discussed:
  - up to 200k RUB — direct purchase;
  - 200k–1m RUB — request for quotations;
  - over 1m RUB — ОСЗ;
  - medium approvals — procurement director;
  - large approvals — executive director.
- Cases handled:
  - cement supply conflict with **ЦЕМРОС**, including shipment stoppage and railcar demurrage;
  - crushed stone supplier and railcar idle time due to non-payment;
  - metal supplier credit limit removal and disrupted delivery.
- Salary negotiation context: employer offer 140k RUB; Roman stated minimum 160k; calculated then-current level around 156k; discussed target 200k + KPI.

## Operational management profile

A reusable self-description developed in prior job-search work:

- operational manager;
- manages warehouse and production-supply contour;
- up to ~50 employees in direct/indirect operational scope;
- parallel experience as director of an organization with ~145m RUB annual turnover and a garbage-truck fleet;
- responsibilities included recruiting, financial control, transport organization and vehicle technical readiness;
- strengths: process design, execution control, discipline, Excel analytics, 1C УПП/ERP, measurable results, checklists/regulations/reporting;
- previous sales experience in the automotive sector;
- experience with Bitrix24 and 1C ERP.

## Industrial oils sales

On **29.08.2026**, Roman discussed an offer for **industrial oils sales manager** at **«Движение автомасла» in Kirov**.

- Focus: industrial customers.
- Forestry/logging customers were described as a separate direction.
- A sales plan and market approach were requested.

## Inert materials / logistics context

Prior working context included:

- management of suppliers of crushed stone, sand and gravel;
- operational dispatching of dump-truck routes and tonnage;
- work base on **Луганская, 3** (work location, not necessarily personal address);
- self-pickup logistics;
- six dump trucks in one historical fleet snapshot:
  - 601, 611, 478 — 8×4, 35 t;
  - 896, 790, 068 — 6×4, 25 t;
- suppliers/locations discussed: «Вяткапромжелдортранс», quarries «Подозерье», «Западный», and Pудлинговский crushed-stone plant.

## Job search context (Aug 2026)

Recent applications/research included:

- head of procurement and logistics;
- real estate sales manager at «СЗ Железно»;
- operational leadership roles;
- due diligence on employers and legal entities in Kirov.
```


---

## FILE `roman-claude-context/scripts/push_to_github.ps1`

```text
$ErrorActionPreference = "Stop"
$RepoName = "roman-claude-context"

# Run from the repository root after installing/authenticating GitHub CLI (`gh auth login`).
git init
git add .
git commit -m "Initial Claude context migration"
gh repo create $RepoName --private --source=. --remote=origin --push
```


---

## FILE `roman-claude-context/scripts/push_to_github.sh`

```text
#!/usr/bin/env bash
set -euo pipefail

# Run from the repository root after installing/authenticating GitHub CLI (`gh auth login`).
REPO_NAME="roman-claude-context"

git init
git add .
git commit -m "Initial Claude context migration"
gh repo create "$REPO_NAME" --private --source=. --remote=origin --push
```


---

## FILE `roman-claude-context/sensitive/family.md`

```text
# Sensitive — family context

Use only when directly relevant.

Historical family details previously discussed:

- Spouse was described as an МВД/ГАИ employee, captain, senior road-safety propaganda inspector; earlier conversation referenced the title «Мисс Полиция Кировской области 2021».
- Children referenced in prior context include:
  - София — 03.03.2019;
  - Александр — 21.06.2024;
  - a son Лев, around 12–13 in 2026 depending on snapshot.
- In an Aug 2026 divorce/property discussion, Roman referred to two minor children aged roughly 2 and 7, plus a son from a first marriage aged roughly 13.
- A possible school context previously discussed: Вятская православная гимназия and МВД-related admission benefits.
- A possible Serbia relocation/residence concept was discussed in July 2026; this was exploratory, not confirmed as completed.

Treat ages and family status as time-sensitive.
```


---

## FILE `roman-claude-context/sensitive/health.md`

```text
# Sensitive — health discussion history

Use only when directly relevant. Not a diagnosis.

Topics previously raised by Roman:

- right little-finger pain;
- chest pressure/heaviness the morning after drinking alcohol the prior evening;
- at that time he reported no shortness of breath, sweating or nausea;
- questions about taking magnesium together with Valoserdin;
- questions about Phenibut timing, dosage and duration;
- an ECG PDF dated 2026-08-15 was referenced in conversation.

Health status is highly time-sensitive. Never infer current symptoms from this file.
```
