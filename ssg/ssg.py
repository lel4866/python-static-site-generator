import typer
from site import Site


def main(source="content", dest="dist"):
    config={"source": source, "dest": dest}
    site = Site(source, dest)
