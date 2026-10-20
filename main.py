from pyscript import document, display

my_listcuh = ["Jacob Cortez", "Luis Pablo", "Mason Amos", "Earl Abadam", "JC Macalalag", "Joaquin Tovera"]

def show_list():
    output = document.getElementById("output")
    output.innerHTML = ""

    for item in my_listcuh:
        badge_html = f"<span class='archer-badge'>{item}</span>"
        display(badge_html, target="output", append=True)

def append_value(e):
    value = document.getElementById("user_input").value.strip()
    message = document.getElementById("message")

    if value:
        my_listcuh.append(value)
        message.innerHTML = "data added successfully"
        show_list()
    else:
        message.innerHTML = "please add a value"
    document.getElementById("user_input").value = ""

def delete_value(e):
    value = document.getElementById("user_input").value.strip()
    message = document.getElementById("message")

    if value in my_listcuh:
        my_listcuh.remove(value)
        message.innerHTML = "Player kicked successfully"
        show_list()
    else:
        message.innerHTML = "value not found"
    document.getElementById("user_input").value = ""

show_list()
