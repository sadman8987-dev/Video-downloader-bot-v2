# Video Downloader Bot V2

نسخة مستقلة من بوت Telegram لتنزيل الوسائط من الروابط العامة المدعومة.

## الوظائف
- اختيار فيديو أو صوت MP3.
- اختيار جودة 360p و480p و720p و1080p أو أعلى جودة متاحة.
- محرك yt-dlp، مع gallery-dl كمسار بديل لبعض محتوى Instagram.
- حدود افتراضية: 100MB و30 دقيقة.
- Redis اختياري لحفظ الاختيارات والأقفال الموزعة.
- FFmpeg وDeno وaria2.
- Sentry اختياري لتقارير الأخطاء.

## إعداد Railway
اربط المستودع بخدمة Worker مستقلة تستخدم Dockerfile والفرع main. أضف BOT_TOKEN في Variables. أضف REDIS_URL اختياريًا وSENTRY_DSN اختياريًا. لا تحفظ أي أسرار في Git.

## حدود الإرسال
حد التنزيل الافتراضي 100MB، لكن Telegram Bot API السحابي محدود هنا بـ49MB. الملفات الأكبر تحتاج Telegram Local Bot API Server مُدارًا بشكل مستقل؛ مجرد ضبط MAX_FILE_MB لا يرفع حد Telegram.

## GitHub automation
- Tests: compileall واختبارات sanity.
- Security: pip-audit وCodeQL وTrivy filesystem.
- Docker Build: بناء الصورة وفحصها بـTrivy.
- Dependabot: تحديث pip وGitHub Actions أسبوعيًا.

Secret Scanning وPush Protection يجب تفعيلهما من إعدادات Security في GitHub إذا كانا متاحين للمستودع. لا تضع BOT_TOKEN أو Cookies أو DSN داخل الملفات.

## تنبيه
إتاحة التنزيل تختلف حسب الموقع والرابط وقد تتطلب بعض المنصات ملفات Cookies صالحة. لا يدعم المحتوى الخاص أو المحمي بـDRM أو تجاوز تسجيل الدخول. استخدمه فقط للمحتوى الذي تملك حق تنزيله.
