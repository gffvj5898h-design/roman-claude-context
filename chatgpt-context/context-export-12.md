# CHATGPT CONTEXT EXPORT — CONTINUATION

## Personal financial snapshot

At one point Roman stated:

- income: **35,000 RUB/month**;
- mortgage payment: **36,000 RUB/month**;
- other credit obligations: **20,000 RUB/month**.

Questions discussed:

- personal bankruptcy;
- whether and how to preserve a mortgaged apartment;
- child share issues;
- sole-housing protections.

These are historical facts from conversation, not legal conclusions. Re-check current law and current balances before giving advice.

---
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


# CHATGPT CONTEXT EXPORT — UNIQUE CURRENT-CHAT ARTIFACTS (CONTINUED)



---

## FILE `roman-claude-context-v2/CLAUDE_IMPORT_PROMPT.txt`

```text
Используй загруженные файлы как долговременную базу контекста пользователя Романа.
Сначала прочитай 00_CLAUDE_INSTRUCTIONS.md и 01_CORE_PROFILE.md.
Далее подгружай тематические файлы по релевантности вопросу.
При конфликте данных руководствуйся 17_CONFIDENCE_AND_UPDATE_POLICY.md.
Не считай исторические данные текущими без подтверждения.
Не раскрывай чувствительные сведения, если они не относятся напрямую к запросу.
```


---

## FILE `roman-claude-context-v2/context.json`

```text
{
  "schema_version": "2.0",
  "generated_for": "Claude context migration",
  "user": {
    "preferred_name": "Роман",
    "base_location_context": "Киров, Кировская область",
    "education": "Вятский государственный гуманитарный университет, государственное и муниципальное управление, 2015",
    "languages": [
      "русский — родной",
      "английский — C1 (historical career profile)"
    ],
    "licenses": [
      "B",
      "C"
    ]
  },
  "response_preferences": {
    "direct": true,
    "avoid_emotional_filler": true,
    "fact_interpretation_forecast_separation": true,
    "show_calculations": true,
    "explicit_uncertainty": true,
    "prefer_structured_analysis": true
  },
  "major_context_domains": [
    "career",
    "procurement",
    "logistics",
    "ERP",
    "Bitrix24",
    "industrial_oils",
    "AI_sales_manager",
    "taxi",
    "vehicles",
    "legal_financial",
    "family",
    "health",
    "content_projects",
    "employer_research",
    "military_technology",
    "geopolitics"
  ],
  "current_or_recent_open_threads": [
    "industrial oils sales",
    "AI sales manager/mobile app",
    "career search",
    "taxi economics in Kirov",
    "bankruptcy and mortgage preservation",
    "ETRN for industrial waste transport",
    "Alisa Instagram",
    "Bitrix24/ERP automation"
  ]
}
```


---

## FILE `roman-claude-context-v2/README.md`

```text
# Roman Claude Context — Full Export v2

Назначение: перенос накопленного контекста пользователя из ChatGPT в Claude или другой LLM.

## Как использовать

1. Загрузить все `.md`-файлы в Claude Project / Knowledge.
2. В Project Instructions добавить содержимое `00_CLAUDE_INSTRUCTIONS.md`.
3. Основной консолидированный файл — `CLAUDE_MEMORY_FULL_V2.md`.
4. Для экономии контекста модель может сначала читать `01_CORE_PROFILE.md`, а затем тематические файлы по необходимости.

## Статусы сведений

- **SELF_REPORTED** — пользователь сообщил факт сам.
- **WORKING_CONTEXT** — использовалось как рабочий контекст в предыдущих диалогах.
- **HISTORICAL** — факт относится к определённому периоду и может быть уже неактуален.
- **PREFERENCE** — устойчивая настройка взаимодействия.
- **OPEN_THREAD** — тема не закрыта и может продолжиться.
- **VERIFY_CURRENT** — перед использованием как актуального факта нужно уточнять/проверять.
- **SENSITIVE** — личные, семейные, финансовые, юридические или медицинские сведения; использовать только когда они прямо релевантны запросу пользователя.
