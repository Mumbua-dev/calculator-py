from pathlib import Path

def modify_content(text: str) -> str:

    lines = text.splitlines()
    cleaned = []
    prev_blank = False
    for line in lines:
        trimmed = line.rstrip()
        is_blank = (trimmed == "")
        if is_blank and prev_blank:
        
            continue
        cleaned.append(trimmed)
        prev_blank = is_blank

    numbered = [f"{i+1:>4} | {line}" for i, line in enumerate(cleaned)]
    return "\n".join(numbered) + ("\n" if text.endswith("\n") else "")

def main():
   
    user_input = input("Enter the path to the file to read: ").strip()
    src_path = Path(user_input)
    if not src_path.exists():
        print(f"❌ File not found: {src_path}")
        return
    if not src_path.is_file():
        print(f"❌ Not a file: {src_path}")
        return

    try:
        text = src_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"❌ File disappeared or cannot be found: {src_path}")
        return
    except PermissionError:
        print(f"❌ Permission denied when reading: {src_path}")
        return
    except UnicodeDecodeError:
        print(f"❌ Could not decode file as UTF-8. Try a different encoding.")
        return
    except OSError as e:
        print(f"❌ OS error while reading: {e}")
        return

    modified = modify_content(text)

    out_path = src_path.with_stem(src_path.stem + "_modified")

    try:
        out_path.write_text(modified, encoding="utf-8", newline="\n")
    except PermissionError:
        print(f"❌ Permission denied when writing: {out_path}")
        return
    except OSError as e:
        print(f"❌ OS error while writing: {e}")
        return

    print("✅ Success!")
    print(f"• Source:  {src_path}")
    print(f"• Output:  {out_path}")
    print(f"• Bytes written: {out_path.stat().st_size}")

if __name__ == "__main__":
    main()
