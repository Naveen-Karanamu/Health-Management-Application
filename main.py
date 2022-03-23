print("Hey Admin! WELCOME to your Health Management Application 😉")

print("As you know, you can handle this application with numbers!")

def client_name_selection():
    client=int(input("To Checkon Thor Enter '1' or to checkon Loki Enter '2' "))

    if(client==1):
        client_name="Thor"
    elif(client==2):
        client_name="Loki"
    else:
        print("Invalid client name ⚠️, Please select from the given client id's!")
        client_name_selection()
        
    def client_file_selection():
        client_file=int(input(f"Enter '1' for {client_name}'s Diet file or '2' for {client_name}'s Exercise file or '3' to go Back "))

        if(client_file==1):
            client_file_name="diet"
        elif(client_file==2):
            client_file_name="exercise"
        elif(client_file==3):
            client_name_selection()
        else:
            print("Invalid client file name ⚠️, Please select from the given client id's!")
            client_file_selection()
            
        def file_operation_selection():
            file_operation=int(input(f"Enter '1' to read {client_name}'s {client_file_name}'s file. Enter '2' to write {client_name}'s {client_file_name}'s file. Enter '3' to go back "))
            
            if(file_operation==1):
                file=open(f"Data\{client_name}.{client_file_name}.txt")
                print(file.read())
            elif(file_operation==2):
                file=open(f"Data\{client_name}.{client_file_name}.txt", "a")
                add_data=input(f"Enter the new {client_file_name} for {client_name} ")
                file.write(f"\n{add_data}")
            elif(file_operation==3):
                client_file_selection()
            else:
                print("Invalid client file operation ⚠️, Please select from the given client id's!")
                
                
        file_operation_selection()
            
    client_file_selection()
    
client_name_selection()