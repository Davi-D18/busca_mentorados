from repositories.mentoreado_repository import MentoreadoRepository
from utils import convert_date, pause, show_loading, sleep

repo = MentoreadoRepository()


def menu():
    print("\n" + "=" * 45)
    print("SISTEMA DE MENTORIA")
    print("=" * 45)
    print("1. Buscar mentorado e encontros inscritos")
    print("2. Verificar vaga em um encontro")
    print("3. Inscrever alguém novo")
    print("4. Confirmar presença em um encontro")
    print("5. Inscrever-se em um encontro")
    print("6. Sair")
    return input("Escolha uma opção: ")


def seek_mentorship():
    name = input("Digite o nome ou parte do nome do mentoreado: ").strip()

    results = repo.get_meetings_by_mentee_name(name)

    if results:
        for row in results:
            status = "✅ Confirmou" if row["confirmou_presenca"] == 1 else "❌ Não confirmou"
            print(f"\nNome: {row['nome']}")
            print(f"Email: {row['email']}")
            print(f"Data: {convert_date(row['data'])}")
            print(f"Status: {status}")
    else:
        print("Nenhum resultado encontrado.")

    print()
    pause()


def check_availability():

    while True:
        date_str = input("Digite a data do encontro (dd/mm/yyyy): ").strip()
        try:
            date_obj = convert_date(date_str, input_format="%d/%m/%Y", output_format="%Y-%m-%d")
            break
        except ValueError:
            print("Formato de data inválido. Tente novamente.")

    show_loading("Verificando disponibilidade")

    total = repo.count_enrollments_by_date(date_obj)

    if not total:
        print("Nenhuma inscrição para esse encontro.")
        sleep(1.5)
        return True

    if total < 3:
        print("Ainda há vaga nesse encontro.")
        sleep(1.5)
        return True

    print("Não há vagas disponíveis para esse encontro.")
    pause()


def register_new_mentoree():
    name = input("Informe seu nome: ").strip()
    email = input("Informe seu email: ").strip()

    if not name or not email:
        print("Nome e email são obrigatórios.")
        sleep(1.5)
        return

    show_loading("Registrando")

    mentoreado = repo.get_mentoreado_by_email(email)
    if mentoreado:
        print("Esse email já está registrado.")
        sleep(1.5)
        return

    repo.new_mentoreado(name, email)
    print(f"{name} foi registrado com sucesso! ")
    sleep(2.5)


def update_confirmation():
    email = input("Informe o email: ").strip()
    date_str = input("Informe a data do encontro (dd/mm/yyyy): ").strip()

    while True:
        try:
            date_obj = convert_date(date_str, input_format="%d/%m/%Y", output_format="%Y-%m-%d")
            break
        except ValueError:
            print("Formato de data inválido.")
            sleep(1.5)

    show_loading("Buscando")

    mentoreado = repo.get_mentoreado_by_email(email)
    if not mentoreado:
        print("Mentorado não encontrado. Por favor, registre-se primeiro.")
        sleep(1.5)
        return

    repo.update_confirmation(mentoreado["id"], date_obj, 1)

    print(
        f"Presença de {mentoreado['nome']} para o encontro em {date_str} foi confirmada."
    )
    pause()


def create_enrollment():
    email = input("Informe o email: ").strip()
    date_str = input("Informe a data do encontro (dd/mm/yyyy): ").strip()

    while True:
        try:
            date_obj = convert_date(date_str, input_format="%d/%m/%Y", output_format="%Y-%m-%d")
            break
        except ValueError:
            print("Formato de data inválido.")
            sleep(1.5)

    show_loading("Buscando mentorado")

    mentoreado = repo.get_mentoreado_by_email(email)
    if not mentoreado:
        print("Mentorado não encontrado. Por favor, registre-se primeiro.")
        sleep(1.5)
        return

    total = repo.count_enrollments_by_date(date_obj)

    if total >= 3:
        print("Não há vagas disponíveis para esse encontro.")
        pause()
        return

    repo.create_enrollment(mentoreado["id"], date_obj)

    print(
        f"{mentoreado['nome']} foi inscrito para o encontro em {date_str} com sucesso!"
    )
    pause()
