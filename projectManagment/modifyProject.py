def modifyProject(controller, i):
    print("change to : ", i)
    try:
        with open('./common/data.txt', 'w') as file:
            file.write(str(i))
    except FileNotFoundError:
        with open('./common/data.txt', 'x') as file:
            file.write(str(i))

    controller.reload_creation()
    controller.show_frame("projectCreation")
