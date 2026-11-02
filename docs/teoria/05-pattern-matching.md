## Pattern - *Parte 1*

Sono una generalizzazione degli statement `case` o `switch` nei linguaggi procedurali. Sono molto potenti nella definizione delle funzioni.
La definizione delle funzioni usa una sequenza di pattern. Il primo che matcha l'argomento determina il valore ritornato.

```sml
fun <identifier> (<first pattern>) = <first expression>
  | <identifier> (<second pattern>) = <second expression>
  ...
  | <identifier> (<last pattern>) = <last expression>;
```

> **Esempio**
>
> Riscriviamo la funzione `reverse` per invertire una lista, con e senza il pattern matching.

- usando il pattern matching:

```sml
> fun reverse (nil) = nil
    | reverse (x::xs) = reverse(xs) @ [x];
(* val reverse = fn: 'a list -> 'a list *)
```

Il pattern `x::xs` matcha quando trova `elemento::lista`.

- senza il pattern matching:

```sml
> fun reverse L =
    if L = nil then nil
	else reverse (tl L) @ [hd L];
(* val reverse = fn: ''a list -> ''a list *)
```

> **⚠️ Attenzione**
>
> La lista di alternative espressa nei pattern deve essere esaustiva (come un `if-then-else`). Altrimenti viene restituito un errore, come segue.

```sml
> fun reverse (nil) = nil;
(* poly: : warning: Matches are not exhaustive. Found near fun
reverse (nil) = nil
val reverse = fn: 'a list -> 'b list *)
> reverse([3]);
(* poly: : warning: The type of (it) contains a free type variable.
Setting it to a unique monotype.
Exception- Match raised *)
```

> Gli esercizi di questa parte sono nel [Laboratorio 3](../laboratori/03-laboratorio-3.md).

---

[← Torna all'Indice del Corso](../index.md)
