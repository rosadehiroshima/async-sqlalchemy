- Não vamos abrir uma sessão para cada dado que deverá ser inderido no banco
- Focar em fazer sempre bulk-insert's, ou seja, insert de batches ao invés de inserts individuais
- Usar Asyncio (ou Redis) para implementar sistema de Queue para armazenar lotes que estão na fila


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
