from tkinter import *
from tkinter import ttk, messagebox
import psycopg2


# ------------------------ DATABASE HANDLER ------------------------ #
class Database:
    def __init__(self):
        self.db = "studentdb"
        self.user = "postgres"
        self.password = "admin123"
        self.host = "localhost"
        self.port = "5432"

    def query(self, q, params=()):
        conn = psycopg2.connect(
            dbname=self.db,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        cur = conn.cursor()
        result = None
        try:
            cur.execute(q, params)
            if q.strip().lower().startswith("select"):
                result = cur.fetchall()
            conn.commit()
        except psycopg2.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cur.close()
            conn.close()
        return result


# ------------------------ MAIN APP ------------------------ #
class StudentApp:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title("AI-Enhanced Student Management System")
        self.root.geometry("750x500")

        self.build_ui()
        self.refresh_table()

    # ------------------------ UI SETUP ------------------------ #
    def build_ui(self):
        # Top Form Frame
        form_frame = LabelFrame(self.root, text="Student Information")
        form_frame.pack(fill="x", padx=10, pady=5)

        Label(form_frame, text="Name").grid(row=0, column=0, sticky="w")
        Label(form_frame, text="Address").grid(row=1, column=0, sticky="w")
        Label(form_frame, text="Age").grid(row=2, column=0, sticky="w")
        Label(form_frame, text="Phone").grid(row=3, column=0, sticky="w")

        self.name = Entry(form_frame)
        self.address = Entry(form_frame)
        self.age = Entry(form_frame)
        self.phone = Entry(form_frame)

        self.name.grid(row=0, column=1, padx=5, pady=2)
        self.address.grid(row=1, column=1, padx=5, pady=2)
        self.age.grid(row=2, column=1, padx=5, pady=2)
        self.phone.grid(row=3, column=1, padx=5, pady=2)

        # Buttons
        btn_frame = Frame(self.root)
        btn_frame.pack(fill="x")

        Button(btn_frame, text="Create Table", command=self.create_table).pack(side=LEFT, padx=5)
        Button(btn_frame, text="Add", command=self.insert_data).pack(side=LEFT, padx=5)
        Button(btn_frame, text="Update", command=self.update_data).pack(side=LEFT, padx=5)
        Button(btn_frame, text="Delete", command=self.delete_data).pack(side=LEFT, padx=5)

        # Search Bar
        search_frame = Frame(self.root)
        search_frame.pack(fill="x", pady=3)

        Label(search_frame, text="Search:").pack(side=LEFT)
        self.search_var = StringVar()
        self.search_var.trace("w", lambda *args: self.search())
        Entry(search_frame, textvariable=self.search_var).pack(side=LEFT, padx=5, fill="x", expand=True)

        # Table
        table_frame = Frame(self.root)
        table_frame.pack(fill="both", expand=True, pady=10)

        self.tree = ttk.Treeview(table_frame, columns=("id", "name", "address", "age", "phone"))
        self.tree.pack(fill="both", expand=True)

        for col in ("id", "name", "address", "age", "phone"):
            self.tree.heading(col, text=col.upper())

        self.tree.bind("<<TreeviewSelect>>", self.fill_fields)

        # Status Bar
        self.status = Label(self.root, text="Ready", relief=SUNKEN, anchor="w")
        self.status.pack(fill="x")

    # ------------------------ CRUD FUNCTIONS ------------------------ #
    def create_table(self):
        q = """
        CREATE TABLE IF NOT EXISTS students(
            student_id SERIAL PRIMARY KEY,
            name TEXT,
            address TEXT,
            age INT,
            phone TEXT
        );
        """
        self.db.query(q)
        messagebox.showinfo("Success", "Table created.")

    def insert_data(self):
        if not self.validate_inputs():
            return

        q = "INSERT INTO students(name, address, age, phone) VALUES (%s, %s, %s, %s)"
        params = (self.name.get(), self.address.get(), self.age.get(), self.phone.get())
        self.db.query(q, params)
        self.refresh_table()
        self.status.config(text="Record inserted.")

    def update_data(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a row to update.")
            return

        student_id = self.tree.item(selected[0])["values"][0]

        q = "UPDATE students SET name=%s, address=%s, age=%s, phone=%s WHERE student_id=%s"
        params = (self.name.get(), self.address.get(), self.age.get(), self.phone.get(), student_id)
        self.db.query(q, params)

        self.refresh_table()
        self.status.config(text="Record updated.")

    def delete_data(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a row to delete.")
            return

        student_id = self.tree.item(selected[0])["values"][0]
        q = "DELETE FROM students WHERE student_id=%s"
        self.db.query(q, (student_id,))
        self.refresh_table()
        self.status.config(text="Record deleted.")

    # ------------------------ TABLE OPERATIONS ------------------------ #
    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        data = self.db.query("SELECT * FROM students ORDER BY student_id ASC")
        if data:
            for row in data:
                self.tree.insert("", "end", values=row)

    def search(self):
        text = self.search_var.get().lower()
        for row in self.tree.get_children():
            vals = self.tree.item(row)["values"]
            row_str = " ".join(str(v).lower() for v in vals)
            self.tree.item(row, tags=("" if text in row_str else "hidden"))

        self.tree.tag_configure("hidden", foreground="gray80")

    def fill_fields(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        vals = self.tree.item(selected[0])["values"]
        self.name.delete(0, END)
        self.address.delete(0, END)
        self.age.delete(0, END)
        self.phone.delete(0, END)

        self.name.insert(0, vals[1])
        self.address.insert(0, vals[2])
        self.age.insert(0, vals[3])
        self.phone.insert(0, vals[4])

    # ------------------------ VALIDATION ------------------------ #
    def validate_inputs(self):
        if not self.name.get():
            messagebox.showerror("Invalid Input", "Name is required.")
            return False
        if not self.age.get().isdigit():
            messagebox.showerror("Invalid Input", "Age must be a number.")
            return False
        return True


# ------------------------ RUN APP ------------------------ #
root = Tk()
app = StudentApp(root)
root.mainloop()
