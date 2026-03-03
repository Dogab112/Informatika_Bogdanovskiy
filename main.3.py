# TODO Найдите количество книг, которое можно разместить на дискете
obiom_1_stranichki = 4 * 25 * 50 * 100
obiom_na_diske = 1.44 * 1024 * 1024
kolichestvo = obiom_na_diske // obiom_1_stranichki
print("Количество книг, помещающихся на дискету:", int(kolichestvo))
