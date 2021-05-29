#!/usr/bin/env python3

import click

from send_mic import send_mic
from print_stream import print_stream

@click.group()
def cli():
    pass

cli.add_command(send_mic)
cli.add_command(print_stream)

if __name__ == '__main__':
    cli()
