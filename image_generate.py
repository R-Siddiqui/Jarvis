from os import system, listdir

cookies = "12oAAdVFd_QDsD9VxVaZwJAQ9AIIZud5lLlRF2xJeU9pxoxe_E2r-UcQxqrDIGvetvq8sfHR2jAFwvYggG2sBKIq_yRBDgVBaZo1ZG0CSAWtXSgxgUyVbvCJKLeKqWyYzh6ZrduUrz1d9zk5LENUJDaBeovD6y_bf5mNU-g_qrfaFMk6frOu0NNVmeJYHbnc2v6SPbN_5vXjomCQajP8BNQ"

def generate_img(prompt):
    cammond = f'python -m BingImageCreator --prompt "{prompt}" -U "{cookies}"'
    system(cammond)

    return listdir('output')
generate_img('create a horse, 3d render')