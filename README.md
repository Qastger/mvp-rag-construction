# mvp-rag-construction

RAG-сервис для работы с документацией в сфере **тендеров и строительства**:
отвечает на вопросы по документам клиента, опираясь на их содержимое,
а не на «общие знания» модели.

> ⚠️ **Ранняя стадия.** Это «building in public» — репозиторий растёт публично
> по мере разработки. Текущий статус честно отражён ниже.

## Проблема

Работа с тендерной документацией съедает много времени и внимания: нужно вычитать
ТЗ и требования закупки, понять, подходит ли она предприятию, и собрать пакет
документов под её условия. Пропустишь важный пункт — в лучшем случае не допустят
к тендеру, в худшем попадёшь в РНП (реестр недобросовестных поставщиков).

Сервис помогает быстро находить нужные пункты в документации и проверять, все ли
требования закрыты, — чтобы не упустить критичное.

> Поиск подходящих закупок и поставщиков — отдельная задача; ею занимается смежный
> инструмент [tender-monitoring](https://github.com/Qastger/tender-monitoring-n8n).

## Текущий статус

- ✅ Каркас FastAPI + PostgreSQL в Docker — поднимается одной командой
- ✅ Эндпоинт `GET /health`
- ✅ Connection-check к БД при старте приложения (lifespan + retry)
- 🔜 Загрузка корпуса документов (`POST /ingest`) — Неделя 2–3
- 🔜 Эмбеддинги и семантический поиск по документам — Неделя 2–3
- 🔜 Ответы LLM с опорой на найденные фрагменты — далее

## Стек

- **FastAPI** — API-слой
- **PostgreSQL** — хранилище
- **Docker / docker-compose** — запуск всего одной командой
- **План:** эмбеддинги + векторный поиск, LLM через OpenRouter

## Запуск

```bash
docker compose up --build
```

Затем открыть http://localhost:8000/health → `{"status": "ok"}`

## Roadmap

1. **Неделя 1** — каркас и инфраструктура *(в работе)*
2. **Неделя 2–3** — загрузка документов, эмбеддинги, семантический поиск
3. **Далее** — RAG-ответы на реальном корпусе, демо

---

# (EN) mvp-rag-construction

Per-client RAG service for **tender & construction documentation**: answers questions
based on the client's own documents, not the model's general knowledge.

> ⚠️ Early stage. Built in public — the repo grows as development progresses.

## Status
- ✅ FastAPI + PostgreSQL skeleton in Docker (one-command start)
- ✅ `GET /health`, DB connection-check on startup
- 🔜 Document ingestion, embeddings, semantic search

## Stack
FastAPI · PostgreSQL · Docker · (planned: embeddings + vector search, LLM via OpenRouter)

## Run
```bash
docker compose up --build
```
