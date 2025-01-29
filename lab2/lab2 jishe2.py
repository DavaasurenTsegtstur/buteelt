# MADLIB 1
course_id = input("хичээлийн код: ")
course_name = input("хичээлийн нэр: ")
credit = input("хичээлийн кредит: ")

madlib = "энэ нь хичээлийн код {}".format(course_id).lower() + ", хичээлийн нэр нь {}".format(course_name).lower() + \
    " бөгөөд уг хичээл нь {}".format(credit) + " кредитийн хичээл юм."

print(madlib)
