from pyscript import document

my_listcuh = [
    "Jacob Cortez",
    "Luis Pablo",
    "Mason Amos",
    "Earl Abadam",
    "JC Macalalag",
    "Joaquin Tovera"
]


def verify_candidate(event):
    first = document.getElementById("first_name").value.strip()
    last = document.getElementById("last_name").value.strip()
    full_name = f"{first} {last}"
    result_area = document.getElementById("result_area")

    is_member = full_name in my_listcuh

    messages = {
        True: f"Congratulations {full_name}! You are now part of the ICT club.",
        False: f"Sorry {full_name}, your name is not on the list."
    }

    result_area.innerText = messages[is_member]

    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""
