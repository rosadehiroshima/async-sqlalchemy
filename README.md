- Não vamos abrir uma sessão para cada dado que deverá ser inderido no banco
- Focar em fazer sempre bulk-insert's, ou seja, insert de batches ao invés de inserts individuais
- Usar Asyncio (ou Redis) para implementar sistema de Queue para armazenar lotes que estão na fila


```

[ API / PRODUCER ] (Receives CVs)
       |
       v
(Queue 1: Raw Data) <---------------+
       |                            |
       v                            | (Backpressure limits 
[ WORKER 1: VALIDATOR ]             |  flow if downstream 
       |                            |  is too slow)
       +---(Invalid)---+            |
       |               v            |
       |     [ DEAD LETTER QUEUE ]  |
       |               |            |
       v (Valid)       v (Logs)     |
(Queue 2: Valid Data) <-------------+
       |                            |
       v                            |
[ WORKER 2: PARSER ] (Heavy CPU)    |
       |                            |
       v (Extracted Data)           |
(Queue 3: Batch Buffer) <-----------+
       |
       v
[ WORKER 3: BATCH INSERTER ] (Time or Size Trigger)
       |
       v (Bulk Insert - 1 Transaction)
[    DATABASE (PostgreSQL)    ]

```
