const { chromium } = require('playwright');
const fs = require('fs');
// Abre la enciclopedia oficial en Chromium, reproduce el vídeo de cada supertécnica en su propio reproductor
// y guarda 8 fotogramas: <carpeta>/<id>_<n>.png. Después: python3 -I tools/zukan/palette.py <carpeta> tools/zukan/palette.json
// Uso: node tools/zukan/frames.cjs <carpeta de salida>   (hace falta acceso a zukan.inazuma.jp y a su CDN)
const OUT = process.argv[2] || 'zukan-frames';
fs.mkdirSync(OUT, { recursive: true });
const match = require('./skills.json');
// url del vídeo -> ids de nuestras técnicas
const wanted = {};

for (const [id, m] of Object.entries(match)) {
  (wanted[m.movie] ??= []).push(id);
}
const FRAMES = 8;
const T0 = Date.now();
const log = (...a) => console.log(((Date.now() - T0) / 1000).toFixed(1) + 's', ...a);
(async () => {
  const browser = await chromium.launch({ args: ['--autoplay-policy=no-user-gesture-required'] });
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  let done = 0;
  for (let p = 1; p <= 19; p++) {
    await page.goto(`https://zukan.inazuma.jp/en/skill/?page=${p}`, { waitUntil: 'networkidle', timeout: 90000 });
    await page.addStyleTag({ content: '.playBtn,.vjs-big-play-button,.vjs-control-bar,.vjs-loading-spinner{display:none!important}' });
    const urls = await page.$$eval('a.btnMovie', (as) => as.map((a) => a.getAttribute('data-movie-url')));
    for (let i = 0; i < urls.length; i++) {
      const ids = wanted[urls[i]];
      if (!ids || ids.every((id) => fs.existsSync(`${OUT}/${id}_${FRAMES - 1}.png`))) continue;
      try {
        await page.locator('a.btnMovie').nth(i).click();
        await page.waitForFunction(() => { const v = document.querySelector('#videoSkill video, video'); return v && v.readyState >= 2 && v.duration > 0; }, null, { timeout: 30000 });
        const dur = await page.evaluate(() => document.querySelector('video').duration);
        const nv = await page.evaluate(() => document.querySelectorAll('video').length);
        const video = page.locator('video').first();
        for (let k = 0; k < FRAMES; k++) {
          const t = Math.min(dur - 0.05, (dur * (k + 0.5)) / FRAMES);
          await page.evaluate((t) => new Promise((r) => { const v = document.querySelector('video'); v.pause(); const done = () => r(); v.addEventListener('seeked', done, { once: true }); setTimeout(done, 2000); v.currentTime = t; }), t);
          await page.waitForTimeout(80);
          const buf = await video.screenshot({ type: 'jpeg', quality: 70, timeout: 15000 });
          for (const id of ids) fs.writeFileSync(`${OUT}/${id}_${k}.png`, buf);
        }
        done += ids.length;
        if (done % 10 < ids.length) log(done, 'técnicas');
        await page.keyboard.press('Escape');
        await page.evaluate(() => { const c = document.querySelector('.modaal-close, .mfp-close, .close, [class*="close"]'); if (c) c.click(); });
        await page.waitForTimeout(300);
      } catch (e) {
        console.log('fallo', ids.join(','), String(e).slice(0, 120));
        await page.goto(`https://zukan.inazuma.jp/en/skill/?page=${p}`, { waitUntil: 'networkidle', timeout: 90000 });
        await page.addStyleTag({ content: '.playBtn,.vjs-big-play-button,.vjs-control-bar,.vjs-loading-spinner{display:none!important}' });
      }
    }
    log('página', p, 'hecha; técnicas con fotogramas:', done);
  }
  await browser.close();
})();
