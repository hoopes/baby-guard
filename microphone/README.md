
This is intended to be run from the "microphone" side. It is meant to take audio data from
your microphone, and send them over the network to your speaker side.

The hard part of this is finding the specific values for your input/output to transmit
the bytes correctly. You should be using a USB mic, I think (?).

This is intended to be run from a python virtual environment, or possible a docker container.
You should install the packages from `requirements.txt`

```
$ pip install -r requirements.txt
```

To find the device after you've plugged it in, use:
`$ ./print_devices.sh`

You should see something with USB in it - mine is:

```
$ ./print_devices.sh | grep USB
   2 UACDemoV1.0: USB Audio (hw:2,0), ALSA (1 in, 2 out)
```

Here, my device id is `2`. This is a required argument for our script, so remember it!

You can find some important values by using the `print_stream.py` command:

```
$ ./cli.py print-stream --device-num 2
  Dtype = float32
  SampleRate = 48000.0
```

These values should be used on the "speaker" side as well. See the README there for more info.

Once you've started the server, we should be ready to send bytes:

```
$ ./cli.py send-mic --server <server_hostname_or_ip_address> --port <server_port> --device-num 2 --dtype float32 --sample-rate 48000
```

The client will print a running average of the volume. Currently, the threshold for when it sends data to the
speaker is a relatively arbitrary `5.0`. It will print in red when its over the threshold.
