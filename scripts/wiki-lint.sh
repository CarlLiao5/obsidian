#!/bin/bash

# Wiki Compliance Audit Script
# Checks for unauthorized edits, stale pending items, and illegal references

set -e

WIKI_DIR="$(dirname "$0")/../wiki"
THEORY_DIR="$WIKI_DIR/theory"
PRACTICE_DIR="$WIKI_DIR/practice"
PENDING_DIR="$WIKI_DIR/pending"
ARCHIVE_DIR="$WIKI_DIR/archive"

ERRORS=0
WARNINGS=0

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║               Wiki Compliance Audit Report                    ║"
echo "║                   Generated: $(date '+%Y-%m-%d %H:%M:%S')                     ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Check 1: Unauthorized edits to theory/
echo "📋 Check 1: Unauthorized Modifications to wiki/theory/"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if command -v git &> /dev/null; then
    # Check for recent edits to theory/ by non-admin accounts
    # (This is a simplified check; in production, you'd use proper access control)

    theory_edit_count=$(git log --name-only --since="7 days ago" "$THEORY_DIR" 2>/dev/null | wc -l)

    if [ "$theory_edit_count" -gt 0 ]; then
        recent_editors=$(git log --name-only --since="7 days ago" "$THEORY_DIR" 2>/dev/null | grep -E "^Author:" | sort -u | wc -l)
        echo "⚠️  Found $recent_editors recent editors to wiki/theory/ in the last 7 days"
        echo "   Recommendation: Verify these are authorized changes"
    else
        echo "✅ No unauthorized edits detected in wiki/theory/"
    fi
else
    echo "ℹ️  Git not available, skipping unauthorized edit check"
fi

echo ""

# Check 2: Stale pending items (>7 days)
echo "📋 Check 2: Stale Pending Items (>7 days)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ -d "$PENDING_DIR" ]; then
    stale_count=0
    echo "Checking files in $PENDING_DIR..."

    while IFS= read -r file; do
        if [ -f "$file" ]; then
            # Get file modification time
            mod_time=$(stat -f %m "$file" 2>/dev/null || stat -c %Y "$file" 2>/dev/null)
            current_time=$(date +%s)
            age_seconds=$((current_time - mod_time))
            age_days=$((age_seconds / 86400))

            if [ "$age_days" -gt 7 ]; then
                filename=$(basename "$file")
                echo "⚠️  STALE: $filename (${age_days} days old)"
                ((stale_count++))
                ((WARNINGS++))
            fi
        fi
    done < <(find "$PENDING_DIR" -name "*.md" -type f)

    if [ "$stale_count" -eq 0 ]; then
        echo "✅ No stale pending items (all within 7-day window)"
    else
        echo ""
        echo "⚠️  Action Required: $stale_count items need review or rejection"
    fi
else
    echo "ℹ️  wiki/pending/ does not exist, skipping stale item check"
fi

echo ""

# Check 3: Illegal references
echo "📋 Check 3: Illegal Cross-References"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

echo "Scanning for illegal references..."

# 3a: theory/ referencing pending/
illegal_refs_count=0
if [ -d "$THEORY_DIR" ]; then
    while IFS= read -r file; do
        if grep -q "\[\[pending/" "$file" 2>/dev/null; then
            filename=$(basename "$file")
            echo "❌ ILLEGAL: wiki/theory/$filename references wiki/pending/"
            ((illegal_refs_count++))
            ((ERRORS++))
        fi
    done < <(find "$THEORY_DIR" -name "*.md" -type f)
fi

# 3b: theory/ referencing practice/ (warning only)
practice_refs_in_theory=0
if [ -d "$THEORY_DIR" ]; then
    while IFS= read -r file; do
        if grep -q "\[\[practice/" "$file" 2>/dev/null; then
            filename=$(basename "$file")
            echo "⚠️  WARNING: wiki/theory/$filename references wiki/practice/"
            ((practice_refs_in_theory++))
            ((WARNINGS++))
        fi
    done < <(find "$THEORY_DIR" -name "*.md" -type f)
fi

# 3c: practice/ referencing pending/
practice_pending_refs=0
if [ -d "$PRACTICE_DIR" ]; then
    while IFS= read -r file; do
        if grep -q "\[\[pending/" "$file" 2>/dev/null; then
            filename=$(basename "$file")
            echo "⚠️  WARNING: wiki/practice/$filename references wiki/pending/ (review before merge)"
            ((practice_pending_refs++))
            ((WARNINGS++))
        fi
    done < <(find "$PRACTICE_DIR" -name "*.md" -type f)
fi

if [ "$illegal_refs_count" -eq 0 ] && [ "$practice_refs_in_theory" -eq 0 ] && [ "$practice_pending_refs" -eq 0 ]; then
    echo "✅ All cross-references are legal"
fi

echo ""

# Check 4: Frontmatter completeness
echo "📋 Check 4: Frontmatter Completeness"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

missing_frontmatter=0

for dir in "$THEORY_DIR" "$PRACTICE_DIR" "$PENDING_DIR"; do
    if [ -d "$dir" ]; then
        dir_name=$(basename "$dir")
        echo "Checking wiki/$dir_name/..."

        while IFS= read -r file; do
            if [ -f "$file" ]; then
                if ! head -1 "$file" | grep -q "^---"; then
                    filename=$(basename "$file")
                    echo "⚠️  MISSING: wiki/$dir_name/$filename has no Frontmatter"
                    ((missing_frontmatter++))
                    ((WARNINGS++))
                fi
            fi
        done < <(find "$dir" -name "*.md" -type f 2>/dev/null)
    fi
done

if [ "$missing_frontmatter" -eq 0 ]; then
    echo "✅ All pages have Frontmatter headers"
fi

echo ""

# Summary
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                        SUMMARY REPORT                         ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "Errors:   $ERRORS"
echo "Warnings: $WARNINGS"
echo ""

if [ "$ERRORS" -eq 0 ]; then
    echo "✅ No critical errors found."
else
    echo "❌ $ERRORS critical error(s) found. Please fix before merging."
    exit 1
fi

if [ "$WARNINGS" -gt 0 ]; then
    echo "⚠️  $WARNINGS warning(s) found. Review recommended."
fi

echo ""
echo "Run this script regularly to maintain wiki compliance."
echo ""
