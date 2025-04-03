import argparse

from thumper.ping import ping_api


def setup_args():
    parser = argparse.ArgumentParser(
        prog="Thumper", description="API 'ping' CLI Tool"
    )

    parser.add_argument("url", help="API endpoint URL to ping")
    parser.add_argument(
        "-c",
        "--count",
        type=parse_count,
        default=None,
        help="Limit the number of pings (default=None)",
    )

    return parser.parse_args()


def parse_count(value):
    return None if value.lower() == "none" else int(value)


def main():
    args = setup_args()
    ping_api(args.url, args.count)


if __name__ == "__main__":
    main()
