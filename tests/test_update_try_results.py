"""Test the writer of the "Try it" SPARQL results"""
from pathlib import Path

from click.testing import CliRunner

from tools.update_try_results import (
    compact,
    form_of,
    prefixes_of,
    render_page,
    strip_results,
    update_try_results,
)

PAGE = '''# Page

Text before.

??? example try-sparql "Try it"

    ```turtle { .try-data }
    @prefix ex: <http://example.org/> .
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

    ex:a ex:p "test" , "test"@de , "42"^^xsd:integer .
    ```

    ```sparql { .try-query }
    PREFIX ex: <http://example.org/>
    SELECT ?o WHERE { ex:a ex:p ?o . } ORDER BY STR(?o) LANG(?o)
    ```

    ```sparql { .try-query }
    PREFIX ex: <http://example.org/>
    INSERT DATA { ex:b ex:p "new" . }
    ```

    ```sparql { .try-query }
    PREFIX ex: <http://example.org/>
    ASK { ex:b ex:p "new" . }
    ```

Text after.
'''


def test_render_page_writes_results_under_queries(tmp_path: Path) -> None:
    out = render_page(PAGE, tmp_path / "index.md")
    assert '''    ```

    <div class="try-result" markdown>

    3 rows

    | o |
    | --- |
    | `"42"^^xsd:integer` |
    | `"test"` |
    | `"test"@de` |

    </div>
''' in out
    # the queries of a box share one store: the update is visible to the ASK
    assert "    Update done (+1), the store holds 4 triples." in out
    assert "    Answer: true" in out
    assert out.startswith("# Page\n\nText before.\n")
    assert out.endswith("\nText after.\n")


def test_render_page_is_idempotent(tmp_path: Path) -> None:
    once = render_page(PAGE, tmp_path / "index.md")
    assert render_page(once, tmp_path / "index.md") == once


def test_strip_results_restores_the_page(tmp_path: Path) -> None:
    out = render_page(PAGE, tmp_path / "index.md")
    assert "\n".join(strip_results(out.split("\n"))) == PAGE


def test_render_page_leaves_other_admonitions_alone(tmp_path: Path) -> None:
    page = PAGE.replace("try-sparql ", "")
    assert render_page(page, tmp_path / "index.md") == page


def test_render_page_reads_data_files(tmp_path: Path) -> None:
    (tmp_path / "data.ttl").write_text('<http://example.org/x> <http://example.org/p> "v" .\n')
    page = '''??? example try-sparql "Try it"

    Data: [file](data.ttl){ .try-data }

    ```sparql { .try-query }
    SELECT ?s WHERE { ?s ?p ?o . }
    ```
'''
    out = render_page(page, tmp_path / "index.md")
    assert "    | `<http://example.org/x>` |" in out


def test_compact_uses_turtle_local_names() -> None:
    prefixes = prefixes_of(["@prefix pi: <http://ld.company.org/prod-instances/> ."])
    assert compact("http://ld.company.org/prod-instances/empl-A.B%40c.org", prefixes) == "pi:empl-A.B%40c.org"
    assert compact("http://ld.company.org/prod-instances/x.", prefixes) == "<http://ld.company.org/prod-instances/x.>"
    assert compact("http://www.w3.org/2001/XMLSchema#integer", prefixes) == "xsd:integer"


def test_form_of_ignores_prologue_iris_and_strings() -> None:
    assert form_of("PREFIX ex: <http://example.org/select#>\nASK { ?s ?p ?o }") == "ASK"
    assert form_of('# DELETE nothing\nSELECT * WHERE { ?s ?p "INSERT" }') == "SELECT"
    assert form_of("DROP GRAPH <http://example.org/g>") == "DROP"


def test_check_fails_on_drift(tmp_path: Path) -> None:
    docs = tmp_path / "docs"
    docs.mkdir()
    page = docs / "index.md"
    page.write_text(PAGE)
    runner = CliRunner()

    drift = runner.invoke(update_try_results, ["--docs-dir", str(docs), "--check"])
    assert drift.exit_code == 1
    assert "task update:try-results" in drift.output

    assert runner.invoke(update_try_results, ["--docs-dir", str(docs)]).exit_code == 0
    clean = runner.invoke(update_try_results, ["--docs-dir", str(docs), "--check"])
    assert clean.exit_code == 0, clean.output
