# Search email files for specific phrases from particular sender
# Place email files in subfolder email

# Imports
from os import listdir
from os.path import isfile, join
from email.parser import BytesParser
from email import policy

# Initial values
emailPath = "./emails/"
options = []

# Edit these
emailSender = "sender@domain.com"
emailPhrases = ["phrase1", "phrase2"]

allEmails = [f for f in listdir(emailPath) if isfile(join(emailPath, f))]

def parseMails():
    print("Filename,", "Date Sent,", "Subject,", "Phrases Found,", "Phraselist", sep="\t\t")
    for eachMail in allEmails:
        with open(join(emailPath, eachMail), "rb") as emailFile:
            msg = BytesParser(policy=policy.default).parse(emailFile)
            sender = msg["From"]
            sentDate = msg["Date"]
            subject = msg["Subject"]
            # Lotus Notes will normally include previous messages in a thread
            # If the email containing the phrase you're looking for was replied to, it will appear multiple times
            # Switch if statements to exclude replies - if phrase wasn't in original email, it will be missed
            # if str(sender).lower() == emailSender.lower() and "Re" not in subject:
            if str(sender).lower() == emailSender.lower():
                totalPhrases = 0
                phrasesFound = []
                for phrase in emailPhrases:
                    for part in msg.walk():
                        testString = str(part).lower()
                        if phrase.lower() in testString:
                            totalPhrases += 1
                            phrasesFound.append(phrase)
                            break
                if totalPhrases > 1:
                    messageSummary = [eachMail, sentDate, subject, totalPhrases, phrasesFound]
                    options.append(messageSummary)
    for option in options:
        print(option)
        print("\n")


def main():
    parseMails()


main()
