import mgame_manager.settings as ms
import mgame_manager.functions as mf

from mcreature.creature_manager import CreatureManager

from mcreature.mplayer.player_manager import PlayerManager
from mcreature.mplayer.player import Player

from mcreature.mrobot.robot_manager import RobotManager
from mcreature.mrobot.robot import Robot

from mcreature.mcreature_items.mcreature_health_bar.creature_health_bar_manager import CreatureHealthBarManager
from mcreature.mcreature_items.mcreature_health_bar.creature_health_bar import CreatureHealthBar

from mcreature.mcreature_items.mcreature_name_bar.mcreature_name_bar import CreatureNameBar
from mcreature.mcreature_items.mcreature_name_bar.mcreature_name_bar_manager import CreatureNameBarManager

from mcreature.mcreature_items.mcreature_attack_icon.mcreature_attack_icon import CreatureAttackIcon

from mweapon.weapon import Weapon
from mweapon.weapon_manager import WeaponManager

from mscreen.screen import Screen

from mweapon.gravity.gravity import GravityAttack

mf.start_game()
temp = Player(
    name="aa",
    health=100,
    power=10,
    defense=100,
    speed=8,
    width=100,
    height=100,
    x=100,
    y=400,
    jumpSize=100,
    playerType="gravity"
)
ms.monster_num += 1

wtemp = Weapon(
    name="bb",
    power=100,
    width=50,
    height=50,
    x=100,
    y=100,
    player = temp,
    mother_creature=temp,
)
ms.monster_num += 1

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
ms.monster_num += 1

hitemp = CreatureHealthBar(temp)
rhitemp = CreatureHealthBar(rtemp)
natemp = CreatureNameBar(rtemp)

aitemp = CreatureAttackIcon("b1", temp)

gctemp = GravityAttack(540, 270, 100)

pm = PlayerManager()
pm.add_element(temp)
rm = RobotManager()
rm.add_element(rtemp)
wm = WeaponManager()
wm.add_element(wtemp)
game_screen = Screen()
him = CreatureHealthBarManager()
him.add_element(hitemp)
him.add_element(rhitemp)
nam = CreatureNameBarManager()
nam.add_element(natemp)

gctemp.append_creatures(temp)

print(temp.x, temp.y)

while ms.running:
    mf.is_QUIT()

    game_screen.screen_fill_bg(ms.screen)
    
    aitemp.draw(ms.screen)
    pm.update_element(game_screen)
    pm.draw_element(ms.screen)
    wm.update_element(temp, rm)
    wm.draw_element(ms.screen)
    rm.update_element(temp)
    rm.draw_element(ms.screen)
    him.update_element()
    him.draw_element(ms.screen)
    nam.update_element()
    nam.draw_element(ms.screen)

    gctemp.draw(ms.screen)

    mf.update(ms.screen)

# 파이게임 종료
mf.end_game()