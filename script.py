inputPath = open(str(input("Enter input .txt: ")), "r")
lines = inputPath.readlines()
inputPath.close()
outputPath1 = open("UserPass.txt", "w")
outputPath2 = open("MailPass.txt", "w")
for line in lines:
    outputPath1.write(line.split(":")[0] + ":" + line.split(":")[2])
    outputPath2.write(line.split(":")[1] + ":" + line.split(":")[2])
outputPath1.close()
outputPath2.close()

