import os

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from Champion import Champion
from bs4 import BeautifulSoup
import re

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()
driver.get('https://tftactics.gg/champions')

champs = []
for i in range(99999):
    champion_elements = driver.find_elements(By.CSS_SELECTOR, 'div.characters-list a p')
    if i < len(champion_elements):
        champ = Champion()
        champion_element = champion_elements[i]
        champ.name = champion_element.text
        champion_element.click()
        img = driver.find_element(By.CSS_SELECTOR, 'img.character-image').get_attribute('src')
        champ.image = img
        items = driver.find_elements(By.CSS_SELECTOR, 'a.characters-item div img.character-icon')
        for item in range(3):
            champ.item_builder.append(items[item].get_attribute('alt'))
        list_stats = driver.find_elements(By.CSS_SELECTOR, 'ul.stats-list li')
        txt = list_stats[0].text
        cost = [int(s) for s in txt.split() if s.isdigit()]
        champ.cost = cost[0]
        txt = list_stats[1].text
        champ.health = [int(s) for s in txt.split() if s.isdigit()]
        txt = list_stats[3].text
        armor = [int(s) for s in txt.split() if s.isdigit()]
        champ.armor = armor[0]
        txt = list_stats[4].text
        magic_resist = [int(s) for s in txt.split() if s.isdigit()]
        champ.magic_resist = magic_resist[0]
        txt = list_stats[5].text
        ability_power = [int(s) for s in txt.split() if s.isdigit()]
        champ.ability_power = ability_power[0]
        txt = list_stats[6].text
        champ.DPS = [int(s) for s in txt.split() if s.isdigit()]
        txt = list_stats[7].text
        champ.Damage = [int(s) for s in txt.split() if s.isdigit()]
        txt = list_stats[8].text
        atk_spd = re.findall("\d+\.\d+", txt)
        champ.atk_spd = atk_spd[0]
        txt = list_stats[9].text
        # crit_rate = [int(s) for s in txt.split() if s.isdigit()]
        champ.crit_rate = int(re.search(r'\d+', txt).group())
        txt = list_stats[10].text
        range_ = [int(s) for s in txt.split() if s.isdigit()]
        champ.range_ = range_[0]
        txt = driver.find_element(By.CSS_SELECTOR, 'div.ability-description-cost span').text
        champ.mana = [int(s) for s in txt.split() if s.isdigit()]
        if len(champ.mana) == 1:
            champ.mana.append(0)
        champ.skill_name = driver.find_element(By.CSS_SELECTOR, 'img.ability-image').get_attribute('alt')
        html_skill_content = driver.find_element(By.CSS_SELECTOR, 'p.ability-bonus').get_attribute('innerHTML')
        soup = BeautifulSoup(html_skill_content, 'lxml')
        img_tags = soup.find_all('img')
        for img_tag in img_tags:
            alt_value = img_tag['alt']
            img_tag.replace_with(f" {alt_value} ")

        result = soup.p.get_text(strip=True)
        champ.skill_content = result
        list_misc = driver.find_elements(By.CSS_SELECTOR, 'img.misc-image')
        for m in range(len(list_misc) // 2):
            misc = list_misc[m]
            champ.misc.append(misc.get_attribute('alt'))
        print(champ.to_string())
        champs.append(champ)
        driver.execute_script("window.history.go(-1)")
    else:
        break

raw = [r.to_list() for r in champs]


def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


data = []
for r in raw:
    data.append(flatten_list(r))

df = pd.DataFrame(data, columns=['name', 'image', 'item_builder_1', 'item_builder_2', 'item_builder_3', 'cost',
                                 'health_1_star', 'health_2_stars', 'health_3_stars', 'armor', 'magic_resist',
                                 'ability_power', 'DPS_1_star', 'DSP_2_stars', 'DPS_3_stars', 'Damage_1_star',
                                 'Damage_2_stars', 'Damage_3_stars',
                                 'attack_speed', 'crit_rate', 'range', 'starting_mana', 'activated_mana',
                                 'skill_name', 'skill_content', 'misc_1', 'misc_2', 'misc_3'])
df.to_excel('data.xlsx')
