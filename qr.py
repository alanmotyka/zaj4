import qrcode
tresc = "Kochamy uczyć się Analizy"
obraz = qrcode.make(tresc)
obraz.save("qr.png")
print("Gotowe")

import qrcode
kod = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
kod.add_data("Warsztaty matematyczne")
kod.make(fit=True)
obraz = kod.make_image(fill_color="yellow", back_color="blue")
obraz.save("warsztaty.png")
print("Wersja kodu:", kod.version)