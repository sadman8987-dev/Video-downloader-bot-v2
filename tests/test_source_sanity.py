from pathlib import Path
import ast
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SourceSanityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = (ROOT / "main.py").read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.source)

    def test_main_is_valid_python(self):
        self.assertIsInstance(self.tree, ast.Module)

    def test_required_bot_features_are_present(self):
        for marker in (
            "CommandStart()", "build_quality_keyboard", "FFmpegExtractAudio",
            "MAX_DURATION_SECONDS", "TELEGRAM_UPLOAD_LIMIT_MB",
            "save_pending_link", "valid_public_url", "send_media_with_retry",
            "falling back to local yt-dlp", "MAX_FILE_BYTES",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.source)

    def test_blocking_dns_validation_runs_off_event_loop(self):
        self.assertIn("await asyncio.to_thread(valid_public_url, url)", self.source)

    def test_token_is_read_from_environment(self):
        self.assertIn('os.getenv("BOT_TOKEN"', self.source)
        self.assertNotIn("123456789:", self.source)

    def test_remote_engine_is_optional(self):
        self.assertIn('os.getenv("DOWNLOAD_ENGINE_API_URL"', self.source)
        self.assertIn("return await asyncio.to_thread(download_media, url, folder, mode, quality)", self.source)

    def test_upload_retries_only_transient_telegram_errors(self):
        self.assertIn("except (TelegramNetworkError, TelegramServerError)", self.source)
        self.assertIn("for attempt in range(3)", self.source)


if __name__ == "__main__":
    unittest.main()
