import socket
import time
import functools
from threading import Lock

import click
from clint.textui import colored
import sounddevice as sd
import numpy as np

from numpy_ringbuffer import RingBuffer

# FIXME: How do i come to this?
THRESHOLD = 5.0

RUNNING_AVG_SEC = 10 # Amount of secs that the running average has to be above threshold

# Amount of seconds before we stop audio, if the running avg is below threshold
RESET_DELAY = 10

LOCK = Lock()

# TODO: Convert to a queue based solution?
def audio_callback(indata, frames, time, status, buf, sock):
    """This is called (from a separate thread) for each audio block."""

    # FIXME: What does this do?
    volume_norm = np.linalg.norm(indata) * 10

    with LOCK:
        buf.append(volume_norm)

    running_avg = np.average(np.array(buf))

    if running_avg > THRESHOLD:
        print (colored.red(running_avg))
        sock.sendall(indata)
    else:
        print (colored.green(running_avg))

@click.command()
@click.option(
    '--server',
    type=str,
    default='192.168.1.132',
)
@click.option(
    '--port',
    type=int,
    default=8000,
)
@click.option(
    '--device-num',
    type=int,
    required=True,
    help="Use 'python -m sounddevice' to see available devices.",
)
@click.option(
    '--data-type',
    type=str,
    help="Use 'print-stream' command to see values for the device number from --device-num.",
)
@click.option(
    '--sample-rate',
    type=float,
    help="Use 'print-stream' command to see values for the device number from --device-num.",
)
def send_mic(server, port, device_num, data_type, sample_rate):
    """

    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server, port))

    # This is probably wrong, how i'm doing this.
    BUFFER_CAPACITY = int(RUNNING_AVG_SEC * 1000)
    ring_buf = RingBuffer(capacity=BUFFER_CAPACITY, dtype=float)

    # Pre-apply the arguments we want to always send to the callback
    cb = functools.partial(audio_callback, buf=ring_buf, sock=sock)

    with sd.InputStream(device=device_num, dtype=data_type, callback=cb) as stream:
        # Loop forever, doing nothing, letting the stream callback work
        while True:
            time.sleep(10)
