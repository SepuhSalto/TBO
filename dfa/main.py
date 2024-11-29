import tkinter as tk
from tkinter import filedialog, messagebox
from hat_delta_dfa import l1Hat
import pandas as pd
import os


class Application:
    def __init__(self, root):
        self.root = root
        self.state = 'login'
        self.expected_file_names = {
            'q0': 'surat_permohonan.pdf',
            'q1': ['formulir_keikutsertaan.pdf', 'surat_penunjukkan_admin.pdf', 'surat_kuasa.pdf'],
            'q2': 'formulir_penyedia.pdf',
            'q3': ['ktp_kitap_passport_direktur.pdf', 'ktp_penerima_kuasa.pdf'],
            'q4': ['npwp_perusahaan.pdf', 'tdb_nib.pdf', 'siup.pdf', 'akta_pendirian.pdf', 'akta_perubahan.pdf'],
            'q5': 'slip_gaji.pdf',
            'q6': 'rekening_koran_2_bulan_terakhir.pdf',
            'q7': 'surat_keterangan_domisili.pdf',
            'q8': None  # End state
        }
        self.upload_buttons = []
        self.create_widgets()
        self.update_state()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="", font=("Arial", 14))
        self.label.pack(pady=20)
        self.next_button = tk.Button(self.root, text="Next", command=self.next_state, font=("Arial", 12))
        self.next_button.pack(pady=20)

    def upload_file(self, index, expected_file_name):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            file_name = os.path.basename(file_path)

            if isinstance(expected_file_name, list):
                if file_name in expected_file_name:
                    self.upload_buttons[index]['file_path'] = file_path
                    self.upload_buttons[index]['button'].config(text=f"File selected: {file_name}")
                else:
                    messagebox.showerror("Error", f"File name must match: {', '.join(expected_file_name)}")
            else:
                if file_name == expected_file_name:
                    self.upload_buttons[index]['file_path'] = file_path
                    self.upload_buttons[index]['button'].config(text=f"File selected: {file_name}")
                else:
                    messagebox.showerror("Error", f"File name must match: {expected_file_name}")
        else:
            self.upload_buttons[index]['file_path'] = None

    def next_state(self):
        if self.state == 'login':
            username = self.username_entry.get()
            password = self.password_entry.get()
            if self.validate_login(username, password):
                self.state = l1Hat(self.state, 'Y')
                self.update_state()
            else:
                messagebox.showerror("Error", "Invalid credentials")
            return

        all_files_uploaded = all(button['file_path'] for button in self.upload_buttons)
        if not all_files_uploaded:
            self.state = l1Hat(self.state, 'T')
            messagebox.showerror("Error", "Please upload all required files before proceeding.")
        else:
            self.state = l1Hat(self.state, 'Y')

        for button in self.upload_buttons:
            button['button'].pack_forget()
        self.upload_buttons.clear()
        self.update_state()

    def validate_login(self, username, password):
        try:
            df = pd.read_csv('users.csv')
            if username.strip() not in df["username"].values:
                messagebox.showerror("Error", "Username not found.")
                return False

            stored_password = str(df[df["username"].str.strip() == username.strip()]["password"].values[0])
            return password.strip() == stored_password.strip()
        except FileNotFoundError:
            messagebox.showerror("Error", "User data file not found")
            return False

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            df = pd.read_csv('users.csv')
        except FileNotFoundError:
            df = pd.DataFrame(columns=['username', 'password'])

        if username in df['username'].values:
            messagebox.showerror("Error", "Username already exists")
        else:
            df = pd.concat([df, pd.DataFrame([{'username': username, 'password': password}])], ignore_index=True)
            df.to_csv('users.csv', index=False)
            messagebox.showinfo("Success", "User registered successfully")

    def update_state(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

        if self.state == 'login':
            self.label.config(text="Login")
            self.label.pack(pady=20)
            tk.Label(self.root, text="Username:", font=("Arial", 12)).pack(pady=0, padx=200, anchor=tk.W)
            self.username_entry = tk.Entry(self.root, font=("Arial", 12))
            self.username_entry.pack(pady=0, padx=10)

            tk.Label(self.root, text="Password:", font=("Arial", 12)).pack(pady=0, padx=200, anchor=tk.W)
            self.password_entry = tk.Entry(self.root, show='*', font=("Arial", 12))
            self.password_entry.pack(pady=0, padx=10)

            tk.Button(self.root, text="Login", command=self.next_state).pack(pady=10, padx=10)
            tk.Button(self.root, text="Register", command=self.register_user).pack(pady=10, padx=10)

        elif self.state == 'q0':
            self.label.config(text="Surat Permohonan")
            self.label.pack(pady=20)
            self.add_upload_button("Upload Surat Permohonan", "surat_permohonan.pdf")

        elif self.state == 'q1':
            self.label.config(text="Formulir keikutsertaan, Surat Penunjukkan Admin, Surat Kuasa")
            self.label.pack(pady=20)
            self.add_upload_button("Upload Formulir keikutsertaan", "formulir_keikutsertaan.pdf")
            self.add_upload_button("Upload Surat Penunjukkan Admin", "surat_penunjukkan_admin.pdf")
            self.add_upload_button("Upload Surat Kuasa", "surat_kuasa.pdf")

        elif self.state == 'q2':
            self.label.config(text="Formulir Penyedia")
            self.label.pack(pady=20)
            self.add_upload_button("Upload Formulir Penyedia", "formulir_penyedia.pdf")

        elif self.state == 'q3':
            self.label.config(text="KTP/KITAS/Passport Direktur, KTP Penerima Kuasa")
            self.label.pack(pady=20)
            self.add_upload_button("Upload KTP/KITAS/Passport Direktur", "ktp_kitap_passport_direktur.pdf")
            self.add_upload_button("Upload KTP Penerima Kuasa", "ktp_penerima_kuasa.pdf")

        elif self.state == 'q4':
            self.label.config(text="NPWP Perusahaan, TDB/NIB, SIUP, Akta Pendirian, Akta Perubahan")
            self.label.pack(pady=20)
            self.add_upload_button("Upload NPWP Perusahaan", "npwp_perusahaan.pdf")
            self.add_upload_button("Upload TDP/NIB", "tdb_nib.pdf")
            self.add_upload_button("Upload SIUP", "siup.pdf")
            self.add_upload_button("Upload Akta Pendirian", "akta_pendirian.pdf")
            self.add_upload_button("Upload Akta Perubahan", "akta_perubahan.pdf")

        elif self.state == 'q5':
            self.label.config(text="Slip Gaji")
            self.label.pack(pady=20)
            self.add_upload_button("Upload Slip Gaji", "slip_gaji.pdf")

        elif self.state == 'q6':
            self.label.config(text="Rekening Koran 2 Bulan terakhir")
            self.label.pack(pady=20)
            self.add_upload_button("Upload Rekening Koran 2 Bulan terakhir", "rekening_koran_2_bulan_terakhir.pdf")

        elif self.state == 'q7':
            self.label.config(text="Surat Keterangan Domisili")
            self.label.pack(pady=20)
            self.add_upload_button("Upload Surat Keterangan Domisili", "surat_keterangan_domisili.pdf")

        elif self.state == 'q8':
            self.label.config(text="Semua File Diterima")
            self.label.pack(pady=20)
            self.next_button.config(state=tk.DISABLED)

        if self.state != 'login' and self.state != 'q8':
            self.next_button.pack(pady=20)

    def add_upload_button(self, text, expected_file_name):
        button = tk.Button(self.root, text=text, command=lambda idx=len(self.upload_buttons): self.upload_file(idx, expected_file_name), font=("Arial", 12))
        button.pack(pady=10)
        self.upload_buttons.append({'button': button, 'file_path': None, 'expected_file_name': expected_file_name})


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x300")  # Set fixed size for the window (width x height)
    root.resizable(False, False)  # Disable resizing of the window
    app = Application(root)
    root.mainloop()
