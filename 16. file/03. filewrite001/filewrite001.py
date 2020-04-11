print("===============ファイル書き込みテスト===================")

msg = input("input test: ")
with open("samplewrite.txt", "w") as f:
    f.write(msg)
    print("Save message!")
