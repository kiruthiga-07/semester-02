#1
class Password:
    def __init__(self,password):
        self.password=password
    def validatepassword(self):
        if not any(char.isupper() for char in self.password):
            print("Password must contain atleast 1 upper case letter")
        elif not any(char.islower() for char in self.password):
            print("Password must contain atleast 1 lowercase letter")
        elif not any(char.isdigit() for char in self.password):
            print("Password must contain atleast 1 digit")
        elif not any(char in "!@#$%^&*()<>|?" for char in self.password):
            print("Password must contain atleast 1 special character")
        elif len(self.password)<8:
            print("Password must be atlest 8 characters long")
        else:
            print("Password is valid")
user_password=input("Enter your password: ")
pw=Password(user_password)
pw.validatepassword()



#2
class TextProcessor:
    def __init__(self,text):
        self.text=text
    def split_into_sentence(self):
        sentences=[]
        sentence=""
        for char in self.text:
            sentence+=char
            if char in ".!?":
                sentences.append(sentence.strip())
                sentence=""
        return sentences
    def process_sentence(self):
        sentences=self.split_into_sentence()
        print("Processed Sentence Data:")
        for sentence in sentences:
            word_c=len(sentence.split())
            print(f"Sentence: {sentence},Word Count: {word_c}")
para=input("Enter your paragraph: ")
t=TextProcessor(para)
print("Split Sentences")
sentences=t.split_into_sentence()
for sentence in sentences:
    print(f"{sentence}")
t.process_sentence()

#
class Password:
    def __init__(self,password):
        self.password=password
    def validatepassword(self):
        if not self.password[0].isupper():
            print("1st letter of the password must be uppercase")
            if not any(char.islower() for char in self.password):
                print("Password must contain atleast 1 lowercase letter")
                if not any(char.isdigit() for char in self.password):
                    print("Password must contain atleast 1 digit")
                    if not any(char in "!@#$%^&*()<>|?" for char in self.password):
                        print("Password must contain atleast 1 special character")
                        if len(self.password)<8:
                            print("Password must be atlest 8 characters long")
        else:
            print("Password is valid")
user_password=input("Enter your password: ")
pw=Password(user_password)
pw.validatepassword()


