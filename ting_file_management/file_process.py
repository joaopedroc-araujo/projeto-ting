import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for item in list(instance._data):
        if item["nome_do_arquivo"] == path_file:
            return

    lines = txt_importer(path_file)
    if lines is None:
        return

    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(file_data)
    print(file_data)


def remove(instance):
    removed = instance.dequeue()
    if removed is None:
        print("Não há elementos")
    else:
        print(f"Arquivo {removed['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        file_data = instance.search(position)
        print(file_data)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
