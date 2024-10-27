day_until_exam = 10
with open("basic_info.txt", "w") as file:
            file.writelines(str(day_until_exam))
            file.close()