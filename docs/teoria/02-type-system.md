## Type systems

Il type system di un linguaggio comprende:

1. I tipi predefiniti
2. I meccanismi per definire nuovi tipi
3. La specificazione se i tipi sono controllati staticamente o dinamicamente
4. I meccanismi di controllo (equivalenza, compatibilità, inferenza)

### Tipi semplici vs tipi composti

- **Tipi semplici** (o scalari): sono i tipi primitivi, non derivano da altri tipi.
- **Tipi composti**: sono ottenuti dalla combinazione di altri tipi, usando appositi costruttori.

Con `type` si crea un **alias** di un tipo esistente, non un tipo nuovo e distinto. La sintassi è:

```sml
type nuovo_tipo = espressione_di_tipo;
```

Ad esempio, `type intlist = int list;` rende `intlist` un altro nome per `int list`.

### Controllo dei tipi

- **Statico**: avviene a tempo di compilazione, prima di arrivare all'utente. Dunque è più efficiente a runtime, ma il design è più complesso e la compilazione richiede più tempo.
- **Dinamico**: avviene durante l'esecuzione del codice. Identifica gli errori di tipo, ma lo fa soltanto a runtime e non è efficiente.

### Linguaggi Strongly typed vs linguaggi Weakly typed

- **Strongly typed**: il linguaggio impedisce le operazioni non valide per il tipo di un valore e garantisce che gli errori di tipo non passino inosservati (di solito tramite controlli statici).
- **Weakly typed**: il linguaggio è più permissivo e può permettere che errori di tipo passino inosservati (ad esempio tramite conversioni implicite o cast non controllati).

> **⚠️ Attenzione**
>
> ML è un linguaggio **strongly typed** che controlla i tipi in modo **statico**.

### Type safety

Un type system è **type safe** se non è possibile che errori di tipo passino inosservati. I linguaggi strongly typed hanno un alto grado di type safety.
C e C++ sono staticamente tipizzati, ma non sono type safe: cast espliciti, aritmetica dei puntatori e union permettono di aggirare i controlli.

### Meccanismi di controllo

#### Equivalenza di tipo

Due tipi sono equivalenti se ogni oggetto del primo tipo appartiene anche al secondo tipo e viceversa.
Esistono due regole per l'equivalenza di tipo:

1. **Equivalenza per nome**: definizione del tipo opaca.
   Due tipi sono equivalenti per nome se hanno lo stesso nome.
2. **Equivalenza strutturale**: definizione del tipo trasparente.
   Due tipi sono equivalenti se hanno la stessa struttura.

#### Compatibilità e conversione

`T` è compatibile con `S` se gli oggetti di tipo `T` possono essere usati in contesti dove ci si aspetta oggetti di tipo `S`.

> **Esempio**
>
> ```C++
> int n;
> float r;
> r = r + n;
> ```
> In alcuni linguaggi questo si può fare; in quei casi `int` e `float` sono compatibili.

La compatibilità è riflessiva e transitiva ma non è simmetrica.

Se `T` è compatibile con `S`, allora esiste qualche meccanismo di **conversione** tra i due. I due principali metodi sono:

- **Conversione implicita** (coercizione), non menzionata nel programma
- **Conversione esplicita** (cast), menzionata nel programma
I linguaggi moderni preferiscono il cast alla coercizione.

### Type errors in ML

```sml
> 1 + 2
(* val it = 3: int *)
> 1.0 + 2.0;
(* val it = 3.0: real *)
> 1 + 2.0;
(* poly: : error: Type error in function application.
Function: + : int * int -> int
Argument: (1, 2.0) : int * real
Reason:
Can't unify int (*In Basis*) with real (*In Basis*)
(Different type constructors)
Found near 1 + 2.0
Static Errors *)
> 1.0 + 2;
(* poly: : error: Type error in function application.
Function: + : real * real -> real
Argument: (1.0, 2) : real * int
Reason:
Can't unify int (*In Basis*) with real (*In Basis*)
(Different type constructors)
Found near 1.0 + 2
Static Errors *)
```

> **⚠️ Attenzione**
>
> L'operatore `+` è overloaded: ML ne deduce il tipo unificando i tipi degli argomenti. L'errore nasce quando i due argomenti hanno tipi che non possono essere unificati.

```sml
> #"a" ^ "bc";
(* poly: : error: Type error in function application.
Function: ^ : string * string -> string
Argument: (#"a", "bc") : char * string *)
> 1/2;
(* poly: : error: Type error in function application.
Function: / : real * real -> real
Argument: (1, 2) : int * int *)
> if 1<2 then #"a" else "bc";
(* poly: : error: Type mismatch between then-part and else-part.
Then: #"a" : char
Else: "bc" : string *)
```

### Conversione di tipi in ML

Non esiste la conversione automatica dei tipi in ML, deve essere fatta esplicitamente. A questo proposito sono fornite una serie di funzioni apposite.

#### Conversione tra interi e reali

- `real: int -> real`
- `floor: real -> int`, arrotonda per difetto
- `ceil: real -> int`, arrotonda per eccesso
- `round: real -> int`, arrotonda all'intero più vicino
- `trunc: real -> int`, tronca

```sml
> real(4);
(* val it = 4.0: real *)
> real 4;
(* val it = 4.0: real *)
> floor(3.5);
(* val it = 3: int *)
> ceil(3.5);
(* val it = 4: int *)
> round(3.5);
(* val it = 4: int *)
> trunc(3.5);
(* val it = 3: int *)
> floor(~3.5);
(* val it = ~4: int *)
> trunc(~3.5);
(* val it = ~3: int *)
```

#### Conversione tra caratteri e interi

- `ord: char -> int`
- `chr: int -> char`

```sml
> ord #"a";
(* val it = 97: int *)
> ord #"a" - ord #"A";
(* val it = 32: int *)
> chr 97;
(* val it = #"a": char *)
```

#### Conversione da caratteri a stringhe

- `str: char -> string`

```sml
> str #"a";
(* val it = "a": string *)
```

## Nomi, Oggetti denotabili e variabili

Un **nome** è una sequenza di caratteri usata per denotare qualcos'altro.
Un **oggetto denotabile** è un oggetto a cui può essere associato un nome.
Il **binding** è l'associazione tra un nome e un oggetto denotabile. Tali associazioni non sono fissate una volta per tutte.
L'**environment** è la collezione di tutte le associazioni tra nomi e oggetti denotabili a runtime a uno specifico punto del programma in uno specifico momento dell'esecuzione.
La **dichiarazione** è il meccanismo (implicito o esplicito) che crea le associazioni.

> **Osservazione**
>
> Lo stesso nome può indicare oggetti denotabili differenti in punti diversi del programma. Uno stesso oggetto può avere più nomi (alias) associati in punti diversi del codice.

Una **variabile** è un oggetto che può assumere dei valori all'interno di un dominio.

> **⚠️ Attenzione**
>
> In ML un'associazione creata con `val` non può essere riassegnata; esistono però le referenze (`ref`) per gestire stato mutabile.

### Variabili

Nei linguaggi di programmazione funzionali, come ML, una **variabile** è un identificatore associato a un valore; con `val` l'associazione non è modificabile, come in matematica.
L'environment di ML è l'insieme delle coppie `(identificatore, valore)` e viene esteso tramite le val-declarations (simili agli assegnamenti):

- `val <name> = <value>;`
- `val <name>:<type> = <value>;`
- `val <name> = <expression>;`
Questo comando crea un'associazione tra un nome e un valore.

```sml
> val pi = 3.14159;
(* val pi = 3.14159: real *)
> val v = 10.0/2.0;
(* val v = 5.0: real *)
```

> **Osservazione**
>
> Non è necessario specificare il tipo delle variabili; un'associazione creata con `val` non può essere modificata.

Se avviene una nuova dichiarazione di una variabile con lo stesso nome di una già precedentemente dichiarata, esisteranno due versioni diverse di tale variabile e, quando si proverà ad accedere alla variabile in questione, si accederà alla seconda. Ma la prima rimane in memoria.

```sml
> val pi = 3.14159;
(* val pi = 3.14159: real *)
> val radius = 4.0;
(* val radius = 4.0: real *)
> pi * radius * radius;
(* val it = 50.26544: real *)
> val area = pi * radius * radius;
(* val area = 50.26544: real *)
```

### Tipi complessi in ML

#### Tuple

```sml
> val t = (4, 5.0, "six");
(* val t = (4, 5.0, "six"): int * real * string *)
```

> **Osservazione**
>
> Una tupla può contenere al suo interno valori dai tipi diversi tra di loro.

```sml
> val t = (4, 5.0, "six");
(* val t = (4, 5.0, "six"): int * real * string *)
> val t = (1, (2, 3, 4));
(* val t = (1, (2, 3, 4)): int * (int * int * int) *)
```

Per accedere alle componenti di una tupla si usa `#`.

```sml
> val t = (4, 5.0, "six");
(* val t = (4, 5.0, "six"): int * real * string *)
> #1 (t);
(* val it = 4: int *)
> #3 (t);
(* val it = "six": string *)
> #4 (t);
(* poly: : error: Type error in function application.
Function: #4 : 'a * 'b * 'c * 'd -> 'd
Argument: (t) : int * real * string
Reason: Can't unify {4: 'a} to int * real * string (Field 4 missing)
Found near #4 (t)
Static Errors *)
```

#### Liste

Si rappresentano con le parentesi quadre. Tutti gli elementi di una lista devono essere dello stesso tipo.

```sml
> [1,2,3];
(* val it = [1, 2, 3]: int list *)
> [1.0,2.0];
(* val it = [1.0, 2.0]: real list *)
> [1,2.0];
(* poly: : error: Elements in a list have different types.
Item 1: 1 : int
Item 2: 2.0 : real
Reason:
Can't unify int (*In Basis*) with real (*In Basis*)
(Different type constructors) *)
> [];
(* val it = []: 'a list *)
```

> **Osservazione**
>
> Il tipo `'a` è un tipo generico: viene specificato solamente quando viene utilizzato.

- `hd` → primo elemento della lista

```sml
> val L = [2,3,4];
(* val L = [2, 3, 4]: int list *)
> val M = [5];
(* val M = [5]: int list *)
> hd(L);
(* val it = 2: int *)
> hd(M);
(* val it = 5: int *)
```

- `tl` → tutto ciò che non è il primo elemento della lista

```sml
> L;
(* val it = [2, 3, 4]: int list *)
> M;
(* val it = [5]: int list *)
> tl (L);
(* val it = [3, 4]: int list *)
> tl (M);
(* val it = []: int list *)
```

Si possono **concatenare le liste** con `@` (le due liste devono essere dello stesso tipo).

```sml
> [1,2] @ [3,4];
(* val it = [1, 2, 3, 4]: int list *)
> [1,2] @ ["a","b"];
(* poly: : error: Type error in function application.
Function: @ : int list * int list -> int list
Argument: ([1, 2], ["a", "b"]) : int list * string list
Reason:
Can't unify int (*In Basis*) with string (*In Basis*)
(Different type constructors) *)
```

Con `::` si può combinare un elemento e una lista dello stesso tipo. Questa operazione è associativa a destra.

```sml
> 2 :: [3,4];
(* val it = [2, 3, 4]: int list *)
> 2 :: nil;
(* val it = [2]: int list *)
> 2 :: [];
(* val it = [2]: int list *)
> 1 :: 2 :: 3 :: nil;
(* val it = [1, 2, 3]: int list *)
> (1 :: (2:: (3::nil)));
(* val it = [1, 2, 3]: int list *)
```

> **Osservazione**
>
> `nil` corrisponde ad una lista vuota.

Con `explode` si trasforma una stringa in una lista di caratteri.

```sml
> explode ("abcd");
(* val it = [#"a", #"b", #"c", #"d"]: char list *)
> explode ("");
(* val it = []: char list *)
```

E con `implode` si trasforma una lista di caratteri in una stringa.

```sml
> implode ([ #"a", #"b", #"c", #"d"]);
(* val it = "abcd": string *)
> implode (nil);
(* val it = "": string *)
> implode (explode ("xyz"));
(* val it = "xyz": string *)
```

## Il type system di ML

- Tipi primitivi: `int`, `real`, `bool`, `char`, `string`, `unit`
- Tipi complessi: due costruttori
    - `T1 * T2 * ... * Tn` (tuple)
    - `T list`

```sml
> [1, 2, 3];
(* val it = [1, 2, 3]: int list *)
> ("ab", [1,2,3], 4);
(* val it = ("ab", [1, 2, 3], 4): string * int list * int *)
> [[(1,2),(3,4)], [(5,6)], nil];
(* val it = [[(1, 2), (3, 4)], [(5, 6)], []]: (int * int) list list *)
```

## Funzioni in ML

Le funzioni (rappresentate come espressioni parametrizzate) sono un altro tipo di valore in ML.

La sintassi è `fn <param> => <expression>;`, ma si può anche applicare direttamente la funzione al parametro richiesto:

```sml
(fn n => n+1)5;
(* val it = 6: int *)
```

Si possono associare le funzioni a un nome, come se fossero valori:

```sml
> val increment = fn n => n+1;
(* val increment = fn: int -> int *)
```

Esiste anche una notazione sintattica semplificata per le funzioni con nome:

```sml
> fun increment n = n+1;
(* val increment = fn: int -> int *)
> increment 5;
(* val it = 6: int *)
```

In caso di ambiguità, ML assegna dei tipi di default. Ad esempio, nella prima definizione di `square(x)` il tipo assegnato è `int`: tra i tipi ammessi per `*`, `int` è quello di default.
È possibile specificare esplicitamente i tipi di una funzione:

```sml
> fun square (x) = x * x;
(* val square = fn: int -> int *)
> fun square (x:real) = x * x;
(* val square = fn: real -> real *)
```

Tutte le funzioni in ML hanno un solo parametro, ma questo può essere una tupla.

> **Esempio**
>
> Scriviamo una funzione che trova il massimo di tre numeri reali.

```sml
> fun max3(a:real,b,c) =
	if a>b then
		if a>c then a else c
		else
			if b>c then b else c;
(* val max3 = fn: real * real * real -> real *)
> max3(5.0,4.0,7.0);
(* val it = 7.0: real *)
```

---

[← Torna all'Indice del Corso](../index.md)
