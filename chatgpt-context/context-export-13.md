# CHATGPT CONTEXT EXPORT — CONTINUATION

## Важное ограничение

Ни один файл не содержит паролей, API-ключей, cookies, session/access tokens и иных секретов доступа.
```


---

## FILE `roman-claude-context-v3/CLAUDE_IMPORT_PROMPT.txt`

```text
Используй загруженные файлы как долговременную базу контекста пользователя Романа.
Сначала прочитай 00_CLAUDE_INSTRUCTIONS.md и 01_CORE_PROFILE.md.
Далее подгружай тематические файлы по релевантности вопросу.
При конфликте данных руководствуйся 17_CONFIDENCE_AND_UPDATE_POLICY.md.
Не считай исторические данные текущими без подтверждения.
Не раскрывай чувствительные сведения, если они не относятся напрямую к запросу.
```


---

## FILE `roman-claude-context-v3/context.json`

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

## FILE `roman-claude-context-v3/conversation_export_index.json`

```text
{
  "schema_version": "3.0",
  "includes_reconstructed_chat_history": true,
  "includes_full_verbatim_chat_export": false,
  "limitations": [
    "No complete API archive of all prior ChatGPT messages is available in this session",
    "Reconstructed history is based on visible prior-chat context and stored memory",
    "Verbatim snippets are included only where exact text is available"
  ],
  "files": [
    "00_CLAUDE_INSTRUCTIONS.md",
    "01_CORE_PROFILE.md",
    "02_RESPONSE_AND_RESEARCH_PREFERENCES.md",
    "03_CAREER_AND_WORK_HISTORY.md",
    "04_PROCUREMENT_LOGISTICS_AUTOMATION.md",
    "05_INDUSTRIAL_OILS_SALES.md",
    "06_AI_SALES_MANAGER_PROJECT.md",
    "07_TAXI_ECONOMICS.md",
    "08_VEHICLES_AND_TECH.md",
    "09_FAMILY_AND_HOUSEHOLD_SENSITIVE.md",
    "10_LEGAL_FINANCIAL_SENSITIVE.md",
    "11_HEALTH_SENSITIVE.md",
    "12_CONTENT_AND_SOCIAL_PROJECTS.md",
    "13_RESEARCH_INTERESTS.md",
    "14_EMPLOYER_RESEARCH_CASES.md",
    "15_OPEN_THREADS.md",
    "16_TOPIC_INDEX.md",
    "17_CONFIDENCE_AND_UPDATE_POLICY.md",
    "18_CHAT_HISTORY_RECONSTRUCTED.md",
    "19_VERBATIM_AVAILABLE_SNIPPETS.md",
    "20_CURRENT_CHAT_EXPORT.md",
    "CLAUDE_IMPORT_PROMPT.txt",
    "CLAUDE_MEMORY_FULL_V2.md",
    "CLAUDE_MEMORY_FULL_V3.md",
    "README.md",
    "context.json"
  ]
}
```


# CHATGPT CONTEXT EXPORT — PART 5: БИНАРНЫЕ АРТЕФАКТЫ, МАНИФЕСТ И ОГРАНИЧЕНИЯ

Markdown-файл не может содержать исходные бинарные байты PNG/ZIP как нативные вложения. Поэтому для каждого бинарного артефакта ниже зафиксированы точный размер, SHA-256 и смысл. Для ZIP полное текстовое содержимое входящих файлов уже включено в PART 3 / PART 4.

