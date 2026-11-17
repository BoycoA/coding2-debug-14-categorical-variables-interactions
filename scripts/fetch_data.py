"""Verify or restore the exact CPS teaching CSV. Students already have this file."""

import hashlib
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ROOT / "data/cps1985.csv"
SOURCE = "https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/cc03c29690889dbe83089f5206e2422db8c3f71f/csv/AER/CPS1985.csv"
SHA256 = "1b4bf681b94ecb82e534a0f97773c704205e13ccf13d273e439e44eaa9f5435c"


def main():
    if DESTINATION.exists():
        if hashlib.sha256(DESTINATION.read_bytes()).hexdigest() != SHA256:
            raise RuntimeError("The local dataset differs from the source. Refusing to overwrite it.")
        print("Verified the included CPS1985 data; no download needed.")
        return
    with urlopen(SOURCE, timeout=60) as response:
        payload = response.read()
    if hashlib.sha256(payload).hexdigest() != SHA256:
        raise RuntimeError("Source checksum mismatch; no data saved.")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(payload)
    print("Saved the verified CPS1985 data.")


if __name__ == "__main__":
    main()
