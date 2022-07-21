from cryptography.fernet import Fernet


class PasswordManager:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, "wb") as f:
            f.write(self.key)

    def load_key(self, path):
        with open(path, "rb") as f:
            self.key = f.read()

    def create_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for k, v in initial_values.items():
                self.add_password(k, v)

    def load_file(self, path):
        self.password_file = path

        with open(path, "r") as f:
            for line in f.readlines():
                site, encrypt_pass = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypt_pass.encode()).decode()

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, "a+") as f:
                encrypt_pass = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypt_pass.decode() + "\n")

    def get_password(self, site):
        return self.password_dict[site]


if __name__ == '__main__':
    passwords = {
        "email": "123241",
        "vk": "fsag21421"
    }

    pm = PasswordManager()

    print("""
        (1) Create key
        (2) Load key
        (3) Create passwords file
        (4) Load password file
        (5) Add password to dictionary
        (6) Get password by site
        (q) Quit 
    """)

    while True:
        choosed = input("Choose action: ")
        if choosed == "1" or choosed == "2" or choosed == "3" or choosed == "4":
            file_path = input("Path of command: ")
            if choosed == "1":
                pm.create_key(file_path)
                print("Key is created.")
            elif choosed == "2":
                pm.load_key(file_path)
                print("Key is loaded.")
            elif choosed == "3":
                pm.create_file(file_path, passwords)
                print("Create file with encoded passwords")
            elif choosed == "4":
                pm.load_file(file_path)
                print("Passwords was loaded into dictionary")
        elif choosed == "5" or choosed == "6":
            site = input("Site: ")
            if choosed == "5":
                new_pass = input(f"Password for {site}: ")
                pm.add_password(site, new_pass)
            else:
                print(f"The site {site} have a {pm.get_password(site)}")
        elif choosed == "q":
            print("Byeee!!!")
            break