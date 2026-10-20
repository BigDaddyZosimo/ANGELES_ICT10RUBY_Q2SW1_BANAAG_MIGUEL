from pyscript import document

my_listcuh = ["Jacob Cortez", "Luis Pablo", "Mason Amos", "Earl Abadam", "JC Macalalag", "Joaquin Tovera"]

def show_list():
    output = document.getElementById("output")
    output.innerHTML = "".join([f"<span class='archer-badge'>{item}</span>" for item in my_listcuh])

def verify_candidate(e):
    first = document.getElementById("first_name").value.strip()
    last = document.getElementById("last_name").value.strip()
    full_name = f"{first} {last}"
    result_area = document.getElementById("result_area")

    if full_name in my_listcuh:
        result_area.innerHTML = f"Congratulations {full_name}! You are now part of the ICT club."
    else:
        result_area.innerHTML = f"Sorry {full_name}, your name is not on the list."
        
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""

show_list()
