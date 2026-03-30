from flask import Flask, render_template, request, redirect, url_for, flash
from dataclasses import dataclass, asdict
from typing import List, Optional
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "tasks.json")


@dataclass
class Task:
    id: int
    title: str
    description: str
    priority: str
    status: str


def load_tasks() -> List[Task]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    return [Task(**item) for item in data]


def save_tasks(tasks: List[Task]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump([asdict(task) for task in tasks], file, ensure_ascii=False, indent=2)


def create_task(title: str, description: str, priority: str, status: str) -> Task:
    if not title or len(title.strip()) < 3:
        raise ValueError("O título deve possuir pelo menos 3 caracteres.")
    if priority not in {"Alta", "Média", "Baixa"}:
        raise ValueError("Prioridade inválida.")
    if status not in {"A Fazer", "Em Progresso", "Concluído"}:
        raise ValueError("Status inválido.")

    tasks = load_tasks()
    next_id = max([task.id for task in tasks], default=0) + 1
    task = Task(
        id=next_id,
        title=title.strip(),
        description=description.strip(),
        priority=priority,
        status=status
    )
    tasks.append(task)
    save_tasks(tasks)
    return task


def update_task(task_id: int, title: str, description: str, priority: str, status: str) -> Task:
    tasks = load_tasks()
    for task in tasks:
        if task.id == task_id:
            if not title or len(title.strip()) < 3:
                raise ValueError("O título deve possuir pelo menos 3 caracteres.")
            if priority not in {"Alta", "Média", "Baixa"}:
                raise ValueError("Prioridade inválida.")
            if status not in {"A Fazer", "Em Progresso", "Concluído"}:
                raise ValueError("Status inválido.")

            task.title = title.strip()
            task.description = description.strip()
            task.priority = priority
            task.status = status
            save_tasks(tasks)
            return task
    raise ValueError("Tarefa não encontrada.")


def delete_task(task_id: int) -> bool:
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task.id != task_id]
    if len(updated_tasks) == len(tasks):
        raise ValueError("Tarefa não encontrada.")
    save_tasks(updated_tasks)
    return True


def get_task(task_id: int) -> Optional[Task]:
    tasks = load_tasks()
    for task in tasks:
        if task.id == task_id:
            return task
    return None


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = "techflow-secret-key"

    @app.route("/")
    def index():
        tasks = load_tasks()
        summary = {
            "A Fazer": len([task for task in tasks if task.status == "A Fazer"]),
            "Em Progresso": len([task for task in tasks if task.status == "Em Progresso"]),
            "Concluído": len([task for task in tasks if task.status == "Concluído"]),
        }
        return render_template("index.html", tasks=tasks, summary=summary)

    @app.route("/tasks/new", methods=["GET", "POST"])
    def new_task():
        if request.method == "POST":
            try:
                create_task(
                    request.form.get("title", ""),
                    request.form.get("description", ""),
                    request.form.get("priority", ""),
                    request.form.get("status", ""),
                )
                flash("Tarefa criada com sucesso.", "success")
                return redirect(url_for("index"))
            except ValueError as exc:
                flash(str(exc), "error")
        return render_template("form.html", task=None)

    @app.route("/tasks/<int:task_id>/edit", methods=["GET", "POST"])
    def edit_task(task_id: int):
        task = get_task(task_id)
        if not task:
            flash("Tarefa não encontrada.", "error")
            return redirect(url_for("index"))

        if request.method == "POST":
            try:
                update_task(
                    task_id,
                    request.form.get("title", ""),
                    request.form.get("description", ""),
                    request.form.get("priority", ""),
                    request.form.get("status", ""),
                )
                flash("Tarefa atualizada com sucesso.", "success")
                return redirect(url_for("index"))
            except ValueError as exc:
                flash(str(exc), "error")
        return render_template("form.html", task=task)

    @app.route("/tasks/<int:task_id>/delete", methods=["POST"])
    def remove_task(task_id: int):
        try:
            delete_task(task_id)
            flash("Tarefa removida com sucesso.", "success")
        except ValueError as exc:
            flash(str(exc), "error")
        return redirect(url_for("index"))

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
