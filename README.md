```


      [ ENVIRONMENT 1: FASTAPI APPLICATION ]
      (Handles HTTP, scales via Uvicorn/Gunicorn)

 HTTP POST /ingest
        |
        v
 +--------------+     DI via FastAPI Depends()
 |  Endpoint    | <------------------------- [ Broker Client ]
 +--------------+                              (Redis/Kafka)
        |                                           |
        | Push (Fire & Forget)                      |
        v                                           |
 +----------------------------------------+         |
 |             MESSAGE BROKER             | <-------+
 +----------------------------------------+         |
        |                                           |
        | Pull (Consumer Group)                     |
        v                                           |
      [ ENVIRONMENT 2: BACKGROUND WORKER ]          |
      (Standalone asyncio loop, scales separately)  |
                                                    |
 +--------------+     DI via Class Constructor      |
 | Worker Class | <------------------------- [ Broker Client ]
 +--------------+
        |             DI via Class Constructor
        | <------------------------- [ DB SessionFactory ]
        |                              (SQLAlchemy)
        | Bulk Insert
        v
 +----------------------------------------+
 |         DATABASE (PostgreSQL)          |
 +----------------------------------------+
```


# TODO

- [ ] D.I. via FastAPI para o client Redis
- [ ] Usar Depends para delegar 'a rota o gerenciamento da sessao
- [ ] Montar funcionamento de engines redis para uso tanto do worker tanto da API
