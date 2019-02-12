contatore = 0

# if contatore <= 10:
#     print(contatore)
#     contatore += 1  # contatore = contatore + 1


# while contatore <= 10:
#     print(contatore)
#     contatore += 1  # --> contatore = contatore + 1


# while 10 == 10: # LOOP INFINITO!
#     print(contatore)
    # contatore += 1  contatore = contatore + 1


# while contatore <= 10:
#     print(contatore)
#     contatore += 1  #  contatore = contatore + 1
#     if contatore == 5:
#         print(contatore)
#         print("Sto uscendo dal loop...")
#         break


while contatore <= 10:
    contatore += 1    #  contatore = contatore + 1
    if contatore == 5:
        print("saltato")
        continue
    print(contatore)
