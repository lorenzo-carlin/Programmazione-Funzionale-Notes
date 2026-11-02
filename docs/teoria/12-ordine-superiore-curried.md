Alcuni linguaggi permettono di passare funzioni come argomenti a procedure o anche di ritornare funzioni come valore di ritorno delle procedure.

## Funzioni come parametri di funzioni

La funzione viene passata come parametro ad un'altra funzione e poi viene chiamata tramite il parametro attuale.

```cpp
{
	int x = 1;

	int f(int y){
		return x+y;
	}

	void g (int h(int b)){
		int x = 2;
		return h(3) + x;
	}
	...
	{
		int x = 4;
		int z = g(f);
	}
}
```

La variabile `x` viene dichiarata tre volte. Quando chiamiamo `f`, quale `x` stiamo usando?

- se assumiamo di usare scope statico, allora usiamo la prima `x`, quella settata a 1
- se assumiamo di usare scope dinamico, il nome va risolto nell'ambiente attivo al momento della chiamata; per le funzioni passate come parametro bisogna però specificare se usare l'ambiente del passaggio (deep binding) o quello dell'invocazione (shallow binding)

## Regole di binding

Quando una procedura viene passata come parametro, si crea una referenza tra un nome (parametro formale `h`) e una procedura (parametro attuale `f`). Bisogna specificare quale environment non-locale viene applicato quando `f` viene eseguita, che può essere:

- quello al momento in cui `f` viene passata come argomento (**deep binding**)
- quello al momento in cui `f` viene invocata (**shallow binding**)

Nell'esempio precedente con deep binding si userebbe la terza `x`, mentre con shallow binding la seconda.

> **⚠️ Attenzione**
>
> Lo scope statico corrisponde sempre al deep binding.

## Funzioni come valore di ritorno di funzioni

La generazione di funzioni come valore di ritorno di una funzione permette la creazione dinamica di funzioni a runtime.

```cpp
{
	int x = 1;

	void->int F () {
		int g () {
			return x+1;
		}
		return g;
	}

	void->int gg = F();
	int z = gg();
}
```

- `void -> int` denota il tipo della funzione (in questo caso non prende nessun argomento e ritorna un `int`)
- `void -> int F()` è la dichiarazione della funzione, che ritorna una funzione che non prende nessun argomento e ritorna un `int`
- `return g` ritorna la funzione, senza farne il run
- `gg` viene dinamicamente associata con il valore di ritorno di `F` (ossia `g`)
- la funzione `gg` ritorna il successore della `x` catturata da `F`

## Funzioni di ordine superiore

> **Esempio**
>
> Supponiamo di voler scrivere una funzione che calcola l'approssimazione dell'integrale $\int_{a}^{b}f(x)dx$.

Quello che la funzione deve fare è dividere l'intervallo da `a` a `b` in `n` parti uguali e sommare le aree degli `n` trapezi risultanti.

Definiamo la funzione `trap(a,b,n,F)`, dove `F` è la funzione da integrare e viene presa come parametro.

```sml
> fun trap (a,b,n,F) =
	if n<=0 orelse b-a<=0.0 then 0.0
	else
		let
			val delta = (b-a)/real(n)
		in
			delta * (F(a)+F(a+delta))/2.0 + trap (a+delta,b,n-1,F)
		end;
(* val trap = fn: real * real * int * (real -> real) -> real *)

> fun square(x:real) = x*x;
(* val square = fn: real -> real *)

> trap (0.0,1.0,8,square);
(* val it = 0.3359375: real *)
```

> **Esempio**
>
> Scriviamo una funzione `simpleMap` che prende una lista $[a_1, ... a_n]$ e una funzione $f(x)$ in input e ritorna la lista $[f(a_1), ..., f(a_n)]$.

```sml
> fun simpleMap (F,nil) = nil
	| simpleMap (F,x::xs) = F(x) :: simpleMap(F,xs);
(* val simpleMap = fn: ('a -> 'b) * 'a list -> 'b list *)
> simpleMap (square, [1.0,2.0,3.0]);
(* val it = [1.0, 4.0, 9.0]: real list *)
> simpleMap (op ~, [1,2,3]);
(* val it = [~1, ~2, ~3]: int list *)
> simpleMap ( fn x => x*x, [1.0,2.0,3.0]);
(* val it = [1.0, 4.0, 9.0]: real list *)
```

> **Osservazione**
>
> `#1` è una funzione polimorfica: il tipo della tupla viene inferito dall'uso. Ad esempio `fun f x = #1 x` ha tipo `'a * 'b -> 'a`.

> **Esercizio**
>
> Scrivere una funzione `reduce` come segue:
>
> - $[a_1]$ ritorna $a_1$
> - $[a_1, ..., a_n]$: riduce la tail applicando una funzione $F$ che prende una coppia e ritorna $b$, poi calcola $F(a_1,b)$, ossia $reduce(F,[a_1, ..., a_n])=F(a_1,F(a_2,...F(a_{n-1},a_n)))$

Questa funzione è tale che se la funzione in input è la somma restituisce la somma di tutti gli elementi, se è l'operatore di prodotto ritorna il prodotto di tutti gli elementi, e così via...

```sml
> exception EmptyList;
(* exception EmptyList *)

> fun reduce (F,nil) = raise EmptyList
	| reduce (F,[a]) = a
	| reduce (F,x::xs) = F(x, reduce(F,xs));
(* val reduce = fn: ('a * 'a -> 'a) * 'a list -> 'a *)
```

> **Esercizio**
>
> Usare le funzioni `simpleMap` e `reduce` per calcolare la varianza di una lista di reali.

La varianza di una lista di reali è definita come

$$
\mathrm{Var}(a_1, \dots, a_n) = \frac{\sum_{i=1}^{n} a_i^2}{n} - \left( \frac{\sum_{i=1}^{n} a_i}{n} \right)^2
$$

Definiamo due funzioni

```sml
> fun square (x:real) = x*x;
(* val square = fn: real -> real *)

> fun plus (x:real,y) = x+y;
(* val plus = fn: real * real -> real *)
```

La funzione per il calcolo della varianza risulta essere

```sml
> fun variance (L) =
	let
		val n = real(length(L))
	in
		reduce(plus,simpleMap(square,L))/n - square(reduce(plus,L)/n)
	end;
(* val variance = fn: real list -> real *)

> variance ([1.0,2.0,5.0,8.0]);
(* val it = 7.5: real *)
```

## `op`

Usando `op` è possibile convertire un operatore infisso in un operatore prefisso.

```sml
> reduce (+, [1,2,3]);
(* poly: : warning: (+) has infix status but was not preceded by op. *)
> fun plus (x,y) = x+y;
(* val plus = fn: int * int -> int *)
> reduce(plus, [1,2,3]);
(* val it = 6: int *)

> reduce (op +, [1,2,3]);
(* val it = 6: int *)
```

> **Esercizio**
>
> Scrivere una funzione `filter` che prende come input una funzione booleana ed una lista e ritorna la lista contenente soltanto gli elementi che soddisfano la condizione della funzione booleana.

```sml
> fun filter (P,nil) = nil
	| filter (P,x::xs) =
		if P(x) then x::filter(P,xs)
		else filter (P,xs);
(* val filter = fn: ('a -> bool) * 'a list -> 'a list *)
> filter (fn x => x>=10, [1,10,23,5,16]);
(* val it = [10, 23, 16]: int list *)
```

## Curried functions

In ML una funzione ha un solo parametro. Quindi una funzione a due argomenti in realtà è:

- una funzione che prende come argomento una tupla
- oppure una funzione che restituisce un'altra funzione (currying)

> **Esempio**
>
> Scriviamo una funzione che calcola l'elevamento a potenza.

```sml
> fun exponent1 (x,0) = 1.0
	| exponent1 (x,y) = x * exponent1 (x,y-1);
(* val exponent1 = fn: real * int -> real *)
> exponent1 (3.0,4);
(* val it = 81.0: real *)
```

Questo è il primo modo possibile, classico.

```sml
> fun exponent2 x 0 = 1.0
	| exponent2 x y = x * exponent2 x (y-1);
(* val exponent2 = fn: real -> int -> real *)
> exponent2 3.0 4 ;
(* val it = 81.0: real *)
```

Questo è un altro modo, che fa uso del currying. Il significato del tipo della funzione (`real -> int -> real`) è in realtà `real -> (int -> real)`, cioè:

- prende un `real`
- restituisce una funzione `int -> real`

Quando scriviamo `exponent2 3.0 4` ML lo interpreta come `(exponent2 3.0) 4`: `exponent2 3.0` restituisce una funzione, che viene poi applicata al parametro `4`.

### Applicazione parziale

La forma curried è utile perché permette di creare delle funzioni parzialmente applicate (anche dette funzioni specializzate), dove solo alcuni argomenti sono dati.

```sml
> val g = exponent2 3.0;
(* val g = fn: int -> real *)
> g 4;
(* val it = 81.0: real *)
> g (4);
(* val it = 81.0: real *)
```

Nella prima riga abbiamo applicato parzialmente la funzione `exponent2`.  `g` è la funzione potenza con base `3.0`.

---

[← Torna all'Indice del Corso](../index.md)
