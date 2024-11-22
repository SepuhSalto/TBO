import tkinter as tk
from tkinter import filedialog, messagebox
from hat_delta_dfa import l1Hat

class Application:
    def __init__(self, root):
        self.root = root
        self.state = 'q0'
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
        all_files_uploaded = True
        for button in self.upload_buttons:
            if not button['file_path']:
                button['file_path'] = 'T'
                all_files_uploaded = False

        if not all_files_uploaded:
            messagebox.showerror("Error", "Please upload all required files.")
            return
        else:
            self.state = l1Hat(self.state, 'Y')

        self.state = l1Hat(self.state, 'Y')

        for button in self.upload_buttons:
            button['button'].pack_forget()
        self.upload_buttons.clear()

        self.update_state()

    def update_state(self):
        if self.state == 'q0':
            self.label.config(text="Surat permohonan")
            self.add_upload_button("Upload Surat permohonan")
        elif self.state == 'q1':
            self.label.config(text="Formulir keikutsertaan, Surat Penunjukkan Admin, Surat Kuasa")
            self.add_upload_button("Upload Formulir keikutsertaan")
            self.add_upload_button("Upload Surat Penunjukkan Admin")
            self.add_upload_button("Upload Surat Kuasa")
        elif self.state == 'q2':
            self.label.config(text="Formulir Penyedia")
            self.add_upload_button("Upload Formulir Penyedia")
        elif self.state == 'q3':
            self.label.config(text="KTP/KITAS/Passport Direktur, KTP Penerima Kuasa")
            self.add_upload_button("Upload KTP/KITAS/Passport Direktur")
            self.add_upload_button("Upload KTP Penerima Kuasa")
        elif self.state == 'q4':
            self.label.config(text="NPWP Perusahaan")
            self.add_upload_button("Upload NPWP Perusahaan")
        elif self.state == 'q5':
            self.label.config(text="SIUP")
            self.add_upload_button("Upload SIUP")
        elif self.state == 'q6':
            self.label.config(text="TDP/NIB")
            self.add_upload_button("Upload TDP/NIB")
        elif self.state == 'q7':
            self.label.config(text="Akta Pendirian, Akta Perubahan")
            self.add_upload_button("Upload Akta Pendirian")
            self.add_upload_button("Upload Akta Perubahan")
        elif self.state == 'q8':
            self.label.config(text="Surat Keterangan Domisili")
            self.add_upload_button("Upload Surat Keterangan Domisili")
        elif self.state == 'q9':
            if l1Hat('q0', 'Y' * 10) == 'q10':
                self.label.config(text="Q10: Diterima")
                self.next_button.config(state=tk.DISABLED)
            else:
                messagebox.showerror("Error", "Not in final state")

    def add_upload_button(self, text):
        button = tk.Button(self.root, text=text, command=lambda idx=len(self.upload_buttons): self.upload_file(idx), font=("Arial", 12))
        button.pack(pady=10)
        self.upload_buttons.append({'button': button, 'file_path': None})

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()