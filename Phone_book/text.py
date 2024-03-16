
main_menu = ['Главное меню',
             'Открыть телефонную книгу',
             'Сохранить телефонную книгу',
             'Показать контакты',
             'Создать контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']

choice_main_menu = f'Выберите пункт меню ({1}-{len(main_menu)-1}):'
choice_main_menu_error = f'Нужно ввести число от 1 до {len(main_menu)-1}!'

phone_book_opened_succesful = 'Телефонная книга успешно открыта!'
phone_book_saved_succesful = 'Телефонная книга успешно сохранена!'
empty_phone_book_error = 'Телефонная книга пуста или не открыта!'

input_new_contact = ['Введите имя контакта: ',
                     'Введите номер контакта: ',
                     'Введите комментарий к контакту: ']

input_search_word = 'Введите слово для поиска: '
input_search_word_for_edit = 'Введите слово для поиска, который хотите изменить: '
input_search_word_for_delete = 'Введите слово для поиска, который хотите удалить: '
input_id_for_edit = 'Введите ID контакта, который хотите изменить: '
input_id_for_delete = 'Введите ID контакта, который хотите удалить: '

no_changes = 'или Enter, для пропуска'

edit_contact = [f'Введите новое имя ({no_changes}): ',
                f'Введите новый телефон ({no_changes}): ',
                f'Введите новый комментарий к телефону ({no_changes}): ']

def new_contact_added_succesful(name: str) -> str:
    return f'Контакт "{name}" успешно добавлен!'

def find_contact_no_resault(word:str) -> str:
    return f'Контакты содержащие "{word}" не найдены!'

def edit_contact_succesful(name) -> str:
    return f'Контакт "{name}" успешно изменен!'

def delete_contact_succesful(name) -> str:
    return f'Контакт "{name}" успешно удален!'