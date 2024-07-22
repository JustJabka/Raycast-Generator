distance = int(input("Enter the ray length (in blocks): "))
step = float(input("Enter the ray step: "))
block = str(input("Enter the block that will be the target of the ray: "))
function = str(input("Enter the command to be run after the target block is found: "))
def raycast_in_line(question):
    while True:
        answer = str(input(question)).strip().lower()
        if answer == "y" or raycast_in_line == "yes":
             return True
        elif answer == "n" or raycast_in_line == "no":
             return False
        else:
             print("Enter Yes or No")
def generate_ray_steps(distance, step, block):
    steps = [f"\033[34munless block \033[32m^ ^ ^ \033[33m{block}"]
    for i in range(1, int(distance / step) + 1):
        current_position = round(i * step, 2)
        steps.append(f"\033[34munless block \033[32m^ ^ ^{current_position} \033[33m{block}")
    steps.append("\033[34mrun \033[35mreturn \033[34mfail")
    return " ".join(steps)
if raycast_in_line("Will there be a raycast in the line (Y/N): "):
      steps = generate_ray_steps(distance, step, block)
      result = (
                "\033[0mtick.mcfunction\n"
                "\033[35mexecute \033[34mas \033[36m@a \033[34mat \033[36m@s \033[34mif \033[35mfunction \033[33mnamespace:raycast/pre \033[0mrun \033[35mfunction \033[33mnamespace:raycast/start\n\n"
                "\033[0mraycast/pre.mcfunction\n"
                f"\033[35mexecute \033[34manchored eyes positioned \033[32m^ ^ ^ {steps}\n"
                "\033[35mreturn \033[32m1\n\n"
                "\033[0mraycast/start.mcfunction\n"
                f"\033[35mscoreboard \033[34mplayers set \033[36m#distance \033[0mmain_score \033[32m{distance*5}\n"
                "\033[35mexecute \033[34manchored eyes positioned \033[32m^ ^ ^ \033[34mrun \033[35mfunction \033[33mnamespace:raycast/main\n\n"
                "\033[0mraycast/main.mcfunction\n"
                "\033[35mscoreboard \033[34mplayers remove \033[36m#distance \033[0mmain_score \033[32m1\n"
                "\033[35mexecute \033[34munless block \033[32m~ ~ ~ \033[33m#namespace:raycast_ignored \033[34mrun \033[35mfunction \033[33mnamespace:raycast/end\n"
                f"\033[35mexecute \033[34mif score \033[36m#distance \033[0mmain_score \033[34mmatches \033[32m1\033[35m.. \033[34mpositioned \033[32m^ ^ ^{step} \033[34mrun \033[35mfunction \033[33mnamespace:raycast/main\n\n"
                "\033[0mraycast/end.mcfunction\n"
                f"\033[35mexecute \033[34mif block \033[32m~ ~ ~ \033[33m{block} \033[34mrun \033[0m{function}\n"
                "\033[35mscoreboard \033[34mplayers set \033[36m#distance \033[0mmain_score \033[32m0\n\n\n"
                "\033[0m"
        )
else:
     result = (
                "\033[0mraycast/start.mcfunction\n"
                f"\033[35mscoreboard \033[34mplayers set \033[36m#distance \033[0mmain_score \033[32m{distance*5}\n"
                "\033[35mexecute \033[34manchored eyes positioned \033[32m^ ^ ^ \033[34mrun \033[35mfunction \033[33mnamespace:raycast/main\n\n"
                "\033[0mraycast/main.mcfunction\n"
                "\033[35mscoreboard \033[34mplayers remove \033[36m#distance \033[0mmain_score \033[32m1\n"
                "\033[35mexecute \033[34munless block \033[32m~ ~ ~ \033[33m#namespace:raycast_ignored \033[34mrun \033[35mfunction \033[33mnamespace:raycast/end\n"
                f"\033[35mexecute \033[34mif score \033[36m#distance \033[0mmain_score \033[34mmatches \033[32m1\033[35m.. \033[34mpositioned \033[32m^ ^ ^{step} \033[34mrun \033[35mfunction \033[33mnamespace:raycast/main\n\n"
                "\033[0mraycast/end.mcfunction\n"
                f"\033[35mexecute \033[34mif block \033[32m~ ~ ~ \033[33m{block} \033[34mrun \033[0m{function}\n"
                "\033[35mscoreboard \033[34mplayers set \033[36m#distance \033[0mmain_score \033[32m0\n\n\n"
                "\033[0m"
        )
print(f"\n\n\n{result}")
input("< Press ENTER to quit >")
