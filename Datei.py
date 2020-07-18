# Open .txt file
datei = open('text.txt', 'r', encoding='utf-8')

for zeile in datei:
    print(zeile)

datei.close()
