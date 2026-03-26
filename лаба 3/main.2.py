participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


def find_common_participants(group1: str, group2: str, delimiter: str = ','):
    participants1 = group1.split(delimiter)
    participants2 = group2.split(delimiter)

    common = set(participants1) & set(participants2)

    return sorted(common)


result = find_common_participants(participants_first_group, participants_second_group, '|')
print(f"Общие участники: '{result}'.")
