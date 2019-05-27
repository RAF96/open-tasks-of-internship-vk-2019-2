# Постановка задачи
- Реализовать алгоритм из статьи "Exploiting Music Play Sequence for Music Recommendation"
- Реализовать ImplicitALS. 
- Сравнить результаты работы на следующем датасете https://grouplens.org/datasets/movielens/ (из архива нужен файл ratings.csv)
# Build
Вся работа проделана в jupyter notebook. Сборка не должна составить особых проблем.
# ImplicitALS
## Bugs
- После разбиение функций на файлы, common2.to_sparce_matrix почему-то возвращает неверные данные. 
# Алгоритм из статьи
## Bugs
- На данный момент, после добавления word2vec и слагаемого с alpha, алгоритм перестал сходиться и устремляется в бесконечность.
- Алгоритм работает медленно даже на rating_mock данных из data. 
