import mgame_manager.settings as ms
import mgame_manager.functions as mf

from mcreature.creature_manager import CreatureManager

from mcreature.mplayer.player_manager import PlayerManager
from mcreature.mplayer.player import Player

from mcreature.mrobot.robot_manager import RobotManager
from mcreature.mrobot.robot import Robot

from mcreature.mcreature_items.mcreature_health_bar.creature_health_bar_manager import CreatureHealthBarManager
from mcreature.mcreature_items.mcreature_health_bar.creature_health_bar import CreatureHealthBar

from mweapon.weapon import Weapon
from mweapon.weapon_manager import WeaponManager

from mscreen.screen import Screen

mf.start_game()
temp = Player(
    name="aa",
    health=100,
    power=100,
    defense=100,
    speed=8,
    width=100,
    height=100,
    x=100,
    y=400,
    jumpSize=100,
    playerType="gravity"
)

wtemp = Weapon(
    name="bb",
    power=100,
    width=50,
    height=50,
    x=100,
    y=100
)

rtemp = Robot(
    name="cc",
    health=100,
    power=100,
    defense=100,
    speed=10,
    width=100,
    height=100,
    x=540,
    y=270,
    jumpSize=3
)

hitemp = CreatureHealthBar(temp, 100, 40)

pm = PlayerManager()
pm.add_player(temp)
rm = RobotManager()
rm.add_robot(rtemp)
wm = WeaponManager()
wm.add_weapon(wtemp)
game_screen = Screen()
him = CreatureHealthBarManager()
him.add_healthBar(hitemp)

while ms.running:
    mf.is_QUIT()

    game_screen.screen_fill(ms.screen)
    
    pm.update_player(game_screen)
    pm.draw_player(ms.screen)
    wm.update_weapon(temp)
    wm.draw_weapon(ms.screen)
    rm.update_robot(temp)
    rm.draw_robot(ms.screen)
    him.update_healthBar()
    him.draw_healthBar(ms.screen)

    mf.update(ms.screen)

# 파이게임 종료
mf.end_game()