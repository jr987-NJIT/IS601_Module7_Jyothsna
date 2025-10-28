import argparse
import logging
import os
import datetime
import urllib.parse

import qrcode


def setup_dirs():
    os.makedirs("logs", exist_ok=True)
    os.makedirs("qr_codes", exist_ok=True)


def setup_logging():
    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s:%(message)s",
    )


def generate_qr(url: str, outfile: str | None = None) -> str:
    img = qrcode.make(url)
    if not outfile:
        parsed = urllib.parse.urlparse(url)
        host = parsed.netloc or "qr"
        ts = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d%H%M%S")
        outfile = f"qr_codes/{host}_{ts}.png"
    img.save(outfile)
    return outfile


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="QR Code Generator")
    parser.add_argument("--url", required=True, help="URL to encode into QR code")
    parser.add_argument("--out", default=None, help="Output file path (optional)")
    return parser.parse_args()


def main():
    args = parse_args()
    print("=" * 60)
    print("QR Code Generator Application")
    print("=" * 60)
    setup_dirs()
    setup_logging()
    print(f"📝 Directories initialized: logs/ and qr_codes/")
    print(f"🔗 Input URL: {args.url}")
    logging.info(f"Generating QR for {args.url}")
    print(f"⚙️  Generating QR code...")
    try:
        out = generate_qr(args.url, args.out)
        print(f"✅ Success! QR code saved to: {out}")
        logging.info(f"Saved QR to {out}")
        print("=" * 60)
    except Exception as e:
        logging.exception("Failed to generate QR code")
        print("❌ Error: failed to generate QR code. See logs/app.log for details.")
        raise


if __name__ == "__main__":
    main()
