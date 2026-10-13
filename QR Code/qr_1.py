import qrcode as qr

img=qr.make("https://github.com/shanna33?tab=overview&from=2026-09-01&to=2026-09-28")
img.save("github_shanna.png")