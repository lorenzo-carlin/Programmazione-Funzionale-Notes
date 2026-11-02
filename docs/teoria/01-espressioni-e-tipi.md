# 01. Introduzione a Standard ML, Espressioni e Tipi

## Introduzione a ML

- ML è un linguaggio di **programmazione funzionale**: le protagoniste sono le funzioni, con le loro definizioni e applicazioni.
- In ML viene fatto massiccio uso della **ricorsione**, al posto di costrutti come i cicli `for` e `while`.
- Le regole di `if-then-else` vengono implementate tramite il **pattern matching**, ossia un insieme di regole del tipo:
  se il valore ha questa forma → fai {questo},
  altrimenti → fai {quest'altro}
- In ML la computazione avviene principalmente tramite valutazione di espressioni e non tramite assegnazioni che modificano le variabili. Il linguaggio, però, non è puro: mette a disposizione comandi come la stampa e le referenze, che producono side effect e non fanno parte del paradigma funzionale.
- I tipi di valori e variabili sono controllati a tempo di compilazione. ML è un linguaggio **strongly-typed**, ossia prevede una notevole rigidità sui tipi.
- Una funzione può avere più tipi (firme), differenti l'una dall'altra. Questo comportamento prende il nome di **polimorfismo**.
- I **Data Types** in ML permettono di costruire nuovi tipi a partire dai tipi primitivi.

## Espressioni e Comandi

Le **espressioni** sono entità sintattiche la cui valutazione produce un valore oppure non termina (*undefined expression*).

Esistono due modi per valutare le espressioni:

1. **eager evaluation**: valuta prima tutti gli operandi e solo dopo applica gli operatori.
2. **lazy evaluation**: valuta gli operandi solo quando strettamente necessario.

📌 **Esempio: Lazy Evaluation**

```cpp
if (a && b && c) {}
```

In questo caso un linguaggio come C++ applica la *lazy evaluation*: se `a` è `false` non va a valutare il resto dell'espressione, perché sa già che sarà per forza falsa.

Anche **ML** usa la valutazione lazy (non stretta) per i costrutti `andalso`, `orelse` e `if-then-else`. **Altrimenti** usa **sempre** la **eager evaluation**.

```sml
> 1+2*3;
(* val it = 7: int *)
```

- `val`: valore dell'espressione
- `it`: nome del risultato
- `int`: tipo del risultato (assegnato automaticamente)

I **comandi** sono entità sintattiche la cui valutazione non ritorna necessariamente un valore ma può avere un side effect. Per questo motivo la programmazione funzionale pura tende a evitarli.

Un **side effect** è un qualsiasi cambio nello stato del sistema. Il più comune, che si verifica nei linguaggi imperativi, è la modifica del valore di una variabile.

ML non è un linguaggio puro: **consente i side effect** tramite l'I/O e le referenze (`ref`), anche se il paradigma funzionale li evita.

## Tipi di Dati in ML

Un **data type** è un insieme di valori e di operatori definiti su tali valori.

### Tipi Primitivi

- **`int`** → interi decimali ed esadecimali:

```sml
> 0x124;
(* val it = 292: int *)
> ~0x124;
(* val it = ~292: int *)
```

> **⚠️ Attenzione — Simbolo di Negazione**
>
> In ML non si utilizza il simbolo `-` per indicare il segno meno dei numeri, si usa invece il simbolo `~`.
> Il simbolo `-` è riservato esclusivamente all'operatore di sottrazione.

- **`real`** → reali (scritti per intero oppure usando `E`/`e` come potenza di 10):

```sml
> ~123.0;
(* val it = ~123.0: real *)
> 3E~3;
(* val it = 0.003: real *)
> 3.14e12;
(* val it = 3.14E12: real *)
```

- **`bool`** → `true` o `false`:

```sml
> true;
(* val it = true: bool *)
> 1 = 3;
(* val it = false: bool *)
```

- **`char`** → singoli caratteri, indicati come `#"<carattere>"`:

```sml
> #"a";
(* val it = #"a": char *)
```

- **`string`** → stringhe, racchiuse tra doppi apici `" "`:

```sml
> "foo";
(* val it = "foo": string *)
```

> **Osservazione — Caratteri Speciali nelle Stringhe**
>
> ML prevede i classici caratteri di escape:
>
> - `\n`: newline
> - `\t`: tab
> - `\\`: backslash
> - `\"`: doppi apici
> - `\ddd`: carattere espresso da tre cifre decimali `ddd`

- **`unit`** → assume un solo valore, ossia `()`. È usato per le espressioni che non ritornano un valore informativo.

## Operatori in ML

### Operatori Aritmetici

- `+` → somma
- `-` → differenza
- `*` → moltiplicazione
- `/` → divisione tra reali
- `div` → divisione intera (arrotonda per difetto)
- `mod` → resto della divisione intera

```sml
> 3.0 - 4.5 + 6.7;
(* val it = 5.2: real *)
> 3 - 4 * 2;
(* val it = ~5: int *)
> 43 div (8 mod 3) * 5;
(* val it = 105: int *)
> 3 + 4.0;
(* poly: : error: Type error in function application.
Function: + : int * int -> int *)
```

### Operatori delle Stringhe

- `^` → concatenazione tra due stringhe

```sml
> "house" ^ "cat";
(* val it = "housecat": string *)
> "house" ^ "";
(* val it = "house": string *)
```

### Operatori di Confronto

- `=` → uguale
- `<` → minore
- `>` → maggiore
- `<=` → minore o uguale
- `>=` → maggiore o uguale
- `<>` → diverso

```sml
> 1 < 2;
(* val it = true: bool *)
> 1.0 < 2.0;
(* val it = true: bool *)
> 1 = 2;
(* val it = false: bool *)
> 1.0 = 2.0;
(* poly: : error: Type error in function application.
Reason: Can't unify ''a to real (Requires equality type) *)
```

> **⚠️ Attenzione — Eguaglianza sui Reali**
>
> Non sono consentite le operazioni di eguaglianza `=` e diversità `<>` sui numeri di tipo `real` a causa della precisione in virgola mobile.

```sml
> #"Z" < #"a";
(* val it = true: bool *)
> "abc" <= "ab";
(* val it = false: bool *)
> "abc" <= "acc";
(* val it = true: bool *)
```

### Operatori Logici

- `not`
- `andalso`
- `orelse`

```sml
> 1<2 andalso 3>4;
(* val it = false: bool *)
> 1<2 orelse 3>4;
(* val it = true: bool *)
```

> **Osservazione — Precedenza Logica**
>
> `not` ha la precedenza massima, seguito da `andalso`, e infine `orelse`.

### Construct `if-then-else`

Sintassi: `if <p> then <exp1> else <exp2>`. Il ramo `else` è obbligatorio e i due rami devono restituire lo stesso tipo.

```sml
> if 1<2 then 3+4 else 5+6;
(* val it = 7: int *)
> if 5<6 then 5 else 6;
(* val it = 5: int *)
> if 5<6 then 5;
(* poly: : error: else expected but ; was found *)
> if 5<6 then 5 else 6.0;
(* poly: : error: Type mismatch between then-part and else-part. *)
```

---

[← Torna all'Indice del Corso](../index.md)
