## Pattern - *Parte 2*

### La keyword `as`

È anche possibile assegnare un nome ai valori passati come argomenti dei pattern, in contemporanea alla loro valutazione, con la sintassi `<identifier> as <pattern>`

```sml
> fun reverse (nil) = nil
	| reverse (L as x::xs) = reverse(xs) @ [x];
(* val reverse = fn: 'a list -> 'a list *)
```

> **Esempio**
>
> Scriviamo una funzione `merge` che unisca due liste di interi `L` e `M`, assumendo che entrambe siano ordinate in modo crescente, in modo tale che anche la lista finale risulti ordinata.

- Caso base: se `L` è vuota, allora restituiamo `M` (e viceversa)
- Passo induttivo: confrontiamo la testa di `L` e la testa di `M`. Aggiungiamo quella minore alla lista finale e ricorsivamente chiamiamo la funzione sull'altra lista e la tail di quella usata.

```sml
> fun merge (nil,M) = M
	| merge (L,nil) = L
	| merge (L as x::xs, M as y::ys) =
		if x<y then x::merge(xs,M)
		else y::merge (L,ys);
(* val merge = fn: int list * int list -> int list *)
```

### Variabile anonima (o wildcard)

Se vogliamo catturare una variabile ma non ci interessa usarla si può usare una wildcard, ossia nominarla con il simbolo `_`.

```sml
> fun comb (_,0) = 1
	| comb (n,k) =
		if k=n then 1
		else comb(n-1,k)+comb(n-1,k-1);
(* val comb = fn: int * int -> int *)
```

> **⚠️ Attenzione**
>
> Una variabile non può essere ripetuta in un pattern.

> **⚠️ Attenzione**
>
> Nei pattern non è consentito inserire:
>
> - operatori aritmetici
> - concatenazione di liste (`@`)
> - valori reali

Il pattern matching si può usare anche con la dichiarazione di funzione con `fn`.

```sml
> val day = fn 1 => "Monday"
			 | 2 => "Tuesday"
			 | _ => "Other";
(* val day = fn: int -> string *)
> day 5;
(* val it = "Other": string *)
```

### Costrutto `Case`

È possibile fare pattern matching anche tramite il costrutto `case`, con la seguente sintassi:

```sml
case <expression> of
	<pattern_1> => <expression_1>
	| <pattern_2> => <expression_2>
	...
	| <pattern_n> => <expression_n>
```

Deve essere esaustivo, quindi deve contenere anche il caso di default.

Il `case`, di fatto, lavora come il pattern matching, ma a differenza di quest'ultimo può gestire anche i risultati di un'espressione.

## Environment locale in ML

Per definire un environment locale si usa la seguente sintassi:

```sml
> fun name(par) =
	let
		val <first variable> = <first expression>;
		val <second variable> = <second expression>;
		…
		val <last variable> = <last expression>
	in
		<expression>
	end;
```

Dopo `let` si dichiarano le variabili locali e dopo `in` si possono usare nelle espressioni.

> **Esempio**
>
> Scrivere una funzione che calcola la potenza centesima di un reale `x`

```sml
> fun hundredthPower (x:real) =
	let
		val four = x*x*x*x;
		val twenty = four * four * four * four * four
	in
		twenty * twenty * twenty * twenty * twenty
	end;
(* val hundredthPower = fn: real -> real *)
> hundredthPower 1.01;
(* val it = 2.704813829: real *)
> hundredthPower 2.0;
(* val it = 1.2676506E30: real *)
```

O anche, equivalentemente,

```sml
> fun hundredthPower (x:real) =
	let
		val x = x*x*x*x;
		val x = x*x*x*x*x;
	in
		x*x*x*x*x
	end;
(* val hundredthPower = fn: real -> real *)
```

> **Esempio**
>
> Scrivere una funzione `split(L)` che divide una lista `L` in 2 liste:
>
> - una contenente il primo elemento, il terzo, il quinto, ...
> - una contenente il secondo, il quarto, ...

```sml
> fun split(nil) = (nil,nil)
	| split([a]) = ([a],nil)
	| split (a::b::cs) =
		let
			val (M,N) = split (cs)
		in
			(a::M,b::N)
		end;
(* val split = fn: 'a list -> 'a list * 'a list *)

> split [1,2,3,4,5];
(* val it = ([1,3,5], [2,4]): int list * int list *)
```

> **Esempio**
>
> Scrivere la funzione `mergeSort` che esegue l'algoritmo di merge sort su una lista, usando `merge` e `split`.

```sml
> fun merge (nil,M) = M
	| merge (L,nil) = L
	| merge (L as x::xs, M as y::ys) =
		if x<y then x::merge(xs,M)
		else y::merge (L,ys);
(* val merge = fn: int list * int list -> int list *)

> fun mergeSort (nil) = nil
	| mergeSort([a]) = [a]
	| mergeSort (L) =
		let
			val (M,N) = split(L);
			val M = mergeSort (M);
			val N = mergeSort (N)
		in
			merge (M,N)
		end;
(* val mergeSort = fn: int list -> int list *)
> mergeSort [1,4,2,3,8,7];
(* val it = [1, 2, 3, 4, 7, 8]: int list *)
> mergeSort([5,3,2,6,4,1]);
(* val it = [1, 2, 3, 4, 5, 6]: int list *)
```

---

[← Torna all'Indice del Corso](../index.md)
