#!/bin/bash

# Add Frontmatter to wiki pages that don't have one

WIKI_DIR="$(dirname "$0")/../wiki"
THEORY_DIR="$WIKI_DIR/theory"
PRACTICE_DIR="$WIKI_DIR/practice"

add_frontmatter_theory() {
    local file="$1"
    local filename=$(basename "$file")

    # Check if already has frontmatter
    if head -1 "$file" | grep -q "^---"; then
        return
    fi

    # Create temp file with frontmatter
    {
        echo "---"
        echo "author: Walmart 官方文档"
        echo "auditor: 知识库管理员"
        echo "status: verified"
        echo "audit_date: $(date +%Y-%m-%d)"
        echo "tags: [官方文档, 知识库]"
        echo "---"
        echo ""
        cat "$file"
    } > "$file.tmp"

    mv "$file.tmp" "$file"
    echo "✓ $filename"
}

add_frontmatter_practice() {
    local file="$1"
    local filename=$(basename "$file")

    # Check if already has frontmatter
    if head -1 "$file" | grep -q "^---"; then
        return
    fi

    # Create temp file with frontmatter
    {
        echo "---"
        echo "author: 运营团队"
        echo "auditor: 待审核"
        echo "status: pending"
        echo "audit_date: null"
        echo "tags: [运营实践, 待审核]"
        echo "---"
        echo ""
        cat "$file"
    } > "$file.tmp"

    mv "$file.tmp" "$file"
    echo "✓ $filename"
}

echo "Adding Frontmatter to wiki pages..."
echo ""

echo "Processing wiki/theory/..."
count=0
for file in "$THEORY_DIR"/*.md; do
    if [ -f "$file" ]; then
        add_frontmatter_theory "$file"
        ((count++))
    fi
done
echo "Total: $count files processed"
echo ""

echo "Processing wiki/practice/..."
count=0
for file in "$PRACTICE_DIR"/*.md; do
    if [ -f "$file" ]; then
        add_frontmatter_practice "$file"
        ((count++))
    fi
done
echo "Total: $count files processed"
echo ""

echo "✅ Frontmatter addition complete!"
