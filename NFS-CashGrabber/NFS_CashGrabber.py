import PySimpleGUI as sg

def generate_race_script(yaris_adi, yaris_id, koordinatlar, IntroNisA, available_in_qr, TrafficLevelo, gameplayvaulta, TimeLimits, race_regiona,Bariyerler ):
    script = f"#Yaris Kodu\n"
    script += f"add_node gameplay cashgrab {yaris_adi}\n"
    script += f"add_field gameplay {yaris_adi} EventID\n"
    script += f"add_field gameplay {yaris_adi} IntroNis\n"
    script += f"add_field gameplay {yaris_adi} racestart\n"
    script += f"add_field gameplay {yaris_adi} region\n"
    script += f"add_field gameplay {yaris_adi} Name\n"
    script += f"add_field gameplay {yaris_adi} Template\n"
    script += f"add_field gameplay {yaris_adi} TrafficLevel\n"

    script += f"add_field gameplay {yaris_adi} Children {len(koordinatlar)}\n"

    script += f"add_field gameplay {yaris_adi} gameplayvault\n"
    script += f"add_field gameplay {yaris_adi} TimeLimit\n"
    script += f"add_field gameplay {yaris_adi} Opponents\n"
    script += f"change_field gameplay {yaris_adi} {yaris_id}\n"
    script += f"change_field gameplay {yaris_adi} IntroNis {IntroNisA}\n"
    script += f"change_field gameplay {yaris_adi} AvailableInQR {available_in_qr}\n"
    script += f"change_field gameplay {yaris_adi} racestart {yaris_adi}/startgrid\n"
    script += f"change_field gameplay {yaris_adi} TrafficLevel {TrafficLevelo}\n"
    script += f"change_field gameplay {yaris_adi} gameplayvault {gameplayvaulta} \n"
    script += f"change_field gameplay {yaris_adi} TimeLimit {TimeLimits}\n"
    script += f"change_field gameplay {yaris_adi} Name {yaris_adi}\n"
    script += f"change_field gameplay {yaris_adi} region {race_regiona}\n"

# script += f"add_field gameplay {yaris_adi} Opponents {opponent_value}"

# script +=f"add_field gameplay {yaris_adi} Barriers {Bariyerler}"





    for i, koordinat in enumerate(koordinatlar):
        script += f"Checkpoint_{i}={koordinat}\n"

    script += "StartPoint=0\n"

    return script

layout = [
    [sg.Text("Yarış Adı: "), sg.Input(key="-YarisAdi-")],
    [sg.Text("Yarış ID: "), sg.Input(key="-YarisID-")],
    [sg.Text("Intro Cutscene: "), sg.Input(key="-IntroNisF-")],
    [sg.Text("Race Region: "), sg.Input(key="-RaceRegion-")],
    [sg.Text("Traffic Level: "), sg.Input(key="-TrafficLevel-")],
    [sg.Text("Time Limit: "), sg.Input(key="-TimeLimit-")],
    [sg.Text("GamePlay Vault: "), sg.Input(key="-GamePlayVault-")],
    [sg.Text("Koordinatlar (Her satırda bir koordinat):")],
    [sg.Multiline(key="-Koordinatlar-", size=(40, 5))],
    [sg.Checkbox("Available in Quick Race", key="-AvailableInQR-")],
    [sg.Button("Yarış Scripti Oluştur"), sg.Button("Çıkış")]
]

window = sg.Window("NFS-CashGrabber", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Çıkış":
        break
    elif event == "Yarış Scripti Oluştur":
        yaris_adi = values["-YarisAdi-"]
        yaris_id = values["-YarisID-"]
        IntroNisA = values["-IntroNisF-"]
        koordinatlar = values["-Koordinatlar-"].splitlines()
        available_in_qr = values["-AvailableInQR-"]
        TrafficLevelo = values["-TrafficLevel-"]
        gameplayvaulta = values["-GamePlayVault-"]
        TimeLimits = values["-TimeLimit-"]
        race_regiona = values["-RaceRegion-"]

        if not yaris_adi or not yaris_id or not koordinatlar or not IntroNisA:
            sg.popup_error("Lütfen tüm alanları doldurun.")
            continue

        try:
            yaris_scripti = generate_race_script(yaris_adi, yaris_id, koordinatlar, IntroNisA, available_in_qr, race_regiona, TimeLimits, gameplayvaulta, TrafficLevelo, )

            with open(f"script.nfsms", "w") as dosya:
                dosya.write(yaris_scripti)

            sg.popup(f"script.nfsms dosyası oluşturuldu.")
        except Exception as e:
            sg.popup_error(f"Bir hata oluştu: {str(e)}")

window.close()
