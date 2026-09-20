import re

padrao_email = r"[A-Za-z0-9_+-]+(?:\.[A-Za-z0-9_+-]+)*@(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}"

validos = []
invalidos = []

def explicar_erro(email):
    if "@" not in email:
        return "Não possui o símbolo @."

    if email.startswith("@"):
        return "Não possui usuário antes do @."

    usuario, dominio = email.split("@", 1)

    if usuario.startswith("."):
        return "O usuário não pode começar com ponto."

    if usuario.endswith("."):
        return "O usuário não pode terminar com ponto."

    if ".." in usuario:
        return "O usuário não pode possuir dois pontos consecutivos."

    if dominio == "":
        return "Não possui domínio."

    partes_dominio = dominio.split(".")

    for parte in partes_dominio:
        if parte.startswith("-"):
            return "Uma parte do domínio não pode começar com hífen."

        if parte.endswith("-"):
            return "Uma parte do domínio não pode terminar com hífen."

    if "." not in dominio:
        return "Não possui uma extensão válida."

    extensao = dominio.split(".")[-1]

    if len(extensao) < 2:
        return "A extensão deve possuir pelo menos duas letras."

    return "O endereço não corresponde ao formato esperado."

for i in range(5):
    email = input(f"Digite o {i + 1}º e-mail: ")

    if re.fullmatch(padrao_email, email):
        validos.append(email)
    else:
        invalidos.append((email, explicar_erro(email)))


print("\nE-mails válidos:")

for email in validos:
    print(email)


print("\nE-mails inválidos:")

for email, motivo in invalidos:
    print(f"{email} -> {motivo}")
