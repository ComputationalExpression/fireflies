"""Structure checks for Lab 3: Fireflies at Bousson.

These read `src/main.py` as Python, not as text, so the words `for`, `while`
and `if` are free to appear in the story and in comments. Only real statements
count. Each assertion message says what was found and what was expected.
"""

import ast
from pathlib import Path

SOURCE = Path(__file__).resolve().parent.parent / "src" / "main.py"

LOOPS = (ast.For, ast.While)


def tree():
    return ast.parse(SOURCE.read_text(encoding="utf-8"))


def nodes(kind):
    return [n for n in ast.walk(tree()) if isinstance(n, kind)]


def inside(outer_kinds, inner_kind):
    """Return the inner nodes of `inner_kind` that sit in the body of some `outer_kinds` node."""
    found = []
    for outer in nodes(outer_kinds):
        for child in ast.walk(outer):
            if child is not outer and isinstance(child, inner_kind):
                found.append(child)
    return found


def uses_range(loop):
    return (
        isinstance(loop, ast.For)
        and isinstance(loop.iter, ast.Call)
        and isinstance(loop.iter.func, ast.Name)
        and loop.iter.func.id == "range"
    )


def test_at_least_three_for_loops_over_range():
    count = sum(1 for loop in nodes(ast.For) if uses_range(loop))
    assert count >= 3, f"found {count} for loop(s) over range(...), expected at least 3: Stage One, Stage Three, and Stage Four each need one"


def test_one_while_loop():
    count = len(nodes(ast.While))
    assert count >= 1, "found no while loop: Stage Two repeats until the reading is 20 or lower"


def test_an_if_inside_a_loop():
    found = inside(LOOPS, ast.If)
    assert found, "found no if inside a for or while loop: Stage Three decides on every trip whether the flash is held long"


def test_a_loop_inside_a_loop():
    found = inside(LOOPS, LOOPS)
    assert found, "found no loop inside another loop: Stage Four sends the three letters of SOS inside the loop that repeats the signal"


def test_no_lists():
    kinds = (ast.List, ast.ListComp, ast.Subscript)
    found = nodes(kinds)
    lines = sorted({n.lineno for n in found})
    assert not found, f"found a list or an index on line(s) {lines}: this lab is loops and decisions only, every stage is a count"
