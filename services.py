from datetime import datetime


def logs(user):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    id_user = user.id
    name = user.username
    log = f"created_at: {dt_string}, id: {id_user}, name: {name}"
    with open("logs.txt", "a") as file:
        file.write(f'\n{log}')
