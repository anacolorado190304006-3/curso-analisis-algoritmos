
"""Implementación de una lista enlazada y una tabla hash con encadenamiento.

Las estructuras almacenan guías de envío de tipo entero y sus estados.
"""


class Nodo:
    """Representa un nodo de una lista enlazada.

    Attributes:
        guia: Número entero de la guía de envío.
        estado: Estado actual del envío.
        siguiente: Referencia al siguiente nodo.
    """

    def __init__(self, guia: int, estado: str) -> None:
        """Inicializa un nodo con su guía y estado."""
        self.guia: int = guia
        self.estado: str = estado
        self.siguiente: Nodo | None = None


class ListaEnlazada:
    """Lista enlazada simple para almacenar guías y estados."""

    def __init__(self) -> None:
        """Inicializa una lista vacía."""
        self.cabeza: Nodo | None = None
        self.tamano: int = 0

    def insertar(self, guia: int, estado: str) -> None:
        """Inserta una guía al inicio de la lista.

        Args:
            guia: Número de guía del envío.
            estado: Estado actual del envío.

        Complejidad:
            Θ(1).
        """
        nuevo_nodo = Nodo(guia, estado)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.tamano += 1

    def buscar(self, guia: int) -> str | None:
        """Busca una guía y devuelve su estado si existe.

        Args:
            guia: Número de guía que se desea consultar.

        Returns:
            Estado del envío si la guía existe; None en caso contrario.

        Complejidad:
            Θ(n) en el peor caso.
        """
        actual = self.cabeza

        while actual is not None:
            if actual.guia == guia:
                return actual.estado
            actual = actual.siguiente

        return None


class TablaHash:
    """Tabla hash que resuelve colisiones mediante encadenamiento."""

    def __init__(self, m: int) -> None:
        """Inicializa la tabla con m casillas.

        Args:
            m: Número de casillas de la tabla.

        Raises:
            ValueError: Si m no es un entero positivo.
        """
        if not isinstance(m, int) or isinstance(m, bool) or m <= 0:
            raise ValueError("El tamaño de la tabla debe ser un entero positivo.")

        self.m: int = m
        self.casillas: list[ListaEnlazada] = [
            ListaEnlazada() for _ in range(m)
        ]
        self.tamano: int = 0

    def hash(self, guia: int) -> int:
        """Calcula la posición de una guía mediante el método de división.

        Args:
            guia: Número de guía que se desea ubicar.

        Returns:
            Índice de la casilla correspondiente.

        Complejidad:
            Θ(1).
        """
        return guia % self.m

    def insertar(self, guia: int, estado: str) -> None:
        """Inserta una guía en la casilla correspondiente.

        Las colisiones se almacenan en la lista enlazada de la casilla.

        Args:
            guia: Número de guía del envío.
            estado: Estado actual del envío.

        Complejidad:
            Θ(1) para calcular la casilla, más el costo de insertar
            al inicio de su lista enlazada.
        """
        indice = self.hash(guia)
        self.casillas[indice].insertar(guia, estado)
        self.tamano += 1

    def buscar(self, guia: int) -> str | None:
        """Busca una guía únicamente en su casilla correspondiente.

        Args:
            guia: Número de guía que se desea consultar.

        Returns:
            Estado del envío si existe; None en caso contrario.

        Complejidad:
            Θ(1 + α) esperada bajo hashing uniforme simple.
            Θ(n) en el peor caso.
        """
        indice = self.hash(guia)
        return self.casillas[indice].buscar(guia)

    def factor_carga(self) -> float:
        """Calcula el factor de carga de la tabla.

        Returns:
            Cantidad de elementos dividida entre el número de casillas.

        Complejidad:
            Θ(1).
        """
        return self.tamano / self.m
