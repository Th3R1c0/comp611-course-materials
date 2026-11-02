# 01 · Algorithm analysis & asymptotics (Week 1)  — budget ~12% of the A4 side

**[AA-1] RAM model.** Running time on an input = **number of elementary operations** (each cost 1): + − × ÷ %, comparisons (== != < >), assignment/creation of a primitive, array access, pointer ops, return/branch. Worst case = max over all inputs of size n; average = mean over inputs (needs a distribution). Space = max memory in use at any instant; report **auxiliary** space (input array doesn't count).

**[AA-2] Definitions.** f = O(g): ∃ c, n₀ > 0 with f(n) ≤ c·g(n) ∀ n ≥ n₀ (upper, need not be tight). f = Ω(g): f(n) ≥ c·g(n) ∀ n ≥ n₀ (lower). f = Θ(g): both O and Ω. **Θ exists only when O and Ω agree.**

**[AA-3] Finding c, n₀ (recipe).**
1. Upper (O(nᵏ)): for n ≥ 1 raise every term to nᵏ → **c = sum of positive coefficients, n₀ = 1**. (3n²+5n+2 ≤ 10n²)
2. Lower (Ω(nᵏ)): drop the positive lower terms → **c = leading coefficient, n₀ = 1**.
3. Negative term (n²/2 − 5n): pick n₀ where it's ≤ half the leading term → c = half the leading coeff (n₀ = 20, c = 1/4).
4. Checking an MCQ pair: plug n = n₀ in and make sure f(n₀) ≤ c·g(n₀), and c ≥ leading coeff.

**[AA-4] Simplifying.** Drop constant factors · keep only the dominant term · log base doesn't matter (log₁₀n = Θ(log n)). Trap: 5n−2 = O(n²) is TRUE but it is NOT Θ(n²) (tight bound is Θ(n)).

**[AA-5] Growth order + doubling test.** 1 < log n < √n < n < n log n < n² < n³ < 2ⁿ < n!
Timing table: ratio r = T(2n)/T(n) → **r≈1 log n · 2 n · just over 2 n log n · 4 n² · 8 n³** (exponent = log₂ r). Exponential: T(n+1)/T(n) is constant (2ⁿ doubles per +1).

**[AA-6] Counting from pseudocode.** T(n) = Σ (cost × times run), then drop constants.
| Pattern | Count |
|---|---|
| `for i=1..n` header / body | n+1 / n |
| `for i=1..n, for j=i+1..n` | n(n−1)/2 → Θ(n²) |
| `for i=1..n, for j=1..i` | n(n+1)/2 → Θ(n²) |
| `while n>1: n=n/2` (or `i=i*2`) | ⌊log₂n⌋ → Θ(log n) |
| halving loop inside an n-loop | Θ(n log n) |
| triple nested to n | Θ(n³) |
Sums: 1+2+…+n = n(n+1)/2 · 1+2+4+…+2ᵏ = 2ᵏ⁺¹−1.

**[AA-7] Best/worst table.** Early `return` ⇒ cost depends on the values ⇒ **no single Θ**; say O(worst) and Ω(best).
| Algorithm | Best | Worst |
|---|---|---|
| Linear search | Θ(1) key first | Θ(n) not found (2n+1 ops) |
| Insertion sort | Θ(n) sorted | Θ(n²) reverse, n(n−1)/2 shifts |
| Merge sort | Θ(n log n) | Θ(n log n) (any input) |
| Binary search T(n)=T(n/2)+1 | Θ(1) | Θ(log n) |
| Selection / bubble sort | Θ(n²) | Θ(n²) |

**[AA-8] Fibonacci.** Naive recursion: exponential, ~1.618ⁿ (O(2ⁿ)), repeats subproblems · memo / iterative array: O(n) · matrix exponentiation: O(log n).

**[AA-9] Traps / definitions.** "O(n²) ⇒ quadratic on every input" FALSE (O is an upper bound). Seconds on one laptop ≠ complexity (machine-dependent, one data point, unknown case). Algorithm = finite, well-defined steps input→output; properties: inputs, outputs, finiteness, definiteness, effectiveness.
