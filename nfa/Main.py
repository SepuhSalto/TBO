from nfa_conclusions import l1nfa, l2nfa, l3nfa, l4nfa

def menu():
    print("Pilih Salah Satu Opsi: ")
    print("1. L1: Semua string yang diterima berawalan 10 dan berakhiran 01")
    print("2. L2: Semua string yang mengandung substring 000 dan berakhiran 1.")
    print("3. L3: Semua string yang berawalan dan berakhiran dengan simbol yang berbeda.")
    print("4. L4: Semua string yang berawalan dan berakhiran dengan simbol yang sama dan mengandung substring 101.")
    print("5. Keluar")

def main():
    menu()
    
    while True:
        try:
            option = int(input("Masukkan Opsi: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if option == 1:
            x = input("Masukkan input (0 dan 1): ")
            if l1nfa(x):
                print(f"String '{x}' diterima.")
            else:
                print(f"String '{x}' ditolak.")
        elif option == 2:
            x = input("Masukkan input (0 dan 1): ")
            if l2nfa(x):
                print(f"String '{x}' diterima.")
            else:
                print(f"String '{x}' ditolak.")
        elif option == 3:
            x = input("Masukkan input (0 dan 1): ")
            if l3nfa(x):
                print(f"String '{x}' diterima.")
            else:
                print(f"String '{x}' ditolak.")
        elif option == 4:
            x = input("Masukkan input (0 dan 1): ")
            if l4nfa(x):
                print(f"String '{x}' diterima.")
            else:
                print(f"String '{x}' ditolak.")
        elif option == 5:
            confirm = input("Apakah Anda yakin ingin keluar? (y/n): ")
            if confirm.lower() == 'y':
                print("Program selesai.")
                break
            else:
                print("Kembali ke menu.")
        else:
            print("Pilihan Invalid")
        menu()  

main()
