import students
import flet
from time import sleep

def main(page: flet.Page):
    page.title = "Grading System"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.window_width = 900
    page.window_height = 700
    page.padding = 25
    page.bgcolor = "#121212"

    t = flet.Text(value="Grading System", color="white", size=25)
    studentID = flet.TextField(label = "Student ID", width = 300, color="white", border_color="white", cursor_color="green")
    name = flet.TextField(label = "Student Name", width = 300, color="white", border_color="white", cursor_color="green")
    surname = flet.TextField(label = "Student Surname", width = 300, color="white", border_color="white", cursor_color="green")
    lesson = flet.TextField(label = "Lesson", width = 300, color="white", border_color="white", cursor_color="green")
    grade = flet.TextField(label = "Grade", width = 300, color="white", border_color="white", cursor_color="green")

    def sendData(e):
        i = 0
        for item in [studentID,name,surname,lesson,grade]:
            if not item.value:
                item.error_text = "please fill the required fields"
                page.update()
                i -= 1
            else:
                item.error_text = None
                page.update()
                i += 1

        try:
            if ( (int(grade.value) >= 0) and (int(grade.value) <= 100) ):
                grade.error_text = None
                page.update()
            else:
                grade.error_text = "please enter a value between 0 and 100"
                page.update()
                i -= 1
        except:
            grade.error_text = "please enter a value between 0 and 100"
            page.update()
            i -= 1

        if i == 5:
            students.Student(studentID.value, name.value, surname.value, lesson.value, grade.value)
            for item in [studentID,name,surname,lesson,grade]:
                item.value = None
                page.update()
            t.value = "Data Sent Successfully!"
            t.color = "green"
            t.size = 40
            t.update()
            sleep(3)
            t.value = "Grading System" 
            t.color = "white"
            t.size = 25
            t.update()

    bt = flet.ElevatedButton("submit", on_click=sendData)

    page.add(t,studentID,name,surname,lesson,grade,bt)

flet.app(target=main)