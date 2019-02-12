età = 25
patente = True

# if età >= 18:
#    print("Sei Maggiorenne")

# if età >= 18:
#     print("Sei Maggiorenne")
# else:
#     print("Sei Minorenne!")


if età >= 18 and patente == True:
    print("Puoi noleggiare una Ferrari!")
elif età >= 18 and patente == False:
    print("Niente patente... niente Ferrari!")
else:
    print("Torneremo a parlare di macchine da corsa tra qualche anno...")
