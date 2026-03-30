import json
import os
import sys
import tempfile
import importlib
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
app_module = importlib.import_module("src.app")


@pytest.fixture
def temp_data_file(monkeypatch):
    handle, path = tempfile.mkstemp(suffix=".json")
    os.close(handle)
    with open(path, "w", encoding="utf-8") as file:
        json.dump([], file)
    monkeypatch.setattr(app_module, "DATA_FILE", path)
    yield path
    if os.path.exists(path):
        os.remove(path)


def test_create_task_success(temp_data_file):
    task = app_module.create_task(
        "Planejar sprint",
        "Detalhar backlog da primeira sprint.",
        "Alta",
        "A Fazer"
    )
    assert task.id == 1
    assert task.title == "Planejar sprint"


def test_create_task_invalid_title(temp_data_file):
    with pytest.raises(ValueError):
        app_module.create_task("Oi", "Descrição", "Alta", "A Fazer")


def test_update_task_success(temp_data_file):
    task = app_module.create_task("Criar tela", "Tela inicial", "Média", "A Fazer")
    updated = app_module.update_task(task.id, "Criar tela inicial", "Tela revisada", "Alta", "Em Progresso")
    assert updated.title == "Criar tela inicial"
    assert updated.status == "Em Progresso"


def test_delete_task_success(temp_data_file):
    task = app_module.create_task("Remover bug", "Validar bug do formulário", "Baixa", "A Fazer")
    assert app_module.delete_task(task.id) is True
    assert app_module.load_tasks() == []


def test_index_route_returns_success(temp_data_file):
    flask_app = app_module.create_app()
    client = flask_app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"TechFlow Task Manager" in response.data
