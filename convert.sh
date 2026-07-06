#!/usr/bin/env bash
set -euo pipefail

# --- PDF registry (id:filename, relative to docs/pdf/) ---
# Add entries as "id:filename" — no spaces around the colon
REGISTRY=(
    "1:ACE - Cars Physics Assets.pdf"
    # "2:autre-fichier.pdf"
    # "3:encore-un-autre.pdf"
)

PYTHON=/opt/homebrew/bin/python3.12
VENV_DIR=".venv"
PDF_DIR="docs/pdf"
OUTPUT_DIR="docs/markdown"

# --- Usage ---
usage() {
    echo "Usage: $0 <id>"
    echo ""
    echo "Available files:"
    for entry in "${REGISTRY[@]}"; do
        local_id="${entry%%:*}"
        local_file="${entry#*:}"
        echo "  $local_id  →  $local_file"
    done
    exit 1
}

# --- Resolve file by ID ---
[ $# -lt 1 ] && usage

ID="$1"
PDF_FILE=""

for entry in "${REGISTRY[@]}"; do
    entry_id="${entry%%:*}"
    entry_file="${entry#*:}"
    if [ "$entry_id" = "$ID" ]; then
        PDF_FILE="$entry_file"
        break
    fi
done

if [ -z "$PDF_FILE" ]; then
    echo "Error: unknown id '$ID'"
    usage
fi

PDF_PATH="$PDF_DIR/$PDF_FILE"

if [ ! -f "$PDF_PATH" ]; then
    echo "Error: file not found: $PDF_PATH"
    exit 1
fi

# --- Setup virtualenv ---
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment with Python 3.12..."
    "$PYTHON" -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"

if ! python -c "import marker" >/dev/null 2>&1; then
    echo "Installing marker-pdf..."
    pip install --quiet --upgrade pip
    pip install --quiet marker-pdf
fi

# --- Convert ---
mkdir -p "$OUTPUT_DIR"

echo "Converting [$ID]: $PDF_PATH"
marker_single "$PDF_PATH" --output_dir "$OUTPUT_DIR"

echo ""
echo "Done. Output in: $OUTPUT_DIR/"
ls "$OUTPUT_DIR"/
