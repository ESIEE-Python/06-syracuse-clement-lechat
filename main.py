#### Fonctions secondaires

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    
    >>> syracuse_l(3)
    [3 10 5 16 8 4 2 1]
    """
    # votre code ici
    l = [ n]
    while n!=1:
        if n%2==0:
            n=n//2
            l.append(n)
        else:
            n=n*3+1
            l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    
    >>> temps_de_vol([8 4 2 1])
    4
    """
    # votre code ici
    return len(l)

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude

    >>> temps_de_vol_en_altitude([11 34 17 52 26 13 40 20 10 5 16 8 4 2 1])
    8
    """
    # votre code ici
    n = 0
    p = l[0]
    for elt in l:
        if elt >= p:
            n +=1
        else: 
            break
    return n

def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale

    >>> altitude_maximale([11 34 17 52 26 13 40 20 10 5 16 8 4 2 1])
    52
    """
    # votre code ici
    n = max(l)
    return n

#### Fonction principale


def main():
    """
    Fonction main: test le bon fonctionnement des fonctions secondaires
    """
    # vos appels à la fonction secondaire ici
    print(syracuse_l(11))
    syr_plot(syracuse_l(11))
    print(temps_de_vol(syracuse_l(11)))
    print(temps_de_vol_en_altitude(syracuse_l(11)))
    print(altitude_maximale(syracuse_l(11)))

    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
