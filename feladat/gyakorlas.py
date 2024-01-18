homerseklet = int(input("Kérerm írd be a hőmérsékleted:"))
if homerseklet < 37:
    print("normális")
elif homerseklet >= 40:
    print("korház")
elif homerseklet >= 38:
    print("lázas")
elif homerseklet >= 37:
    print("hőemelkedés")