"""Pinterest video pin from article images (2:3, 1080x1620, 30 fps, H.264).
Scenes: title -> numbered ideas -> before/after -> end card. Slow zoom on photos, text slides in, crossfades."""
import sys, os, json, subprocess, shutil
sys.path.insert(0, '/home/claude/dsh-pins')
from PIL import Image, ImageDraw, ImageFilter
from pinh2 import anton, script, mont, INK, CREAM, SAGE, TERRA, SUN

W, H, FPS = 1080, 1620, 30
HEAD = 440; PH = 1080; FOOT = H - HEAD - PH  # 100

def ease(t): return 1 - (1 - t) ** 3

def photo_frame(im, t, z0=1.0, z1=1.09, pan=(0.5, 0.5)):
    z = z0 + (z1 - z0) * t
    s = int(PH * z)
    big = im.resize((s, s), Image.LANCZOS)
    x = int((s - W) * pan[0]); y = int((s - PH) * pan[1])
    return big.crop((x, y, x + W, y + PH))

def text_center(d, y, txt, font, fill):
    d.text((W / 2, y), txt, font=font, fill=fill, anchor="mt")

def fit(d, txt, fn, maxw, s):
    while d.textlength(txt, font=fn(s)) > maxw and s > 30: s -= 2
    return fn(s)

def scene_frame(sc, t, imgs):
    c = Image.new("RGB", (W, H), CREAM); d = ImageDraw.Draw(c)
    im = imgs[sc["img"]]
    c.paste(photo_frame(im, t, *sc.get("zoom", (1.0, 1.09)), pan=sc.get("pan", (0.5, 0.5))), (0, HEAD))
    k = ease(min(1, t * sc["dur"] / 0.45))  # slide-in progress over 0.45 s
    off = int((1 - k) * 40)
    if sc["kind"] == "title":
        text_center(d, 40 + off, sc["kicker"], script(78), TERRA)
        f1 = fit(d, sc["t1"], anton, 980, 150); text_center(d, 140 + off, sc["t1"], f1, INK)
        f2 = fit(d, sc["t2"], anton, 980, 110); text_center(d, 140 + f1.size + 20 + off, sc["t2"], f2, INK)
    elif sc["kind"] == "idea":
        r = 62; cx, cy = 120, 150 + off
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=TERRA)
        d.text((cx, cy + 2), str(sc["n"]), font=mont(76, 800), fill=CREAM, anchor="mm")
        f1 = fit(d, sc["t1"], anton, 820, 120); d.text((210, 92 + off), sc["t1"], font=f1, fill=INK, anchor="lt")
        d.text((210, 92 + f1.size + 26 + off), sc["t2"], font=mont(44, 600), fill=SAGE, anchor="lt")
        d.text((W / 2, 400), "idea %d of %d" % (sc["n"], sc["total"]), font=mont(30, 600), fill=(150, 140, 130), anchor="mm")
    elif sc["kind"] == "ba":
        f1 = fit(d, sc["t1"], anton, 980, 130); text_center(d, 90 + off, sc["t1"], f1, INK)
        text_center(d, 90 + f1.size + 30 + off, sc["t2"], mont(46, 600), SAGE)
        for lab, x in (("BEFORE", W * 0.25), ("AFTER", W * 0.75)):
            tw = d.textlength(lab, font=mont(40, 800)) + 50
            d.rounded_rectangle([x - tw / 2, HEAD + 30, x + tw / 2, HEAD + 100], 35, fill=INK if lab == "BEFORE" else TERRA)
            d.text((x, HEAD + 65), lab, font=mont(40, 800), fill=CREAM, anchor="mm")
    elif sc["kind"] == "end":
        text_center(d, 60 + off, sc["t1"], anton(140), TERRA)
        text_center(d, 230 + off, sc["t2"], anton(96), INK)
        # sticker
        st = Image.new("RGBA", (300, 300), (0, 0, 0, 0)); sd = ImageDraw.Draw(st)
        sd.ellipse([10, 10, 290, 290], fill=SUN + (255,), outline=INK + (255,), width=6)
        for i, wd in enumerate(sc["sticker"].split("\n")):
            sd.text((150, 150 + (i - (len(sc["sticker"].split("\n")) - 1) / 2) * 58), wd, font=mont(48, 800), fill=INK, anchor="mm")
        sc_k = 0.6 + 0.4 * ease(min(1, t * sc["dur"] / 0.5))
        st = st.resize((int(300 * sc_k), int(300 * sc_k))).rotate(12, resample=Image.BICUBIC)
        c = c.convert("RGBA"); c.alpha_composite(st, (W - st.width - 40, HEAD + PH - st.height - 40)); c = c.convert("RGB"); d = ImageDraw.Draw(c)
    # footer
    d.rectangle([0, HEAD + PH, W, H], fill=SAGE)
    d.text((W / 2, HEAD + PH + FOOT / 2), sc.get("foot", "dailyspacehacks.com"), font=mont(40, 700), fill=CREAM, anchor="mm")
    return c

def render(spec, out):
    imgs = [Image.open(p).convert("RGB") for p in spec["images"]]
    imgs = [im.crop(((im.width - min(im.size)) // 2, (im.height - min(im.size)) // 2, (im.width + min(im.size)) // 2, (im.height + min(im.size)) // 2)).resize((PH, PH), Image.LANCZOS) for im in imgs]
    tmp = "/tmp/claude-0/-home-claude/f83b8538-bfe1-526d-9871-d75f72442669/scratchpad/vframes"
    shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    XF = int(0.3 * FPS); frames = []; n = 0
    scenes = spec["scenes"]
    for i, sc in enumerate(scenes):
        nf = int(sc["dur"] * FPS)
        for f in range(nf):
            fr = scene_frame(sc, f / nf, imgs)
            if i + 1 < len(scenes) and f >= nf - XF:  # crossfade into next scene
                nxt = scenes[i + 1]; a = (f - (nf - XF) + 1) / (XF + 1)
                fr = Image.blend(fr, scene_frame(nxt, 0, imgs), a)
            fr.save(f"{tmp}/f{n:05d}.jpg", quality=92); n += 1
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{tmp}/f%05d.jpg",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-crf", "20", "-movflags", "+faststart", out], check=True)
    # cover image = first title frame at 60%
    scene_frame(scenes[0], 0.99, imgs).save(out.replace(".mp4", "-cover.jpg"), quality=90)
    return n

if __name__ == "__main__":
    spec = json.load(open(sys.argv[1])); print(render(spec, sys.argv[2]), "frames")
