# Write to external file
employee_file = open("employees.txt", "a")
employee_file.write("\nSivar - Developer")
employee_file.close()

# Write or create then write a file
employee_file = open("employees_1.txt", "w")
employee_file.write("\nSivar - Developer")
employee_file.close()

# Custom file type writing
employee_file = open("index.html", "w")
employee_file.write("<p> Sivar Sarkawt </p>")
employee_file.close()
