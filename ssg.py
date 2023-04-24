import ssg.parsers
import typer
from ssg.site import Site


def main(source="content", dest="dist"):
    config={"source": source, "dest": dest, "parsers": [ssg.parsers.ResourceParser()]}
    site = Site(**config).build()


typer.run(main)

