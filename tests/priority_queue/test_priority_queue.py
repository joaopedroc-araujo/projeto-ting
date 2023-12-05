import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    pq = PriorityQueue()
    pq.enqueue({"nome_do_arquivo": "arquivo_grande.txt", "qtd_linhas": 10})
    pq.enqueue({"nome_do_arquivo": "arquivo_pequeno.txt", "qtd_linhas": 3})

    def test_enqueue_priority():
        pq = PriorityQueue()
        pq.enqueue(
            {"nome_do_arquivo": "arquivo_prioritario.txt", "qtd_linhas": 3}
        )
        pq.enqueue(
            {"nome_do_arquivo": "arquivo_regular.txt", "qtd_linhas": 10}
        )
        assert pq.search(0)["nome_do_arquivo"] == "arquivo_prioritario.txt"

    # Teste de busca
    def test_search_priority():
        pq = PriorityQueue()
        pq.enqueue({"nome_do_arquivo": "arquivo_pequeno.txt", "qtd_linhas": 3})
        pq.enqueue({"nome_do_arquivo": "arquivo_grande.txt", "qtd_linhas": 10})
        assert len(pq) > 0
        removed_file = pq.dequeue()
        assert removed_file is not None
        assert removed_file["nome_do_arquivo"] == "arquivo_pequeno.txt"

    # Teste de remoção
    def test_dequeue_priority():
        removed_file = pq.dequeue()
        assert removed_file["nome_do_arquivo"] == "arquivo_pequeno.txt"

    # Teste de índice inválido
    def test_invalid_index():
        pq = PriorityQueue()
        pq.enqueue({"nome_do_arquivo": "arquivo.txt", "qtd_linhas": 4})
        with pytest.raises(IndexError):
            pq.search(10)

    # Chama os testes auxiliares
    test_search_priority()
    test_dequeue_priority()
    test_invalid_index()
    test_enqueue_priority()
