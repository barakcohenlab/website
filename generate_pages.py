#!/usr/bin/env python3

import csv
import pathlib
import typing

"""
Parse a CSV file into a list of dictionaries, with each dictionary keyed by the CSV header.
"""
def parse_csv(source_path: typing.Union[str, pathlib.Path]) -> list[dict[str, str]]:
    with open(source_path, "r") as source:
        reader = csv.reader(source, delimiter=",", quotechar="\"")
        header = next(reader)
        entries = []
        for row in reader:
            entries.append(dict(zip(header, row)))
        return entries

"""
Replace Markdown syntax characters with escaped equivalents
"""
def _escape_markdown(string: str) -> str:
    #string = string.replace("*", r"\*")
    #string = string.replace("#", r"\#")
    #string = string.replace("_", r"\_")
    return string

"""
Given a dictionary and a list of keys, construct a string of key-value pairs appropriate to pass to a Tera templating macro.
"""
def keys_to_string(dictionary: dict[str, str], keys: list[str]) -> str:
    for key in dictionary:
        dictionary[key] = _escape_markdown(dictionary[key])
    return ", ".join(map(lambda pair: f"{pair[0]}=\"{pair[1]}\"", filter(lambda pair: pair[1] != "",map(lambda key: (key, dictionary[key]), keys))))

PEOPLE_HEADER = """+++
title = "People"
description = "Members of the Cohen Lab"
+++
# People

"""

def make_people_page(source_path: typing.Union[str, pathlib.Path] = "content/people/people.csv", output_path: typing.Union[str, pathlib.Path] = "content/people/index.md", header: str = PEOPLE_HEADER):
    people = parse_csv(source_path)
    current = []
    alumni = []
    for person in people:
        if person["current"] == "yes":
            current.append(person)
        else:
            alumni.append(person)

    keys = ["name", "role", "url", "photo"]

    with open(output_path, "w") as out:
        out.write(header)

        out.write(f"## Current\n\n")
        out.write(r"""<div class="people-container">""" + "\n\n")
        for person in current:
            out.write(r"{{ person(" + keys_to_string(person, keys) + ", photo_size=300) }}" + "\n\n")
        out.write(r"""</div>""" + "\n\n")

        out.write(f"## Alumni\n\n")
        out.write(r"""<div class="people-container">""" + "\n\n")
        for person in alumni:
            out.write(r"{{ person(" + keys_to_string(person, keys) + ", photo_size=200) }}" + "\n\n")
        out.write(r"""</div>""" + "\n")

def make_safe(string: str, forbidden_characters: list[str] = [">", "<", ":", "/", "|", "?", "*", "#", "\\", "(", ")", "[", "]"]) -> str:
    translation_table = str.maketrans("".join(forbidden_characters), "-" * len(forbidden_characters))
    return string.translate(translation_table)

def make_publications_page(source_path: typing.Union[str, pathlib.Path] = "content/publications/publications.csv", output_dir: typing.Union[str, pathlib.Path] = "content/publications"):
    papers = parse_csv(source_path)

    papers.sort(key=lambda paper: int(paper["publication_year"]), reverse=True)

    for i, paper in enumerate(papers):
        safe_doi = make_safe(paper["doi"])
        print(safe_doi)
        output_path = str(pathlib.Path(output_dir).joinpath(f"pub_{safe_doi}")) + ".md"
        print(output_path)
        with open(output_path, "x") as out:
            out.write("+++\n")
            out.write(f"title = \"{paper['title']}\"\n")
            out.write(f"slug = \"{safe_doi}\"\n")
            out.write(f"weight = {i}\n")
            out.write("[extra]\n")
            out.write(f"authors = \"{paper['authors']}\"\n")
            out.write(f"journal = \"{paper['journal']}\"\n")
            out.write(f"publication_year = \"{paper['publication_year']}\"\n")
            out.write(f"doi = \"{paper['doi']}\"\n")
            out.write("+++\n")

JC_HEADER = """+++
title = "Journal Club"
description = "Papers discussed in the Cohen Lab journal club"
+++
# Journal Club

The Cohen Lab journal club meets at 10:00 AM on Wednesdays in Couch 4304.

Every few weeks, each lab member pitches an article that they have recently read. They have two minutes to sell the lab on the exciting findings and merits of the experiments. At the conclusion, the lab votes on the papers that will populate the coming weeks’ discussions.

## Previously-Discussed Papers

"""

def make_jc_page(source_path: typing.Union[str, pathlib.Path] = "content/journal_club/journal_club_papers.csv", output_path: typing.Union[str, pathlib.Path] = "content/journal_club/index.md", header: str = JC_HEADER):
    papers = parse_csv(source_path)

    keys = ["title", "authors", "journal", "publication_year", "doi"]

    with open(output_path, "w") as out:
        out.write(header)

        out.write("""{% section() %}\n\n""")
        for paper in papers:
            out.write(r"**" + paper['date_discussed'] + r"**: {{ paper(" + keys_to_string(paper, keys) + r") }}" + "\n\n")
        out.write("{% end %}\n\n")

if __name__ == "__main__":
    make_people_page()
    make_publications_page()
    make_jc_page()
