from cli.menus import (
    check_availability,
    create_enrollment,
    menu,
    register_new_mentoree,
    seek_mentorship,
    update_confirmation,
)
from scripts.init_db import DBInitializer
from utils import clear_screen, show_loading, sleep

OPTIONS = {
    1: seek_mentorship,
    2: check_availability,
    3: register_new_mentoree,
    4: update_confirmation,
    5: create_enrollment,
}


def main():
    show_loading("Iniciando o sistema")

    db = DBInitializer()

    show_loading("Iniciando banco de dados")
    db.run()

    try:
        while True:
            selected_option = menu()
            action = OPTIONS.get(selected_option)

            if selected_option == 6:
                show_loading("Saindo do sistema")
                break

            if not action:
                print("Opção inválida.")
                sleep(1.5)
                clear_screen()
                continue

            action()

            clear_screen()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
