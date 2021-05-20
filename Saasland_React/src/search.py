#basic imports
import os, sys, shutil

#simple function which parses and adds information based on the respective media query
def MediaQueryGenerator(x):
    if(1<=x<=7):
        return "@media(min-width:2000px){\n"
    elif(9<=x<=44):
        return "@media(max-width:1650px){\n"
    elif(47<=x<=175):
        return "@media(max-width:1550px){\n"
    elif(179<=x<=366):
        return "@media(max-width:1450px){\n"
    elif(369<=x<=408):
        return "@media(max-width:1350px){\n"
    elif(411<=x<=1280):
        return "@media(max-width:1199px){\n"
    elif(1283<=x<=2742):
        return "@media(max-width:991px){\n"
    elif(2745<=x<=3543):
        return "@media(max-width:768px){\n"
    elif(3546<=x<=3940):
        return "@media(max-width:650px){\n"
    elif(3943<=x<=4774):
        return "@media(max-width:576px){\n"
    elif(4777<=x<=4884):
        return "@media(max-width:480px){\n"
    elif(4887<=x<=5116):
        return "@media(max-width:450px){\n"
    elif(5119<=x<=5124):
        return "@media(max-width:420px){\n"
    elif(5127<=x<=5136):
        return "@media(max-width:400px){\n"

def main():
    # preps the all the initial values that will be used
    dir_path = os.path.dirname(os.path.realpath(__file__))
    inputFile = sys.argv[1]
    # inputFile = "AgencyAction.js" #TEST INPUT THAT MUST BE COMMENTED OUT
    outputDir = ""
    filePath = "mt"
    mainStyle = "mt"
    responseStyle = "mt"
    animateStyle = "mt"

    #for loop which processes the repository for basic file paths necessary for the code to work
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if(file == "output.css"):
                outputPath = root + "/"
                print("Dir Found: " + outputPath)
            if(file == inputFile):
                filePath = root+'/'+str(file)
                print("File Found: " + filePath)
            elif(file == "main.css"):
                mainStyle = root+'/'+str(file)
                print("File Found: " + mainStyle)
            elif(file == "animate.css"):
                animateStyle = root+'/'+str(file)
                print("File Found: " + animateStyle)
            elif(file == "responsive.css"):
                responseStyle = root+'/'+str(file)
                print("File Found: " + responseStyle)

    # error if files can't be found
    if(filePath == "mt" or mainStyle == "mt" or responseStyle == "mt" or animateStyle == "mt"):
        print("File(s) Not Found")
        sys.exit()

    print("--------------------------")
    print("Class Indexes")
    print("--------------------------")

    # This Code Block Parses the the component className strings into a string to search the css
    f = open(filePath)
    file_contents = f.readlines()
    f.close()
    classArray = []
    for line in file_contents:
        indexTargetFile = line.find("className=\"")
        if (indexTargetFile != -1):
            indexTargetFile = indexTargetFile + 11
            classstr = line[indexTargetFile:]
            classstr = classstr[:classstr.find("\"")]
            subclass = classstr.split(" ")
            # print(subclass)
            for item in subclass:
                classArray.append(item)


    #print(classArray)
    print("--------------------------")
    print("Line Numbers in main.css")
    print("line#: class utilized")
    print("--------------------------")

    # codeblock which opens all of css files and reads them into arrays line by line
    f = open(mainStyle)
    file_contents1 = f.readlines()
    f.close()

    f = open(responseStyle)
    file_contents2 = f.readlines()
    f.close()

    f = open(animateStyle)
    file_contents3 = f.readlines()
    f.close()

    outputArray = []

    # main for loop which searches item by item in the class array if a tag is found
    # will copy all files and paste them into an outputArray if found
    # 
    for item in classArray:
        nonEmptyOutput = False
        print("--------------------------")
        print("Class being searched: " + item)
        print("--------------------------")

        print("----------main.css----------")
        classFound = False
        for index,  line in enumerate(file_contents1):
            
            if(line.find("."+item) != -1):
                nonEmptyOutput = True
                classFound = True

                outputArray.append(line)
                print(str(index) + ": " + line[:len(line)-1])
            elif(line.find("}") == -1 and classFound == True):
                outputArray.append(line)
                print(str(index) + ": " + line[:len(line)-1])
            elif(line.find("}") != -1 and classFound == True):
                outputArray.append(line)
                print(str(index) + ": " + line[:len(line)-1])
                classFound = False
        
        if(nonEmptyOutput == False):
            print("------------------------------NO CLASSES FOUND in main.css-----------------------")

        nonEmptyOutput = False
        print("----------response.css----------")
        classFound = False
        for index,  line in enumerate(file_contents2):
            #print(line.find("."+item))
            if(line.find("."+item) != -1):
                nonEmptyOutput = True
                classFound = True
                mediaQuery = MediaQueryGenerator(index)
                outputArray.append(mediaQuery)
                print(mediaQuery, index , line)
                print(str(index) + ": " + mediaQuery[:len(mediaQuery)-1])
                outputArray.append(line)
                print(str(index) + ": " + line[:len(line)-1])

            elif(line.find("}") == -1 and classFound == True):
                outputArray.append(line)
                print(str(index) + ": " + line[:len(line)-1])

            elif(line.find("}") != -1 and classFound == True):
                outputArray.append(line)
                print(str(index) + ": " + line[:len(line)-1])
                outputArray.append(line)
                print(str(index) + ": " + line[:len(line)-1])
                classFound = False
        
        if(nonEmptyOutput == False):
            print("------------------------------NO CLASSES FOUND in response.css-----------------------")

        nonEmptyOutput = False
        print("----------animate.css----------")
        classFound = False
        for index,  line in enumerate(file_contents3):
            
            if(line.find("."+item) != -1):
                nonEmptyOutput = True
                classFound = True
                outputArray.append(line)
                print(str(index) + ": " + line[:len(line)-1])
            elif(line.find("}") == -1 and classFound == True):
                outputArray.append(line)
                print(str(index) + ": " + line[:len(line)-1])
            elif(line.find("}") != -1 and classFound == True):
                outputArray.append(line)
                print(str(index) + ": " + line[:len(line)-1])
                classFound = False
        
        if(nonEmptyOutput == False):
            print("------------------------------NO CLASSES FOUND in animate.css-----------------------")

        print("-------------------------------------------")

    #join all the outputs into a single string, prepare the output file, and present final information
    test = "".join(outputArray)
    f=open('output/output.css', 'w')
    f.write(test)
    shutil.copy(filePath, outputPath)
    print("The output is complete!\n The accompanying Component file is found at"+ filePath)
    f.close()

main()