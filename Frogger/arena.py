class Arena():
    '''Generica 2D game, cui vengono assegnate le dimensioni di gioco
       e che contiene la lista dei personaggi del gioco
    '''
    def __init__(self, width: int, height: int):
        '''Crea una arena con specifica altezza e larghezza
           e lista di personaggi inizialmente vuota
        '''
        self._w, self._h = width, height
        self._actors = []

    def add(self, a: Actor):
        '''Aggiunge un personaggio al gioco
           I personaggi sono gestiti seguendo il loro ordine di inserimento
        '''
        if a not in self._actors:
            self._actors.append(a)

    def remove(self, a: Actor):
        '''Elimina un personaggio dal gioco
        '''
        if a in self._actors:
            self._actors.remove(a)

    def move_all(self):
        '''chiama il metodo move di ogni personaggio
           dopo aver effettuato il movimento verica
           se è avvenuta un collisione tra il personaggio
           e un altro personaggio e in tal caso chiama
           il metodo collide di entrambi
        '''
        actors = list(reversed(self._actors))
        for a in actors:
            previous_pos = a.position()
            a.move()
            if a.position() != previous_pos:  # inutile per personaggi statici
                for other in actors:
                    # reversed order, so actors drawn on top of others
                    # (towards the end of the cycle) are checked first
                    if other is not a and self.check_collision(a, other):
                            a.collide(other)
                            other.collide(a)

    def check_collision(self, a1: Actor, a2: Actor) -> bool:
        '''Verifica se i due personaggi (parametri) sono in collisione 
           (bounding-box collision detection)
        '''
        x1, y1, w1, h1 = a1.position()
        x2, y2, w2, h2 = a2.position()
        return (y2 < y1 + h1 and y1 < y2 + h2
            and x2 < x1 + w1 and x1 < x2 + w2
            and a1 in self._actors and a2 in self._actors)

    def actors(self) -> list:
        '''Restituisce una copia della lista dei personaggi
        '''
        return list(self._actors)

    def size(self) -> (int, int):
        '''Restituisce le dimensioni dell'arena di gioco: (width, height)
        '''
        return (self._w, self._h)
