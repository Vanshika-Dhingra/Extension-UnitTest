import points as pt
import village
import unittest
import king

V = village.createVillage(1)
directions = ["left", "right", "up", "down"]
coordinates = [[0, -1], [0, 1], [-1, 0], [1, 0]]


class TestKingMove(unittest.TestCase):
    def test_position(self):
        vmap = V.map
        King = king.getHero(0)
        for k in range(0, 18):
            for l in range(0, 36):
                if (vmap[k][l] != pt.BLANK and vmap[k][l] != pt.SPAWN):
                    continue
                else:
                    King.position[0] = k
                    King.position[1] = l
                    King.facing=''
                    for i in range(0, 4):
                        King.position = [k, l]
                        initialPosition = [k, l]
                        King.alive=False
                        facing=King.facing
                        King.move(directions[i],V)
                        self.assertEqual(King.position,initialPosition)
                        self.assertEqual(King.facing,facing)
                        King.alive=True
                        King.move(directions[i], V)
                        self.assertEqual(King.facing,directions[i])
                        finalPosition = King.position.copy()
                        for j in range(King.speed):
                            r = initialPosition[0]+coordinates[i][0]
                            c = initialPosition[1]+coordinates[i][1]
                            if (c < 0):
                                continue
                            if (c >= len(vmap[0])):
                                continue
                            if (r >= len(vmap)):
                                continue
                            if (r < 0):
                                continue
                            if (vmap[r][c] != pt.BLANK and vmap[r][c] != pt.SPAWN):
                                break
                            initialPosition[0] += coordinates[i][0]
                            initialPosition[1] += coordinates[i][1]
                        self.assertEqual(initialPosition, finalPosition)
                        self.assertEqual(pt.HERO_POS,King.position)

if __name__ == '__main__':
    result = unittest.TextTestRunner().run(
        unittest.TestLoader().loadTestsFromTestCase(TestKingMove))
    f = open("output.txt", "w")
    if result.wasSuccessful() and result.wasSuccessful():
        f.write("True")
    else:
        f.write("False")
f.close()