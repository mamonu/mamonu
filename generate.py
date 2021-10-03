#!/usr/bin/env python3
import feedparser

python_projects = [
    "splink",
    "splink_graph",
    "splink_data_standardisation"
]


def get_release(name):
    pypi_feed = f"https://pypi.org/rss/project/{name}/releases.xml"
    latest = feedparser.parse(pypi_feed)["entries"][0]
    pub = latest["published_parsed"]
    return {
        "package": name,
        "version": latest["title"],
        "published": f"{pub.tm_year}-{pub.tm_mon:02d}-{pub.tm_mday:02d}",
    }


def get_latest_releases():
    projects = sorted(
        [get_release(proj) for proj in python_projects],
        key=lambda p: p["published"],
        reverse=True,
    )
    return projects


def format_as_markdown(releases):
    rows = [
        "| [{package}](https://github.com/moj-analytical-services/{package}) | {version} | {published} |".format(
            **proj
        )
        for proj in releases
    ]
    header = """| package | version | released |\n|--------------|-----------|-------------|\n"""
    return header + "\n".join(rows)

if __name__ == "__main__":

    print("## Latest Releases")
    print(format_as_markdown(get_latest_releases()))
