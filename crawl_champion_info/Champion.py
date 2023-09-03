class Champion:
    def __init__(self):
        self.name = ''
        self.image = ''
        self.item_builder = []
        self.cost = 0
        self.health = []
        self.armor = 0
        self.magic_resist = 0
        self.ability_power = 0
        self.DPS = []
        self.Damage = []
        self.atk_spd = 0.0
        self.crit_rate = 0
        self.range_ = 0
        self.mana = []
        self.skill_name = ''
        self.skill_content = ''
        self.misc = []

    def to_string(self):
        print(self.name)
        print(self.image)
        for i in self.item_builder:
            print(i)
        print(self.cost)
        for i in self.health:
            print(i)
        print(self.armor)
        print(self.magic_resist)
        print(self.ability_power)
        for i in self.DPS:
            print(i)
        for i in self.Damage:
            print(i)
        print(self.atk_spd)
        print(self.crit_rate)
        print(self.range_)
        for i in self.mana:
            print(i)
        print(self.skill_name)
        print(self.skill_content)
        for i in self.misc:
            print(i)

    def to_list(self):
        return [self.name, self.image, self.item_builder, self.cost, self.health, self.armor, self.magic_resist,
                self.ability_power, self.DPS, self.Damage, self.atk_spd, self.crit_rate, self.range_, self.mana,
                self.skill_name, self.skill_content, self.misc]
