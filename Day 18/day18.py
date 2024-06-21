class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.attendance = []

    def mark_attendance(self, date, status):
        self.attendance.append({"date": date, "status": status})

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}"


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' added to the classroom.")

    def mark_attendance(self, student_id, date, status):
        for student in self.students:
            if student.student_id == student_id:
                student.mark_attendance(date, status)
                print(f"Marked {status} for '{student.name}' on {date}.")
                return
        print(f"Student with ID '{student_id}' not found.")

    def display_attendance(self):
        for student in self.students:
            print(f"\nAttendance for {student.name} (ID: {student.student_id}):")
            for record in student.attendance:
                print(f"Date: {record['date']}, Status: {record['status']}")

# Contoh Penggunaan
classroom = Classroom()

# Menambahkan siswa ke dalam kelas
student1 = Student("Ramadani", "S001")
student2 = Student("Rachmad", "S002")

classroom.add_student(student1)
classroom.add_student(student2)

# Menandai kehadiran siswa
classroom.mark_attendance("S001", "2023-06-20", "Present")
classroom.mark_attendance("S002", "2023-06-20", "Absent")
classroom.mark_attendance("S001", "2023-06-21", "Absent")
classroom.mark_attendance("S002", "2023-06-21", "Present")

# Menampilkan daftar kehadiran siswa
print("\nDaftar Kehadiran:")
classroom.display_attendance()
