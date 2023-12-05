def exists_word(word, instance):
    result = list()
    word = word.lower()

    for index in range(len(instance)):
        file_data = instance.search(index)
        occurrences = []
        for line_index, line in enumerate(file_data["linhas_do_arquivo"]):
            if word in line.lower():
                occurrences.append({"linha": line_index + 1})

        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file_data["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return result


def search_by_word(word, instance):
    found_words = exists_word(word, instance)
    search_results = []

    for word_occurrence in found_words:
        search_results.append(
            format_occurrence(word, word_occurrence, instance)
        )

    return search_results


def format_occurrence(word, occurrence, instance):
    detailed_occurrence = []
    file_data = get_file_data(occurrence["arquivo"], instance)

    for occ in occurrence["ocorrencias"]:
        line_content = file_data["linhas_do_arquivo"][occ["linha"] - 1].strip()
        detailed_occurrence.append(
            {"linha": occ["linha"], "conteudo": line_content}
        )

    return {
        "palavra": word,
        "arquivo": occurrence["arquivo"],
        "ocorrencias": detailed_occurrence,
    }


def get_file_data(filename, instance):
    for index in range(len(instance)):
        file_data = instance.search(index)
        if file_data["nome_do_arquivo"] == filename:
            return file_data
