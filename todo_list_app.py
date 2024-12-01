import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")

        # Lista de tarefas
        self.tasks = []

        # Interface do Usuário
        self.criar_interface()

    def criar_interface(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(
            self.frame,
            width=50,
            height=10,
            selectmode=tk.SINGLE,
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry_task = tk.Entry(self.root, width=50)
        self.entry_task.pack(pady=10)

        self.button_add_task = tk.Button(
            self.root, text="Adicionar Tarefa", width=48, command=self.adicionar_tarefa
        )
        self.button_add_task.pack(pady=5)

        self.button_delete_task = tk.Button(
            self.root, text="Excluir Tarefa", width=48, command=self.excluir_tarefa
        )
        self.button_delete_task.pack(pady=5)

        self.button_complete_task = tk.Button(
            self.root, text="Marcar como Concluída", width=48, command=self.concluir_tarefa
        )
        self.button_complete_task.pack(pady=5)

    def adicionar_tarefa(self):
        tarefa = self.entry_task.get()
        if tarefa != "":
            self.tasks.append(tarefa)
            self.atualizar_listbox()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Você deve inserir uma tarefa.")

    def excluir_tarefa(self):
        try:
            task_index = self.listbox.curselection()[0]
            del self.tasks[task_index]
            self.atualizar_listbox()
        except:
            messagebox.showwarning("Aviso", "Você deve selecionar uma tarefa para excluir.")

    def concluir_tarefa(self):
        try:
            task_index = self.listbox.curselection()[0]
            self.tasks[task_index] = self.tasks[task_index] + " (Concluída)"
            self.atualizar_listbox()
        except:
            messagebox.showwarning("Aviso", "Você deve selecionar uma tarefa para marcar como concluída.")

    def atualizar_listbox(self):
        self.listbox.delete(0, tk.END)
        for tarefa in self.tasks:
            self.listbox.insert(tk.END, tarefa)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
