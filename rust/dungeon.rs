mod dungeon {
    pub struct Weapon {
        look: char,
        name: String,
        description: String,
        strength: i32,
        damage: i32,
        accuracy: i32,
    }

    pub struct Armor {
        look: char,
        name: String,
        description: String,
        strength: i32,
        block: i32,
        evasion: i32,
    }

    pub struct Person {
        look: [i32; 2],
        name: String,
        description: String,
        level: i32,
        strength: i32,
        max_health: i32,
        health: i32,
        hunger: i32,
        speed: i32,
        weapon: Weapon,
        armor: Armor,
        damage: i32,
        accuracy: i32,
        block: i32,
        evasion: i32,
    }


    impl Person {
        fn equip_weapon(&mut self, weapon: Weapon) {
            self.weapon = weapon;
            self.calc_stats();
        }

        fn equip_armor(&mut self, armor: Armor) {
            self.armor = armor;
            self.calc_stats();
        }

        fn calc_stats(&mut self) {
            let raw_damage = self.weapon.damage * (1 + self.strength / self.weapon.strength);
            self.damage = raw_damage;

            let raw_accuracy = self.weapon.accuracy * (1 + self.strength / self.weapon.strength);
            let accuracy_modifier = self.level + 10;

            let raw_block = self.armor.block
        }

        fn appear(&self, x: i32, y: i32) {
        }
    }
}


fn main() {
    println!("HELLO")
}
