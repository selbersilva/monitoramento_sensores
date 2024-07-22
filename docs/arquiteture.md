# Arquitetura do Sistema

## Visão Geral
O sistema de monitoramento automatizado é composto por três principais componentes:

1. **Leitura de Sensores**: Coleta dados dos sensores.
2. **Processamento de Dados**: Processa e converte os dados coletados.
3. **Armazenamento de Dados**: Armazena os dados processados para posterior análise.

## Diagrama de Arquitetura
```plaintext
+-----------------+        +-------------------+        +--------------------+
| Leitura de      |        | Processamento     |        | Armazenamento      |
| Sensores        |  --->  | de Dados          |  --->  | de Dados           |
+-----------------+        +-------------------+        +--------------------+
