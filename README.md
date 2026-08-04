# Assetto Corsa EVO — Vehicle Physics Reference

Community documentation of **Assetto Corsa EVO** car physics assets (target version **0.7.1**): schemas, units, and field descriptions for modders and vehicle-dynamics work.

This is **not** official Kunos Simulazioni documentation. The Markdown source opens with a **Preface** that explains scope, methodology, and how inferred entries should be treated — read it before relying on any field.

## Repository layout

| Path | Contents |
| :--- | :--- |
| [`docs/pdf/`](./docs/pdf/) | Source PDF reference |
| [`docs/markdown/`](./docs/markdown/) | PDF converted to Markdown (via Marker) |
| [`descriptions/`](./descriptions/) | Per-asset written descriptions (role, architecture, examples) |
| [`scripts/convert.sh`](./scripts/convert.sh) | PDF → Markdown conversion helper |

## Report a correction

Found a wrong unit, a shaky description, or a missing field?

→ **[Open a documentation correction issue](https://github.com/CorsaClub/ace-documentation/issues/new?template=documentation-correction.yml)**

Include the section, field ID (when relevant), current text, proposed change, and evidence (asset values, in-game behaviour, game version). Maintainers will review and update the reference.

If you already have a concrete edit ready, open a **Pull Request** instead — Issues remain preferred for “something is wrong, please fix it.”

## PDF conversion (maintainers)

Conversion uses [Marker](https://github.com/datalab-to/marker). Requires Python 3.12. Register new PDFs in the `REGISTRY` array inside `scripts/convert.sh`.

```sh
make list                 # list available PDF IDs
make convert ID=1         # convert ID 1 → docs/markdown/
make setup                # install deps into .venv only

./scripts/convert.sh      # same listing (no args)
./scripts/convert.sh 1    # convert by ID
```

```sh
make clean                # remove docs/markdown/
make distclean            # remove output + .venv
```

## License

Released under **[CC BY 4.0](./LICENSE)**. You may share and adapt the material with appropriate credit.

Assetto Corsa EVO is a trademark of Kunos Simulazioni. This repository is an independent, non-commercial community project.
