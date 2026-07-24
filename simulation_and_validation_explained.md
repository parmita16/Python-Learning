# Understanding "Simulation" and "Data Validation" Questions

These two terms show up together on the syllabus under Real-World
Scenario questions, but they mean different things and often overlap
in the same problem. Here's the breakdown.

---

## What is a "simulation" question?

A simulation question asks you to **model something that changes state
over time or in response to actions** — you're not just computing one
answer, you're building a small system that remembers what happened
before and reacts to new events.

**The tell-tale signs of a simulation question:**
- It describes an object/system with **internal state** (a balance, a
  set of seats, a queue, a stock count).
- It gives you a **sequence of actions** to process (deposit then
  withdraw; book then cancel; add order then serve).
- The result of one action **depends on what happened in earlier
  actions** (you can't overbook a seat that's already taken).

**How to approach it:**
1. Identify what "state" needs to be remembered — this usually becomes
   instance variables in a class, or a dictionary/list you keep
   updating.
2. Identify each "action" the system supports — these become methods
   or functions (`book_seat`, `withdraw`, `add_order`).
3. For every action, ask: **"What rule could make this action fail?"**
   That rule becomes your validation checks (see below) — simulation
   and validation are almost always paired.
4. Write the state changes as plain, obvious operations (increment,
   decrement, append, pop) — simulations are rarely about clever
   algorithms, they're about careful bookkeeping.

**Worked mini-example — a light switch simulation:**

```python
class LightSwitch:
    def __init__(self):
        self.is_on = False        # <-- the "state"
        self.toggle_count = 0     # <-- also state, tracked over time

    def toggle(self):             # <-- the "action"
        self.is_on = not self.is_on
        self.toggle_count += 1
        return "ON" if self.is_on else "OFF"

switch = LightSwitch()
print(switch.toggle())  # ON
print(switch.toggle())  # OFF
print(switch.toggle_count)  # 2
```

Notice: no clever algorithm at all. The whole "difficulty" is correctly
tracking state across multiple calls. That's what makes it a
simulation rather than a one-shot calculation.

Bigger real examples from your practice files: `SeatBooking`,
`Inventory`, `ParkingLot`, and `OrderQueue` in
`05_realworld/practice.py` and `practice_batch2.py`.

---

## What is "data validation with multiple conditions"?

This means: **before you trust or use an input, check it against
several rules, and each rule can independently reject it.** The
"multiple conditions" part means you can't get away with a single
`if` — you need a chain of checks, often in a specific order, and each
one needs its own clear error message or rejection reason.

**The tell-tale signs of a validation question:**
- Words like "eligible", "valid", "allowed", "acceptable".
- A list of **criteria** described in the problem (age range, minimum
  amount, required format, business rule).
- You're expected to identify or return **why** something failed, not
  just true/false.

**How to approach it:**
1. **List every rule separately** before writing code — turn the
   problem's paragraph into a bullet list of conditions.
2. **Order matters for clarity and marks**: check the "cheapest"
   or most obviously invalid conditions first (e.g. negative numbers,
   wrong types) before more nuanced business rules.
3. Use **early returns** for each failing condition instead of one giant
   nested if-else — it's easier to read, easier to debug, and matches
   how hidden test cases usually probe one broken rule at a time.
4. Only after every check passes do you compute/return the "success"
   result.

**Worked mini-example — event ticket validation:**

```python
def validate_ticket_purchase(age, ticket_count, has_id):
    # Rule 1: age restriction
    if age < 13:
        return "Rejected: must be 13 or older"
    # Rule 2: ID requirement for a specific age band
    if 13 <= age < 18 and not has_id:
        return "Rejected: minors need ID verification"
    # Rule 3: purchase limit
    if ticket_count < 1 or ticket_count > 6:
        return "Rejected: can only buy 1-6 tickets at a time"
    # all rules passed
    return "Approved: " + str(ticket_count) + " ticket(s)"

print(validate_ticket_purchase(15, 2, False))  # Rejected: minors need ID
print(validate_ticket_purchase(15, 2, True))   # Approved: 2 ticket(s)
print(validate_ticket_purchase(25, 8, True))   # Rejected: purchase limit
```

Notice the pattern: **each rule is its own `if`, each with its own
early `return`.** This is the shape almost every "multiple conditions"
validation question wants — see `loan_eligibility` in
`05_realworld/practice.py` for a bigger version of the same pattern.

---

## Why they're graded well under partial-credit scoring

Both patterns are actually **great news** under the syllabus's
per-test-case scoring:
- For **simulations**, each action you implement correctly (book,
  cancel, check availability) is likely its own test case — so getting
  3 of 4 methods right still earns real partial marks.
- For **validation**, each *rule* is likely its own test case — so if
  you implement 3 of 4 rules correctly, you still pass roughly 3/4 of
  the hidden tests, even with a bug in the last rule.

This means: **don't freeze up trying to get a validation/simulation
question perfect on the first pass.** Implement the rules/actions you
are sure about first, in separate clearly-named functions or methods,
and add the trickier ones after — partial credit rewards this approach
directly.
