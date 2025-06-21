import datetime as dt
import os
import time

def clear_screen():
    os.system('cls')

tday = dt.date.today()
tanggal = str(tday)
buku = {}

def load_catatan():
    if os.path.exists("catatan.txt"):
        with open("catatan.txt", "r") as file:
            data = file.read().strip()
            catatan_list = data.split("\n\n")
            for catatan in catatan_list:
                lines = catatan.splitlines()
                judul = ""
                tanggal_ctt = ""
                isi_lines = []
                parsing_isi = False
                for line in lines:
                    if line.startswith("Title:"):
                        judul = line.replace("Title:", "").strip()
                        # parsing_isi = False
                    elif line.startswith("Date:"):
                        tanggal_ctt = line.replace("Date:", "").strip()
                        # parsing_isi = False
                    elif line.startswith("Content:"):
                        isi_lines.append(line.replace("Contentss:", "").strip())
                        parsing_isi = True
                    elif parsing_isi:
                        isi_lines.append(line)
                if judul:
                    buku[judul] = {
                        "Date": tanggal_ctt,
                        "Content": "\n".join(isi_lines)
                    }


def tampilan():
    clear_screen()
    print("\n--- Menu ---")
    print("1. Create a new note")
    print("2. Find note")
    print("3. See previous note")
    print("4. Out of the program")
    print("------------")

def main():
    load_catatan()
    while True:
        tampilan()
        pilihan = input("Enter your choice [1-4]: ")
        clear_screen()
        if pilihan == '1':
            baru()
        elif pilihan == '2':
            search()
        elif pilihan == '3':
            lihat()
        elif pilihan == '4':
            print("Thank you, the program is over..")
            break 
        else:
            print("Invalid selection. Please enter a number 1-4.")

def load_catatan():
    if os.path.exists("catatan.txt"):
        with open("catatan.txt", "r") as file:
            data = file.read().strip()
            catatan_list = data.split("\n\n")
            for catatan in catatan_list:
                lines = catatan.splitlines()
                judul = ""
                tanggal_ctt = ""
                isi_lines = []
                parsing_isi = False
                for line in lines:
                    if line.startswith("Title:"):
                        judul = line.replace("Title:", "").strip()
                        # parsing_isi = False
                    elif line.startswith("Date:"):
                        tanggal_ctt = line.replace("Date:", "").strip()
                        # parsing_isi = False
                    elif line.startswith("Content:"):
                        isi_lines.append(line.replace("Content:", "").strip())
                        parsing_isi = True
                    elif parsing_isi:
                        isi_lines.append(line)
                if judul:
                    buku[judul] = {
                        "Date": tanggal_ctt,
                        "Content": "\n".join(isi_lines)
                    }
                    
def input_paragraf():
    print("Write the contents of your note. Type 'END' (without the quotes) and then press Enter to end it.\n")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line)
    return '\n'.join(lines)

def baru():
    print(f'Today is {tday:%A}, {tday}')
    judul = input('Judul: ').strip()

    isi = input_paragraf()

    buku[judul] = {
        'Date': tanggal,
        'Content': isi
    }
    with open("catatan.txt", "a") as file:
        file.write(f"Title: {judul}\nDate: {tanggal}\nContent: {isi}\n\n")
    print('Currently saving....')
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(' thank you note saved.')
    time.sleep(2)
    clear_screen()

def lihat():
    if not buku:
        print("There are no notes saved yet.")
        return
    print("\n=== List of Note Titles ===")
    for i, judul in enumerate(buku.keys(), start=1):
        print(f"{i}. {judul}")

    pilihan = input("Enter the note number you want to view: ").strip()
    clear_screen()
    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(buku):
        print("Invalid input.")
        return

    judul_terpilih = list(buku.keys())[int(pilihan) - 1]
    details = buku[judul_terpilih]
    print(f"\nTitle: {judul_terpilih}\nDate: {details['tanggal']}\nContent: {details['isi']}")
    

    while True:
        action = input("What do you want to do? (e)dit, (d)elete, (b)ack to menu: ").lower()
        if action == 'e':
            edit(judul_terpilih)
            break
        elif action == 'd':
            hapus(judul_terpilih)
            break
        elif action == 'b':
            break
        else:
            print("Unrecognized option, please try again.")
    clear_screen()

def search():
    while True:
        keyword = input('Enter keywords to search for titles: ').strip()
        found = False
        for judul, details in buku.items():
            if keyword.lower() in judul.lower():
                print(f'Found:\nTitle: {judul}\nDate: {details["tanggal"]}\nContent: {details["isi"]}\n')
                found = True

        if not found:
            print("Tidak ada catatan dengan judul yang sesuai.")
        pil= input('(f)ind other title or (b)ack to menu:  ')
        if pil.lower()=='b':
            break
        clear_screen()


def hapus(judul=None):
    if judul in buku:
        del buku[judul]
        save_catatan()
        print(f"Note '{judul}' Deleted Successfully.")
        time.sleep(2)
        clear_screen()

def save_catatan():
    with open("catatan.txt", "w") as file:
        for judul, details in buku.items():
            file.write(f"Title: {judul}\nDate: {details['tanggal']}\nContent: {details['isi']}\n\n")

def edit(judul):
    if judul in buku:
        print(f"Editing note: {judul}")
        buku[judul]['isi'] = input_paragraf()

        save_catatan()
        print("The Note Successfully Edited!!")
        time.sleep(2)
    clear_screen()
    
main()