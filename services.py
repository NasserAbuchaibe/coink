from datetime import datetime


def logs(user):
    """[Log the creation event and save these logs to a .txt file]

    Args:
        user ([object]): [Usuario model instance]
    """

    # Obtaining the data to register
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    id_user = user.id
    name = user.username

    # Creation of the string with the data
    log = f"created_at: {dt_string}, id: {id_user}, name: {name}"

    # Adding log to the logs.txt file
    with open("logs.txt", "a") as file:
        file.write(f'\n{log}')
