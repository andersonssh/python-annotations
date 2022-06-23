with open('example.txt', 'r') as f:
    # f.read(n_de_bytes)
    # realiza a leitura dos primeiros caracteres
    print(f.read(2)) # >> 01
    # realiza uma segunda leitura, desconsiderando os caracteres ja lidos
    print(f.read(2)) # >> 23

    while True:
        bytes_read = f.read(128)
        print(bytes_read)
        if not bytes_read:
            print('parando loop de leitura do arquivo')
            break
