from pathlib import Path


def copy_file(full_command: str) -> None:
    command_list = full_command.split()
    if len(command_list) < 3:
        return

    if command_list[0] != "cp":
        return

    if not Path(command_list[1]).is_file():
        return

    if command_list[1] == command_list[2]:
        return

    with (open(command_list[1], "r") as file_from,
          open(command_list[2], "w") as file_to):
        file_to.write(file_from.read())
