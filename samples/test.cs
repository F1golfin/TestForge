using System;
using System.Collections.Generic;

namespace GameNamespace
{
    public enum CharacterClass
    {
        Warrior,
        Mage,
        Rogue
    }

    public class GameCharacter
    {
        public string Name { get; private set; }
        public CharacterClass Class { get; private set; }
        public int Level { get; private set; }
        public int Health { get; private set; }
        public List<string> Inventory { get; private set; }

        public GameCharacter(string name, CharacterClass charClass)
        {
            if (string.IsNullOrWhiteSpace(name))
                throw new ArgumentException("Name cannot be empty");

            Name = name;
            Class = charClass;
            Level = 1;
            Health = 100;
            Inventory = new List<string>();
        }

        public void TakeDamage(int damage)
        {
            if (damage < 0) throw new ArgumentException("Damage must be positive");
            Health = Math.Max(0, Health - damage);
        }

        public void Heal(int healAmount)
        {
            if (healAmount < 0) throw new ArgumentException("Heal amount must be positive");
            Health = Math.Min(100, Health + healAmount);
        }

        public void LevelUp()
        {
            Level++;
            Health = 100;
        }

        public void AddItem(string item)
        {
            if (string.IsNullOrWhiteSpace(item))
                throw new ArgumentException("Item cannot be empty");
            Inventory.Add(item);
        }

        public bool HasItem(string item)
        {
            return Inventory.Contains(item);
        }
    }
}
