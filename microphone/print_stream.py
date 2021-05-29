import click
import sounddevice as sd

@click.command()
@click.option(
    '--device-num',
    type=int,
    required=True,
    help="Use 'python -m sounddevice' to see available devices.",
)
def print_stream(device_num):
    with sd.InputStream(device=device_num) as stream:
        print (f"""
            Dtype = {stream.dtype}
            SampleRate = {stream.samplerate}
        """)
