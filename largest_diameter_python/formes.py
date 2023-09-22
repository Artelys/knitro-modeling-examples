'''Diamètre d'un trou (MMI - Problèmes)
Sujet : déterminer la plus grande dimension d'un trou (plan)

Définition des formes.

(c) Pierre Lemaire, 2022.
version : 2022-11-20
_____________________________________________________________________________

Ce fichier contient la définition de la classe Forme ainsi que
différentes fonctions pour générer des formes.

Classe Forme:
- une forme est créée par Forme(x, y) où x et y sont des fonctions float -> float.
- pour une forme f, les fonctions sont accessibles par f.x(t), f.y(t).
- une méthode f.dessiner() permet de dessiner une forme. Des paramètres optionnels
  permettent d'adapter ce tracer :
  - lignes   : liste de couples (t1, t2); les segments entre les points t1 et t2 sont tracés
  - nb_points: nombre de points pour le tracer
  - imgfile  : nom de fichier d'image (par exemple "toto.png"); si non None, la forme n'est pas
               affichée à l'écran, mais dessinée dans le fichier indiqué.


Fonctions pour créer des formes :
- cercle(r)       : cercle de rayon r
- ellipse(a, b)   : ellipse d'axes a et b
- rectangle(a, b) : rectangle de côtés a et b
- patate(s)       : patatoide aléatoire ; un même s produit toujours la même forme ;
                    toutes les patatoides ne sont des formes correctes (croisements possibles).
                    Un paramètre optionnel (complexite) permet de définir la complexité de la
                    forme.
- transformer     : transforme une forme en appliquant la matrice A (matrice 2x2) à chaque point
                    utile pour des rotations, homothéties, etc
- decaler         : décale les valeurs de t de dx et dy ; permet des déformations additionnelles

Voir les exemples en fin de fichier.
'''
from typing import Callable, List, Tuple, Optional
import math
import random
import matplotlib.pyplot as plt

## -----------------------------------------------------------------------------
## Classe Forme
## (ne pas modifier, sauf dessiner())
## -----------------------------------------------------------------------------
class Forme:
    ''' Une forme, prête à être dessinée !'''

    @staticmethod
    def _corriger(t: float) -> float:
        ''' Corrige t (positif) dans [0, 1].'''
        return t - int(t)

    def __init__(self,
                 x: Callable[[float], float],
                 y: Callable[[float], float],
                 nom: str = "") -> None:
        ''' Crée une nouvelle forme avec les fonctions x et y indiquées.'''
        self._x = x
        self._y = y
        self._nom = nom

    def x(self, t: float) -> float:
        ''' x(t) de cette Forme.'''
        return self._x(Forme._corriger(t))

    def y(self, t: float) -> float:
        ''' y(t) de cette Forme.'''
        return self._y(Forme._corriger(t))

    def dessiner(self,
                 lignes: List[Tuple[int, int]] = [],
                 nb_points: int = 1000,
                 imgfile: Optional[str] = None) -> None:
        ''' dessine la forme et ajoute les lignes indiquées (liste de couples (t1, t2)).'''
        ts = [i/nb_points for i in range(0, nb_points+1)]
        xs = [self.x(t) for t in ts]
        ys = [self.y(t) for t in ts]

        x_min = min(xs)
        x_max = max(xs)
        y_min = min(ys)
        y_max = max(ys)
        dx = (x_max - x_min)*0.05
        dy = (y_max - y_min)*0.05

        _, axes = plt.subplots()
        axes.plot(xs, ys, linewidth=2.0)
        for t1, t2 in lignes:
            axes.plot([self.x(t1), self.x(t2)],
                      [self.y(t1), self.y(t2)], linewidth=1.0)
        axes.set(
            aspect="equal",
            xlim=(x_min-dx, x_max+dx),
            ylim=(y_min-dy, y_max+dy))

        if imgfile is None:
            plt.show()
        else:
            plt.savefig(imgfile)
            plt.close()

    @property
    def nom(self) -> str:
        ''' Renvoie le nom de cette Forme.'''
        return self._nom

## -----------------------------------------------------------------------------
## Formes de base
## -----------------------------------------------------------------------------
def cercle(rayon: float) -> Forme:
    ''' Renvoie un cercle du rayon indiqué. '''
    return Forme(
        lambda t: rayon*math.cos(t*2*math.pi),
        lambda t: rayon*math.sin(t*2*math.pi),
        nom=f"cercle({rayon})")

## -----------------------------------------------------------------------------
def ellipse(axe1: float, axe2: float) -> Forme:
    ''' Renvoie une ellipse avec les axes indiqués. '''
    return Forme(
        lambda t: axe1*math.cos(t*2*math.pi),
        lambda t: axe2*math.sin(t*2*math.pi),
        nom=f"ellipse({axe1}, {axe2})")

## -----------------------------------------------------------------------------
def rectangle(cote1: float, cote2: float) -> Forme:
    ''' Renvoie un rectangle avec les cotes indiquées. '''
    def x(t):
        if t < 0.25: return 4*cote1*t
        if t < 0.50: return cote1
        if t < 0.75: return cote1 - 4*cote1*(t-0.5)
        return 0
    def y(t):
        if t < 0.25: return 0
        if t < 0.50: return 4*cote2*(t-0.25)
        if t < 0.75: return cote2
        return cote2 - 4*cote2*(t-0.75)
    return Forme(x, y, nom=f"rectangle({cote1}, {cote2})")

## -----------------------------------------------------------------------------
def patate(s: int, complexite: int = -1) -> Forme:
    ''' Renvoie une patate de numéro s, et de complexité donnée. '''
    funcs = [
        lambda t: math.cos(t*2*math.pi),
        lambda t: math.sin(t*2*math.pi),
        lambda t: 4*(0.5-t)**2,
        lambda t: 25/3*abs(0.5-t)**3,
        lambda t: math.exp(-25*(t-0.5)**2),
        lambda t: math.cos(t*10*math.pi)/10,
        lambda t: math.sin(t*12*math.pi)/15
    ]
    if complexite > 0:
        funcs = funcs[:complexite]

    random.seed(s)
    cx = [random.random() for _ in range(len(funcs))]
    cy = [random.random() for _ in range(len(funcs))]
    return Forme(
        lambda t: sum([cx[i] * funcs[i](t) for i in range(len(funcs))]),
        lambda t: sum([cy[i] * funcs[i](t) for i in range(len(funcs))]),
        nom=f"patate({s}, complexite={complexite})")

## -----------------------------------------------------------------------------
## Transformations de formes
## -----------------------------------------------------------------------------
def transformer(forme: Forme, A: List[List[float]]) -> Forme:
    ''' Renvoie une nouvelle forme, transformée par la matrice A.'''
    return Forme(
        lambda t: A[0][0]*forme.x(t) + A[0][1]*forme.y(t),
        lambda t: A[1][0]*forme.x(t) + A[1][1]*forme.y(t),
        nom=f"transformer({forme.nom}, {str(A)})"
    )

def decaler(forme: Forme, dx: float, dy: float) -> Forme:
    ''' Renvoie une nouvelle forme, décallée de dx et dy. '''
    return Forme(
        lambda t: forme.x(t+dx),
        lambda t: forme.y(t+dy),
        nom=f"decaler({forme.nom}, {dx}, {dy})")

## -----------------------------------------------------------------------------
## Tests
## -----------------------------------------------------------------------------
if __name__ == "__main__":
    ## Exemples :    
    if False:
        f1 = cercle(10)
        f1.dessiner([(0, 0.5), (0.25, 0.73)])

        f2 = ellipse(10, 7)
        f2.dessiner([(0, 0.5), (0.25, 0.73)])

        angle = math.pi/4
        f3 = transformer(
            rectangle(5, 7),
            [[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        f3.dessiner()

        rectangle(5, 7).dessiner()
        decaler(rectangle(5, 7), .2, 0.3).dessiner()

        patate(1, complexite=2).dessiner()
        patate(1, complexite=4).dessiner()
        patate(2, complexite=6).dessiner()
        patate(1).dessiner()

        for s in range(20):
            patate(s, complexite=4).dessiner(imgfile=f"p4_{s:02d}")
            patate(s, complexite=5).dessiner(imgfile=f"p5_{s:02d}")
            patate(s).dessiner(imgfile=f"pX_{s:02d}")


    # Premier tests de Caseine :
    if False:
        # Test 1
        cercle(5).dessiner(imgfile=f"x011.png")

        # Test 2
        base = rectangle(6, 8)
        base.dessiner(imgfile=f"x021.png")
        decaler(base, 0.2, 0.2).dessiner(imgfile=f"x022.png")
        decaler(base, 0.2, 0.3).dessiner(imgfile=f"x023.png")
        transformer(decaler(base, 0.2, 0.3), \
                    [[0.2, 0.8], [0.8, 0.2]]).dessiner(imgfile=f"x024.png")

        # Test 3
        base = patate(3, complexite=4)
        base.dessiner(imgfile=f"x031.png")
        decaler(base, 0.2, 0.2).dessiner(imgfile=f"x032.png")
        decaler(base, 0.2, 0.3).dessiner(imgfile=f"x033.png")
        transformer(decaler(base, 0.2, 0.3), \
                    [[0.2, 0.8], [0.8, 0.2]]).dessiner(imgfile=f"x034.png")

        # Test 4
        base = patate(7, complexite=6)
        base.dessiner(imgfile=f"x041.png")
        decaler(base, 0.2, 0.2).dessiner(imgfile=f"x042.png")
        decaler(base, 0.3, 0.2).dessiner(imgfile=f"x043.png")
        transformer(decaler(base, 0.3, 0.2), \
                    [[0.2, 0.8], [0.8, 0.2]]).dessiner(imgfile=f"x044.png")

        # Test 5
        base = transformer(rectangle(7, 6), [[0.5, 0.866], [-0.866, 0.5]])
        base.dessiner(imgfile=f"x051.png")
        decaler(base, 0.2, 0.3).dessiner(imgfile=f"x052.png")
        decaler(base, 0.4, 0.2).dessiner(imgfile=f"x053.png")
        decaler(base, 0.2, 0.9).dessiner(imgfile=f"x054.png")

        # Test 6
        base = patate(16)
        base.dessiner(imgfile=f"x061.png")
        decaler(base, 0.25, 0.33).dessiner(imgfile=f"x062.png")
        transformer(base, [[0.123, -0.23], [0.32, -0.15]]).dessiner(imgfile=f"x063.png")
