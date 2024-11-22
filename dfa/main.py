import tkinter as tk
from tkinter import filedialog, messagebox
from hat_delta_dfa import l1Hat
import pandas as pd
from pandas import DataFrame

class Application:
    def __init__(self, root):
        self.root = root
        self.state = 'login'
        self.create_widgets()
        self.update_state()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="", font=("Arial", 14))
        self.label.pack(pady=20)
        self.upload_buttons = []
        self.next_button = tk.Button(self.root, text="Next", command=self.next_state, font=("Arial", 12))
        self.next_button.pack(pady=20)

    def upload_file(self, index):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.upload_buttons[index]['file_path'] = file_path
            self.upload_buttons[index]['button'].config(text=f"File selected: {file_path.split('/')[-1]}")
        else:
            self.upload_buttons[index]['file_path'] = None

    def next_state(self):
            if self.state == 'login':
                username = self.username_entry.get()
                password = self.password_entry.get()
                if self.validate_login(username, password):
                    self.state = l1Hat(self.state, 'T')
                    self.update_state()

                else:
                    messagebox.showerror("Error", "Invalid credentials")
                return
    
            all_files_uploaded = True
            for button in self.upload_buttons:
                if not button['file_path']:
                    button['file_path'] = 'T'
                    button['button'].config(text="File not uploaded (T)")
                    all_files_uploaded = False
    
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
                print("Username does not exist.")
                return False

            stored_password = str(df[df["username"].str.strip() == username.strip()]["password"].values[0])

            if password.strip() == stored_password.strip():
                print("Login successful!")
                return True
            else:
                print("Incorrect password.")
                return False
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
            self.username_entry = tk.Entry(self.root, font=("Arial", 12))
            self.username_entry.pack(pady=10)
            self.password_entry = tk.Entry(self.root, show='*', font=("Arial", 12))
            self.password_entry.pack(pady=10)
            self.login_button = tk.Button(self.root, text="Login", command=self.next_state, font=("Arial", 12))
            self.login_button.pack(pady=10)
            self.register_button = tk.Button(self.root, text="Register", command=self.register_user, font=("Arial", 12))
            self.register_button.pack(pady=10)
        elif self.state == 'q0':
            self.label.config(text="Surat Permohonan")
            self.label.pack(pady=20)
            self.add_upload_button("Upload Surat Permohonan")
        elif self.state == 'q1':
            self.label.config(text="Formulir keikutsertaan, Surat Penunjukkan Admin, Surat Kuasa")
            self.label.pack(pady=20)
            self.add_upload_button("Upload Formulir keikutsertaan")
            self.add_upload_button("Upload Surat Penunjukkan Admin")
            self.add_upload_button("Upload Surat Kuasa")
        elif self.state == 'q2':
            self.label.config(text="Formulir Penyedia")
            self.label.pack(pady=20)
            self.add_upload_button("Upload Formulir Penyedia")
        elif self.state == 'q3':
            self.label.config(text="KTP/KITAS/Passport Direktur, KTP Penerima Kuasa")
            self.label.pack(pady=20)
            self.add_upload_button("Upload KTP/KITAS/Passport Direktur")
            self.add_upload_button("Upload KTP Penerima Kuasa")
        elif self.state == 'q4':
            self.label.config(text="NPWP Perusahaan, TDB/NIB, SIUP, Akta Pendirian, Akta Perubahan")
            self.label.pack(pady=20)
            self.add_upload_button("Upload NPWP Perusahaan")
            self.add_upload_button("Upload TDP/NIB")
            self.add_upload_button("Upload SIUP")
            self.add_upload_button("Upload Akta Pendirian")
            self.add_upload_button("Upload Akta Perubahan")
        elif self.state == 'q5':
            self.label.config(text="Slip Gaji")
            self.label.pack(pady=20)
            self.add_upload_button("Upload Slip Gaji")
        elif self.state == 'q6':
            self.label.config(text="Rekening Koran 2 Bulan terakhir")
            self.label.pack(pady=20)
            self.add_upload_button("Upload Rekening Koran 2 Bulan terakhir")
        elif self.state == 'q7':
            self.label.config(text="Surat Keterangan Domisili")
            self.label.pack(pady=20)
            self.add_upload_button("Upload Surat Keterangan Domisili")
        elif self.state == 'q8':
                self.label.config(text="Semua File Diterima")
                self.label.pack(pady=20)
                self.next_button.config(state=tk.DISABLED)

        if self.state != 'login' and self.state != 'q8':
            self.next_button.pack(pady=20)


    def add_upload_button(self, text):
        button = tk.Button(self.root, text=text, command=lambda idx=len(self.upload_buttons): self.upload_file(idx), font=("Arial", 12))
        button.pack(pady=10)
        self.upload_buttons.append({'button': button, 'file_path': None})


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()