# Lab 3: Fireflies at Bousson

|Item |       |
|:----|:------|
|Released |Week 5, Friday lab |
|Due |See the [course schedule](https://computationalexpression.com/schedule/) |
|Progress |[![Grade](../../actions/workflows/main.yml/badge.svg?branch=main)](../../actions/workflows/main.yml) |

Seven miles from campus, there are 283 acres of forest, ponds and wetland called the
Bousson Environmental Research Reserve. On a June night you are at the edge of one of its ponds,
counting fireflies. Fireflies talk in flash patterns, and a lantern flashed in the right rhythm
gets an answer. Your Raspberry Pi Pico 2 W's built-in LED is that lantern. Every stage repeats
something, and a loop is how you say code the repetition once.

## Contents

* [Course learning outcomes](#course-learning-outcomes)
* [Your Pico 2 W](#your-pico-2-w)
* [The four stages](#the-four-stages)
  * [The field log](#the-field-log)
  * [Expected output](#expected-output)
* [Getting started](#getting-started)
* [Evaluation](#evaluation)
  * [Programming, 3.0 points](#programming-30-points)
  * [Code quality and style, 1.0 point](#code-quality-and-style-10-point)
  * [Summary writing, 0.5 points](#summary-writing-05-points)
* [Code review](#code-review)
* [Submitting](#submitting)

## Course learning outcomes

This lab addresses the following course learning outcomes:

**CLO 1.** Apply Python programming fundamentals to execute and explain computer code that
implements interactive, novel solutions to a variety of computable problems.

**CLO 2.** Implement code consistent with industry-standard practices using professional-grade
integrated development environments (IDEs), command-line tools, and version control systems.

Specifically, by the end of this lab you should be able to:

* repeat a block a counted number of times with `for` and `range`, including a range that
  starts at `1`
* repeat a block until a condition changes with `while`, and make sure the condition can change
* make a decision on every trip of a loop with an `if` inside it
* run one loop inside another and count how many times the inner block runs
* control the built-in LED from inside a loop with `machine.Pin` and `time.sleep`

## Your Pico 2 W

Same board, same lantern: `Pin("LED", Pin.OUT)` is the built-in LED, and `led.on()` and
`led.off()` switch it. Open your `cmpsc100` folder in VS Code, plug the board in, and confirm the
bar along the bottom of the window reads **Pico Connected**. If MicroPico is not set up in that
folder yet, the steps are on the
[Week 4 Session 2 slides](https://computationalexpression.com/slides/week-04-session-2/).

If it will not connect, ask an instructor or TL. Do not troubleshoot hardware alone the night
before it is due.

## The four stages

Everything this lab asks for is covered by Friday of Week 5. 

**The story is yours to change.** Every message the program prints is your wording, and you
may rewrite the night at the pond however you like. Two things stay fixed, because the
automated checks depend on them: the questions are asked in the order the starter lists them,
and the field log at the end keeps its labels.

**Stage One: The Call.** Ask the user's name and how many flashes to send toward the pond edge.
An `if`/`elif` keeps the count between `1` and `10`. Then a `for` loop over
`range(1, flashes + 1)` sends the flashes: on every trip it prints the flash number, switches
the lantern on, waits, and switches it off.

**Stage Two: Waiting for Dark.** Fireflies start once the light meter reads `20` or lower. The
user types the current reading, and a `while` loop runs as long as the reading is more than
`20`: each trip prints the reading, lowers it by `10`, and counts one more check. The loop
tests its condition before every trip, so a reading that is already dark makes no trips.

**Stage Three: The Answer.** The species at the pond edge answers a pattern in which every third
flash is held long. A `for` loop counts the flashes from `1`, and an `if` inside it decides
each one: when the flash number divided by `3` leaves no remainder, the lantern stays on longer
and a counter goes up by one.

**Stage Four: SOS.** You look up from the count, and the trail markers you followed in are gone
in the dark. SOS is three short flashes, three long, three short. An outer `for` loop sends the
signal as many times as the user asks, and three `for` loops inside it send the three letters.

### The field log

The program ends with a log, and the automated checks read **only the log**, never the story.
The log has six lines, in this order:

```text
FIELD LOG: JJ
==================================================
Flashes sent: 4
Checks until dark: 3
Long flashes: 2
SOS repeats: 1
```

Print each line any of the three ways from Week 3: `print("Long flashes:", long_flashes)`,
`print("Long flashes: " + str(long_flashes))`, or `print(f"Long flashes: {long_flashes}")`
all pass. The checks forgive extra spaces and letter case.

The checks type the answers in the order the starter asks them: name, flashes, reading,
pattern, repeats. Keep the questions in that order.

### Expected output

One complete run, with `4`, `50`, `6`, and `1` as the answers:

```text
==================================================
FIREFLIES AT BOUSSON
==================================================
What is your name? JJ
How many flashes do you send toward the pond edge? (1-10): 4
JJ raises the lantern toward the pond.
Flash 1
Flash 2
Flash 3
Flash 4

What does the light meter read? (0-100): 50
Still too light. The meter reads 50
Still too light. The meter reads 40
Still too light. The meter reads 30
Dark enough. The first fireflies rise out of the grass.

How many flashes in the pattern? (1-12): 6
Flash 1
Flash 2
Flash 3 held long
Flash 4
Flash 5
Flash 6 held long
Along the pond edge, one by one, the fireflies answer.

You look up from the count. The trail markers you followed in are gone in the dark.
How many times do you send SOS toward the road? (1-5): 1
SOS 1 of 1
Headlights swing across the pond from the road. Someone saw.

==================================================
FIELD LOG: JJ
==================================================
Flashes sent: 4
Checks until dark: 3
Long flashes: 2
SOS repeats: 1
```

## Getting started

Open `src/main.py` and work through the `TODO` markers in order. Run it on your Pico as you go
by clicking **Run** in the bar along the bottom of the window, or from the terminal against a
plain Python interpreter for the parts that do not depend on real hardware timing:

```text
uv run python src/main.py
```

> [!IMPORTANT]
> Run every command in this README from the assignment's **working directory**, the top-level
> folder you land in right after cloning, not from inside `src`.

## Evaluation

This lab is worth **4.5 points**, the standard value for a lab in this course.

| Component | Points | What it measures |
|:----------|:-------|:-----------------|
| Programming | 3.0 | The 13 code checks below. Your score is the fraction passed, times 3.0 |
| Code quality and style | 1.0 | Descriptive names (0.3), clear organization (0.3), useful comments (0.4) |
| Summary writing | 0.5 | A complete, thoughtful `docs/summary.md` |
| **Total** | **4.5** | |

### Programming, 3.0 points

Run the checks yourself, as many times as you like, before you submit:

```text
uv run gatorgrade --config gatorgrade.yml
```

Each check's description says what to look at when it fails. Under a failed check, gatorgrade
also prints a `uv run pytest ...` command. Run it: the last lines name the log line that came
out wrong, what it said, what was expected, and the answers that were typed. A loop that never
ends fails its check after five seconds instead of hanging. Thirteen of the checks are about
your code:

* the field log names you, and asking for `4`, `12`, and `0` flashes logs `4`, `10`, and `1`
* asking for `7` flashes lights the lantern three more times than asking for `4`
* a reading of `70` takes five checks, `30` takes one, and `20` or `15` take none
* a pattern of `9` logs `3` long flashes, `7` logs `2`, and `2` logs `0`
* one more SOS lights the lantern nine more times
* at least three `for` loops over `range`, one `while` loop, an `if` inside a loop, a loop
  inside a loop, and no list anywhere
* no `TODO` markers remain, and there are at least six comments

Partial credit is proportional: passing 10 of 13 checks earns `(10 ÷ 13) × 3.0 = 2.3` points.

The remaining two checks look at `docs/summary.md`. They confirm the document is finished, and
they count toward Summary writing below rather than toward these 3.0 points.

> [!NOTE]
> Automated results are preliminary. Your instructor sets the final grade.

### Code quality and style, 1.0 point

Graded by a human reading your code. Descriptive variable names, sensible organization, and
comments that explain **why** rather than restating what the line already says.

### Summary writing, 0.5 points

Complete [`docs/summary.md`](docs/summary.md). Every question answered fully. Minimum word
count is `150`.

## Code review

A Technical Leader or the instructor will conduct a code review with you on this lab. **Code
reviews are graded separately from the 4.5 points above**, under the Code Reviews category on
the syllabus.

Two things happen, with you present:

1. **You run your program** on your Pico for the reviewer
2. **You answer questions about your own code**, including the concepts behind it

The reviewer opens a **Code Review** issue on your repository and fills it out during the
conversation. The reviewer asks one question about each of four concepts, in their own words
and about your own code, so the questions differ from student to student. Be ready to:

* **Counted repetition**: say what `range` hands the loop on each trip, and point to the line
  that has to be inside the loop for the lantern to flash once per trip
* **Loop until a condition**: explain what makes your `while` loop stop, and predict the number
  of trips for a given reading
* **A decision inside a loop**: trace which trips take the `if` branch, and explain what `% 3`
  has to do with it
* **A loop inside a loop**: count how many times the inner block runs in total, and explain what
  the indentation decides

**Your review must be completed during the lab session on the day this lab is due.** If you
know in advance that you cannot attend that lab, make arrangements to complete your review
beforehand at office hours. If you submitted this lab on time but missed the code review, you
can make it up at office hours within one week of the due date:

* **Technical Leaders**, listed on the calendar at
  [cis.allegheny.edu/community/news](https://www.cis.allegheny.edu/community/news/)
* **Dr. Jumadinova**, [book a time](https://janyljumadinova.com/office-hours/). Drop-ins are welcome
  during posted hours, but students who booked are seen first

## Submitting

Commit and push often. The last version pushed before the deadline is the one that gets
graded. If you need more time, apply a late token with
[this form](https://forms.gle/3nGbpaNrG96DpLLdA). One token covers both parts of a lab: the
submission and the code review.

**In the terminal:**

```text
git add src/main.py docs/summary.md
git commit -m "Complete the fireflies at Bousson"
git push
```

**In VS Code**, the Source Control panel in the left sidebar does the same three steps:

1. Click **+** next to a changed file to stage it (this is `git add`)
2. Type a message in the box at the top, then click the checkmark (this is `git commit`)
3. Click **Sync Changes** (or the &uarr; arrow) to push

Either way, then open your repository on GitHub and confirm your latest changes are actually
there.
