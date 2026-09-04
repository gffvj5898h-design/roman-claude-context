# CHATGPT CONTEXT EXPORT — INDEX / READ ORDER

Дата экспорта: 2026-09-04.
Репозиторий: `gffvj5898h-design/roman-claude-context`.
Ветка: `main`.
На момент загрузки через GitHub API репозиторий был подтверждён как `private`.

Этот набор файлов — максимально полный экспорт контекста, который был реально доступен ChatGPT в текущем сеансе: долговременная память, восстановленная история разговоров, текущая ветка, созданные в ней текстовые артефакты и манифесты бинарных файлов.

## Ограничение полноты

У текущего сеанса нет системного API, возвращающего полный архив всех исторических ChatGPT-разговоров слово-в-слово и все старые вложения в исходном виде. Поэтому:

- где доступны точные формулировки — они сохранены;
- где доступна только долговременная память/сводка — история обозначена как реконструированная;
- текстовые артефакты, доступные в текущем разговоре, сохранены текстом;
- бинарные ZIP/PNG описаны через размер, SHA-256, состав/назначение;
- экспорт нельзя считать юридически точной стенограммой всего аккаунта за весь период.

## Порядок чтения Claude

### `context-export-1.md`
Главный master-файл. Содержит:
- инструкции по работе с пользователем;
- профиль;
- карьеру;
- закупки/логистику/автоматизацию;
- промышленные масла;
- AI sales manager;
- такси;
- автомобили/технику;
- семью;
- юридический/финансовый контекст;
- здоровье;
- контент-проекты;
- исследовательские интересы;
- работодателей;
- открытые темы;
- индекс тем;
- политику доверия/обновления;
- восстановленную историю чатов;
- доступные дословные фрагменты;
- дополнительные факты, восстановленные из долговременного контекста.

### `context-export-2.md` — `context-export-7.md`
Продолжение и детализация истории разговоров, включая текущую ветку переноса в Claude, фактические формулировки пользователя, причины решений, отклонённые варианты и изменение архитектуры переноса.

### `context-export-8.md` — `context-export-13.md`
Полное текстовое содержимое доступных артефактов текущего чата и предыдущих версий экспорта, включая:
- `CLAUDE.md`;
- `README.md`;
- `MIGRATION_NOTES.md`;
- `.gitignore`;
- `CLAUDE_MEMORY_FULL.md`;
- `CLAUDE_IMPORT_PROMPT.txt`;
- `context.json`;
- `conversation_export_index.json`.

### `context-export-14.md` — `context-export-15.md`
Манифесты бинарных артефактов:
- `roman-claude-context.zip`;
- `roman-claude-context-v2.zip`;
- `roman-claude-context-v3.zip`;
- `IMG_6048.png`.

Для каждого доступны размер, SHA-256 и описание/состав. Бинарные байты не вставлялись в Markdown как base64, поскольку это ухудшило бы пригодность базы для LLM и не дало бы Claude полезного текстового контекста.

### `context-export-16.md` — `context-export-19.md`
Полные текстовые версии вложенных файлов первой базы, включая:
- `memory/context.json`;
- `memory/interests.md`;
- `memory/preferences.md`;
- `memory/profile.md`;
- `memory/projects.md`;
- `memory/vehicles-tech.md`;
- `memory/work.md`;
- `scripts/push_to_github.ps1`;
- `scripts/push_to_github.sh`;
- `sensitive/family.md`;
- `sensitive/health.md`;
- `sensitive/legal-financial.md`.

### `context-export-20.md`
Этот индекс и инструкция по чтению набора.

## Правила использования контекста другой LLM

1. Новое прямое сообщение Романа имеет приоритет над этим экспортом.
2. Датированные сведения считать историческими, если нет более свежего подтверждения.
3. Не смешивать разные места работы, периоды и проекты.
4. Не превращать исследовательский вопрос в факт поведения пользователя.
5. Не превращать предложенную модель/гипотезу ассистента в принятое решение пользователя.
6. Для быстро меняющихся фактов, законов, цен, вакансий, проектов и GitHub-state — перепроверять актуальность.
7. Семейные, медицинские, юридические и финансовые данные использовать только когда они прямо релевантны запросу.
8. Не выдавать реконструированную историю за дословный transcript.

## Файлы набора

- `chatgpt-context/context-export-1.md`
- `chatgpt-context/context-export-2.md`
- `chatgpt-context/context-export-3.md`
- `chatgpt-context/context-export-4.md`
- `chatgpt-context/context-export-5.md`
- `chatgpt-context/context-export-6.md`
- `chatgpt-context/context-export-7.md`
- `chatgpt-context/context-export-8.md`
- `chatgpt-context/context-export-9.md`
- `chatgpt-context/context-export-10.md`
- `chatgpt-context/context-export-11.md`
- `chatgpt-context/context-export-12.md`
- `chatgpt-context/context-export-13.md`
- `chatgpt-context/context-export-14.md`
- `chatgpt-context/context-export-15.md`
- `chatgpt-context/context-export-16.md`
- `chatgpt-context/context-export-17.md`
- `chatgpt-context/context-export-18.md`
- `chatgpt-context/context-export-19.md`
- `chatgpt-context/context-export-20.md`

## Рекомендуемая точка входа для Claude

Сначала прочитать `context-export-20.md`, затем `context-export-1.md`. Остальные части использовать как продолжение, детализацию и исходные артефакты.
