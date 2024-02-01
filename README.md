# Oresat VPN Docs

[![Documentation Status](https://readthedocs.org/projects/oresat-vpn/badge/?version=latest)](https://oresat-vpn.readthedocs.io/en/latest/?badge=latest)

[Read The Docs Page](https://oresat-vpn.readthedocs.io)

## Manual Build Docs

Clone the git repository

```bash
$ git clone https://github.com/oresat/oresat-vpn.git
```

Change to the `oresat-vpn` directory

```bash
$ cd oresat-vpn
```

Install dependencies

**NOTE**: May need to replace `pip` with `pip3` on your system (it varies on
OS and distro).

```bash
$ pip install -r requirements.txt
```

Build the docs

```bash
$ make html -C docs
```

Open `docs/build/html/index.html` in a web browser.

