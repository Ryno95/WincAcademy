import os
import shutil

# ------------------ #1 -------------------#
# print the files of a directory on your desktop


def checkDirectory(path="/Users/RynoMeiboom/Desktop/Testfiles"):
    for (root, dirs, files) in os.walk(path, topdown=True):
        return files

    # checkDirectory("/Users/RynoMeiboom/Desktop/Testfiles")

    # os.rename("/Users/RynoMeiboom/Desktop/files", "/Users/RynoMeiboom/Desktop/Testfiles")

    # def addFile(fileName):


#
#
# dir = "Juf"
# dir2 = "Rest"
#
# parentDir = "/Users/RynoMeiboom/Desktop/Testfiles"
#
# path1 = os.path.join(parentDir, dir)
# path2 = os.path.join(parentDir, dir2)

# os.mkdir(path2)
# print("Directory '% s' created" % dir2)
parentDir = "/Users/RynoMeiboom/Desktop/Testfiles"
jufDir = "/Users/RynoMeiboom/Desktop/Testfiles/Juf"
restDir = "/Users/RynoMeiboom/Desktop/Testfiles/Rest"


def moveFilesToDir(parentDir, dir1, dir2, files):
    for file in files:
        if "7" in file and "txt" in file:
            shutil.move(f"{parentDir}/{file}", dir1)
            print(f"all files containing '7' has been moved to {jufDir}")
        elif "txt" in file:
            shutil.move(f"{parentDir}/{file}", dir2)
            print(f"all files not containing '7' has been moved to {jufDir}")


moveFilesToDir(parentDir, jufDir, restDir, checkDirectory())
