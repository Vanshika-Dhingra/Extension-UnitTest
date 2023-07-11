import points as pt
import village
import unittest
import king
import copy

directions = ["left", "right", "up", "down"]
coordinates = [[0, -1], [0, 1], [-1, 0], [1, 0]]


class TestKingAttack(unittest.TestCase):
    def funck(self,V):
        a=[]
        a.append(V.town_hall_obj)
        for key in V.cannon_objs:
            a.append(V.cannon_objs[key])
        for key in V.wall_objs:
            a.append(V.wall_objs[key])
        for key in V.wizard_tower_objs:
            a.append(V.wizard_tower_objs[key])
        for key in V.hut_objs:
            a.append(V.hut_objs[key])
        return a
    def test_attack(self):
        King = king.getHero(0)
        V = village.createVillage(1)
        a=self.funck(V)
        for target in a:
            initSize=len(self.funck(V))
            King.alive = False
            copy3=copy.deepcopy(target)
            copy3.V=0
            initialKingHealth = King.health
            initialHealth = target.health
            King.attack_target(target, King.attack)
            copy4=copy.deepcopy(target)
            copy4.V=0
            finalKingHealth = King.health
            finalHealth = target.health
            self.assertEqual(initialKingHealth, finalKingHealth)
            self.assertEqual(initialHealth, finalHealth)
            self.assertEqual(copy3.__dict__,copy4.__dict__)
            King.alive = True
            copy1=copy.deepcopy(target)
            copy1.V=0
            King.attack_target(target, King.attack)
            copy2=copy.deepcopy(target)
            copy2.V=0
            finalHealth = initialHealth-King.attack
            if (finalHealth <= 0):
                finalHealth = 0
                copy1.destroyed=True
                self.assertEqual(target.destroyed, True)
                self.assertEqual(target.health, finalHealth)
                self.assertEqual(initSize-1,len(self.funck(V)))
                copy1.health=finalHealth
                self.assertEqual(copy1.__dict__,copy2.__dict__)


if __name__ == '__main__':
    result = unittest.TextTestRunner().run(
        unittest.TestLoader().loadTestsFromTestCase(TestKingAttack))
    f = open("output_bonus.txt", "w")
    if result.wasSuccessful() and result.wasSuccessful():
        f.write("True")
    else:
        f.write("False")
f.close()
