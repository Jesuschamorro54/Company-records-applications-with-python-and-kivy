def valid_login_func(cursor, ide, post):
    # print to check
    print("Validating\nid:", ide, "job:", post)

    # Query to run
    sql = f"select * from empleados where id={ide} and cargo={post}"
    cursor.execute(sql)
    try:
        if cursor.fetchone() is not None:
            print("Correct validation")
            return True
        else:
            return False
    except:
        pass

def valid_address(address):
    address = address.split(',')

    # check the data that will be sent to the address table
    for i in range(len(address)):
        if address[i] == '':
            address[i] = 'null'
        elif address[4] != 'null':
            try:
                address[4] = int(address[4])
            except:
                print("El valor no es tipo numerico")
                return 1
    if address[5] == 'null' or address[0] == 'null':
        return 2

    address_str = str(address)
    address_str = address_str.replace("['", "('")
    address_str = address_str.replace("']", "')")
    address_str = address_str.replace("'null'", "null")
    return address_str


def valid_insert_user(user, address_id):
    print("\nusuario: ", user)

    # validate that the data is complete

    if user[0] == '':
        print("nombre problem")
        return "Por favor ingrese un nombre"

    elif user[4] == 'YYYY-MM-DD' or user[4] == '' or len(user[4]) != 10:
        print("fecha problem")
        return "La fecha es incorrecta"

    elif user[2] == '':
        print("telefono vacio")
        user[2] = 'null'

    elif user[2] != '' or user[2] != 'null':
        print("cambiando a entero")
        try:
            user[2] = int(user[2])
            print("cambiado: ", user[2])
        except:
            print("numero de telefono no valido")
            return "Numero de telefono incorrecto"


    user[3] = address_id
    print("normal")
    return user


