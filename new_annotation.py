import os
import json

SCRIPT_PATH = os.path.dirname(__file__)
DIRECTORY_NAMES_WITH_ANNOTATIONS = list(filter(
    lambda file_name: os.path.isdir(
        os.path.join(SCRIPT_PATH, file_name)) and not file_name.startswith('.'),
    os.listdir(SCRIPT_PATH)
))

with open(os.path.join(SCRIPT_PATH, 'config.json'), 'r') as f:
    CONFIG_TO_DIR = json.load(f)


def get_suggestion_for_folder_name(path_to_parent_folder: str, folder_name: str) -> str:
    """
    Suggests alternative name for folder that already exists

    :param path_to_parent_folder: path to the parent folder from
    where you want to create a new folder
    :param folder_name: folder name
    :return: unic folder name
    """
    number = 1
    while True:
        suggestion_folder_name = f'{folder_name}_{number}'
        path_to_suggestion_folder = os.path.join(path_to_parent_folder,
                                                 suggestion_folder_name)
        if not os.path.exists(path_to_suggestion_folder):
            return suggestion_folder_name
        number += 1


def get_user_response(title: str, items: list, title_in_center: bool = False) -> int:
    print('\n' * 80)
    print('=-' * 30)
    if title_in_center:
        print(f'\t{title}')
    else:
        print(title)

    for i, item in enumerate(items):
        print(f' {i} - {item}')

    op = input('select the option: ')

    if op.isdigit() and int(op) < len(items):
        return int(op)
    return -1


def _create_structure(main_theme: str, subject: str, config: dict) -> bool:
    """
    create file according to project structures

    Args:
        config: settings for creating the folder
    """
    path_to_main_theme = os.path.join(SCRIPT_PATH, main_theme)
    path_to_new_notes = os.path.join(path_to_main_theme, subject)

    if os.path.exists(path_to_new_notes):
        suggestion_subject_name = get_suggestion_for_folder_name(path_to_main_theme, subject)
        op = get_user_response('O assunto selecionado já foi criado!',
                              [f'Criar "{suggestion_subject_name}"', 'Cancelar'])
        if op != 0:
            return False
        path_to_new_notes = os.path.join(path_to_main_theme, suggestion_subject_name)

    os.mkdir(path_to_new_notes)

    if config.get('readme') is True:
        with open(os.path.join(path_to_new_notes, 'README.md'), 'w') as f:
            f.write(
                f"#{subject}"
            )
        print('README.md criado!')

    if config.get('quick_notes') is True:
        with open(os.path.join(path_to_new_notes, 'quick_note.txt'), 'w') as f:
            pass
        print('quick_note.txt criado!')

    if config.get('references') is True:
        with open(os.path.join(path_to_new_notes, 'references.json'), 'w') as f:
            reference_template = [
                {
                    'description': '',
                    'url': '',
                    'notes': []
                }
            ]
            f.write(json.dumps(reference_template, indent=3))
        print('references.json criado!')

    return True


def main():
    op = get_user_response('Python annotations', DIRECTORY_NAMES_WITH_ANNOTATIONS)
    main_theme = DIRECTORY_NAMES_WITH_ANNOTATIONS[op]
    subject = input('Insert the subject: ').replace(" ", "_").lower().strip()
    config = CONFIG_TO_DIR.get(main_theme)
    if not config:
        config = CONFIG_TO_DIR.get('default')
    result = _create_structure(main_theme, subject, config)
    if result:
        print('Success!')
    else:
        print('Fail!')
    return None


if __name__ == '__main__':
    main()

