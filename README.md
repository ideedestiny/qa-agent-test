# Skip diffs with no Python files — checks the diff file header format
    if "diff --git a/" not in response.text or ".py" not in response.text.split("diff --git")[1]:
        print("  No Python files in diff. Skipping.")
        return None
