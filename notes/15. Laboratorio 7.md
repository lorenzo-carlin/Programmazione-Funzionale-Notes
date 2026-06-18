
---

>[!esercizio] Esercizio 7.1
>Data una funzione `F`, che prende n parametri (con n fissato, in questo caso 3), definire una funzione curried che applica `F` e produce una funzione `G` tale che: $G x_1 ... x_n = F(x_1, ..., x_n)$.

```sml
> fun curry f a b c = f(a,b,c);
(* val curry = fn: ('a * 'b * 'c -> 'd) -> 'a -> 'b -> 'c -> 'd *)
> curry(fn(x,y,z)=>x*y*z) 1 2 3;
(* val it = 6: int *)
```

>[!esercizio] Esercizio 7.2
>Usare `map`, `foldr`, `foldl` per convertire una lista di interi in una lista di reali.

```sml
> fun toReal(l) = map (real) l;
(* val toReal = fn: int list -> real list *)
> toReal([1,2,3]);
(* val it = [1.0, 2.0, 3.0]: real list *)
```

>[!esercizio] Esercizio 7.3
>Usare `map`, `foldr`, `foldl` per calcolare l'AND logico di una lista di booleani.

```sml
> fun andb(L: bool list) = foldr (fn(a,b) => (a andalso b)) true L;
(* val andb = fn: bool list -> bool *)
> andb [true, false, true];
(* val it = false: bool *)
```

>[!esercizio] Esercizio 7.4
>Usare `map`, `foldr`, `foldl` per definire la funzione `implode`.

```sml
> fun implode(L) = foldl (fn(a: char, b: string) => (b^str(a))) "" L;
(* val implode = fn: char list -> string *)
> implode[#"b",#"c"];
(* val it = "bc": string *)
```

>[!esercizio]  Esercizio 7.5
>Dato un datatype `btree`, scrivere la funzione `postOrder` che ritorna la lista dei nodi di un albero binario visitato in post-order. Ossia la label di un nodo segue l'attraversamento post-order di entrambi i suoi sottoalberi.

```sml
> datatype 'a btree = 
    Empty |
    Node of 'a * 'a btree * 'a btree;

> fun postOrder Empty = nil
    | postOrder(Node(v, lTree, rTree)) = postOrder(lTree) @ postOrder(rTree) @ [v];

(* datatype 'a btree = Empty | Node of 'a * 'a btree * 'a btree
val postOrder = fn: 'a btree -> 'a list *)

> postOrder (Node ("ML", Node ("as", Node ("a", Empty, Empty), Node ("in", Empty, Empty)), Node ("types", Empty, Empty)));
(* val it = ["a", "in", "as", "types", "ML"]: string list *)
```

>[!esercizio] Esercizio 7.6
>Dato il datatype `btree`, scrivere una funzione `inOrder` che ritorna la lista dei nodi di un albero binario visitato in in-order. Ossia la label di un nodo si trova tra l'attraversamento in-order del suo sottoalbero di sinistra e quello di destra.

```sml
> datatype 'a btree =
    Empty |
    Node of 'a * 'a btree * 'a btree;

> fun inOrder Empty = nil
    | inOrder(Node(v, lTree, rTree)) = inOrder(lTree) @ [v] @ inOrder(rTree);
    
> inOrder (Node ("ML", Node ("as", Node ("a", Empty, Empty), Node ("in", Empty, Empty)), Node ("types", Empty, Empty)));
(* val it = ["a", "as", "in", "ML", "types"]: string list *)
```

>[!esercizio] Esercizio 7.7
>Definire un tipo `mapTree` che è una specializzazione di `btree` tale per cui ha la label che è un insieme di coppie. Definire un albero `t1` che ha un singolo nodo e ha la coppia `("a", 1)` come label.

```sml
> datatype ('a, 'b) mapTree =
    Empty |
    Node of ('a * 'b) list * ('a, 'b) mapTree * ('a, 'b) mapTree;

> val t1 = Node([("a", 1)], Empty, Empty);

(* datatype ('a, 'b) mapTree =
    Empty
  | Node of ('a * 'b) list * ('a, 'b) mapTree * ('a, 'b) mapTree
val t1 = Node ([("a", 1)], Empty, Empty): (string, int) mapTree
val it = (): unit *)
```

>[!esercizio] Esercizio 7.8
>Scrivere una funzione `sumTree` per un `mapTree` T di tipo `('a, 'b) mapTree`. La funzione visita l'albero e ritorna la somma della seconda componente di tutte le label dei nodi.

```sml
> datatype ('a, 'b) mapTree =
    Empty |
    Node of ('a * 'b) * ('a, 'b) mapTree * ('a, 'b) mapTree;

> fun sumTree Empty = 0
    | sumTree(Node((u,v), lTree, rTree)) = v + sumTree(lTree) + sumTree(rTree);

(* datatype ('a, 'b) mapTree =
    Empty
  | Node of ('a * 'b) * ('a, 'b) mapTree * ('a, 'b) mapTree
val sumTree = fn: ('a, int) mapTree -> int
val it = (): unit *)

> sumTree (Node(("a",1), Node(("c",2), Empty, Node(("d",3), Empty, Empty)), Empty));
(* val it = 6: int *)
```

>[!esercizio] Esercizio 7.9
>Dato il datatype `btree`, definire una funzione `countInternalNodes` di tipo `('a -> bool) -> 'a btree -> int` che prende un predicato `p` (una funzione di tipo `'a -> bool`) e un `'a btree` e ritorna il numero di nodi interni (ossia nodi che hanno almeno un subtree non vuoto), il cuo valore soddisfa il predicato.

```sml
> datatype 'a btree =
    Empty |
    Node of 'a * 'a btree * 'a btree;

> fun countInternalNodes p Empty = 0
    | countInternalNodes p (Node(v, Empty, Empty)) = 0
    | countInternalNodes p (Node(v, lTree, rTree)) =
      if p(v) then 1+countInternalNodes p lTree + countInternalNodes p rTree
      else countInternalNodes p lTree + countInternalNodes p  rTree;

(* datatype 'a btree = Empty | Node of 'a * 'a btree * 'a btree
val countInternalNodes = fn: ('a -> bool) -> 'a btree -> int *)

> countInternalNodes (fn x => x>5) (Node(10, Node(8, Empty, Empty), Empty));
(* val it = 1: int *)
```

>[!esercizio] Esercizio 7.10
>Dato il datatype `bltree`, definire una funzione `doubleTree` di tipo `int bltree -> int bltree` che prende un albero di interi e ritorna un nuovo albero dove ogni valore (sia sulle foglia che sui nodi) viene moltiplicato per 2.

```sml
> datatype 'a bltree = 
      Empty
    | Leaf of 'a
    | Node of 'a * 'a bltree * 'a bltree;

> fun doubleTree Empty = Empty
    | doubleTree (Leaf(v)) = Leaf(2*v)
    | doubleTree (Node(v, lTree, rTree)) = Node(2*v, doubleTree(lTree), doubleTree(rTree));

(* datatype 'a bltree = Empty | Leaf of 'a | Node of 'a * 'a bltree * 'a bltree
val doubleTree = fn: int bltree -> int bltree *)

> doubleTree (Node(10, Leaf(5), Node(3, Empty, Leaf(1))));
(* val it = Node (20, Leaf 10, Node (6, Empty, Leaf 2)): int bltree *)
```