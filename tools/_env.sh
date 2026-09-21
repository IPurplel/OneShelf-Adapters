# Sourced by the tools: the repository root and the pinned OneShelf tooling.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY="$ROOT/.venv/bin/python"
PINNED="$(tr -d '[:space:]' < "$ROOT/tooling/oneshelf-core-ref.txt")"
if [ ! -x "$PY" ]; then
  echo "The OneShelf tooling is not installed yet. Run: ./tools/bootstrap" >&2
  exit 2
fi
INSTALLED="$("$PY" "$ROOT/tools/installed-core-ref" 2>/dev/null || true)"
if [ "$INSTALLED" != "$PINNED" ] && [ "$INSTALLED" != "local" ]; then
  echo "The installed OneShelf tooling ($INSTALLED) is not the pinned one ($PINNED). Run: ./tools/bootstrap" >&2
  exit 2
fi
repo() { "$PY" -m oneshelf.plugins.adapter_repo "$@"; }
baseline_args() {
  if [ -f "$ROOT/.registry-baseline/index.json" ]; then echo "--baseline $ROOT/.registry-baseline"; fi
}
