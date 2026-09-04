# CHATGPT CONTEXT EXPORT — DEEP MEMORY SWEEP 1

Дата: 2026-09-04.

## PromptDeck / ChatGPT Control

При дополнительном проходе по долговременной памяти восстановлен отдельный проект, который в раннем экспорте был описан недостаточно подробно.

### 2026-09-04 — база 120 команд
Создан документ:
`/ChatGPT Control/120_команд_ChatGPT_расширенная_спецификация_люди_и_фото.docx`

Он содержит расширенную спецификацию 120 команд для работы с изображениями и фотографиями.

### 2026-09-04 — control panel
На основе этой базы создавался файл:
`/ChatGPT Control/chatgpt_image_control_panel.html`

В сохранённом контексте зафиксированы функции:
- кликабельные категории и команды;
- выпадающие списки и селекторы;
- автоматическая сборка prompt;
- copy/reset;
- адаптация под iPhone.

### 2026-09-04 — PromptDeck / GPT_Pult
Проект был развёрнут в отдельном GitHub-репозитории:
`gffvj5898h-design/promptdeck`

Назначение: мобильная PWA-панель для 120 ChatGPT image-команд.

Подтверждённый URL проекта:
`https://gffvj5898h-design.github.io/promptdeck/`

GitHub Pages настроен через workflow:
`.github/workflows/deploy-pages.yml`

### Артефакты
В рабочих разговорах и сохранённых файлах фигурировали:
- `GPT_Pult_mobile.html`
- `GPT_Pult_mobile_PWA.zip`
- `PromptDeck_GitHub_ready.zip`
- `chatgpt_image_control_panel.html`
- `120_команд_ChatGPT_расширенная_спецификация_люди_и_фото.docx`

### Подтверждённая структура `promptdeck/main`
- `.github/`
- `.nojekyll`
- `README.md`
- `app.js`
- `data/`
- `icons/`
- `index.html`
- `manifest.webmanifest`
- `refresh.html`
- `service-worker.js`
- `styles.css`

### Ключевое решение v0.2
Пользователь зафиксировал, что PromptDeck должен уйти от зависимости от коротких slash-команд и генерировать полностью самодостаточные prompts с явными ограничениями, не зависящие от памяти конкретного чата.

### Незавершённые задачи
- загрузка фотографии;
- preview фотографии;
- настройки формата, стиля и вариантов;
- генерация полного self-contained prompt;
- передача фото + prompt в ChatGPT;
- presets;
- scenario-first home screen;
- versioning service-worker cache.

### iPhone workflow
Пользователь сообщил, что системный Share не предложил ChatGPT как нужную цель. Рабочий ручной сценарий остался таким:
1. добавить фото в ChatGPT;
2. скопировать prompt из PromptDeck;
3. вставить его в ChatGPT.

### Генерация внутри PromptDeck
Пользователь хотел встроить генератор изображения прямо в PromptDeck и принял направление без отдельного OpenAI API из-за дополнительной стоимости API. Обсуждался self-hosted/open-model backend как отдельный технический контур; готовый backend в памяти не подтверждён.

## Статус
PromptDeck — реально созданный проект с GitHub-репозиторием и PWA, а не просто идея. Его следует хранить как отдельный проект, не смешивая с `Алиса Instagram`, `Profstroy procurement system` и `еНОТ AI`.
