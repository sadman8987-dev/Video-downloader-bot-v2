from pathlib import Path
import ast
import unittest

ROOT = Path(__file__).resolve().parents[1]

class SourceSanityTests(unittest.TestCase):
    def test_main_is_valid_python(self):
        ast.parse((ROOT / "main.py").read_text(encoding="utf-8"))

    def test_required_bot_features_are_present(self):
        source = (ROOT / "main.py").read_text(encoding="utf-8")
        for marker in ("CommandStart()", "build_quality_keyboard", "FFmpegExtractAudio",
                       "MAX_DURATION_SECONDS", "TELEGRAM_UPLOAD_LIMIT_MB",
                       "save_pending_link", "valid_public_url"):
            with self.subTest(marker=marker):
                self.assertIn(marker, source)

    def test_token_is_read_from_environment(self):
        source = (ROOT / "main.py").read_text(encoding="utf-8")
        self.assertIn('os.getenv("BOT_TOKEN"', source)
        self.assertNotIn("123456789:", source)

if __name__ == "__main__":
    unittest.main()
