# TechFlow Task Manager

## 1. Visão geral
Este projeto simula o desenvolvimento de um sistema web básico de gerenciamento de tarefas para a empresa fictícia **TechFlow Solutions**, atendendo ao desafio acadêmico de Engenharia de Software. A aplicação foi pensada para apoiar uma startup de logística na organização do fluxo de trabalho em tempo real, na priorização de tarefas críticas e no acompanhamento do desempenho operacional.

## 2. Escopo inicial
O escopo inicial contemplou:
- cadastro de tarefas;
- listagem das tarefas em tela;
- edição e exclusão;
- classificação por prioridade;
- acompanhamento do status em fluxo Kanban.

## 3. Metodologia ágil adotada
Foi utilizada uma abordagem **híbrida entre Scrum e Kanban**:
- **Scrum** para organizar o backlog, priorizar entregas e estruturar incrementos;
- **Kanban** para controlar o fluxo contínuo das tarefas nas colunas **To Do**, **In Progress** e **Done**.

## 4. Estrutura do projeto
```bash
techflow-task-manager/
├── .github/workflows/ci.yml
├── docs/
├── src/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── app.py
│   └── tasks.json
├── tests/
│   └── test_app.py
├── README.md
└── requirements.txt
```

## 5. Requisitos atendidos
- README com descrição, escopo e metodologia;
- sistema web funcional com CRUD de tarefas;
- testes automatizados com Pytest;
- pipeline básico com GitHub Actions;
- proposta de quadro Kanban com 10 cards;
- simulação de mudança de escopo;
- sugestão de commits semânticos.

## 6. Mudança de escopo simulada
Durante o desenvolvimento, foi simulada a seguinte mudança de escopo:

**Nova feature:** filtro por prioridade no painel principal.

**Justificativa:** durante a validação do fluxo, o cliente percebeu que a equipe precisava identificar rapidamente tarefas críticas para melhorar a tomada de decisão operacional. A alteração foi considerada de alto valor porque impacta diretamente a priorização do trabalho.

**Impactos da mudança:**
- inclusão de novo card no Kanban;
- atualização do backlog;
- previsão de novo commit para implementação;
- atualização desta documentação.

## 7. Como executar localmente
1. Crie e ative um ambiente virtual.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a aplicação:
   ```bash
   python -m src.app
   ```
4. Acesse no navegador:
   ```bash
   http://127.0.0.1:5000
   ```

## 8. Como executar os testes
```bash
pytest
```

## 9. GitHub Actions
O workflow configurado executa:
- instalação das dependências;
- execução dos testes automatizados com `pytest`.

## 10. Kanban sugerido
Ver arquivo `docs/kanban_cards.md`.

## 11. Commits semânticos sugeridos
Ver arquivo `docs/commit_history_suggested.md`.

## 12. UML
Os diagramas UML foram incluídos na pasta `docs/`:
- `uml_casos_de_uso.png`
- `uml_classes.png`

## 13. Prints para o relatório final
Para a entrega acadêmica, inclua no documento:
- print do quadro GitHub Projects;
- print dos commits relevantes;

## 9. Mudança de escopo

Durante o desenvolvimento, foi identificada a necessidade de reforçar a visualização das tarefas mais críticas para a startup de logística. Por esse motivo, o projeto teve uma mudança de escopo controlada: além do CRUD básico de tarefas, passou a considerar com mais destaque a funcionalidade de **priorização das tarefas**.

### Justificativa da mudança
A alteração foi necessária para atender melhor ao cenário do cliente, que precisa acompanhar atividades urgentes em tempo real e tomar decisões rápidas com base na prioridade das tarefas cadastradas.

### Impacto no projeto
- atualização da documentação;
- revisão do quadro Kanban;
- adequação do fluxo de desenvolvimento para contemplar a priorização.
- print do GitHub Actions com workflow executado.

## 14. Reflexão de Engenharia de Software
O projeto demonstra a aplicação integrada de requisitos, modelagem, versionamento, desenvolvimento ágil, automação de testes e gestão de mudanças, elementos centrais para a entrega de software confiável e sustentável.

## 15. Ajuste incremental de escopo
A funcionalidade de filtro por prioridade foi planejada como próximo incremento do produto.
