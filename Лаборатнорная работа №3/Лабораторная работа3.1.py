# TODO Напишите функцию для поиска индекса товара
def найти_индекс_товара(список_товаров, товар):
    for индекс, текущий_товар in enumerate(список_товаров):
        if текущий_товар == товар:
            return индекс
    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = найти_индекс_товара(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
