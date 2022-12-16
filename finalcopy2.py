import sys


class Doctor:

    def __init__(self):
        self.ID = 0
        self.name = ''
        self.specialization = ''
        self.timing = ''
        self.qualification = ''
        self.roomNumber = 0

    def formatDrInfo(self, docInfo):
        formattedDocInfo = "_".join(docInfo)
        return formattedDocInfo

    def enterDrInfo(self):
        docInfoList = []
        infoRequired = ['Enter the doctor\'s ID: ',
                        'Enter the doctor\'s name: ', 'Enter the doctor\'s specility: ', 'Enter the doctor\'s timing (e.g., 7am-10pm): ', 'Enter the doctor\'s qualification: ', 'Enter the doctor\'s room number: ']
        for i in infoRequired:
            userInput = input(i)
            docInfoList.append(userInput)

        return docInfoList

    def readDoctorsFile(self):
        docFilePath = './files/doctors.txt'
        try:
            docFile = open(docFilePath, 'r')
            docFileContent = docFile.read()
            # Splitting file into list
            docList = docFileContent.split('\n')
            # Slicing the list to ignore the first line
            # docList = docList[1:]
            docFile.close()
            return docList
        except:
            print('Something went wrong in reading Reading Doctor file.!!')

    def searchDoctorById(self):
        try:

            docId = input("Enter ID of doctor: ")
            doctorsList = self.readDoctorsFile()
            for doctor in doctorsList:
                docSplit = doctor.split('_')
                # Finding the doctor using id (first element in docSplit list)
                if (docId == docSplit[0]):
                    for docInfo in (doctorsList[0].split('_')):
                        print(f"{docInfo.ljust(20)}", end="")
                    print()
                    for docInfo in docSplit:
                        print(f"{docInfo.ljust(20)}", end="")
                    break
            else:
                print("Can't find the doctor with the same ID on the system")
        except:
            print("Input is invalid!! or Something went wrong!!")
            self.searchDoctorById()

    def searchDoctorByName(self):
        try:

            docName = input("Enter full-name of doctor: ")
            doctorsList = self.readDoctorsFile()
            for doctor in doctorsList:
                docSplit = doctor.split('_')
                # Finding the doctor using name (second element in docSplit list)
                if (docName == docSplit[1]):
                    for docInfo in (doctorsList[0].split('_')):
                        print(f"{docInfo.ljust(20)}", end="")
                    print()
                    for docInfo in docSplit:
                        print(f"{docInfo.ljust(20)}", end="")
                    break
            else:
                print("Can't find the doctor with the same NAME on the system")

        except:
            print("Input is invalid!! or Something went wrong!!")
            self.searchDoctorByName()

    def displayDoctorsList(self):
        doctorsList = self.readDoctorsFile()

        for doctor in doctorsList:
            docSplit = doctor.split('_')
            for docInfo in docSplit:
                print(f"{docInfo.ljust(20)}", end="")
            print()

    def writeListOfDoctorsToFile(self, docList):
        docFilePath = './files/doctors.txt'
        docFile = open(docFilePath, 'w')
        docListJoined = '\n'.join(docList)
        docFile.write(docListJoined)
        docFile.close()

    def addDrToFile(self):
        docInfoList = self.enterDrInfo()

        formattedDoc = self.formatDrInfo(docInfoList)

        doctorsList = self.readDoctorsFile()
        doctorsList.append(formattedDoc)

        self.writeListOfDoctorsToFile(doctorsList)

    def editDoctorInfo(self):
        print("Please enter the id of the doctor that you want to edit their information: ")
        userChoice = input()
        docInfoList = []
        infoRequired = ['Enter new Name: ',
                        'Enter new Specilist in: ', 'Enter new Timing: ', 'Enter new Qualification: ', 'Enter new Room number: ']
        for i in infoRequired:
            userInput = input(i)
            docInfoList.append(userInput)

        docList = self.readDoctorsFile()

        for i in docList:
            docSplit = i.split('_')
            if docSplit[0] == userChoice:
                index = docList.index(i)

        docList[index] = docInfoList

        self.writeListOfDoctorsToFile(docList)


class Facility:
    def __init__(self):
        self.facilityName = ''

    def addFacility(self):
        print("Enter Facility name: ")
        userChoice = input()
        self.writeListOffacilitiesToFile(userChoice)

    def displayFacilities(self):
        try:
            facilitiesFile = open('./files/facilities.txt', 'r')
            print(facilitiesFile.read())
            print()
        except:
            print('Something went wrong in reading Reading file.!!')
            self.displayFacilities()

    def writeListOffacilitiesToFile(self, userChoice):
        facilitiesFile = open("./files/facilities.txt", "a")
        facilitiesFile.write(userChoice)


class Laboratory:
    def __init__(self):
        self.labName = ''
        self.cost = ''

    def addLabToFile(self):
        labInfoList = self.enterLaboratoryInfo()

        formattedlab = self.formatDrInfo(labInfoList)

        labsList = self.readLaboratoriesFile()
        labsList.append(formattedlab)

        self.writeListOfLabsToFile(labsList)

    def writeListOfLabsToFile(self, labList):
        labFilePath = './files/laboratories.txt'
        labFile = open(labFilePath, 'w')
        labListJoined = '\n'.join(labList)
        labFile.write(labListJoined)
        labFile.close()

    def displayLabsList(self):
        laboratoriesList = self.readLaboratoriesFile()
        for laboratory in laboratoriesList:
            laboratorySplit = laboratory.split('_')
            for labInfo in laboratorySplit:
                print(f"{labInfo.ljust(20)}", end="")
            print()

    def formatDrInfo(self, labInfo):
        formattedLabInfo = "_".join(labInfo)
        return formattedLabInfo

    def enterLaboratoryInfo(self):
        print("Enter Laboratory facility: ")
        facilityName = input()
        print("Enter Laboratory cost: ")
        facilityCost = input()
        return [facilityName, facilityCost]

    def readLaboratoriesFile(self):
        labFilePath = './files/laboratories.txt'
        try:
            labFile = open(labFilePath, 'r')
            labFileContent = labFile.read()
            # Splitting file into list
            labList = labFileContent.split('\n')
            # Slicing the list to ignore the first line
            # labList = labList[1:]
            labFile.close()
            return labList
        except:
            print('Something went wrong in reading Reading laboratories file.!!')


class Patient:
    def __init__(self):
        self.pid = ''
        self.name = ''
        self.disease = ''
        self.gender = ''
        self.age = ''

    def formatPatientInfo(self, patientInfo):
        formattedPatientInfo = "_".join(patientInfo)
        return formattedPatientInfo

    def enterPatientInfo(self):
        patientInfoList = []
        infoRequired = ['Enter Patient id: ', 'Enter Patient name: ',
                        'Enter Patient disease: ', 'Enter Patient gender: ', 'Enter Patient age: ']

        for i in infoRequired:
            userInput = input(i)
            patientInfoList.append(userInput)

        return patientInfoList

    def readPatientsFile(self):
        patientFilePath = './files/patients.txt'
        try:
            patientFile = open(patientFilePath, 'r')
            patientFileContent = patientFile.read()
            # Splitting file into list
            patientList = patientFileContent.split('\n')
            # Slicing the list to ignore the first line
            # patientList = patientList[1:]
            patientFile.close()
            return patientList
        except:
            print('Something went wrong in reading Reading patients file.!!')

    def searchPatientById(self):
        try:
            patientId = input("Enter ID of patient: ")
            patientsList = self.readPatientsFile()
            for patient in patientsList:
                patientSplit = patient.split('_')
                # Finding the doctor using id (first element in patientSplit list)
                if patientId == patientSplit[0]:
                    for patientInfo in (patientsList[0].split('_')):
                        print(f"{patientInfo.ljust(20)}", end="")
                    print()
                    for patientInfo in patientSplit:
                        print(f"{patientInfo.ljust(20)}", end="")
                    break
            else:
                print("Can't find the patient with the same ID on the system")
        except:
            print("Input is invalid!! or Something went wrong!!")
            self.searchPatientById()

    def displayPatientsList(self):
        patientsList = self.readPatientsFile()

        for patient in patientsList:
            patientSplit = patient.split('_')
            for patientInfo in patientSplit:
                print(f"{patientInfo.ljust(20)}", end="")
            print()

    def writeListOfPatientsToFile(self, patientList):
        patientFilePath = './files/patients.txt'
        patientFile = open(patientFilePath, 'w')
        patientListJoined = '\n'.join(patientList)
        patientFile.write(patientListJoined)
        patientFile.close()

    def addPatientToFile(self):
        patientInfoList = self.enterPatientInfo()

        formattedPatient = self.formatPatientInfo(patientInfoList)

        patientsList = self.readPatientsFile()
        patientsList.append(formattedPatient)

        self.writeListOfPatientsToFile(patientsList)

    def editPatientInfo(self):

        print(
            "Please enter the id of the Patient that you want to edit their information: ")
        userChoice = input()
        patientInfoList = []
        infoRequired = ['Enter new Name: ', 'Enter new disease: ',
                        'Enter new gender: ', 'Enter new age: ']
        for i in infoRequired:
            userInput = input(i)
            patientInfoList.append(userInput)

        patientList = self.readPatientsFile()

        for i in patientList:
            patientSplit = i.split('_')
            if patientSplit[0] == userChoice:
                index = patientList.index(i)

        patientList[index] = patientInfoList

        self.writeListOfPatientsToFile(patientList)


class Management:

    def __init__(self):
        pass

    def doctorMng(self):
        docMenu = f"Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n: "
        userDocChoice = input(docMenu)
        if (userDocChoice == '6'):
            self.displayMenu()
        else:
            doctorObj = Doctor()
            if userDocChoice == '1':
                doctorObj.displayDoctorsList()
            elif userDocChoice == '2':
                doctorObj.searchDoctorById()
            elif userDocChoice == '3':
                doctorObj.searchDoctorByName()
            elif userDocChoice == '4':
                doctorObj.addDrToFile()
            elif userDocChoice == '5':
                doctorObj.editDoctorInfo()
            print('Back to previous Menu')
            self.doctorMng()

    def facilityMng(self):
        facilityMenu = f"Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n: "
        userFacilityChoice = input(facilityMenu)
        if (userFacilityChoice == '3'):
            self.displayMenu()
        else:
            facilityObj = Facility()
            if userFacilityChoice == '1':
                facilityObj.displayFacilities()
            elif userFacilityChoice == '2':
                facilityObj.addFacility()

            print('Back to previous Menu')
            self.facilityMng()

    def laboratoryMng(self):
        labMenu = f"Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n: "
        userLabChoice = input(labMenu)
        if (userLabChoice == '3'):
            self.displayMenu()
        else:
            labObj = Laboratory()
            if userLabChoice == '1':
                labObj.displayLabsList()
            elif userLabChoice == '2':
                labObj.addLabToFile()

            print('Back to previous Menu')
            self.laboratoryMng()

    def patientMng(self):

        patientMenu = f"Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n: "
        userPatientChoice = input(patientMenu)
        if (userPatientChoice == '6'):
            self.displayMenu()
        else:
            patientObj = Patient()
            if userPatientChoice == '1':
                patientObj.displayPatientsList()
            elif userPatientChoice == '2':
                patientObj.searchPatientById()
            elif userPatientChoice == '3':
                patientObj.addPatientToFile()
            elif userPatientChoice == '4':
                patientObj.editPatientInfo()

            print('Back to previous Menu')
            self.patientMng()

    def displayMenu(self):
        menuString = f"Welcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 0 to stop: \n1 - 	Doctors\n2 - 	Facilities\n3 - 	Laboratories\n4 - 	Patients "
        try:
            userClassChoice = int(input(menuString+'\n'))
        except:
            print('Something went wrong! Try Again!')
            self.displayMenu()

        if userClassChoice == 1:
            # Doctors
            self.doctorMng()
            pass
        elif userClassChoice == 2:
            # Facilities
            self.facilityMng()
            pass
        elif userClassChoice == 3:
            # Laboratories
            self.laboratoryMng()
            pass
        elif userClassChoice == 4:
            # Patients
            self.patientMng()
        elif userClassChoice == 0:
            print("Thank you for using this program!! Visit Again!!")
            sys.exit()


def main():
    mng = Management()
    mng.displayMenu()


if __name__ == "__main__":
    main()
