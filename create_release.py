import subprocess

#Validation 1: Working tree must be clean. #(I'm really liking this format of validations via comments.)
git_status_porcelain_subprocess = subprocess.Popen("git status --porcelain", shell=True, stdout=subprocess.PIPE) #Exactly, exactly what we need.
working_tree_contents = git_status_porcelain_subprocess.stdout.readline().strip().decode("ascii")
if working_tree_contents: #i.e. it is not clean.
    print("The working tree is not empty (clean). I cannot continue with your request of building CreateAnims. Please, revise and let me know.") #This is intended for me so yeah print to the console.
    exit(999) #After Tkinter's experience, I'm kinda preferring using sys. Ah but wait. This is pure Python so arghh... whatever, like the old times.