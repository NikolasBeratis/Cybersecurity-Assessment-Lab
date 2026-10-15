
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = PROJECT_ROOT / "evidence"

CHAPTERS = [
    "chapter-01-network-recon",
    "chapter-02-wireshark",
    "chapter-03-ssh-sessions",
    "chapter-04-linux-auth",
    "chapter-05-john-the-ripper",
    "chapter-06-hardening-firewall",
]

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg"}

def main():
    print("Cybersecurity Assessment Lab")
    print("Evidence Checker")
    print("-" * 35)

    if not EVIDENCE_DIR.is_dir():
        print("ERROR: The evidence folder was not found.")
        return

    for chapter in CHAPTERS:
        folder = EVIDENCE_DIR / chapter

        if not folder.is_dir():
            print(f"[MISSING FOLDER] {chapter}")
            continue

        images = [
            file for file in folder.iterdir()
            if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS
        ]

        if images:
            print(f"[OK] {chapter}: {len(images)} image(s)")
        else:
            print(f"[CHECK] {chapter}: no screenshots found")

    print("-" * 35)
    print("Evidence check complete.")

if __name__ == "__main__":
    main()