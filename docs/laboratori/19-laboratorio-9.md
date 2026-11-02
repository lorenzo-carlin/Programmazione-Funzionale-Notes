>[!esercizio] Esercizio 9.1
>Dato il tipo `tree`, per la rappresentazione di un generico albero, scrivere una funzione `isOn` che, dato un elemento `x` e un albero generico `T`, dice se `x` appare tra le label di `T`.

```sml
> datatype ('label) tree =
    Node of 'label * 'label tree list;

> fun isOn x (Node(y, nil)) = if x = y then true else false
    | isOn x (Node(y, u::ux)) = (isOn x (Node(y, ux)) orelse (isOn x u));

> isOn 3 (Node(2, [Node (3,nil), Node(5,nil)]));

(* datatype 'a tree = Node of 'a * 'a tree list
val isOn = fn: ''a -> ''a tree -> bool
val it = true: bool *)
```

>[!esercizio] Esercizio 9.2
>Dato il tipo `tree`, per la rappresentazione di un generico albero, scrivere una funzione `count(T, x)` che, dato un albero `T` e un elemento `x`, ritorna il numero di occorrenze di `x` tra le label di `T`.

```sml
> datatype ('label) tree =
    Node of 'label * 'label tree list;

> fun count (Node(y, nil)) x = (if x = y then 1 else 0)
    | count (Node(y, u::ux)) x = ((count u x) + (count (Node(y, ux)) x));

> count(Node(2, [Node(3,nil), Node(2,nil)])) 2;

(* datatype 'a tree = Node of 'a * 'a tree list
val count = fn: ''a tree -> ''a -> int
val it = 2: int *)
```

>[!esercizio] Esercizio 9.3
>Dato il tipo `tree`, per la rappresentazione di un generico albero, scrivere una funzione `depth` che, dato un albero `T`, ritorna la profondità di `T`.

```sml
> datatype ('label) tree =
    Node of 'label * 'label tree list;

> fun depth (Node(y, nil)) = 1
    | depth (Node(y, u::ux)) =
      let
        val t1 = depth (Node(y, ux))
        val t2 = depth u + 1
      in
        if t1 > t2 then t1 else t2
      end;

> depth (Node(2, [Node(3, [Node(4, nil)]), Node(2, nil)]));

(* datatype 'a tree = Node of 'a * 'a tree list
val depth = fn: 'a tree -> int
val it = 3: int *)
```

>[!esercizio] Esercizio 9.4
>Dato il tipo `tree`, per la rappresentazione di un generico albero, scrivere una funzione `preOrder` che, dato un albero `T`, ritorna la lista dei nodi di `T` in pre-ordine.

```sml
> datatype ('label) tree =
    Node of 'label * 'label tree list;

> fun preOrderList nil = nil
    | preOrderList (t::ts) = preOrder t @ preOrderList ts
  and preOrder (Node(y, children)) = y :: preOrderList children;

> preOrder(Node(2, [Node(3, [Node(4, nil)]), Node(2, nil)]));

(* datatype 'a tree = Node of 'a * 'a tree list
val preOrderList = fn: 'a tree list -> 'a list
val preOrder = fn: 'a tree -> 'a list
val it = [2, 3, 4, 2]: int list *)
```

>[!esercizio] Esercizio 9.5
>Definire una structure `Tree` contenente il datatype `tree` per la rappresentazione di un albero generico. La structure deve contenere:
>- `create(a)`, che ritorna un nodo dell'albero con label a
>- `build(a, L)`, che ritorna un albero con la radice che ha label a e ha L come lista dei sottoalberi
>- `subtree(i, T)`, che trova l'i-esimo sottoalbero della radice, con tanto di eccezione `Missing` se questo non esiste.
>Costruire un albero `myTree` usando le funzioni della structure e testarne le funzionalità.

```sml
> structure Tree = struct
    datatype ('label) tree =
      Node of 'label * 'label tree list

    exception Missing

    fun create(a) = Node(a, nil)

    fun build(a, L) = Node(a, L)

    fun subtree(i, (Node(a, nil))) = raise Missing
      | subtree(1, (Node(a, x::xs))) = x
      | subtree(i, (Node(a, x::xs))) = subtree(i-1, (Node(a,xs)))
end;

> val v4 = Tree.create(4);
> val v3 = Tree.build(3, [v4]);
> val v2 = Tree.create(2);
> val v1 = Tree.build(2, [v3, v2]);

> Tree.subtree(2, v1);

(*structure Tree:
  sig
    exception Missing
    val build: 'a * 'a tree list -> 'a tree
    val create: 'a -> 'a tree
    val subtree: int * 'a tree -> 'a tree
    datatype 'a tree = Node of 'a * 'a tree list
  end
val v4 = Node (4, []): int Tree.tree
val v3 = Node (3, [Node (4, [])]): int Tree.tree
val v2 = Node (2, []): int Tree.tree
val v1 = Node (2, [Node (3, [Node (4, [])]), Node (2, [])]): int Tree.tree
val it = Node (2, []): int Tree.tree *)
```

>[!esercizio] Esercizio 9.6
>Nell'esercizio precedente, `create(a)` corrisponde a fare `build(a, nil)`. Definire una nuova structure `SimpleTree` che ha le stesse funzionalità di `Tree` tranne `create()` e che pone le label tutte di interi.

```sml
> signature SIMPLE = sig
    datatype 'label tree =
      Node of 'label * 'label tree list

    exception Missing

    val build: int * int tree list -> int tree
    val subtree: int * int tree -> int tree
  end;

> structure Tree = struct
    datatype ('label) tree =
      Node of 'label * 'label tree list

    exception Missing

    fun create(a) = Node(a, nil)

    fun build(a, L) = Node(a, L)

    fun subtree(i, (Node(a, nil))) = raise Missing
      | subtree(1, (Node(a, x::xs))) = x
      | subtree(i, (Node(a, x::xs))) = subtree(i-1, (Node(a,xs)))
  end;

> structure SimpleTree : SIMPLE = Tree;

(* signature SIMPLE =
  sig
    exception Missing
    val build: int * int tree list -> int tree
    val subtree: int * int tree -> int tree
    datatype 'a tree = Node of 'a * 'a tree list
  end
structure Tree:
  sig
    exception Missing
    val build: 'a * 'a tree list -> 'a tree
    val create: 'a -> 'a tree
    val subtree: int * 'a tree -> 'a tree
    datatype 'a tree = Node of 'a * 'a tree list
  end
structure SimpleTree: SIMPLE *)
```

>[!esercizio] Esercizio 9.7
>Utilizzare la funzione `build()` di `SimpleTree` per costruire un albero con radice con label 1 e tre figli con label 2,3,4. Applicare `subtree` per ottenere il secondo subtree della radice.

```sml
> val root = SimpleTree.build(1, [SimpleTree.build(2, []), SimpleTree.build(3, []), SimpleTree.build(4, [])]);

> val s2 = SimpleTree.subtree(2, root);

(* val root = Node (1, [Node (2, []), Node (3, []), Node (4, [])]):
   int SimpleTree.tree
val s2 = Node (3, []): int SimpleTree.tree *)
```

>[!esercizio] Esercizio 9.8
>Definire una structure `Stack` che rappresenta uno stack di elementi di un tipo arbitrario. Includere le funzioni:
>- `create`, per creare uno stack vuoto
>- `push x s`, che inserisce `x` in cima allo stack
>- `pop s`, che ritorna lo stack senza il primo elemento oppure alza un'eccezione `EmptyStack`
>- `isEmpty s`, che controlla se lo stack è vuoto
>- `top s`, che ritorna l'elemento in cima allo stack o alza `EmptyStack`.

```sml
> structure Stack = struct
    type 'a stack = 'a list;
    exception EmptyStack;
    val emptyStack = [];

    fun create() = emptyStack;

    fun push x s = (x::s);

    fun pop nil = raise EmptyStack
      | pop (x::xs) = xs;

    fun isEmpty nil = true
      | isEmpty s = false;

    fun top nil = raise EmptyStack
      | top (x::xs) = x;
  end;

(* structure Stack:
  sig
    exception EmptyStack
    val create: unit -> 'a list
    val emptyStack: 'a list
    val isEmpty: 'a list -> bool
    val pop: 'a list -> 'a list
    val push: 'a -> 'a list -> 'a list
    eqtype 'a stack
    val top: 'a list -> 'a
  end *)
```

>[!esercizio] Esercizio 9.9
>Si realizzi una signature che permetta di creare una structure `StringStack`, i cui elementi sono di tipo string e che omette l'operazione `top`.

```sml
> signature StringStack = sig
    type 'a stack
    exception EmptyStack
    val emptyStack: string stack
    val create: unit -> string stack
    val push: string -> string stack -> string stack
    val pop: string stack -> string stack
    val isEmpty: string stack -> bool
  end;

(* signature StringStack =
  sig
    exception EmptyStack
    val create: unit -> string stack
    val emptyStack: string stack
    val isEmpty: string stack -> bool
    val pop: string stack -> string stack
    val push: string -> string stack -> string stack
    type 'a stack
  end *)
```

>[!esercizio] Esercizio 9.10
>Realizzare una structure `Queue` che rappresenta una coda di elementi. Includere:
>- `create`, per creare una coda vuota
>- `EmptyQueue`, un'eccezione
>- `Enqueue(x, Q)`, che aggiunge un elemento alla fine e ritorna la coda
>- `Dequeue Q`, che ritorna la coppia del primo elemento della coda e il resto della coda. Se è vuota, alza `EmptyQueue`
>- `isEmpty Q`, che controlla se la coda è vuota

```sml
> structure Queue = struct
    type 'a queue = 'a list;

    exception EmptyQueue;

    val create = nil;

    fun Enqueue(x, Q) = Q @ [x];

    fun Dequeue nil = raise EmptyQueue
      | Dequeue Q = (hd(Q), tl(Q));

    fun isEmpty nil = true
      | isEmpty Q = false;
  end;

(* structure Queue:
  sig
    val Dequeue: 'a list -> 'a * 'a list
    exception EmptyQueue
    val Enqueue: 'a * 'a list -> 'a list
    val create: 'a list
    val isEmpty: 'a list -> bool
    eqtype 'a queue
  end *)
```

>[!esercizio] Esercizio 9.11
>Realizzare una signature per creare una structure `PairQueue` di coppie formate da una string e un intero, con le stesse operazioni di `Queue`.

```sml
> signature PAIR_QUEUE = sig
    type 'a queue;
    exception EmptyQueue;
    val create: (string * int) queue;
    val Enqueue: ((string * int) * (string * int) queue) -> (string * int) queue;
    val Dequeue: (string * int) queue -> ((string * int) * (string * int) queue);
    val isEmpty: (string * int) queue -> bool
  end;

(* signature PAIR_QUEUE =
  sig
    val Dequeue:
       (string * int) queue -> (string * int) * (string * int) queue
    exception EmptyQueue
    val Enqueue:
       (string * int) * (string * int) queue -> (string * int) queue
    val create: (string * int) queue
    val isEmpty: (string * int) queue -> bool
    type 'a queue
  end *)
```

>[!esercizio] Esercizio 9.12
>Scrivere una structure `IntTriple` che implementa la signature `TOTALORDER` che, al posto di `string`, definisce gli elementi di un albero binario di ricerca come tuple di 3 interi.
>La funzione `lt((a, b, c), (x, y, z))` è vera se:
>- $a < x$
>- $a = x$ e $b < y$
>- $a = x$, $b = y$ e $c < z$
>Usare il funtore `MakeBST` per ottenere una structure che conserva le triple di interi in alberi binari.

```sml
> signature TOTALORDER = sig
	type element;
	val lt : element * element -> bool
  end;
(* signature TOTALORDER = sig type element val lt: element * element -> bool end; *)

functor MakeBST(Lt: TOTALORDER):
	sig
		type 'label btree;
		exception EmptyTree;
		val create: Lt.element btree;
		val lookup: Lt.element * Lt.element btree -> bool;
		val insert: Lt.element * Lt.element btree -> Lt.element btree;
		val deletemin : Lt.element btree -> Lt.element * Lt.element btree;
		val delete : Lt.element * Lt.element btree -> Lt.element btree
	end
	=
	struct
		open Lt;
		datatype 'label btree
			= Empty
			| Node of 'label * 'label btree * 'label btree;
		val create = Empty;
		fun lookup(x, Empty) = false
			| lookup(x, Node(y, left, right)) =
				if lt(x, y)
				then lookup(x, left)
				else if lt(y, x)
					then lookup(x, right)
					else (* x=y *) true;
		fun insert(x, Empty) = Node(x, Empty, Empty)
		  | insert(x, T as Node(y, left, right)) =
			if lt(x, y)
			then Node(y, insert(x, left), right)
			else
				if lt(y, x)
				then Node(y, left, insert(x, right))
				else (* x=y *) T; (* do nothing; x was already there *)
		exception EmptyTree;
		fun deletemin(Empty) = raise EmptyTree
		  | deletemin(Node(y, Empty, right)) = (y, right)
		  | deletemin(Node(w, left, right)) = let
				val (y, L) = deletemin(left)
			in
				(y, Node(w, L, right))
			end;
		fun delete(x, Empty) = Empty
		  | delete(x, Node(y, left, right)) =
			if lt(x, y)
			then Node(y, delete(x, left), right)
			else if lt(y, x)
				then Node(y, left, delete(x, right))
				else (* x=y *) case (left, right)
					of (Empty, r) => r
					| (l, Empty) => l
					| (l, r) => let
					val (z, r1) = deletemin(r)
					in
						Node(z, l, r1)
					end;
end;

structure IntTriple: TOTALORDER = struct
	type element = int * int * int;
	fun lt((l1, l2, l3), (r1, r2, r3)) =
		l1 < r1 orelse
		(l1 = r1 andalso l2 < r2) orelse
		(l1 = r1 andalso l2 = r2 andalso l3 < r3);
end;

(* structure IntTriple: TOTALORDER *)

structure IntTripleBST = MakeBST (IntTriple);
```
