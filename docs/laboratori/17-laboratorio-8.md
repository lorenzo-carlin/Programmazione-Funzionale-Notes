> **Esercizio 8.1**
>
> Definire la signature `SET` che preveda:
>
> - un parametro di tipo: `'a set`
> - un valore per un set vuoto: `emptyset`
> - un operatore per testare se un elemento fa parte del set o no: `isin`
> - un operatore per aggiungere un elemento ad un set: `addin`
> - un operatore per rimuovere un elemento da un set: `removefrom`

```sml
signature SET = sig
  type 'a set
  val emptyset : 'a set
  val isin : 'a * 'a set -> bool
  val addin : 'a * 'a set -> 'a set
  val removefrom : 'a * 'a set -> 'a set
end;

(*signature SET = sig
  type 'a set
  val emptyset : 'a set
  val isin : 'a * 'a set -> bool
  val addin : 'a * 'a set -> 'a set
  val removefrom : 'a * 'a set -> 'a set
end;*)
```

> **Esercizio 8.2**
>
> Con la signature `SET` data, aggiungere la definizione per la struttura `Set` che implementi tale signature.

```sml
signature SET = sig
  type 'a set
end;

structure Set = struct
  type 'a set = 'a list
end:>SET;

(*signature SET = sig type 'a set end
structure Set: SET*)
```

> **Esercizio 8.3**
>
> Con la signature `SET` data, aggiungere la definizione per la struttura `Set` che implementi tale signature e aggiungere dei casi di test.

```sml
signature SET = sig
  type 'a set
  val emptyset: 'a set
end;

structure Set = struct
  type 'a set = 'a list
  val emptyset = []
end:>SET;

val a = Set.emptyset;

(*signature SET = sig val emptyset: 'a set type 'a set end
structure Set: SET
val a = []: 'a Set.set*)
```

> **Esercizio 8.4**
>
> Con la signature `SET` data, aggiungere la definizione per la struttura `Set` che implementi tale signature e aggiungere dei casi di test.

```sml
signature SET = sig
  type ''a set
  val emptyset: ''a set
  val isin: ''a -> ''a set -> bool
end;

structure Set = struct
  type ''a set = ''a list
  val emptyset = []
  fun isin y nil = false
    | isin y (x::xs) = if y = x then true else isin y xs
end:>SET;

val a = Set.emptyset;
val b = Set.isin 1 a;

(*signature SET =
  sig val emptyset: ''a set val isin: ''a -> ''a set -> bool type 'a set end
structure Set: SET
val a = ?: ''a Set.set
val b = false: bool*)
```

> **Esercizio 8.5**
>
> Con la signature `SET` data, aggiungere la definizione per la struttura `Set` che implementi tale signature e aggiungere dei casi di test.

```sml
signature SET = sig
  type ''a set
  val emptyset: ''a set
  val isin: ''a -> ''a set -> bool
  val addin: ''a -> ''a set -> ''a set
end;

structure Set = struct
  type ''a set = ''a list
  val emptyset = []
  fun isin y nil = false
    | isin y (x::xs) = if y = x then true else isin y xs
  fun addin y s = if isin y s then s else y::s
end:>SET;

val a = Set.emptyset;
val b = Set.isin 1 a;
val c = Set.addin 1 a;
val d = Set.isin 1 c;

(*signature SET =
  sig
    val addin: ''a -> ''a set -> ''a set
    val emptyset: ''a set
    val isin: ''a -> ''a set -> bool
    type 'a set
  end
structure Set: SET
val a = ?: ''a Set.set
val b = false: bool
val c = ?: int Set.set
val d = true: bool*)
```

> **Esercizio 8.6**
>
> Con la signature `SET` data, aggiungere la definizione per la struttura `Set` che implementi tale signature e aggiungere dei casi di test.

```sml
signature SET = sig
  type ''a set
  val emptyset: ''a set
  val isin: ''a -> ''a set -> bool
  val addin: ''a -> ''a set -> ''a set
  val removefrom: ''a -> ''a set -> ''a set
end;

structure Set = struct
  type ''a set = ''a list
  val emptyset = []
  fun isin y nil = false
    | isin y (x::xs) = if y = x then true else isin y xs
  fun addin y s = if isin y s then s else y::s
  fun removefrom y nil = nil
    | removefrom y (x::xs) = if y = x then xs else (x::(removefrom y xs))
end:>SET;

val a = Set.emptyset;
val b = Set.isin 1 a;
val c = Set.addin 1 a;
val d = Set.addin 2 c;
val e = Set.isin 1 d;
val f = Set.removefrom 1 d;
val g = Set.isin 1 f;

(*signature SET =
  sig
    val addin: ''a -> ''a set -> ''a set
    val emptyset: ''a set
    val isin: ''a -> ''a set -> bool
    val removefrom: ''a -> ''a set -> ''a set
    type 'a set
  end
structure Set: SET
val a = ?: ''a Set.set
val b = false: bool
val c = ?: int Set.set
val d = ?: int Set.set
val e = true: bool
val f = ?: int Set.set
val g = false: bool*)
```

> **Esercizio 8.7**
>
> Con il datatype `'a T` dato, si definisca una signature `TREE` che preveda:
>
> - una funzione per calcolare il numero di nodi nell'albero, escludendo le foglie: `countNodes`
> - una funzione per calcolare la profondità dell'albero, escludendo le foglie: `depth`
> - una funzione che calcola l'albero specchiato, ossia l'albero ottenuto invertendo left e right subtree di ogni nodo: `mirror`

```sml
datatype 'a T =
  Lf |
  Br of 'a * 'a T * 'a T

signature TREE = sig
  val countNodes: 'a T -> int
  val depth: 'a T -> int
  val mirror: 'a T -> 'a T
end;

(*datatype 'a T = Br of 'a * 'a T * 'a T | Lf
signature TREE =
  sig
    val countNodes: 'a T -> int
    val depth: 'a T -> int
    val mirror: 'a T -> 'a T
  end*)
```

> **Esercizio 8.8**
>
> Data la signature `TREE`, definire la struttura `Tree`. Aggiungere dei casi di test.

```sml
signature TREE = sig
  datatype 'a T =
    Lf |
    Br of 'a * 'a T * 'a T
  val countNodes: 'a T -> int
  val depth: 'a T -> int
  val mirror: 'a T -> 'a T
end;

structure Tree = struct
  datatype 'a T =
    Lf |
    Br of 'a * 'a T * 'a T
  fun countNodes Lf = 0
    | countNodes (Br(v, left, right)) = ((countNodes left) + (countNodes right) + 1)
  fun depth Lf = 0
    | depth (Br(v, left, right)) =
      let
        val l = depth left
        val r = depth right
      in
        if l > r then l+1 else r+1
      end;
  fun mirror Lf = Lf
    | mirror (Br(v, left, right)) = Br(v, mirror right, mirror left)
end:>TREE;

val a = Tree.Br(1,
          Tree.Br(2, Tree.Lf, Tree.Lf),
          Tree.Br(3,
            Tree.Br(4, Tree.Lf, Tree.Lf),
            Tree.Br(5, Tree.Lf, Tree.Lf)));
val b = Tree.countNodes a;
val c = Tree.depth a;
val d = Tree.mirror a;

(*signature TREE =
  sig
    datatype 'a T = Br of 'a * 'a T * 'a T | Lf
    val countNodes: 'a T -> int
    val depth: 'a T -> int
    val mirror: 'a T -> 'a T
  end
structure Tree: TREE
val a = Br (1, Br (2, Lf, Lf), Br (3, Br (4, Lf, Lf), Br (5, Lf, Lf))):
   int Tree.T
val b = 5: int
val c = 3: int
val d = Br (1, Br (3, Br (5, Lf, Lf), Br (4, Lf, Lf)), Br (2, Lf, Lf)):
   int Tree.T*)
```

> **Esercizio 8.9**
>
> Dato il tipo `('a,'b) mapTree`, definito come un BST in cui l'ordine è definito dalla prima componente della tupla, scrivere una funzione `lookup lt T a` che cerca una coppia `(a, b)` la cui prima componente sia `a`. Se la trova, ritorna `b`, altrimenti solleva l'eccezione `Missing`.
> Scrivere un `(int, string) mapTree` per testare la funzione.

```sml
datatype 'a btree =
  Empty |
  Node of 'a * 'a btree * 'a btree;

type ('a, 'b) mapTree = ('a * 'b) btree;

val lt = (op <);

exception Missing;

fun lookup lt (Empty) (a, b) = raise Missing
  | lookup lt (Node((x, y), left, right)) (a, b) =
    if x = a then y
    else
      if lt(x, a) then lookup lt right (a, b)
      else lookup lt left (a, b);

val t : (int, string) mapTree =
  Node((5, "cinque"),
    Node((3, "tre"),
      Node((1, "uno"), Empty, Empty),
      Node((4, "quattro"), Empty, Empty)),
    Node((8, "otto"),
      Node((6, "sei"), Empty, Empty),
      Node((10, "dieci"), Empty, Empty))
  );

val test1 = lookup lt t (5, "");
val test2 = lookup lt t (1, "");
val test3 = lookup lt t (6, "");
val test4 = lookup lt t (10, "");

(*datatype 'a btree = Empty | Node of 'a * 'a btree * 'a btree
type ('a, 'b) mapTree = ('a * 'b) btree
val lt = fn: int * int -> bool
exception Missing
val lookup = fn: (''a * ''a -> bool) -> (''a * 'b) btree -> ''a * 'c -> 'b
val t =
   Node
    ((5, "cinque"),
     Node
      ((3, "tre"), Node ((1, "uno"), Empty, Empty),
       Node ((4, "quattro"), Empty, Empty)),
     Node
      ((8, "otto"), Node ((6, "sei"), Empty, Empty),
       Node ((10, "dieci"), Empty, Empty))): (int, string) mapTree
val test1 = "cinque": string
val test2 = "uno": string
val test3 = "sei": string
val test4 = "dieci": string*)
```

> **Esercizio 8.10**
>
> Dato il tipo `('a, 'b) mapTree` definito in precedenza, scrivere la funzione `assign lt T a b` che cerca nel BST la coppia `(a, c)`. Se la trova, sostituisce `c` con `b`, altrimenti inserisce la coppia `(a, b)` nel posto corretto nel BST.
> Scrivere un `(int, string) mapTree` per testare la funzione.

```sml
datatype 'a btree =
  Empty |
  Node of 'a * 'a btree * 'a btree;

type ('a, 'b) mapTree = ('a * 'b) btree;

val lt = (op <);

fun assign lt (Empty) a b = (Node((a,b), Empty, Empty))
  | assign lt (Node((x,y), left, right)) a b =
    if x = a then (Node((x,b), left, right))
    else
      if lt(x, a) then (Node((x,y), left, assign lt right a b))
      else (Node((x,y), assign lt left a b, right))

val t : (int, string) mapTree =
  Node((5, "cinque"),
    Node((3, "tre"),
      Node((1, "uno"), Empty, Empty),
      Node((4, "quattro"), Empty, Empty)),
    Node((8, "otto"),
      Node((6, "sei"), Empty, Empty),
      Node((10, "dieci"), Empty, Empty))
  );

val test1 = assign lt t 1 "undici";
val test2 = assign lt t 7 "sette";

(*datatype 'a btree = Empty | Node of 'a * 'a btree * 'a btree
type ('a, 'b) mapTree = ('a * 'b) btree
val lt = fn: int * int -> bool
val assign = fn:
   (''a * ''a -> bool) -> (''a * 'b) btree -> ''a -> 'b -> (''a * 'b) btree
val t =
   Node
    ((5, "cinque"),
     Node
      ((3, "tre"), Node ((1, "uno"), Empty, Empty),
       Node ((4, "quattro"), Empty, Empty)),
     Node
      ((8, "otto"), Node ((6, "sei"), Empty, Empty),
       Node ((10, "dieci"), Empty, Empty))): (int, string) mapTree
val test1 =
   Node
    ((5, "cinque"),
     Node
      ((3, "tre"), Node ((1, "undici"), Empty, Empty),
       Node ((4, "quattro"), Empty, Empty)),
     Node
      ((8, "otto"), Node ((6, "sei"), Empty, Empty),
       Node ((10, "dieci"), Empty, Empty))): (int * string) btree
val test2 =
   Node
    ((5, "cinque"),
     Node
      ((3, "tre"), Node ((1, "uno"), Empty, Empty),
       Node ((4, "quattro"), Empty, Empty)),
     Node
      ((8, "otto"),
       Node ((6, "sei"), Empty, Node ((7, "sette"), Empty, Empty)),
       Node ((10, "dieci"), Empty, Empty))): (int * string) btree*)
```
