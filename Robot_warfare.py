# This method select the component of robot to show if is available

from time import sleep

def make_shield_art(robot_parts: dict):
    if robot_parts["shield_status"]:
        return r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⠀⠀⠀⠀⠀⠀    |7: {shield_name}
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀    |Is available: {shield_status}
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀-------> |Is active: {shield_active}
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀    |Available use: {shield_use}
⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀         |Defense: {shield_defense}
⠀⠀⠀ ⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃   ⠀⠀⠀     |Energy consumption: {shield_energy_consump}
⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    else:
        return ""

def select_upper_body(robot_parts: dict):
    if robot_parts["head_status"] and robot_parts["weapon_status"]:
        return r"""
             1: {head_name}
             Is available: {head_status}
             Attack: {head_attack}                              
             Defense: {head_defense}
             Energy consumption: {head_energy_consump}
                      ^
                      |                  |2: {weapon_name}
                      |                  |Is available: {weapon_status}
             ____     |    ____          |Attack: {weapon_attack}
            |oooo|  ____  |oooo| ------> |Defense: {weapon_defense}
            |oooo| '    ' |oooo|         |Available use: {weapon_use}
            |oooo|/\_||_/\|oooo|         |Energy consumption: {weapon_energy_consump}"""

    elif not robot_parts["head_status"] and robot_parts["weapon_status"]:
        return r"""         
                                         |2: {weapon_name}
                                         |Is available: {weapon_status}
             ____          ____          |Attack: {weapon_attack}
            |oooo|        |oooo| ------> |Defense: {weapon_defense}
            |oooo|        |oooo|         |Available use: {weapon_use}
            |oooo|        |oooo|         |Energy consumption: {weapon_energy_consump}"""

    elif not robot_parts["weapon_status"] and robot_parts["head_status"]:
        return r"""
             1: {head_name}
             Is available: {head_status}
             Attack: {head_attack}                              
             Defense: {head_defense}
             Energy consumption: {head_energy_consump}
                      ^
                      |                  
                      |                  
                      |                  
                    ____          
                   '    '                
                  /\_||_/\      """
    else:
        return """

        """

def select_body(robot_parts: dict):
    if robot_parts["left_arm_status"] and robot_parts["right_arm_status"]:
        return r"""                    
            `----' / __ \  `----'           |3: {left_arm_name}
           '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
           /  \|#|| |/\| ||#|/  \           |Attack: {left_arm_attack}
          / \_/|_|| |/\| ||_|\_/ \          |Defense: {left_arm_defense}
         |_\/    O\=----=/O    \/_|         |Energy consumption: {left_arm_energy_consump}
         <_>      |=\__/=|      <_> ------> |
         <_>      |------|      <_>         |4: {right_arm_name}
         | |   ___|======|___   | |         |Is available: {right_arm_status}
        // \\ / |O|======|O| \  //\\        |Attack: {right_arm_attack}
        |  |  | |O+------+O| |  |  |        |Defense: {right_arm_defense}
        |\/|  \_+/        \+_/  |\/|        |Energy consumption: {right_arm_energy_consump}
        \__/  _|||        |||_  \__/       
              | ||        | ||"""

    elif not robot_parts["left_arm_status"] and robot_parts["right_arm_status"]:
        return r"""
            `----' / __ \  `----'           
               |#|/\/__\/\|#|  \'           
               |#|| |/\| ||#|/  \           
               |_|| |/\| ||_|\_/ \          |4: {right_arm_name}
                 O\=----=/O    \/_|         |Is available: {right_arm_status}
                  |=\__/=|      <_> ------> |Attack: {right_arm_attack}
                  |------|      <_>         |Defense: {right_arm_defense}
               ___|======|___   | |         |Energy consumption: {right_arm_energy_consump}
              / |O|======|O| \  //\\        
              | |O+------+O| |  |  |        
              \_+/        \+_/  |\/|        
              _|||        |||_  \__/        
              | ||        | ||"""
    elif robot_parts["left_arm_status"] and not robot_parts["right_arm_status"]:
        return r"""
            `----' / __ \  `----'           
           '/  |#|/\/__\/\|#|               
           /  \|#|| |/\| ||#|               
          / \_/|_|| |/\| ||_|               |3: {left_arm_name}
         |_\/    O\=----=/O                 |Is available: {left_arm_status}
         <_>      |=\__/=|          ------> |Attack: {left_arm_attack}
         <_>      |------|                  |Defense: {left_arm_defense}
         | |   ___|======|___               |Energy consumption: {left_arm_energy_consump}
        // \\ / |O|======|O| \              
        |  |  | |O+------+O| |              
        |\/|  \_+/        \+_/              
        \__/  _|||        |||_              
              | ||        || |"""
    else:
        return rf"""
            `----' / __ \  `----'           
               |#|/\/__\/\|#|               
               |#|| |/\| ||#|               
               |_|| |/\| ||_|               
                 O\=----=/O                 
                  |=\__/=|           
                  |------|                  
               ___|======|___               
              / |O|======|O| \              
              | |O+------+O| |              
              \_+/        \+_/              
              _|||        |||_              
              | ||        || |
"""

def select_bottom_body(robot_parts: dict):
    if robot_parts["left_leg_status"] and robot_parts["right_leg_status"]:
        return r"""
             [==|]        [|==]         |5: {left_leg_name}
             [===]        [===]         |Is available: {left_leg_status} 
              >_<          >_<          |Attack: {left_leg_attack}
             || ||        || ||         |Defense: {left_leg_defense}
             || ||        || || ------> |Energy consumption: {left_leg_energy_consump}
             || ||        || ||         |
           __|\_/|__    __|\_/|__       |6: {right_leg_name}
          /___n_n___\  /___n_n___\      |Is available: {right_leg_status}
                                        |Attack: {right_leg_attack}
                                        |Defense: {right_leg_defense}
                                        |Energy consumption: {right_leg_energy_consump}


        """
    elif not robot_parts["left_leg_status"] and robot_parts["right_leg_status"]:
        return r"""
                          || |           
                          [|==]         
                          [===]         
                           >_<          |6: {right_leg_name}
                          || ||         |Is available: {right_leg_status}
                          || || ------> |Attack: {right_leg_attack}
                          || ||         |Defense: {right_leg_defense}
                        __|\_/|__       |Energy consumption: {right_leg_energy_consump}
                       /___n_n___\      
        """
    elif robot_parts["left_leg_status"] and not robot_parts["right_leg_status"]:
        return r"""
              | ||                       
             [==|]                      
             [===]                      
              >_<                       |5: {left_leg_name}
             || ||                      |Is available: {left_leg_status}
             || ||              ------> |Attack: {left_leg_attack}
             || ||                      |Defense: {left_leg_defense}
           __|\_/|__                    |Energy consumption: {left_leg_energy_consump}
          /___n_n___\                   
          
        """
    return "\n\n"

class Parts:
    def __init__(self, name: str, attack: int, defense: int, energy_consumption: int, is_special=False, selector='',
                 is_shield=False):
        self.name = name
        self.is_available = True
        self.is_special = is_special
        self.available_usability = 2
        self.attack = attack
        self.defense = defense
        self.energy_consumption = energy_consumption
        self.selector = selector
        self.is_shield = is_shield
        self.is_active_shield = False

    def get_status_dict(self):
        return {
            f"{self.selector}_name": self.name.capitalize().strip(),
            f"{self.selector}_status": self.is_available,
            f"{self.selector}_attack": self.attack,
            f"{self.selector}_defense": self.defense,
            f"{self.selector}_energy_consump": self.energy_consumption,
            f"{self.selector}_use": self.available_usability,
            f"{self.selector}_active": self.is_active_shield
        }

    def set_status(self, status: bool):
        self.is_available = status

    def decrease_usability(self):
        self.available_usability -= 1
        if self.available_usability <= 0:
            self.is_available = False

    def decrease_defense(self, decrease: int):
        self.defense -= decrease
        if self.defense <= 0:
            self.is_available = False

    def get_attack(self):
        return self.attack

    def active_shield(self, value=True):
        if value:
            self.decrease_usability()
        self.is_active_shield = value

class Robot:
    colors = {
        "black": '\x1b[90m',
        "blue": '\x1b[94m',
        "cyan": '\x1b[96m',
        "green": '\x1b[92m',
        "magenta": '\x1b[95m',
        "red": '\x1b[91m',
        "white": '\x1b[97m',
        "yellow": '\x1b[93m',
    }

    stop_color = '\x1b[0m'

    colors_options = {}

    parts_options = {}

    def __init__(self, name_player: str, robot_name: str, default_robot_color: str = "blue"):
        for index, color in enumerate(self.colors):
            self.colors_options[index + 1] = color

        self.parts = {
            "head": Parts(name="Head", attack=15, defense=30, energy_consumption=10, selector="head"),
            "weapon": Parts(name="Missile Launcher", attack=90, defense=45, energy_consumption=90, is_special=True, selector="weapon"),
            "left_arm": Parts(name="Left Arm", attack=18, defense=38, energy_consumption=18, selector="left_arm"),
            "right_arm": Parts(name="Right Arm", attack=18, defense=38, energy_consumption=18, selector="right_arm"),
            "left_leg": Parts(name="Left Leg", attack=20, defense=40, energy_consumption=20, selector="left_leg"),
            "right_leg": Parts(name="Right Leg", attack=20, defense=40, energy_consumption=20, selector="right_leg"),
            "shield": Parts(name="Shield", attack=0, defense=60, is_shield=True, is_special=True, energy_consumption=50,selector="shield")
        }

        for index, part in enumerate(self.parts.values()):
            self.parts_options[index + 1] = part.selector

        self.player = {
            "name": name_player
        }

        self.robot = {
            "name": robot_name,
            "parts": self.parts,
            "energy": 100,
            "color": default_robot_color
        }

    def say_hi(self):
        print(
            f"\n{self.colors[self.robot['color']]}hello, i'm {self.robot['name']} and my boss is {self.player['name']}{self.stop_color}")

    def is_available_part(self, part: int) -> bool:
        if self.robot["parts"]["shield"].is_active_shield:
            return part == 7

        try:
            return self.robot["parts"][self.parts_options[part]].is_available
        except:
            return False

    def is_all_parts_not_available(self):
        parts_available = []

        for part in self.robot["parts"].values():
            parts_available.append(part.is_available)

        return not (True in parts_available)

    def is_on(self) -> bool:
        return self.robot["energy"] > 0

    def show_energy(self) -> None:
        energy = self.robot["energy"]

        color: str

        if energy >= 150:
            color = self.colors["green"]
        elif 50 <= energy < 150:
            color = self.colors["yellow"]
        else:
            color = self.colors["red"]
            print(self.colors["yellow"] + "A L E R T!".center(65))

        print(color + "=" * 65)
        print(f"{energy}% of energy".center(65))
        print("=" * 65 + self.stop_color)

    def show_parts_options(self, title="PARTS AVAILABLE"):
        message = f"\n{title}\n\n"

        if self.robot["parts"]["shield"].is_active_shield:
            return print(message + f"{self.colors[self.robot['color']]}7 : shield{self.stop_color}\n")

        for index, part in enumerate(self.parts.values()):
            if part.is_available:
                message += f"[ {index + 1} ] {self.colors[self.robot['color']]} {part.name}{self.stop_color}\n"

        print(message)

    def get_all_parts(self) -> dict:
        all_parts = {}

        for i in self.parts.values():
            all_parts.update(i.get_status_dict())

        return all_parts

    def show_robot(self):
        all_parts = self.get_all_parts()
        print((self.colors[self.robot["color"]] +
               select_upper_body(all_parts) +
               select_body(all_parts) +
               select_bottom_body(all_parts) +
               make_shield_art(all_parts) + self.stop_color).format(**all_parts))

    def decrease_energy(self, decrease: int):
        self.robot["energy"] -= decrease

    def decrease_part_defense(self, part: int, decrease: int):
        self.robot["parts"][self.parts_options[part]].decrease_defense(decrease)

    def decrease_part_usability(self, part: int):
        self.robot["parts"][self.parts_options[part]].decrease_usability()

    def show_color_options(self):
        message = f"\n\nAVAILABLE COLORS\n{'-' * 16}\n"

        colors_options_values = self.colors_options.values()
        for index, color in enumerate(colors_options_values):
            message += f"[ {index + 1} ] {self.colors[color]} {color.capitalize()}{self.stop_color}\n"

        print(message)

    def set_color(self, color_number: int):
        if color_number not in self.colors_options.keys():
            raise Exception("Invalid color")

        self.robot['color'] = self.colors_options[color_number]

    def get_part(self, part: int):
        return self.robot["parts"][self.parts_options[part]]

    def get_part_attack(self, part: int) -> int:
        return self.robot["parts"][self.parts_options[part]].get_attack()

    def active_shield(self, active: bool = True):
        self.robot["parts"]["shield"].active_shield(active)

    def is_active_shield(self):
        return self.robot["parts"]["shield"].is_active_shield

    def is_special_part(self, part: int):
        return self.robot["parts"][self.parts_options[part]].is_special

def config_robot() -> Robot:
    name = input("Player name: ")
    robot_name = input("Your robot name: ")

    robot = Robot(name_player=name, robot_name=robot_name)

    robot.show_color_options()
    color = int(input("Your robot color: "))
    robot.set_color(color)

    return robot

def start():
    def initial(robot: Robot):
        robot.say_hi()
        robot.show_robot()

    def check_winner(robot_1: Robot, robot_2: Robot):
        robot_1_win = f"\n\nNice {robot_1.player['name']}, your robot {robot_1.robot['name']} won this game"
        robot_2_win = f"\n\nNice {robot_2.player['name']}, your robot {robot_2.robot['name']} won this game"

        if not robot_1.is_on():
            print(robot_2_win)
            return True
        elif not robot_2.is_on():
            print(robot_1_win)
            return True
        elif robot_1.is_all_parts_not_available():
            print(robot_2_win)
            return True
        elif robot_2.is_all_parts_not_available():
            print(robot_1_win)
            return True
        return False

    print("Player 1 Configurations")
    robot_1 = config_robot()
    initial(robot_1)

    print("Player 2 Configurations")
    robot_2 = config_robot()
    initial(robot_2)

    sleep(1)
    while True:
        fight(robot=robot_1, enemy=robot_2, player_number=1)
        if check_winner(robot_1, robot_2):
            break
        fight(robot=robot_2, enemy=robot_1, player_number=2)
        if check_winner(robot_1, robot_2):
            break

def fight(robot: Robot, enemy: Robot, player_number: int):
    print(f"\n\n== Player {player_number} fight ==\n\n")
    if robot.is_active_shield():
        robot.active_shield(False)
    robot.show_robot()
    robot.show_energy()
    robot.show_parts_options()
    while True:
        part_to_use = int(input("Select one part to fight: (or use the shield) "))
        if not robot.is_available_part(part=part_to_use):
            print("You can't use that part, it is not available!")
        else:
            break

    if part_to_use == 7:
        robot.active_shield(True)
        print("SHIELD ACTIVATED FOR 1 ROUND")
        sleep(2)
        return

    print("\nChoose enemy part to attack")

    enemy.show_parts_options()
    while True:
        enemy_part_to_attack = int(input("Select enemy part to attack: "))
        if not enemy.is_available_part(part=enemy_part_to_attack):
            print("You can't attack this part, it is not available!")
        else:
            break

    attack = robot.get_part_attack(part_to_use)
    robot.decrease_energy(robot.get_part(part_to_use).energy_consumption)
    print(robot.is_special_part(part_to_use))
    if robot.is_special_part(part_to_use):
        robot.decrease_part_usability(part_to_use)
    enemy.decrease_part_defense(decrease=attack, part=enemy_part_to_attack)

start()