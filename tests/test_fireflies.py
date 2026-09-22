"""Automated checks for Lab 3: Fireflies at Bousson.

Every check reads the field log at the end of the run, or counts how many times
the lantern was switched on, never the narrative lines, so the story is the
student's to word. Log values are matched loosely: any amount of whitespace,
any letter case, and the colon is optional, so `print("Long flashes:", n)`,
`print("Long flashes: " + str(n))`, and `print(f"Long flashes: {n}")` all read
the same.

The two lantern checks compare two runs that differ in one answer, so a
program that switches the lantern on somewhere else as well still passes:
only the change in the count has to match.

When a check fails, the assertion message says which log line came out wrong,
what it said, what was expected, and the answers that were typed. gatorgrade
does not show that message itself; it prints the pytest command to run.
"""

import re
from unittest.mock import patch

import mockro

from main import main

# The order the starter asks its questions. The checks type answers in this
# order, so a program that asks them in a different order reads the wrong
# answer for the wrong question.
QUESTIONS = ["name", "flashes", "reading", "pattern", "repeats"]

# A quiet run. Individual checks change exactly the answers they are about.
SAFE = dict(name="JJ", flashes=4, reading=50, pattern=6, repeats=1)


def run(capsys, **changes):
    """Run main() once with the SAFE answers plus `changes`.

    Returns what it printed, the answers used, and how many times the lantern
    was switched on: every `led.on()` plus every `led.value(1)`.
    """
    answers = {**SAFE, **changes}
    typed = [str(answers[q]) for q in QUESTIONS]
    recorder = mockro.get_recorder()
    recorder.clear()
    # time.sleep is real here (mockro only mocks it under `import utime`), so
    # it is patched directly to keep the checks instant.
    with patch("builtins.input", side_effect=typed), patch("time.sleep", return_value=None):
        main()
    out, err = capsys.readouterr()
    assert err == "", "the program wrote to the error stream:\n" + err
    lit = len(recorder.calls("machine.Pin.on"))
    lit += sum(1 for args, _ in recorder.calls("machine.Pin.value") if len(args) > 1 and args[1])
    return out, answers, lit


def log_value(out, label):
    """Return the value printed after `label` in the field log, normalized.

    Only the part of the output from `FIELD LOG` onward is searched, so a
    narrative line that happens to mention flashes cannot be mistaken for the
    log entry. Whitespace is collapsed inside the label and the value, case is
    folded to upper, a trailing period is dropped, and the colon after the
    label is optional. Returns None when the log, or the label, was never
    printed.
    """
    start = out.upper().find("FIELD LOG")
    if start < 0:
        return None
    # The label itself may be printed with any spacing between its words.
    words = r"\s+".join(re.escape(word) for word in label.split())
    match = re.search(rf"{words}\s*:?\s*([^\n]*)", out[start:], re.IGNORECASE)
    if match is None:
        return None
    return " ".join(match.group(1).split()).upper().rstrip(".! ")


def expect(capsys, label, want, **changes):
    """Run once and check that the field log line `label` says `want`."""
    out, answers, _ = run(capsys, **changes)
    typed = ", ".join(f"{q}={answers[q]}" for q in QUESTIONS)
    if "FIELD LOG" not in out.upper():
        raise AssertionError(f'no "FIELD LOG" line was printed (answers typed: {typed})')
    got = log_value(out, label)
    if got is None:
        raise AssertionError(f'no "{label}" line was printed after FIELD LOG (answers typed: {typed})')
    assert got == str(want), f'the "{label}" line said {got}, expected {want} (answers typed: {typed})'
    return out


def lantern_difference(capsys, **pair):
    """Run twice, changing one answer, and return how many more times the lantern lit."""
    (question, (low, high)), = pair.items()
    _, _, lit_low = run(capsys, **{question: low})
    _, _, lit_high = run(capsys, **{question: high})
    return lit_high - lit_low


def test_program_runs_and_log_names_you(capsys):
    # An untouched starter prints its provided framing text either way, so
    # checking for the user's own name in the log is what actually requires
    # Stage One and the field log to be done.
    expect(capsys, "FIELD LOG", "JJ")


def test_flash_count_is_held_between_one_and_ten(capsys):
    expect(capsys, "Flashes sent", 4, flashes=4)
    expect(capsys, "Flashes sent", 10, flashes=12)
    expect(capsys, "Flashes sent", 1, flashes=0)


def test_lantern_flashes_once_per_trip(capsys):
    # Seven flashes against four: the lantern has to come on exactly three
    # more times, which only happens when led.on() sits inside the loop.
    more = lantern_difference(capsys, flashes=(4, 7))
    assert more == 3, f"asking for 7 flashes instead of 4 lit the lantern {more} more times, expected 3"


def test_checks_until_dark_counts_the_trips(capsys):
    # 70 falls to 60, 50, 40, 30, 20: five trips, and 20 is not more than 20.
    expect(capsys, "Checks until dark", 5, reading=70)
    expect(capsys, "Checks until dark", 1, reading=30)
    # The condition is tested before the first trip, so a reading that is
    # already dark makes no trips at all.
    expect(capsys, "Checks until dark", 0, reading=20)
    expect(capsys, "Checks until dark", 0, reading=15)


def test_every_third_flash_is_long(capsys):
    expect(capsys, "Long flashes", 3, pattern=9)
    expect(capsys, "Long flashes", 2, pattern=7)
    # Two flashes never reach a third, so the if branch never runs.
    expect(capsys, "Long flashes", 0, pattern=2)


def test_sos_is_nine_flashes_per_repeat(capsys):
    # One more repeat is one more pass through all three inner loops: three
    # short, three long, three short, nine flashes.
    more = lantern_difference(capsys, repeats=(1, 2))
    assert more == 9, f"one more SOS lit the lantern {more} more times, expected 9"
    expect(capsys, "SOS repeats", 2, repeats=2)
