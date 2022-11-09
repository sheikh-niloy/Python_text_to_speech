from gtts import gTTS
import os
num = 100000000000000
for i in range(num):
    myText = input("Say What You Want To Hear: ")
    if myText== "restart.all.files": 
        os.remove(f"output{i}.mp3")
    language = 'en'


#extra loop/while

    output = gTTS(text=myText, lang=language, slow=False)
    if myText!= "restart.all.files": 
        output.save(f"output{i}.mp3")
    elif myText== "restart.all.files": 
        output.save(f"output{i}.mp3")     
        pass

    if myText!= "restart": 
        os.system(f"output{i}.mp3")
       
    elif myText== "restart.all.files": 
        os.system(f"output{i}.mp3")     
        pass

    